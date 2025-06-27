from .blockbeats_utils import fetch_news_from_blockbeats
from .coindesk_utils import fetch_news_from_coindesk
from .googlenews_utils import getNewsData
from .binance_utils import *
from .reddit_utils import fetch_top_from_category

from .interface import (
    # News and sentiment functions
    get_blockbeats_news,
    get_coindesk_news,
    get_google_news,
    get_reddit_global_news,
    get_reddit_company_news,
    # Financial statements functions
    # TODO
    # Technical analysis functions
    # TODO
    # Market data functions
    get_binance_data
)

__all__ = [
    # News and sentiment functions
    "get_blockbeats_news",
    "get_coindesk_news",
    "get_google_news",
    "get_reddit_global_news",
    "get_reddit_company_news",
    # Financial statements functions
    # TODO
    # Technical analysis functions
    # TODO
    # Market data functions
    "get_binance_data"
]
