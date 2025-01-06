# AI Agents

[中文文档](README_zh.md)

A research-oriented framework for exploring and implementing AI agents, focusing on practical applications and extensible architectures.

## Features

- 🤖 Modular agent architecture
- 🛠️ Extensible tool integration
- 🔄 Flexible workflow management
- 📊 Performance monitoring
- 🧪 Easy experimentation

## Requirements

- Python 3.10+
- pip or your preferred package manager

## Installation

### For Users
```bash
pip install -r requirements.txt
```

### Simple Conversational Agent

#### Features
This implementation uses LangChain and OpenAI to create a conversational agent system with:
1. Natural language dialogue capabilities based on GPT models
2. Multi-turn conversation history management
3. Simple web interface using Gradio

#### Key Components
1. ChatOpenAI: Interface wrapper for OpenAI chat model interactions
2. RunnableWithMessageHistory: Wrapper for adding message history management to conversation chains
3. ChatMessageHistory: Class for storing and managing conversation history
4. ChatPromptTemplate: For building structured conversation prompts
5. MessagesPlaceholder: Creates placeholders for historical messages in prompt templates

```shell
python agents/simple_conversational_agent.py
```

#### Function Calling Agent Details

#### Core Features:
1. Text Summarization: Intelligent text summarization using GPT models
2. Chinese Translation: Automatic translation of English text to Chinese
3. Tool Chain Integration: Summary and translation functions packaged as callable tools via StructuredTool
4. Automated Processing: Agent automatically decides which tools to use for task completion

#### Main Components:
1. AgentExecutor: Responsible for executing agent tasks
2. StructuredTool: Wraps functions as structured tools
3. PromptTemplate: Defines agent behavior templates

```shell
python agents/function_calling_agent.py
```

## Contributing

We welcome contributions! Please see our contributing guidelines for more information.

## License

MIT License - see LICENSE file for details
