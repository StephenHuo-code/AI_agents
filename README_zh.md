# Smart Agent

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

### 开发者
```bash
pip install -r requirements.txt 
```

### 使用对话式Agent

```python
from src.agents import ConversationalAgent

# 初始化对话式agent
agent = ConversationalAgent()

# 启动聊天界面
agent.launch()
```

这将启动一个基于Gradio的聊天界面，您可以与AI助手进行交互。助手能够保持对话历史并提供上下文相关的回应。

主要特性：
- 基于Web的聊天界面
- 对话记忆功能
- 可配置的AI模型设置
- 易于集成自定义工具

## 参与贡献

我们欢迎各种形式的贡献！请查看贡献指南了解更多信息。

## 许可证

MIT许可证 - 详见LICENSE文件
