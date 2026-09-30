# sawzan-site について

株式会社SAWZAN(2026-09-30時点、法人登記に向けて準備中)が運営する
koinryu-app「えにしる」向けの静的サイトリポジトリ。

## 公開先

- **本番公開**: GitHub Pages経由で https://sawzan.com (カスタムドメイン設定済み)
  - GitHubリポジトリ: https://github.com/studio-sawzan/sawzan-site
  - GitHubアカウント: `studio-sawzan`(studio.sawzan@gmail.com、2026-09-30作成)
- **バックアップ**: DS218j(NAS)の bare リポジトリ
  - `ssh://ds218j/var/services/homes/zeronos/git-repos/sawzan-site.git`
  - second-brainと同じ運用(pull→commit→push、衝突は自動解決せずユーザー判断)

## 現在のページ構成

- `privacy.html` — プライバシーポリシー(App Store/Google Play審査用)
- `terms.html` — 利用規約

## 運営者名義について【重要】

株式会社SAWZANは**まだ法人登記していない**(2026-09-30時点)。そのため
現在のページ内の運営者表記は「SAWZAN」(屋号のみ、個人の実名は非表示)に
している。法人登記が完了したら、運営者表記を法人名義(株式会社SAWZAN)に
更新すること。実名の掲載可否は必ずユーザーに確認してから変更する。

## 今後の拡張候補(ユーザー発言、未着手)

- IR情報ページ(法人化後、投資家向け情報を掲載する構想)

## 作業ルール

- 役割分担せず、pull→commit→push励行
- 衝突は自動解決せずユーザー判断を仰ぐ
- 変更内容([[koinryu_iap_pricing_decision]]や利用規約の内容変更等)は
  ユーザーに確認してから反映する(特に運営者名義・法的表記に関わる変更)
