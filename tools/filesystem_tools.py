"""
ファイルシステムツールモジュール
ファイルシステム操作に関するツールを提供します
"""
import tempfile
import os
from typing import List

from langchain.tools import BaseTool
from langchain.tools.file_management import (
    ReadFileTool,
    WriteFileTool,
    ListDirectoryTool,
    DeleteFileTool,
    MoveFileTool,
    CopyFileTool,
)

def create_filesystem_root() -> str:
    """
    ファイルシステムのルートディレクトリを作成
    
    Returns:
        作成された一時ディレクトリのパス
    """
    # 一時ディレクトリを作成（実際のアプリケーションでは永続的なディレクトリを使用する）
    temp_dir = tempfile.mkdtemp()
    
    # サンプルファイルを作成（オプション）
    with open(os.path.join(temp_dir, "README.txt"), "w") as f:
        f.write("これはチャットボットのファイルシステムです。\nファイルの作成、読み取り、削除などの操作ができます。")
    
    print(f"ファイルシステムのルートディレクトリを作成しました: {temp_dir}")
    return temp_dir

def setup_filesystem_tools(root_dir: str) -> List[BaseTool]:
    """
    ファイルシステムツールをセットアップ
    
    Args:
        root_dir: ファイルシステムのルートディレクトリ
        
    Returns:
        設定されたツールのリスト
    """
    tools = [
        ReadFileTool(root_dir=root_dir),
        WriteFileTool(root_dir=root_dir),
        ListDirectoryTool(root_dir=root_dir),
        DeleteFileTool(root_dir=root_dir),
        MoveFileTool(root_dir=root_dir),
        CopyFileTool(root_dir=root_dir),
    ]
    return tools
