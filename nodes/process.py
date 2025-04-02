"""
処理ノード
ツール呼び出しの結果を処理するためのノード
"""
from typing import Union, Annotated

from core.state import ChatState

def should_call_tool(state: ChatState) -> Union[Annotated[bool, "tools"], Annotated[bool, "end"]]:
    """
    ツール呼び出しが必要かどうかを判断する関数
    
    Args:
        state: 現在の状態
        
    Returns:
        "tools"（ツール呼び出しが必要）または"end"（ツール呼び出しが不要）
    """
    if state.get("tool_calls") and len(state["tool_calls"]) > 0:
        return "tools"
    else:
        return "end"

def process_tool_results(state: ChatState) -> ChatState:
    """
    ツール呼び出し結果を処理する関数
    
    Args:
        state: 現在の状態（ツール呼び出し結果を含む）
        
    Returns:
        更新された状態
    """
    # intermediate_stepsが存在しない場合は初期化
    if "intermediate_steps" not in state:
        state["intermediate_steps"] = []
    
    # 中間ステップとしてツール呼び出しと結果を記録
    for i, (tool_call, result) in enumerate(zip(state.get("tool_calls", []), state.get("tool_results", []))):
        state["intermediate_steps"].append((tool_call, result["content"]))
    
    # ツール結果が存在する場合、次のステップのためにツール呼び出しをクリア
    state["tool_calls"] = []
    
    return state
