/*
 * 作品・サービスの一覧を描く。データは assets/works-data.js(window.SAWZAN_WORKS)。
 * 公開済みに見せないための決まり:
 *  - リンクは「status が published で、https:// の url がある」作品にだけ出す。
 *  - 準備中の作品には、バッジ「準備中」だけで、リンクを出さない。
 *  - 作品が1件も無いカテゴリは、「近日公開予定」の枠だけを出す。
 *  - ?demo=1 のときだけ、デザイン確認用のサンプル(注意書き付き)を出す。通常表示には出ない。
 */
(function () {
  "use strict";

  var CATEGORIES = [
    { id: "app", name: "アプリ・ウェブサービス", en: "APPS & SERVICES", icon: '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="14" y="5" width="20" height="38" rx="4"/><path d="M21 38h6"/><path d="M19 15h10M19 21h10M19 27h6"/></svg>', link: "見る", soon: "アプリ・ウェブサービス" },
    { id: "video", name: "動画", en: "VIDEOS", icon: '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="5" y="11" width="38" height="26" rx="5"/><path d="M20 18l11 6-11 6z"/></svg>', link: "見る", soon: "動画" },
    { id: "music", name: "音楽", en: "MUSIC", icon: '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M18 36V12l22-4v24"/><circle cx="13" cy="36" r="5"/><circle cx="35" cy="32" r="5"/></svg>', link: "聞く", soon: "音楽" }
  ];

  var DEMO = [
    { id: "demo-app", category: "app", title: "サンプルのアプリ", description: "アプリのカード表示の見本です。実在しません。", status: "published", url: "https://example.com/", platforms: ["App Store", "Google Play"], date: "2026-11" },
    { id: "demo-app2", category: "app", title: "サンプル(準備中)", description: "公開前のものは、リンクなしで「準備中」と表示されます。", status: "preparing" },
    { id: "demo-video", category: "video", title: "サンプルの動画", description: "動画のカード表示の見本です。実在しません。", status: "published", url: "https://example.com/", platforms: ["YouTube"], date: "2026-12" },
    { id: "demo-music", category: "music", title: "サンプルの楽曲", description: "楽曲のカード表示の見本です。実在しません。", status: "published", url: "https://example.com/", platforms: ["Suno"], date: "2027-01" }
  ];

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "html") node.innerHTML = attrs[k];
      else node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { node.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return node;
  }

  function isSafeUrl(u) { return typeof u === "string" && /^https:\/\//.test(u); }

  function isLive(w) { return w.status === "published" && isSafeUrl(w.url); }

  function card(w, cat) {
    var live = isLive(w);
    var thumb = el("div", { "class": "thumb" });
    if (w.image && !/^(javascript|data):/i.test(w.image)) {
      thumb.appendChild(el("img", { src: w.image, alt: "", loading: "lazy" }));
    } else {
      thumb.innerHTML = cat.icon;
    }
    thumb.appendChild(el("span", { "class": "badge" + (live ? " live" : "") }, [live ? "公開中" : "準備中"]));

    var body = el("div", { "class": "card-body" });
    body.appendChild(el("h3", {}, [w.title || ""]));
    if (w.description) body.appendChild(el("p", {}, [w.description]));
    var meta = [];
    if (w.platforms && w.platforms.length) meta.push(w.platforms.join(" / "));
    if (w.date) meta.push(w.date);
    if (meta.length) {
      var ul = el("ul", { "class": "meta" });
      meta.forEach(function (m) { ul.appendChild(el("li", {}, [m])); });
      body.appendChild(ul);
    }
    if (live) {
      var a = el("a", { href: w.url, rel: "noopener", target: "_blank" }, [cat.link]);
      body.appendChild(el("div", { "class": "go" }, [a]));
    }
    return el("article", { "class": "card" }, [thumb, body]);
  }

  function group(cat, works) {
    var head = el("div", { "class": "group-head" }, [el("h2", {}, [cat.name]), el("span", { "class": "en" }, [cat.en])]);
    var grid = el("div", { "class": "grid" });
    if (works.length) {
      works.forEach(function (w) { grid.appendChild(card(w, cat)); });
    } else {
      grid.appendChild(el("div", { "class": "empty", html: "<strong>近日公開予定</strong>" + cat.soon + "は、公開できたものから、ここに並べます。" }));
    }
    return el("section", { "class": "group", "data-cat": cat.id }, [head, grid]);
  }

  function render(works, active) {
    var root = document.getElementById("lineup");
    root.textContent = "";
    CATEGORIES.forEach(function (cat) {
      if (active !== "all" && active !== cat.id) return;
      root.appendChild(group(cat, works.filter(function (w) { return w.category === cat.id; })));
    });
  }

  function filters(works, onChange) {
    var ul = document.getElementById("filters");
    ul.textContent = "";
    var items = [{ id: "all", name: "すべて" }].concat(CATEGORIES);
    items.forEach(function (it, i) {
      var b = el("button", { type: "button", "aria-pressed": i === 0 ? "true" : "false" }, [it.name]);
      b.addEventListener("click", function () {
        Array.prototype.forEach.call(ul.querySelectorAll("button"), function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        onChange(it.id);
      });
      ul.appendChild(el("li", {}, [b]));
    });
  }

  var demo = /[?&]demo=1(&|$)/.test(location.search);
  var works = demo ? DEMO : (Array.isArray(window.SAWZAN_WORKS) ? window.SAWZAN_WORKS : []);
  if (demo) document.getElementById("demo-note").hidden = false;
  filters(works, function (id) { render(works, id); });
  render(works, "all");
})();
