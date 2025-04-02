"""
視覚化ユーティリティモジュール
グラフの視覚化に関する機能を提供します
"""
import os
from langgraph.graph import StateGraph

def visualize_graph(builder, output_file="graph"):
    """
    グラフを視覚化してファイルに出力する関数
    
    Args:
        builder: StateGraphのビルダーまたはインスタンス
        output_file: 出力ファイル名（拡張子なし）
    
    Returns:
        None
    """
    try:
        import graphviz
        # グラフの視覚化
        dot = graphviz.Digraph(comment="LangGraph Chatbot Graph")
        
        # ノードを追加
        for node in builder.nodes:
            dot.node(node, node)
        
        # END状態を追加
        dot.node("END", "END", shape="doublecircle")
        
        # エッジを追加
        for edge in builder.edges:
            source = edge[0]
            target = edge[1]
            if target is not None:
                dot.edge(source, target)
            else:
                # 終了エッジの場合
                dot.edge(source, "END")
        
        # 条件付きエッジを追加
        if hasattr(builder, "conditional_edges"):
            for source, condition_func, targets in builder.conditional_edges:
                for target_key, target in targets.items():
                    if target is not None:
                        dot.edge(source, target, label=target_key)
                    else:
                        dot.edge(source, "END", label=target_key)
        
        # ファイルに保存
        dot.render(output_file, format="png", cleanup=True)
        return True
    except ImportError:
        print("グラフ視覚化にはgraphvizが必要です: pip install graphviz")
        return False
    except Exception as e:
        print(f"グラフの視覚化中にエラーが発生しました: {e}")
        return False

def visualize_trace(checkpointer, output_file="trace.html"):
    """
    実行トレースを視覚化してHTMLファイルに出力する
    
    Args:
        checkpointer: チェックポインターオブジェクト
        output_file: 出力ファイル名
        
    Returns:
        成功した場合はTrue、失敗した場合はFalse
    """
    try:
        from langgraph.trace import visualize
        visualize.write_html(checkpointer, output_file)
        return True
    except ImportError:
        print("トレース視覚化にはlanggraphの最新バージョンが必要です")
        return False
    except Exception as e:
        print(f"トレースの視覚化中にエラーが発生しました: {e}")
        return False
