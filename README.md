# 🧠 Human-Like Memory AI Agent

An autonomous AI agent with human-like memory systems and genuine independent thinking. Unlike typical chatbots, this agent forms real opinions, makes predictions, and evolves its personality through conversations.

## ✨ Features

- **Three-Layer Memory System**: Short-term, long-term, and episodic memory like humans
- **Autonomous Thinking**: Forms genuine opinions and makes bold predictions
- **Personality Evolution**: Develops traits and opinions based on interactions
- **Memory Importance Scoring**: Automatically prioritizes emotional and personal information
- **Visual Memory Display**: See what the agent remembers in real-time
- **Cost-Effective**: Uses GPT-3.5-turbo for minimal API costs

## 🎯 What Makes This Different

This isn't just a chatbot. The agent:
- Makes predictions on uncertain topics (sports, stocks, events)
- Forms and defends opinions
- References past conversations naturally
- Disagrees when it has different views
- Evolves based on your interactions

**Example:**
```
You: "Will the 49ers win tomorrow?"
Agent: "Honestly? I think they'll dominate. Their defense has been crushing it, 
and even though their QB situation is shaky, their run game will carry them. 
My prediction: 49ers 27, Opponents 17. Let's see if I'm right!"
```

## 📋 Prerequisites

- **Python 3.6 or higher** (check with `python --version` or `python3 --version`)
- **OpenAI API Key** - Get one at [platform.openai.com](https://platform.openai.com)
- **Internet connection**
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

## 📦 Dependencies

**Good news**: No external dependencies needed! Uses only Python standard library:
- `http.server` - Built-in HTTP server
- `json` - JSON parsing
- `urllib` - HTTP requests

## 🚀 Installation & Setup

### Step 1: Download Files

Create a new folder and add these three files:

1. **server.py** - Python backend server
2. **index.html** - Frontend interface
3. **README.md** - This file

### Step 2: Verify Python Installation

Open terminal/command prompt and run:

```bash
python --version
```

or

```bash
python3 --version
```

You should see Python 3.6 or higher.

### Step 3: Get Your OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy it (starts with `sk-`)

## 🎮 Running the Application

### Start the Server

**On Windows:**
```bash
python server.py
```

**On Mac/Linux:**
```bash
python3 server.py
```

You should see:
```
🚀 Memory Agent Server Starting...
📡 Server running at http://localhost:3000
🌐 Open http://localhost:3000 in your browser
⛔ Press Ctrl+C to stop the server
```

### Access the Application

1. Open your web browser
2. Go to: `http://localhost:3000`
3. Enter your OpenAI API key when prompted
4. Start chatting!

## 💡 Usage Tips

### Training Your Agent

The agent learns from your conversations. To make it more personalized:

1. **Share personal information**: "My name is John, I love basketball"
2. **Express emotions**: The agent prioritizes emotional content
3. **Ask it to remember**: "Remember this: I hate mornings"
4. **Challenge its opinions**: It will refine its thinking

### Memory System

- **Short-term (5 messages)**: Recent context for ongoing conversation
- **Long-term (10 memories)**: Most important interactions (>60% importance)
- **Episodic (15 memories)**: Significant events and personal facts

Click the eye icon 👁️ to see the memory system in action!

### Cost Management

Using GPT-3.5-turbo costs approximately:
- **$0.0005** per 1,000 input tokens
- **$0.0015** per 1,000 output tokens

A typical conversation (100 messages) costs less than **$0.50**.

## 🛠️ Customization

### Change AI Model

Edit `server.py` and `index.html`, find:
```python
'model': 'gpt-3.5-turbo',
```

Change to:
- `gpt-4` - More intelligent (but expensive)
- `gpt-4-turbo` - Faster GPT-4
- `gpt-4o-mini` - Balanced option

### Adjust Personality Traits

In `index.html`, find:
```javascript
let agentPersonality = {
    name: 'Alex',
    traits: ['bold', 'opinionated', 'analytical', 'independent thinker'],
    opinions: {}
};
```

Customize the `name` and `traits` array!

### Tune Creativity

In `index.html`, adjust these values:
```javascript
temperature: 0.9,        // 0.0 = focused, 1.0 = creative
presence_penalty: 0.6,   // Encourages new topics
frequency_penalty: 0.3   // Reduces repetition
```

### Memory Limits

In `index.html`, find and adjust:
```javascript
memories.shortTerm = memories.shortTerm.slice(-5);   // Last 5 messages
memories.longTerm = memories.longTerm.slice(0, 10);  // Top 10 important
memories.episodic = memories.episodic.slice(-15);    // Last 15 episodes
```

## 🔧 Troubleshooting

### Port Already in Use

If port 3000 is taken, edit `server.py`:
```python
server = HTTPServer(('localhost', 3000), Handler)
```
Change `3000` to another port (e.g., `8000`, `5000`)

### API Key Errors

- **401 Unauthorized**: Invalid API key
- **429 Rate Limit**: Too many requests, wait a moment
- **Insufficient Quota**: Add credits at platform.openai.com/account/billing

### Server Won't Start

Make sure you're in the correct directory:
```bash
cd path/to/your/folder
python server.py
```

### CORS Errors (shouldn't happen)

This backend server handles CORS automatically. If you still see CORS errors:
1. Make sure you're accessing via `http://localhost:3000` (not file://)
2. Restart the server
3. Clear your browser cache

## 📁 Project Structure

```
memory-agent/
├── server.py      # Backend server handling OpenAI API calls
├── index.html     # Frontend interface with memory visualization
└── README.md      # This file
```

## 🔒 Security Notes

- Your API key is stored locally in your browser only
- The backend server runs on your computer only
- No data is sent anywhere except OpenAI's API
- Stop the server (Ctrl+C) when not in use

## 🎯 Example Conversations

**Sports Predictions:**
```
You: Who will win the Super Bowl?
Agent: Based on current performance, I'm betting on the Chiefs. 
Mahomes is unstoppable right now...
```

**Opinion Formation:**
```
You: What do you think about pineapple on pizza?
Agent: Honestly? It's divisive, but I'm team pineapple. 
The sweet-savory combo works if done right...
```

**Memory Reference:**
```
You: What do you remember about me?
Agent: Well, you told me you love basketball and hate mornings. 
You also asked about the 49ers game yesterday...
```

## 🚀 Future Enhancements

Ideas for extending this project:
- Add web search for real-time information
- Implement voice input/output
- Save conversation history to file
- Multi-user support with separate memories
- Integration with external APIs (weather, news, stocks)
- Personality A/B testing

## 📝 License

This is a learning project. Feel free to modify and extend it!

## 🤝 Contributing

This is your project to customize! Some ideas:
- Add emotion detection
- Implement memory decay over time
- Create personality presets
- Add conversation export feature

## 💬 Support

Having issues? Check:
1. Python version is 3.6+
2. Server is running on port 3000
3. API key is valid and has credits
4. Browser console for specific errors (F12)

---

**Built with**: Python standard library, Vanilla JavaScript, Tailwind CSS, OpenAI API

**Version**: 1.0.0

**Last Updated**: 2026

Enjoy your autonomous AI agent! 🎉
