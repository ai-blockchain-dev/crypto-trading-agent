from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, AIMessage
from typing import List
from typing import Annotated
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import RemoveMessage
from langchain_core.tools import tool
from datetime import date, timedelta, datetime
import functools
import pandas as pd
import os
from dateutil.relativedelta import relativedelta
from langchain_openai import ChatOpenAI
import tradingagents.dataflows.interface as interface
from tradingagents.default_config import DEFAULT_CONFIG
from langchain_core.messages import HumanMessage


def create_msg_delete():
    def delete_messages(state):
        """Clear messages and add placeholder for Anthropic compatibility"""
        messages = state["messages"]
        
        # Remove all messages
        removal_operations = [RemoveMessage(id=m.id) for m in messages]
        
        # Add a minimal placeholder message
        placeholder = HumanMessage(content="Continue")
        
        return {"messages": removal_operations + [placeholder]}
    
    return delete_messages


class Toolkit:
    _config = DEFAULT_CONFIG.copy()

    @classmethod
    def update_config(cls, config):
        """Update the class-level configuration."""
        cls._config.update(config)

    @property
    def config(self):
        """Access the configuration."""
        return self._config

    def __init__(self, config=None):
        if config:
            self.update_config(config)

    @staticmethod
    @tool
    def get_blockbeats_news(
        count: Annotated[int, "Number of news articles to retrieve, no more than 30"] = 10,
    ) -> str:
        """
        Retrieve the latest news from BlockBeats, especially useful for Cryptos.
        Args:
            count (int): Number of news articles to retrieve, no more than 30
        Returns:
            str: A formatted string containing the latest news from BlockBeats.
        """
        blockbeats_news_result = interface.get_blockbeats_news(count)
        return blockbeats_news_result
    
    @staticmethod
    @tool
    def get_coindesk_news(
        tickers: Annotated[
            List[str],
            "List of tickers to get news for, e.g. ['BTC', 'ETH']",
        ] = [],
        count: Annotated[int, "Number of news articles to retrieve, default is 10"] = 10,
    ) -> str:
        """
        Retrieve the latest news from Coindesk for a given list of tickers.
        Args:
            tickers (List[str]): List of tickers to get news for, e.g. ['BTC', 'ETH']
            count (int): Number of news articles to retrieve, default is 10
        Returns:
            str: A formatted string containing the latest news from Coindesk for the specified tickers.
        """
        coindesk_news_result = interface.get_coindesk_news(tickers, count)
        return coindesk_news_result
    
    @staticmethod
    @tool
    def get_binance_ohlcv(
        symbol: Annotated[str, "ticker symbol of the asset"],
        interval: Annotated[
            str,
            "Interval for the data, e.g. '1m', '5m', '1h', '1d'",
        ] = "15m",
    ) -> str:
        """
        Retrieve the latest OHLCV data from Binance for a given symbol and interval.
        Args:
            symbol (str): Ticker symbol of the asset, e.g. 'BTCUSDT'
            interval (str): Interval for the data, e.g. '1m', '5m', '1h', '1d'
        Returns:
            str: A formatted string containing the latest OHLCV data from Binance for the specified symbol and interval.
        """
        binance_ohlcv_result = interface.get_binance_ohlcv(symbol, interval)
        return binance_ohlcv_result
    
    @staticmethod
    @tool
    def get_binance_data(
        symbol: Annotated[str, "ticker symbol of the asset"],
        interval: Annotated[
            str,
            "Interval for the data, e.g. '1m', '5m', '1h', '1d'",
        ] = "15m",
    ) -> str:
        """
        Retrieve the latest market data from Binance for a given symbol and interval.
        Args:
            symbol (str): Ticker symbol of the asset, e.g. 'BTCUSDT'
            interval (str): Interval for the data, e.g. '1m', '5m', '1h', '1d'
        Returns:
            str: A formatted string containing the latest market data from Binance for the specified symbol and interval.
        """
        binance_data_result = interface.get_binance_data(symbol, interval)
        return binance_data_result
    
    @staticmethod
    @tool
    def get_fear_and_greed_index() -> str:
        """
        Get current crypto market Fear and Greed Index. 0 means "Extreme Fear", while 100 means "Extreme Greed"
        Returns:
            str: A formatted string containing the current crypto market Fear and Greed Index.
        """
        return interface.get_fear_and_greed_index()
    
    @staticmethod
    @tool
    def get_reddit_news(
        curr_date: Annotated[str, "Date you want to get news for in yyyy-mm-dd format"],
    ) -> str:
        """
        Retrieve global news from Reddit within a specified time frame.
        Args:
            curr_date (str): Date you want to get news for in yyyy-mm-dd format
        Returns:
            str: A formatted dataframe containing the latest global news from Reddit in the specified time frame.
        """
        
        global_news_result = interface.get_reddit_global_news(curr_date, 7, 5)

        return global_news_result

    @staticmethod
    @tool
    def get_reddit_stock_info(
        ticker: Annotated[
            str,
            "Ticker of a company. e.g. AAPL, TSM",
        ],
        curr_date: Annotated[str, "Current date you want to get news for"],
    ) -> str:
        """
        Retrieve the latest news about a given stock from Reddit, given the current date.
        Args:
            ticker (str): Ticker of a company. e.g. AAPL, TSM
            curr_date (str): current date in yyyy-mm-dd format to get news for
        Returns:
            str: A formatted dataframe containing the latest news about the company on the given date
        """

        stock_news_results = interface.get_reddit_company_news(ticker, curr_date, 7, 5)

        return stock_news_results

    @staticmethod
    @tool
    def get_google_news(
        query: Annotated[str, "Query to search with"],
        curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    ):
        """
        Retrieve the latest news from Google News based on a query and date range.
        Args:
            query (str): Query to search with
            curr_date (str): Current date in yyyy-mm-dd format
            look_back_days (int): How many days to look back
        Returns:
            str: A formatted string containing the latest news from Google News based on the query and date range.
        """

        google_news_results = interface.get_google_news(query, curr_date, 7)

        return google_news_results

    @staticmethod
    @tool
    def get_stock_news_openai(
        ticker: Annotated[str, "the company's ticker"],
        curr_date: Annotated[str, "Current date in yyyy-mm-dd format"],
    ):
        """
        Retrieve the latest news about a given stock by using OpenAI's news API.
        Args:
            ticker (str): Ticker of a company. e.g. AAPL, TSM
            curr_date (str): Current date in yyyy-mm-dd format
        Returns:
            str: A formatted string containing the latest news about the company on the given date.
        """

        openai_news_results = interface.get_stock_news_openai(ticker, curr_date)

        return openai_news_results

    @staticmethod
    @tool
    def get_global_news_openai(
        curr_date: Annotated[str, "Current date in yyyy-mm-dd format"],
    ):
        """
        Retrieve the latest macroeconomics news on a given date using OpenAI's macroeconomics news API.
        Args:
            curr_date (str): Current date in yyyy-mm-dd format
        Returns:
            str: A formatted string containing the latest macroeconomic news on the given date.
        """

        openai_news_results = interface.get_global_news_openai(curr_date)

        return openai_news_results

    @staticmethod
    @tool
    def get_fundamentals_openai(
        ticker: Annotated[str, "the company's ticker"],
        curr_date: Annotated[str, "Current date in yyyy-mm-dd format"],
    ):
        """
        Retrieve the latest fundamental information about a given stock on a given date by using OpenAI's news API.
        Args:
            ticker (str): Ticker of a company. e.g. AAPL, TSM
            curr_date (str): Current date in yyyy-mm-dd format
        Returns:
            str: A formatted string containing the latest fundamental information about the company on the given date.
        """

        openai_fundamentals_results = interface.get_fundamentals_openai(
            ticker, curr_date
        )

        return openai_fundamentals_results
