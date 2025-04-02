"""
LangGraph チャットボット - メインプログラム
ファイルシステム操作が可能なチャットボット
"""
import os
import sys

from config.config import get_api_key
from core.graph_builder import build_graph
from core.state import ChatState
from tools.filesystem_tools import create_filesystem_root, setup_filesystem_tools
from utils.visualization import visualize_graph

def main():
    """メイン関数"""
    # APIキーの取得
    get_api_key()
    
    # ファイルシステムのルートディレクトリを作成
    filesystem_root = create_filesystem_root()
    
    # ファイルシステムツールのセットアップ
    filesystem_tools = setup_filesystem_tools(filesystem_root)
    
    # グラフを作成
    graph = build_graph(filesystem_tools)
    
    # グラフの視覚化（オプション）
    try:
        visualize_graph(graph.builder, "chatbot_graph")
        print("グラフの構造を chatbot_graph.png に保存しました")
    except Exception as e:
        print(f"グラフの視覚化に失敗しました: {e}")
    
    # スタジオでの表示を試みる（langgraph-studioがインストールされている場合）
    try:
        from langgraph.dev import studio
        print("langgraph studioでグラフを表示します（Ctrl+Cで中断）...")
        print("スタジオが起動したら、メインプログラムを実行するために新しいターミナルを開いてください")
        studio.render(graph)
    except (ImportError, Exception) as e:
        print(f"langgraph studioの表示に失敗しました: {e}")
        print("langgraph studioを使用するには: pip install langgraph-studio")
    
    print("\nチャットボットが起動しました。終了するには 'exit' と入力してください。")
    print(f"ファイルは {filesystem_root} に保存されます。")
    
    # 状態を初期化
    state = ChatState(
        messages=[],
        tool_calls=[],
        tool_results=[],
        intermediate_steps=[],
        filesystem_root=filesystem_root
    )
    
    # チャットループ
    while True:
        try:
            user_input = input("\nあなた: ")
            if user_input.lower() == "exit":
                print("チャットボットを終了します。")
                break
            
            state["messages"].append({"role": "user", "content": user_input})
            state = graph.invoke(state)
            
            # 応答を表示
            assistant_messages = [msg for msg in state["messages"] if msg["role"] == "assistant"]
            if assistant_messages:
                print(f"アシスタント: {assistant_messages[-1]['content']}")
        except KeyboardInterrupt:
            print("\nプログラムを終了します...")
            sys.exit(0)
        except Exception as e:
            print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
