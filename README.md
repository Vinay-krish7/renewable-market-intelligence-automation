# Renewable Market Intelligence Automation

Automated renewable energy market intelligence pipeline built using Python, Selenium, and Claude AI to streamline renewable energy news aggregation, analysis, and content generation workflows.

The project scrapes renewable energy news headlines across solar, wind, and grid sectors from Mercom India, categorizes key developments, and generates structured analytical market summaries using Claude AI. The generated outputs can be used for internal business intelligence reports, monthly market magazines, or stakeholder communication updates.

---

# Features

- Automated web scraping of renewable energy news headlines
- Category-wise extraction across:
  - Solar
  - Wind
  - Grid & Power Markets
- AI-powered analytical content generation using Claude API
- Automated headline categorization and filtering
- JSON-based structured data storage
- Logging and exception handling
- Modular Python architecture
- Config-based project structure
- Automated report generation workflow

---

# Tech Stack

- Python
- Selenium
- Claude API (Anthropic)
- JSON
- Logging
- dotenv
- Chrome WebDriver

---

# Project Workflow

```text
Mercom India Website
        ↓
Selenium Web Scraping
        ↓
Headline Extraction & Categorization
        ↓
Structured JSON Processing
        ↓
Claude AI Content Generation
        ↓
Market Intelligence Report Output

```
---
# Project Structure

```text
renewable-market-intelligence-automation/
│
├── src/
│   ├── main.py
│   ├── data_scrapper.py
│   ├── content_gen.py
│   └── config.py
│
├── output/
│   ├── headlines.json
│   ├── summary.txt
│   └── log.txt
│
├── requirements.txt
├── .gitignore
└── README.md

```
---
## Key Capabilities

- Renewable energy market intelligence automation
- AI-assisted business reporting
- Renewable energy trend analysis
- Automated analytical content generation
- Structured data extraction and processing
- Workflow automation using Python
---
# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-repository-link>
cd renewable-market-intelligence-automation
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create `.env` File

Create a `.env` file in the project root directory:

```env
CLAUDE_API_KEY=your_api_key_here
```

---

## 5. Configure Chrome Driver

Make sure:
- Google Chrome is installed
- Chrome version matches ChromeDriver version

If using `webdriver-manager`, ChromeDriver installs automatically.

---

## 6. Run the Project

```bash
python src/main.py
```

---

## 7. Output Files Generated

```text
output/
│
├── headlines.json
├── summary.txt
└── log.txt
```
