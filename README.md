# AI-Terminal-Assistant 🤖💻

A powerful command-line tool that brings AI intelligence directly to your terminal. Whether you're stuck on a complex `grep` command or need to debug a cryptic error message, AI-Terminal-Assistant is here to help.

## Features ✨
- **Ask Anything**: Get instant help with terminal commands and shell scripting.
- **Smart Debugging**: Paste your error messages and get intelligent suggestions for fixes.
- **Rich Output**: Beautifully formatted markdown responses in your terminal.

## Installation 🚀
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-terminal-assistant.git
   cd ai-terminal-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage 🛠️
### Ask for help:
```bash
python main.py ask "how do I find all files larger than 100MB in the current directory?"
```

### Debug an error:
```bash
python main.py debug "ModuleNotFoundError: No module named 'requests'"
```

## License 📄
MIT License
