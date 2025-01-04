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

def chat(message, history):
    # 使用固定的session_id，或者可以基于用户信息生成
    session_id = "user_123"
    
    response = chain_with_history.invoke(
        {"input": message},
        config={"configurable": {"session_id": session_id}}
    )
    
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