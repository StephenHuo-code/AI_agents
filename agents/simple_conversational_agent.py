"""
简单对话代理实现

本文件实现了一个基于 LangChain 和 OpenAI 的对话代理系统，主要功能包括：
1. 基于 GPT 模型的自然语言对话能力
2. 支持多轮对话的历史记录管理
3. 提供基于 Gradio 的简单 Web 交互界面
"""



"""
LangChain 和 OpenAI 相关接口说明：
1. ChatOpenAI: OpenAI 聊天模型的接口封装，用于与 GPT 模型交互
2. RunnableWithMessageHistory: 为对话链添加消息历史管理功能的包装器
3. ChatMessageHistory: 用于存储和管理对话历史记录的类
4. ChatPromptTemplate: 用于构建结构化的对话提示模板
5. MessagesPlaceholder: 在提示模板中为历史消息创建占位符
"""

# 导入必要的包
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from dotenv import load_dotenv
import gradio as gr

# 设置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

# 初始化ChatOpenAI实例
llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=1000, temperature=0)

# 创建存储聊天历史的字典
store = {}

# 获取或创建聊天历史的函数
def get_chat_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# 设置聊天提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),  # 系统提示
    MessagesPlaceholder(variable_name="history"),   # 历史消息占位符
    ("human", "{input}")                           # 用户输入
])

# 创建基础对话链
chain = prompt | llm

# 创建带有消息历史的对话链
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_chat_history,
    input_messages_key="input",
    history_messages_key="history"
)

# 添加一个打印聊天历史的函数
def print_chat_history(session_id: str):
    if session_id in store:
        history = store[session_id]
        messages = history.messages
        print(f"\n=== Chat History for Session {session_id} ===")
        for msg in messages:
            print(f"{msg.type}: {msg.content}\n")
    else:
        print(f"No history found for session {session_id}")

# 修改 chat 函数来包含历史记录打印
def chat(message, history):
    session_id = "user_123"
    
    response = chain_with_history.invoke(
        {"input": message},
        config={"configurable": {"session_id": session_id}}
    )
    
    # 在每次对话后打印历史记录
    #print_chat_history(session_id)
    
    return response.content

# 创建Gradio界面
demo = gr.ChatInterface(
    chat,
    title="AI Assistant",
    description="Chat with your AI assistant. The assistant remembers your conversation history.",
    theme="soft",
)

# 启动Gradio应用
if __name__ == "__main__":
    demo.launch()