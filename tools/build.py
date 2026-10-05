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


def stamp(text, tag, body):
    pat = re.compile(rf"<!--{tag}-->.*?<!--/{tag}-->", re.S)
    if not pat.search(text):
        raise SystemExit(f"マーカー <!--{tag}--> がありません")
    return pat.sub(lambda m: f"<!--{tag}-->\n{body}\n<!--/{tag}-->", text)


def main():
    check = "--check" in sys.argv
    stale = []
    for rel, (prefix, current) in PAGES.items():
        path = ROOT / rel
        old = path.read_text(encoding="utf-8")
        new = stamp(old, "SITE-HEADER", header(prefix, current))
        new = stamp(new, "SITE-FOOTER", footer(prefix))
        if new != old:
            stale.append(rel)
            if not check:
                path.write_text(new, encoding="utf-8")
    if check and stale:
        print("古い:", ", ".join(stale))
        sys.exit(1)
    print("更新:" if not check else "最新です", ", ".join(stale) if stale else "")


if __name__ == "__main__":
    main()
