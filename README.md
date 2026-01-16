
---

# 📊 Autonomous Market Research Bot

A streamlined AI-powered tool that summarizes competitor information from CSV data or live web pages using OpenAI GPT. Designed for analysts, marketers, and competitive intelligence teams to **automate market research** with ease.

---

## 🚀 Overview

This project uses:

* 🧠 **OpenAI GPT-3.5** for intelligent summarization of competitor descriptions
* 🧼 **BeautifulSoup + Selenium** for optional website scraping
* 🎛️ **Streamlit** for an interactive web interface
* 🔐 `.env` + `python-dotenv` for secure API key handling

---

## 🧠 Example Use Cases

* Generate 1-line summaries of competitors
* Extract key differentiators for market mapping
* Automate landscape reports from scraped text or CSV data

---

## 📄 Sample Input Format

Upload a CSV file with at least these 3 columns:

| company      | description                                                       | website                                              |
| ------------ | ----------------------------------------------------------------- | ---------------------------------------------------- |
| Competitor A | Offers AI-driven automation platforms for finance and operations. | [https://www.companya.com](https://www.companya.com) |
| Competitor B | Provides supply chain optimization tools for retail businesses.   | [https://www.companyb.com](https://www.companyb.com) |

---

## 📤 Example Output (After Summarization)

| company      | summary                                                  |
| ------------ | -------------------------------------------------------- |
| Competitor A | AI-based automation tools for finance and ops.           |
| Competitor B | End-to-end supply chain solutions for retail businesses. |

---

## 📦 How to Run the Project

### ✅ 1. Clone the repository

```bash
git clone https://github.com/amitkharche/agents_market_research_bot.git
cd agents_market_research_bot
```

### ✅ 2. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure Chrome and `chromedriver` are installed if you plan to use web scraping.

### ✅ 3. Add your OpenAI API key in `.env`

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### ✅ 4. Run the Streamlit App

```bash
streamlit run app/app.py
```

---

## 📁 Project Structure

```
market-research-bot/
├── app/
│   └── app.py                  # Streamlit interface
├── data/
│   └── sample_input.csv        # Example input with 25 companies
├── src/
│   ├── summarizer.py           # Summarization via OpenAI GPT
│   └── scraper.py              # Optional website content scraper
├── .env                        # API key (not committed)
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🐳 Optional: Run with Docker

```bash
docker build -t market-research-bot .
docker run -p 8501:8501 market-research-bot
```

Make sure to bind your `.env` or pass the OpenAI API key securely in the container.

---

## 🧪 Future Enhancements

* 🔍 Extract keywords and categories using GPT
* 📊 Cluster summaries by themes or value propositions
* 🌐 Auto-scrape from `website` column and summarize
* 📥 Upload PDFs and DOCX files for summarization

---

## 🧑‍💻 Author

Built by \[Amit Kharche]
[LinkedIn](https://www.linkedin.com/in/amitkharche)
[GitHub](https://github.com/amitkharche)
[Medium](https://medium.com/@amitkharche)


---

