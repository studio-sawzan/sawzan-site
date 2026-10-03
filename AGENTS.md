# sawzan-site について

## 会社情報の参照元

SAWZANの設立・契約状況など、変わり得る会社情報はCodex側の共有HQ
`/Volumes/workspace/Projects/app-company-hq/company/status.md` を確認する。
バーチャルオフィスの利用住所は、2026-10-01のGMOオフィスサポート契約情報として
`〒104-0061 東京都中央区銀座１丁目１２番４号 N&E BLD.6F`。
建物名を省略しない。これは契約中の住所であり、法人登記が完了したという意味ではない。
公開ページに住所を載せるかどうかは、そのページの目的とユーザーの指示を確認する。

株式会社SAWZAN(2026-09-30時点、法人登記に向けて準備中)が運営する
アプリ(現在は enishiru-app「えにしる」)向けの静的サイトリポジトリ。

## 公開先

- **本番公開**: GitHub Pages経由で https://sawzan.com (カスタムドメイン設定済み)
  - GitHubリポジトリ: https://github.com/studio-sawzan/sawzan-site
  - GitHubアカウント: `studio-sawzan`(studio.sawzan@gmail.com、2026-09-30作成)
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
- `enishiru/index.html` — えにしるの案内(ポリシーへのリンク、問い合わせ先)
- `enishiru/privacy.html` — えにしるのプライバシーポリシー(App Store/Google Play審査用)
- `enishiru/terms.html` — えにしるの利用規約
- `privacy.html` / `terms.html`(直下) — 旧URLからの転送ページ(中身は上の2つへの自動転送。消さない)

ストアに登録するURLは `https://sawzan.com/enishiru/privacy.html` を使う。

## 運営者名義について【重要】

株式会社SAWZANは**まだ法人登記していない**(2026-09-30時点)。そのため
現在の規約・プライバシーポリシー内の運営者表記は「ＳＡＷＺＡＮ」(屋号のみ・全角表記、個人の実名は非表示)に
している。一般のWebページのブランド表示は半角「SAWZAN」とする。法人登記が完了したら、運営者表記を法人名義(株式会社ＳＡＷＺＡＮ)に
更新すること。実名の掲載可否は必ずユーザーに確認してから変更する。

## 特定商取引法の表示(2026-10-03)

サブスク販売に伴う特商法ページは、未作成・未公開。電話番号が必要な理由、VO住所の条件、責任者氏名の論点は
`/Volumes/workspace/Projects/app-company-hq/company/tokushoho_handoff_2026-10-03.md` を読むこと。
ユーザーの承認なしに、住所・氏名・電話番号を公開ページに載せない。

## 検索からの保護(2026-10-03、ユーザー指示「効くことは全部やる」)

- `enishiru/` 配下のページには `<meta name="robots" content="noindex, noarchive">` を入れた(検索結果に出さない・キャッシュを残さない)。
- **個人の氏名・住所・電話番号を載せるページ(特商法ページなど)は、必ず `noindex, noarchive, nosnippet` を付けて公開する**。
  `robots.txt` で Disallow しない(検索エンジンが noindex を読めなくなり、URLだけ残ることがある)。
- 限界: noindex は検索エンジンに効くだけで、URLを知る人・収集ツール・ウェブアーカイブ・過去の保存には効かない。法人の代表取締役の氏名は登記簿(公開情報)に載る。
- `index.html`(会社の入口)と `koukoku/`(電子公告)には指定を入れていない。
- 任意: Cloudflareの Transform Rules(Modify Response Header)で、特商法ページに `X-Robots-Tag: noindex, noarchive, nosnippet` を付けると二重になる(ダッシュボード作業。未実施)。

## 今後の拡張候補(ユーザー発言、未着手)

- IR情報ページ(法人化後、投資家向け情報を掲載する構想)

## 作業ルール

- 役割分担せず、pull→commit→push励行
- 衝突は自動解決せずユーザー判断を仰ぐ
- 変更内容([[koinryu_iap_pricing_decision]]や利用規約の内容変更等)は
  ユーザーに確認してから反映する(特に運営者名義・法的表記に関わる変更)
