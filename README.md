# Smart Agent

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

### For Developers
```bash
pip install -r requirements.txt -r requirements-dev.txt
```


### Using the Conversational Agent

```python
from src.agents import ConversationalAgent

# Initialize the conversational agent
agent = ConversationalAgent()

# Start the chat interface
agent.launch()
```

This will launch a Gradio-based chat interface where you can interact with the AI assistant. The assistant maintains conversation history and provides contextual responses.

Key features:
- Web-based chat interface
- Conversation memory
- Configurable AI model settings
- Easy integration with custom tools

## Contributing

We welcome contributions! Please see our contributing guidelines for more information.

## License

MIT License - see LICENSE file for details
