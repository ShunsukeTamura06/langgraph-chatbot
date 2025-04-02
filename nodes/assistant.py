"""
アシスタントノード
LLMを呼び出してアシスタントの応答を生成するノード
"""
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolInvocation

from core.state import ChatState
from config.config import MODEL_NAME, TEMPERATURE, SYSTEM_MESSAGE_TEMPLATE

def assistant(state: ChatState) -> ChatState:
    """
    アシスタントノード - LLMを呼び出して応答を生成
    
    Args:
        state: 現在の状態
        
    Returns:
        更新された状態
    """
    # OpenAIのモデルを初期化
    model = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)
    
    # メッセージをフォーマット
    messages = state["messages"].copy()
    
    # ツール結果が存在する場合は追加
    if state.get("tool_results") and len(state["tool_results"]) > 0:
        for tool_result in state["tool_results"]:
            tool_message = {
                "role": "tool",
                "tool_call_id": tool_result["tool_call_id"],
                "content": str(tool_result["content"]),
            }
            messages.append(tool_message)
    
    # システムメッセージを追加
    system_message = {
        "role": "system",
        "content": SYSTEM_MESSAGE_TEMPLATE.format(root_dir=state["filesystem_root"])
    }
    
    # システムメッセージをメッセージリストの先頭に追加
    messages = [system_message] + messages
    
    # モデルを呼び出して応答を取得
    response = model.invoke(messages)
    
    # ツール呼び出しがある場合はそれを抽出
    tool_calls = []
    if hasattr(response, "tool_calls") and response.tool_calls:
        for tool_call in response.tool_calls:
            tool_calls.append(
                ToolInvocation(
                    tool=tool_call.function.name,
                    tool_input=tool_call.function.arguments,
                    id=tool_call.id,
                )
            )
    
    # アシスタントのメッセージを状態に追加
    state["messages"].append({
        "role": "assistant",
        "content": response.content if response.content else "",
        "tool_calls": response.tool_calls if hasattr(response, "tool_calls") else []
    })
    
    # ツール呼び出しがあれば保存
    if tool_calls:
        state["tool_calls"] = tool_calls
    else:
        state["tool_calls"] = []
    
    return state
