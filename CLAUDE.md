# ときのはり鍼灸院 ウェブサイト

## ブログ記事を追加するときのルール

### 画像の選び方（重要）

**必ず以下のコマンドを実行して画像を決定すること。絶対に自分で決めない。**

```bash
python3 /Users/sakiko/Desktop/ときのはり鍼灸院自動化/website/pick_blog_image.py
```

このスクリプトが返した画像ファイル名をアイキャッチに使う。

**counseling.jpg は使用禁止（スクリプトが自動的に最低優先度にする）。**

### ブログ追加の手順

1. `python3 pick_blog_image.py` を実行 → 画像ファイル名を取得
2. `blog/template.html` をコピーして新しいHTMLファイルを作成
3. `【アイキャッチ画像.jpg】` を手順1で取得した画像名に置き換える
4. `blog/posts.json` の先頭に新記事を追加（imageフィールドに同じ画像名）
5. `sitemap.xml` に新記事URLを追加
6. git add → commit → push

### 利用可能な画像一覧

| ファイル名 | 内容 |
|---|---|
| exterior.jpg | 院の外観 |
| room.jpg | 施術室 |
| interior.jpg | 院内 |
| about.jpg | 院の雰囲気 |
| hero.jpg | メイン画像 |
| profile.jpg | プロフィール |
| counseling.jpg | カウンセリング（使用禁止・スクリプトが制御）|
