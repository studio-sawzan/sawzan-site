/*
 * 作品・サービスの一覧データ。実際の作品は、ここに1件ずつ足す(ページのHTMLは触らない)。
 *
 * 【ルール】
 *  - status が "published"(公開中)の作品だけ、「見る・聞く」のリンクを出す。url は必須。
 *  - 公開前のものを載せる場合は、status を "preparing"(準備中)にする。リンクは出ず、「準備中」と表示される。
 *    ※ 作品名を事前に公にしてよいかは、必ず、ユーザーに確認してから足す。
 *  - 1件も無いカテゴリは、「近日公開予定」の枠だけが出る(公開済みに見える表示はしない)。
 *
 * 項目:
 *   id          半角英数の識別子(重複しない)
 *   category    "app"(アプリ・ウェブサービス) / "video"(動画) / "music"(音楽)
 *   title       作品名
 *   description 一言の説明(60字程度まで)
 *   status      "published"(公開中) / "preparing"(準備中)
 *   url         公開先のURL(published のとき必須。https:// から)
 *   image       サムネイル画像のパス(任意。例 "../assets/works/xxx.jpg")
 *   platforms   載っている場所の表示(任意。例 ["App Store", "Google Play"] / ["YouTube"] / ["Suno"])
 *   date        公開日(任意。例 "2026-11")
 */
window.SAWZAN_WORKS = [
  {
    id: "enishiru",
    category: "app",
    title: "えにしる",
    description: "四柱推命で知る、私とあなた。生年月日から、自分と大切な人との相性を読み解く占いアプリ。",
    status: "preparing",
    image: "../apps/enishiru/img/app-icon.jpg"
  },
  // ここに、実際の作品を足す。(例)
  // {
  //   id: "example-app",
  //   category: "app",
  //   title: "作品名",
  //   description: "一言の説明",
  //   status: "published",
  //   url: "https://example.com/",
  //   platforms: ["App Store"],
  //   date: "2026-11"
  // },
];
