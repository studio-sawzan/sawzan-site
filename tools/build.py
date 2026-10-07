#!/usr/bin/env python3
"""共通のヘッダー(メニュー)とフッターを、各ページへ差し込む。

メニューの項目・順序は、この MENU だけを直す。直したら `python3 tools/build.py` を実行し、
差し込み先ページ(PAGES)に反映して、変更をまとめてコミットする。
差し込み先は、`<!--SITE-HEADER-->…<!--/SITE-HEADER-->`、`<!--SITE-FOOTER-->…<!--/SITE-FOOTER-->` で囲んだ範囲。
`--check` で、差し込み済みの内容が最新かだけを確認する(古ければ終了コード1)。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (表示名, 行き先, 種類)。種類 'in' はトップ内の位置、'page' は別ページ。
MENU = [
    ("事業内容", "#business", "in"),
    ("会社概要", "#about", "in"),
    ("沿革", "#history", "in"),
    ("お問い合わせ", "#contact", "in"),
    ("作品・サービス", "works/", "page"),
]

# 差し込み先: パス -> (ルートまでの相対パス, 現在のページの行き先)
PAGES = {
    "index.html": ("", None),
    "works/index.html": ("../", "works/"),
    "koukoku/index.html": ("../", None),
    "apps/enishiru/index.html": ("../../", None),
    "apps/enishiru/privacy.html": ("../../", None),
    "apps/enishiru/terms.html": ("../../", None),
    "apps/enishiru/account-deletion.html": ("../../", None),
}


def header(prefix, current):
    items = []
    for label, dest, kind in MENU:
        if prefix == "" and kind == "in":
            href = dest
        else:
            href = prefix + dest
        if dest == current:
            href = "./"
            cur = ' aria-current="page"'
        else:
            cur = ""
        arrow = '<span aria-hidden="true"> →</span>' if kind == "page" else ""
        items.append(f'        <li><a href="{href}"{cur}>{label}{arrow}</a></li>')
    brand = "#top" if prefix == "" else prefix
    return (
        '<header class="site-header">\n  <div class="wrap">\n'
        f'    <a class="brand" href="{brand}"><img src="{prefix}assets/sawzan_logo_primary.svg" '
        'alt="創山のロゴ" width="57" height="42"><span>SAWZAN</span></a>\n'
        '    <nav aria-label="メニュー">\n      <ul>\n' + "\n".join(items) + "\n      </ul>\n    </nav>\n"
        "  </div>\n</header>"
    )


def footer(prefix):
    return (
        "<footer>\n  <div class=\"wrap\">\n    <span>&copy; 2026 SAWZAN</span>\n"
        f'    <a href="{prefix}koukoku/">電子公告</a>\n  </div>\n</footer>'
    )


def stamp(text, tag, body, rel):
    pat = re.compile(rf"<!--{tag}-->.*?<!--/{tag}-->", re.S)
    n = len(pat.findall(text))
    if n != 1 or text.count(f"<!--{tag}-->") != 1 or text.count(f"<!--/{tag}-->") != 1:
        raise SystemExit(f"{rel}: マーカー <!--{tag}-->…<!--/{tag}--> が、ちょうど1組ではありません(見つかった数: {n})")
    return pat.sub(lambda m: f"<!--{tag}-->\n{body}\n<!--/{tag}-->", text)


def untracked_pages():
    """マーカーを持つのに PAGES に無いHTML(登録忘れ)を探す。"""
    found = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT).as_posix()
        if rel in PAGES or any(part.startswith(".") for part in path.relative_to(ROOT).parts):
            continue
        if "<!--SITE-HEADER-->" in path.read_text(encoding="utf-8"):
            found.append(rel)
    return found


def main():
    args = sys.argv[1:]
    if any(a != "--check" for a in args):
        raise SystemExit("使い方: python3 tools/build.py [--check]")
    check = bool(args)
    # 先に全ページを検証し、問題が無い時だけ書き込む(途中で止まって、一部だけ更新された状態にしない)。
    results = {}
    for rel, (prefix, current) in PAGES.items():
        old = (ROOT / rel).read_text(encoding="utf-8")
        new = stamp(old, "SITE-HEADER", header(prefix, current), rel)
        new = stamp(new, "SITE-FOOTER", footer(prefix), rel)
        results[rel] = (old, new)
    missing = untracked_pages()
    if missing:
        raise SystemExit("PAGES に未登録のページがあります: " + ", ".join(missing))
    stale = [rel for rel, (old, new) in results.items() if old != new]
    if check:
        if stale:
            print("古い:", ", ".join(stale))
            sys.exit(1)
        print("最新です")
        return
    for rel in stale:
        (ROOT / rel).write_text(results[rel][1], encoding="utf-8")
    print("更新:", ", ".join(stale) if stale else "(変更なし)")


if __name__ == "__main__":
    main()
