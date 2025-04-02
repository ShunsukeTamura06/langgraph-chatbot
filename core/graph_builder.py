"""
グラフ構築モジュール
LangGraphのグラフを構築します
"""
from typing import List, Union, Annotated
from langchain.tools import BaseTool
from langgraph.graph import StateGraph
from langgraph.checkpoint import MemorySaver
from langgraph.prebuilt import ToolNode

from core.state import ChatState
from nodes.assistant import assistant
from nodes.process import process_tool_results, should_call_tool

def build_graph(tools: List[BaseTool]):
    """
    グラフを構築する関数
    
    Args:
        tools: ツールのリスト
        
    Returns:
        コンパイルされたグラフ
    """
    # グラフを初期化
    builder = StateGraph(ChatState)
    
    # ノードを追加
    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))
    builder.add_node("process_tool_results", process_tool_results)
    
    # エッジを設定
    builder.set_entry_point("assistant")
    
    # アシスタントからのエッジ
    builder.add_conditional_edges(
        "assistant",
        should_call_tool,
        {
            "tools": "tools",
            "end": None,  # Noneは終了を意味する
        }
    )
    
    # ツールノードからツール結果処理ノードへの接続
    builder.add_edge("tools", "process_tool_results")
    
    # ツール結果処理ノードからアシスタントへ戻る
    builder.add_edge("process_tool_results", "assistant")
    
    # チェックポイントを設定
    memory = MemorySaver()
    
    # グラフをコンパイル
    return builder.compile(checkpointer=memory)
