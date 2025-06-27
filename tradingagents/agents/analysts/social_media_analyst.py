from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json
from tradingagents.i18n import get_prompts

def create_social_media_analyst(llm, toolkit):
    def social_media_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]
        company_name = state["company_of_interest"]

        tools = [
            toolkit.get_stock_news_openai,
            toolkit.get_reddit_stock_info
        ]

        system_message = (
            get_prompts("analysts", "social_media_analyst", "system_message")
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    get_prompts("analysts", "template")
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(ticker=ticker)

        chain = prompt | llm.bind_tools(tools)

        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "sentiment_report": report,
        }

    return social_media_analyst_node
