# simple-llm-chat

This project is a minimal Python script demonstrating how to interact with the [A4F API](https://a4f.co) using an OpenAI-compatible client. It securely loads your API credentials from a `.env` file, sends a simple chat prompt to the model, and prints the response.

## 📦 Installation

To get started, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KirtanUgreja/simple-llm-chat.git
   ```
   
2. **Install dependencies:**

   ```bash
   pip install openai 
   ```

3. **Insert your a4f api key**

   ```bash
   a4f_api_key = "your_a4f_api_key_here"
   ```

## 🚀 Usage

Simply run the script with:

```bash
python llmchat.py
```

This will send a test message (`"Why?"`) to the `provider-2/gpt-3.5-turbo` model via A4F and print the response to the terminal.

### Example Output:

```
Because it's a fundamental question.
```

## ✨ Features

- Connects to A4F's OpenAI-compatible LLM endpoint
- Uses the OpenAI Python SDK for communication
- Secures API keys using `.env` file loading via `dotenv`
- Simple and beginner-friendly structure for easy customization

## 🧰 Technologies Used

- **OpenAI Python SDK:** Interact with OpenAI-compatible APIs like A4F's
- **python-dotenv:** Load environment variables from a `.env` file
- **A4F API:** A language model provider with OpenAI API compatibility

## 🤝 Contributing

This repository is intended as a learning or starting point. Contributions are welcome! If you improve the script or add new functionality, feel free to fork the repo and open a pull request.
