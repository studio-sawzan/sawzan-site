# sawzan-site について

> **注意: このリポジトリは公開(GitHub Pages)。** 内部メモのうち、住所・氏名・電話・個人メールは書かない。`_config.yml` で、このファイル・`docs/`・`tools/`・`README.md`・`CLAUDE.md` はサイトとして配信しない設定(2026-10-07)。ただし、リポジトリ自体は公開なので、書く内容は公開前提にする。

## 会社情報の参照元

SAWZANの設立・契約状況など、変わり得る会社情報はCodex側の共有HQ
`/Volumes/workspace/Projects/app-company-hq/company/status.md` を確認する。
バーチャルオフィスの利用住所は、上のHQの資料(`company/status.md`)にある。**この公開リポジトリには、住所・氏名・電話番号・個人のメールアドレスを書かない**(リポジトリもGitHub Pagesも公開されるため)。
公開ページに住所を載せるかどうかは、そのページの目的とユーザーの指示を確認する。

株式会社SAWZAN(2026-09-30時点、法人登記に向けて準備中)が運営する
アプリ(現在は enishiru-app「えにしる」)向けの静的サイトリポジトリ。

## 公開先

- **本番公開**: GitHub Pages経由で https://sawzan.com (カスタムドメイン設定済み)
  - GitHubリポジトリ: https://github.com/studio-sawzan/sawzan-site
  - GitHubアカウント: `studio-sawzan`(2026-09-30作成。連絡先のメールアドレスは、HQの資料を参照)
- **バックアップ**: DS218j(NAS)の bare リポジトリ
  - `ssh://ds218j/var/services/homes/zeronos/git-repos/sawzan-site.git`
  - second-brainと同じ運用(pull→commit→push、衝突は自動解決せずユーザー判断)

## HTTPS・Cloudflareの構成(2026-10-01)

- DNSはCloudflare(DNSレコード5本=Aレコード4本+www CNAMEは**プロキシ有効**)。
  GitHub Pagesの「Enforce HTTPS」も有効。
- Cloudflare側: SSL/TLSは**Full (strict)**、「常にHTTPSを使用」オン、
  **HSTS有効(max-age 6か月=15552000秒、サブドメイン適用・プリロードはオフ)**、No-Sniffオン。
- メール転送(support@sawzan.com)のMX/TXTレコードはプロキシ対象外(触らない)。
- **Cloudflareをやめる/プロキシを外す場合の注意**: HSTSがブラウザに最大6か月キャッシュされる。
  先にHSTSを無効にし、max-ageの期間が過ぎるのを待ってから、プロキシ/HTTPSを外すこと
  (順序を誤ると、訪問者がサイトに入れなくなる)。
- SSL/TLSモードをFlexibleにしない(GitHubのHTTPS強制と衝突して無限リダイレクトになる)。

## ページ構成(アプリごとにフォルダを掘る、2026-10-01)

アプリごとに内容が違う(プライバシーポリシーなど)ため、アプリ名のフォルダに置く。
**新しいアプリを作るときは、同じ形のフォルダを足す**(他のアプリのURLに影響しない)。

- `index.html` — 会社の入口(SAWZANのみ。アプリ一覧は載せない)
- `koukoku/index.html` — 電子公告の掲載先。設立前は準備中と表示する
- `apps/enishiru/index.html` — えにしるの案内(ポリシーへのリンク、問い合わせ先)
- `apps/enishiru/privacy.html` — えにしるのプライバシーポリシー(App Store/Google Play審査用)
- `apps/enishiru/terms.html` — えにしるの利用規約
- `apps/enishiru/account-deletion.html` — アカウント削除の案内(Google Play用)
- `privacy.html` / `terms.html`(直下) — 旧URLからの転送ページ(中身は上の2つへの自動転送。消さない)

ストアに登録するURLは `https://sawzan.com/apps/enishiru/privacy.html` を使う(ストアには**最終URLを直接**登録する。転送ページを登録しない)。

### URL設計(2026-10-07、Codex相談のうえ採用)
- 作品は**種類別**: アプリは `/apps/{slug}/`、音楽は `/music/{slug}/`。動画は原則YouTubeへの外部リンク(独自ページは必要になってから `/videos/{slug}/`)。書籍・記事も、必要になってから追加。
- `/works/` は**一覧専用**(画面の名前)。個別作品のURLは、`works` の名前を変えても動かない。
- slugは小文字ASCIIとハイフン。アプリ固有の文書(規約・ポリシー・削除案内)は、そのアプリ配下に置き、**ストア登録後はURLを動かさない**。
- 旧URL(`/enishiru/*`、ルート直下の `/privacy.html` `/terms.html`)は、`meta refresh`(即時)+canonical+noindexの転送ページとして**期限なしで維持**。転送の連鎖を作らない(ルート直下の旧URLは最終URLへ直接)。
- `/koukoku/` は登記に載せる固定URL。再編の対象にしない。
- 新しいアプリを足す時: `apps/{slug}/` に同じ形のページを置き、`tools/build.py` の `PAGES` に追加(prefixは `"../../"`)。

## 運営者名義について【重要】

株式会社SAWZANは**まだ法人登記していない**(2026-09-30時点)。そのため
現在の規約・プライバシーポリシー内の運営者表記は「ＳＡＷＺＡＮ」(屋号のみ・全角表記、個人の実名は非表示)に
している。一般のWebページのブランド表示は半角「SAWZAN」とする。法人登記が完了したら、運営者表記を法人名義(株式会社ＳＡＷＺＡＮ)に
更新すること。実名の掲載可否は必ずユーザーに確認してから変更する。

## 特定商取引法の表示(2026-10-03)

サブスク販売に伴う特商法ページは、未作成・未公開。電話番号が必要な理由、VO住所の条件、責任者氏名の論点は
`/Volumes/workspace/Projects/app-company-hq/company/tokushoho_handoff_2026-10-03.md` を読むこと。
ユーザーの承認なしに、住所・氏名・電話番号を公開ページに載せない。

## 作品・サービスのページ(2026-10-05、ユーザー指示で新設)

- `works/index.html`(URL: `/works/`)。アプリ・動画・音楽(YouTube、将来のSuno楽曲など)を、カードで並べるページ。
- **作品は、`assets/works-data.js` に1件ずつ足す**(HTMLは触らない)。項目と書き方は、そのファイルの冒頭コメントを読むこと。描画は `assets/works.js`。
- **決まり**: 公開済みに見せない。リンクは「status が `published` で、`https://` の url がある」作品だけ。公開前は `preparing`(準備中、リンクなし)。1件も無いカテゴリは「近日公開予定」の枠だけ。
- **作品名を公にする前に、必ずユーザーに確認する**(公開前のアプリ名などを、先に出さない)。
- `?demo=1` を付けると、デザイン確認用のサンプル(注意書き付き)が出る。通常表示には出ない。
- トップページ(`index.html`)には、アプリ一覧を載せない方針のまま(一覧は `works/` に分ける)。

## 検索からの保護(2026-10-05改訂、ユーザー指示「一般の企業と同じがよい。ただし自分の名前が検索されるのは嫌」)

- 通常のページ(トップ、規約、ポリシー、案内、`koukoku/`)は、一般の企業と同じく、検索に出るままにする。`noindex` は付けない。
- **個人の氏名・住所・電話番号を載せるページ(特商法ページなど)だけ**、`<meta name="robots" content="noindex, noarchive, nosnippet">` を付けて公開する。実名は、そのページ以外に書かない。
- `robots.txt` で Disallow しない(検索エンジンが noindex を読めなくなり、URLだけ残ることがある)。noindex はロボットに読まれる前提で、「検索結果に出さない」指示。
- 限界: noindex は検索エンジンに効くだけで、URLを知る人・収集ツール・ウェブアーカイブ・過去の保存には効かない。法人の代表取締役の氏名は登記簿(公開情報)に載る。ストアの販売元表示にも出る。
- Googleの「自分に関する検索結果」から、連絡先情報(住所・電話・メール)の削除を依頼できる(氏名や公的情報には効かない見込み、要確認)。
- Cloudflareの Transform Rules(X-Robots-Tag)は、検討したが、作っていない(2026-10-05に撤回)。

## 今後の拡張候補(ユーザー発言、未着手)

- IR情報ページ(法人化後、投資家向け情報を掲載する構想)

## 作業ルール

- 役割分担せず、pull→commit→push励行
- 衝突は自動解決せずユーザー判断を仰ぐ
- 変更内容([[koinryu_iap_pricing_decision]]や利用規約の内容変更等)は
  ユーザーに確認してから反映する(特に運営者名義・法的表記に関わる変更)

## 共通ヘッダー・フッター
- メニューの項目・順序とフッターは `tools/build.py` が一元管理し、`index.html` と `works/index.html` の `<!--SITE-HEADER-->`/`<!--SITE-FOOTER-->` の間へ差し込む。直接HTMLを編集せず、`MENU` を直して `python3 tools/build.py` を実行する(`--check` で最新か確認)。
- 新しいページを足す時は、`PAGES` に追加し、マーカーを置く。
- 共通スタイルは `assets/site.css`(色・文字・ヘッダー/フッター・文書ページ `<body class="doc">`)。ページ固有のスタイルだけを各ページの `<style>` に書く。トップの山の色(`--ridge-*` 等)は `index.html` に残している。
- 文書ページ(`koukoku/`、`apps/enishiru/*`)も、共通ヘッダー/フッターを使う(`tools/build.py` の `PAGES`)。
