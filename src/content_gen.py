
from anthropic import Anthropic
import os
from dotenv import load_dotenv
import config
import logging 

load_dotenv()

logging.basicConfig(
    filename = config.LOG_PATH,
    level = logging.INFO,
    format = '%(asctime)s-%(levelname)s-%(message)ss'

)
client = Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)



prompt = f"""
You are a renewable energy market analyst.

Analyze the following categorized headlines and divide the headlines into following sections:
1. Key regulatory updates
2. Market trends
3. Renewable energy business developments
4. Important pricing and investment trends

Select the 10 most relevant headlines from each category.

For EACH selected headline:
- Generate a separate professional analytical summary of 150–200 words
- Explain the business impact, market implications, and sector relevance
- Include important figures and statistics where relevant
- Maintain an engaging magazine-style analytical tone
- Avoid simply rewriting the headline
Headlines:
{json.dumps(all_articles, indent=2)}
"""
try:
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2500,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
except exception as e:
    logging.exception(f"Claude API failed: {e}")
    
if response.content:
   summary = response.content[0].text
else:
    logging.info("response not generated")
    summary = "No content generated"

with open(content_path,"w", encoding = "utf-8") as file1:
     file1.write(str(summary))