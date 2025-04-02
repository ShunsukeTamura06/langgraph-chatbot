"""
状態管理モジュール
チャットの状態を定義します
"""
from typing import Dict, List, TypedDict
from langgraph.prebuilt import ToolInvocation

class ChatState(TypedDict):
    """
    チャットの状態を定義するクラス
    
    Attributes:
        messages: チャットメッセージの履歴
        tool_calls: ツール呼び出し情報
        tool_results: ツール実行結果
        intermediate_steps: 中間ステップの記録
        filesystem_root: ファイルシステムのルートディレクトリ
    """
    messages: List[Dict[str, str]]
    tool_calls: List[ToolInvocation]
    tool_results: List[Dict]
    intermediate_steps: List
    filesystem_root: str
