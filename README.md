# AI Agents

[中文](README_zh.md)

A research-oriented AI Agent framework focused on practical applications and exploration of extensible architecture.

## Features

- 🤖 Modular Agent Architecture
- 🛠️ Extensible Tool Integration
- 🔄 Flexible Workflow Management
- 📊 Performance Monitoring
- 🧪 Convenient Experiment Support

## Requirements

- Python 3.10+
- pip or other package managers

## Installation

### For Users
```bash
pip install -r requirements.txt
```

### Agents Description

#### 1. Simple Conversational Agent

# Features #
This module implements a conversational agent system based on LangChain and OpenAI, with the following main features:
1. Natural language conversation capability based on GPT models
2. Multi-turn conversation history management
3. Simple Web interface based on Gradio

# Core Components #
1. ChatOpenAI: Interface wrapper for OpenAI chat model, used for GPT model interaction
2. RunnableWithMessageHistory: Wrapper that adds message history management to conversation chains
3. ChatMessageHistory: Class for storing and managing conversation history
4. ChatPromptTemplate: Used for building structured conversation prompt templates
5. MessagesPlaceholder: Creates placeholders for historical messages in prompt templates

```shell
python agents/simple_conversational_agent.py
```

#### 2. Function Calling Agent

# Features #
1. Text Summarization: Uses GPT models for intelligent text summarization
2. Chinese Translation: Automatically translates English text to Chinese
3. Tool Chain Integration: Encapsulates summarization and translation features as callable tools using StructuredTool
4. Automated Processing: Agent can automatically decide which tools to use to complete tasks

# Core Components #
1. AgentExecutor: Executor responsible for running agent tasks
2. StructuredTool: Wraps functions as structured tools
3. PromptTemplate: Defines agent behavior through prompt templates

```shell
python agents/function_calling_agent.py
```

## Contributing

We welcome all forms of contributions! Please check the contribution guidelines for more information.

## License

MIT License - See LICENSE file for details
