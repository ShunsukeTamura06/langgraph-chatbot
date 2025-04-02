"""
設定モジュール
アプリケーション全体の設定を管理します
"""
import os

# モデル設定
MODEL_NAME = "gpt-3.5-turbo-0125"  # 使用するモデル
TEMPERATURE = 0.0  # 温度パラメータ（0.0から1.0）

# APIキー設定
def get_api_key():
    """OpenAI APIキーを取得します"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        api_key = input("OpenAI API キーを入力してください: ")
        os.environ["OPENAI_API_KEY"] = api_key
    return api_key

# システムメッセージテンプレート
SYSTEM_MESSAGE_TEMPLATE = """あなたはファイルシステム操作ができる便利なアシスタントです。以下のツールが利用可能です：
- ReadFileTool: ファイルの内容を読み取ります。引数: file_path
- WriteFileTool: ファイルを作成または上書きします。引数: file_path, text
- ListDirectoryTool: ディレクトリの内容を一覧表示します。引数: directory_path
- DeleteFileTool: ファイルを削除します。引数: file_path
- MoveFileTool: ファイルを移動します。引数: source_path, destination_path
- CopyFileTool: ファイルをコピーします。引数: source_path, destination_path

ユーザーがファイル関連の操作をリクエストした場合、適切なツールを使用してください。
パスは全て '{root_dir}' からの相対パスとして扱われます。
"""
