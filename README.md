# Crypto Trading Agents 🤖💰

> Your AI-powered trading desk that analyzes crypto markets 24/7. Get professional-grade reports combining technical analysis, news sentiment, and market data—all tailored to your trading style.

---

## ✨ What Makes This Special

**🎯 Real Data, Real Analysis**  
No fluff—we pull actual technical indicators (RSI, MACD, Bollinger Bands) from professional platforms, not just LLM guesses.

**📰 Trader-Focused News**  
Aggregates news from sources crypto traders actually use: CoinDesk, Reddit, Blockbeats, and more.

**💼 Your Style, Your Report**  
Define your risk tolerance and trading strategy. Get reports that match whether you're a day trader or a HODLer.

**🔄 Never Lose Progress**  
Reports stream to log files in real-time. Even if something crashes, your analysis is saved—no wasted API calls.

**📧 Automated Intelligence**  
Schedule reports to hit your inbox daily. Wake up to market insights like you're running a trading floor.

---

## 🚀 Quick Start

### 1. Install
```bash
git clone https://github.com/ai-blockchain-dev/crypto-trading-agent.git
cd TradingAgents

# Create environment
conda create -n tradingagents python=3.13
conda activate tradingagents

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure
Create `./cli/.env` and add your API keys:
```bash
# LLM (choose one)
DASHSCOPE_API_KEY=your_key_here      # For Qwen
# OR
OPENAI_API_KEY=your_key_here         # For ChatGPT

# Optional: Data source APIs (see table below)
TAAPI_API_KEY=your_key_here
COINDESK_API_KEY=your_key_here
# ... etc
```

### 3. Run
**Interactive Mode:**
```bash
python -m cli.main
```
Follow the prompts—enter your coin (BTC, ETH, etc.), pick analysts, and generate your report.

**Automated Mode:**
```bash
# Edit ./cli/run.py with your settings, then:
python -m cli.run
```

---

## 📊 Data Sources

| Source | What You Get | API Key Needed? |
|--------|--------------|-----------------|
| **Binance** | Live price data, K-lines, market depth | ❌ Free |
| **taapi.io** | Technical indicators (RSI, MACD, EMA, etc.) | ✅ [Get one](https://taapi.io/my-account/) |
| **Alternative.me** | Fear & Greed Index | ❌ Free |
| **CoinDesk** | Crypto news | ✅ [Register](https://developers.coindesk.com/settings/api-keys) |
| **Reddit** | Social sentiment | ✅ [Create app](https://old.reddit.com/prefs/apps/) |
| **Blockbeats** | Chinese crypto news | ❌ Free |
| **CoinStats** | News aggregation | ✅ [Sign up](https://openapi.coinstats.app) |

> 💡 **Tip:** Many sources work without API keys. Start with the free ones!

---

## 🎨 Customization

**Change Language/Settings:**  
Edit [`./tradingagents/default_config.py`](./tradingagents/default_config.py)

**Add Your Trading Preferences:**  
Create `./cli/investment_preferences` to define your risk profile

**Modify Prompts:**  
Edit files in [`./tradingagents/i18n/prompts`](./tradingagents/i18n/prompts)

**Add Data Sources:**  
See [`./tradingagents/dataflows/README.md`](./tradingagents/dataflows/README.md) for the guide

---

## 🤖 Supported LLMs

| Model | API Variable | Status |
|-------|--------------|--------|
| Qwen (Alibaba) | `DASHSCOPE_API_KEY` | ✅ Tested |
| ChatGPT (OpenAI) | `OPENAI_API_KEY` | ✅ Tested |

---

## 🔮 What's Coming

- [x] LLM-powered web search
- [x] Automated email delivery
- [ ] Freqtrade integration for backtesting
- [ ] More LLM options (DeepSeek, etc.)
- [ ] Web UI interface
- [ ] Enhanced prompt engineering

---

## ⚠️ Disclaimer

**This is research software, not financial advice.** Use at your own risk. Always do your own research before making trading decisions.

---

## 🤝 Contributing

We love contributions! Found a bug? Want a feature? Have ideas? Open an issue or submit a PR.

**⭐ Star us if this project helps you! ⭐**
