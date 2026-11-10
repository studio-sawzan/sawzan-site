#!/bin/sh
PATH=/usr/bin:$PATH  # /usr/local/bin の古いx86版gitより、/usr/bin を先にする
# このリポジトリのgitフックを入れる(clone直後、またはCodex側の作業場所で1回だけ)。
cd "$(git rev-parse --show-toplevel)" || exit 1
for h in pre-commit pre-push; do cp "tools/git-hooks/$h" ".git/hooks/$h" && chmod +x ".git/hooks/$h"; done
echo "gitフックを入れました: pre-commit, pre-push"

