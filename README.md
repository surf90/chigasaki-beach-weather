# chigasaki-beach-weather

茅ヶ崎ヘッドランド（Tバー）周辺の天気・波情報・潮汐を確認できるWebアプリの試作版です。
スマートフォン（iPhone/Android）およびPCのブラウザから直接利用できます。

## 特徴

- 特別なアプリのインストール不要
- ブラウザのみで動作（バックエンドサーバー不要）
- スマートフォンでの閲覧に最適化されたレイアウト

## 使い方（WEBでの確認方法：推奨）

現在のバージョンは静的なHTML/JavaScriptで構築されているため、特別な開発環境は不要です。

1. 次の[URL](https://surf90.github.io/chigasaki-beach-weather/)にアクセス

## 使い方（ローカルでの確認方法）

現在のバージョンは静的なHTML/JavaScriptで構築されているため、特別な開発環境は不要です。

1. このリポジトリ（フォルダ）をPCにダウンロードします。
2. フォルダ内にある `index.html` をダブルクリックして、ブラウザ（ChromeやEdge、Safariなど）で開きます。
3. 自動的に最新の気象情報が取得・表示されます。

## ~~今後の公開について（予定）~~

~~GitHub Pages等を利用して、URL（例: `https://xxxx.github.io/chigasaki-beach-weather/`）をメンバーに共有するだけで、いつでもスマホからアクセスできるようにする予定です。~~

## 使用技術・API

- HTML / CSS / JavaScript
- 気象データ: [Open-Meteo API](https://open-meteo.com/) (登録不要・無料で利用可能なAPI)****
- 潮汐データ: [Stormglass API](https://stormglass.io/)(登録必要・一日10回無料利用可能なAPI)****
