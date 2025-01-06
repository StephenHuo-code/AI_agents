# AI Agents

[English](README.md)

这是一个面向研究的AI Agent框架，专注于实践应用和可扩展架构的探索与实现。

## 特性

- 🤖 模块化的Agent架构
- 🛠️ 可扩展的工具集成
- 🔄 灵活的工作流管理
- 📊 性能监控
- 🧪 便捷的实验支持

## 环境要求

- Python 3.10+
- pip 或其他包管理器

## 安装说明

### 普通用户
```bash
pip install -r requirements.txt
```

### 简单对话代理实现

#### 功能说明
本文件实现了一个基于 LangChain 和 OpenAI 的对话代理系统，主要功能包括：
1. 基于 GPT 模型的自然语言对话能力
2. 支持多轮对话的历史记录管理
3. 提供基于 Gradio 的简单 Web 交互界面

#### 主要组件
1. ChatOpenAI: OpenAI 聊天模型的接口封装，用于与 GPT 模型交互
2. RunnableWithMessageHistory: 为对话链添加消息历史管理功能的包装器
3. ChatMessageHistory: 用于存储和管理对话历史记录的类
4. ChatPromptTemplate: 用于构建结构化的对话提示模板
5. MessagesPlaceholder: 在提示模板中为历史消息创建占位符

```shell
python agents/simple_conversational_agent.py
```


#### Function Calling Agent 说明

#### 核心功能：
1. 文本摘要：使用 GPT 模型对输入文本进行智能摘要
2. 中文翻译：将英文文本自动翻译成中文
3. 工具链组合：通过 StructuredTool 将摘要和翻译功能封装为可调用的工具
4. 自动化处理：Agent 可以自动决策使用适当的工具完成任务

####主要组件：
1. AgentExecutor: 负责执行代理任务的执行器
2. StructuredTool: 将函数包装为结构化工具
3. PromptTemplate: 定义代理行为的提示模板


```shell
python agents/function_calling_agent.py
```

## 参与贡献

我们欢迎各种形式的贡献！请查看贡献指南了解更多信息。

## 许可证

MIT许可证 - 详见LICENSE文件
