## ChatGPT 関数呼び出しレッド チーム ツールのサンプル
# 言語
- 英語 [英語](README.md)
- 日本語 [日本語](README_ja.md)
## 紹介
ChatGPT関数呼び出しAPIを使用したレッドチームサンプルツール。 ChatGPTの関数呼び出しAPIのサンプルコードはインターネット上に多数ありますが、特定のビジネスとの連携が強くなく、ネットワーク攻撃や防御のビジネスコードとの連携など、開発者に不便をもたらすため、レッドチームのサンプルツールを書きました。 ChatGPT 関数呼び出しを使用します。 開発者による参考用。
## 特徴
自然言語での ChatGPT への攻撃および防御要件の送信をサポートします。ChatGPT は関数呼び出し API を使用して、次のことを自動的に実行します。
- ターゲット情報を自動的に収集します: ポートのスキャン、サブドメイン名の収集、DNS レコードの収集。
- 脆弱性を自動的に悪用する: 現在、CVE-2022-22965 脆弱性の悪用をサポートしており、悪用結果を返します。 エクスプロイトが成功すると、Web シェル アドレスが返されます。
- インテリジェンスの自動検索: 現在、ターゲット IP およびバックドア ファイルの評価情報のクエリをサポートしています。
- 自動暗号化と復号化: 一般的なハッシュ暗号文の復号化と平文に対するハッシュ操作をサポートします。
- 自動ファイル生成: 現在、ChatGPT の回答をテキスト ファイルとして保存することをサポートしています。
## インストール
1. プロジェクトのクローンを作成し、依存パッケージをインストールします。
```bash
git clone https://github.com/magicming200/ChatGPT-Function-Call-Red-Team-Tool.git
cd ChatGPT-Function-Call-Red-Team-Tool
pip install -r requirements.txt
```
2. ChatGPT キーを入力し、/config/system_config.py を開きます。
```python
api_chatgpt_key = '<YOUR_API_KEY>'
```
3. レッド チーム ツールの API キーを入力し、/config/system_config.py を開きます。
```python
# ハッシュ復号API：
api_decrypt_email = '<YOUR_API_EMAIL>'
api_decrypt_key = '<YOUR_API_KEY>'
# ポートスキャンAPI：
api_ports_email = '<YOUR_API_EMAIL>'
api_ports_key = '<YOUR_API_KEY>'
# 脅威インテリジェンス API：
api_reputation_key = '<YOUR_API_KEY>'
```
## 使用法
- 開始：  
```bash
 python .\ChatGPT_Function_Call.py
```  
- 出口：  
「exit」または「quit」と入力し、Enterを押します。
## スクリーンショット
- 情報収集:  
![info gather](readme_pics/info_gather.png)  
- 脆弱性の検証:
![exploit vulnerability](readme_pics/exploit_vul_1.png)  
Webシェルを取得する：  
![exploit vulnerability](readme_pics/exploit_vul_2.png)  
- 検索インテリジェンス:  
![search intelligence](readme_pics/intelligence.png)  
- 暗号化と復号化:  
![encrypt and decrypt](readme_pics/encrypt_decrypt.png)  
- ファイルを保存:  
![save file ](readme_pics/save_file.png)
