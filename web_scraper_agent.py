from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from tools.tools import scrape_website_tool
from langchain import hub


def scrape_website(url):

    template = """
    Based on the entered URL address {url_address}, scrape the given website.
    """

    prompt_template = PromptTemplate(input_variables=["url_address"], template=template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    tools_for_agent = [
        Tool(name="Scrape single website",
             func=scrape_website_tool,
             description="use this tool for scraping single url address")
            ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(url_address=url)})

    scraped_website_data = result["output"]
    return scraped_website_data
