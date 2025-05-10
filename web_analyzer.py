from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.web_scraper_agent import scrape_website as scrape_website_agent


def analyze_website_data(url: str):
    web_content = scrape_website_agent(url=url)

    analyze_template = """
    Based on the following scraped content {web_content} of the website, generate a summary that can be displayed in the user interface.

    1. Briefly summarize what the page is about.
    2. List the 3–5 most important pieces of information found on the page.
    3. If possible, indicate the type of page (e.g. corporate, e-shop, blog, portfolio...)
    4. Use clear and structured output, suitable for display in the UI.
    5. Answer in Slovak language

    """

    analyze_prompt_template = PromptTemplate(input_variables=["web_content"], template=analyze_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain = analyze_prompt_template | llm

    response = chain.invoke(input={"web_content": web_content})

    return response.content


if __name__ == "__main__":
    print("Hello")
    analyze_website_data("WRITE_YOUR_URL")


