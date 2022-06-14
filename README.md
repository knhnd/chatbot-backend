# Flask でつくる LINE Chatbot

Flask で作成した LINE ChatBot のバックエンド API．LINE Developers のコンソールから作成した Messaging API からこのバックエンド API を叩くことでレスポンスを返す．

### 環境情報

- Python : 3.10.2
- Flask : 1.1.2
- line-bot-sdk : 2.2.1

## 開発

開発方法についての詳細は [Zenn の記事](https://zenn.dev/kenken82/articles/ca5e36cf4d5ea1)として公開してあります．

## デプロイ

LINE Developer の公式ドキュメント通り Heroku にデプロイする．

- このリポジトリに push すると自動で Heroku にデプロイされるようになっている
- URL : https://chatbot-backend-api.herokuapp.com/

## Reference

- [Flask 公式ドキュメント](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/index.html)
- [Heroku 公式ドキュメント](https://devcenter.heroku.com/ja/categories/reference)
- [LINE Developers](https://developers.line.biz/ja/)
- [LINE Documentation](https://developers.line.biz/en/docs/)
- [Messaging API Document](https://developers.line.biz/ja/docs/messaging-api/getting-started/)
- [GitHub line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)
- [1 時間で LINE Bot をつくる](https://qiita.com/n0bisuke/items/ceaa09ef8898bee8369d)

---
