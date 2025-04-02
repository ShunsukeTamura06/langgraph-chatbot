# LangGraph チャットボット

langgraphを使った、ファイルシステム操作が可能なチャットボットです。
langgraphの学習用プロジェクトとして作成されました。

## 特徴

- langgraphを使用した明快なグラフ構造
- ファイルシステム操作（読み取り、書き込み、一覧表示、削除、移動、コピー）
- グラフの視覚化機能
- 拡張可能なモジュラー設計（Open-Closed原則に準拠）

## インストール

必要なパッケージをインストールします：

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python main.py
```

初回実行時にOpenAI APIキーの入力を求められます。

## コマンド例

チャットボットとの対話例：

- 「新しいファイルにテキストを書いてください」
- 「ディレクトリの内容を一覧表示してください」
- 「sample.txtの内容を読み取ってください」

## グラフの視覚化

langgraph-studioがインストールされている場合、視覚的にグラフを確認できます：

```bash
langgraph studio
```

または、graphvizによる静的な視覚化も利用可能です（自動的に生成されます）。

## プロジェクト構造

```
langgraph-chatbot/
│
├── main.py                     # アプリのエントリーポイント
├── requirements.txt            # 依存関係
├── README.md                   # プロジェクト説明
│
├── config/                     # 設定関連
│   └── config.py               # 設定（モデル名、温度など）
│
├── core/                       # コア機能
│   ├── __init__.py
│   ├── state.py                # 状態定義
│   └── graph_builder.py        # グラフ構築ロジック
│
├── nodes/                      # グラフノード
│   ├── __init__.py
│   ├── assistant.py            # アシスタントノード
│   └── process.py              # 処理ノード
│
├── tools/                      # ツール定義
│   ├── __init__.py
│   ├── filesystem_tools.py     # ファイルシステムツール
│   └── custom_tools.py         # 将来的なカスタムツール
│
└── utils/                      # ユーティリティ
    ├── __init__.py
    └── visualization.py        # グラフ視覚化ユーティリティ
```

## 拡張方法

新しいツールを追加するには：

1. `tools/` ディレクトリに新しいファイルを作成
2. 必要なツールを実装
3. `main.py` で新しいツールをインポートして追加

## ライセンス

MIT
