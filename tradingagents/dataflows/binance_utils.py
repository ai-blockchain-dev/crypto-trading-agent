
from binance.um_futures import UMFutures

um_futures_client = UMFutures()

def fetch_klines_from_binance(symbol: str, interval: str, limit: int = 75):
    """
    Fetch historical klines (candlestick data) from Binance.

    :param symbol: The trading pair symbol (e.g., 'BTCUSDT').
    :param interval: The time interval for the klines (e.g., '1m', '5m', '1h').
    :param limit: The maximum number of klines to fetch (default is 75).
    :return: A list of klines. [ timestamp, open, high, low, close, volume, ... ]
    """
    return um_futures_client.klines(symbol=symbol, interval=interval, limit=limit)

def fetch_depth_from_binance(symbol: str, limit: int = 50):
    """
    Fetch the order book depth from Binance.

    :param symbol: The trading pair symbol (e.g., 'BTCUSDT').
    :param limit: The maximum number of bids and asks to fetch (default is 50).
    :return: A dictionary containing bids and asks. { "bids": [[price, quantity], ...], "asks": [[price, quantity], ...] }
    """
    return um_futures_client.depth(symbol=symbol, limit=limit)

def fetch_24hr_pricechange_from_binance(symbol: str):
    """
    Fetch 24-hour ticker price change statistics from Binance.

    :param symbol: The trading pair symbol (e.g., 'BTCUSDT').
    :return: A dictionary containing 24-hour statistics. { "priceChange": "...", "priceChangePercent": "...", "weightedAvgPrice": "...", ... }
    """
    return um_futures_client.ticker_24hr_price_change(symbol=symbol)

def fetch_toplongshort_position_ratio_from_binance(symbol: str, period: str, limit: int = 50):
    """
    Fetch the top long/short position ratio from Binance.

    :param symbol: The trading pair symbol (e.g., 'BTCUSDT').
    :param period: The time interval for the data (e.g., '1m', '5m', '1h').
    :param limit: The maximum number of records to fetch (default is 50).
    :return: A list of position ratios. [ { timestamp, longShortRatio, ... } ... ]
    """
    return um_futures_client.top_long_short_position_ratio(symbol=symbol, period=period, limit=limit)

def fetch_toplongshort_account_ratio_from_binance(symbol: str, period: str, limit: int = 50):
    """
    Fetch the top long/short account ratio from Binance.

    :param symbol: The trading pair symbol (e.g., 'BTCUSDT').
    :param period: The time interval for the data (e.g., '1m', '5m', '1h').
    :param limit: The maximum number of records to fetch (default is 50).
    :return: A list of account ratios. [ { timestamp, longShortRatio, ... } ... ]
    """
    return um_futures_client.top_long_short_account_ratio(symbol=symbol, period=period, limit=limit)

def fetch_global_longshort_account_ratio_from_binance(symbol: str, period: str, limit: int = 50):
    """
    Fetch the global long/short account ratio from Binance.

    :param symbol: The trading pair symbol (e.g., 'BTCUSDT').
    :param period: The time interval for the data (e.g., '1m', '5m', '1h').
    :param limit: The maximum number of records to fetch (default is 50).
    :return: A list of global account ratios. [ { timestamp, longShortRatio, ... } ... ]
    """
    return um_futures_client.long_short_account_ratio(symbol=symbol, period=period, limit=limit)

def fetch_taker_longshort_ratio_from_binance(symbol: str, period: str, limit: int = 50):
    """
    Fetch the taker long/short ratio from Binance.

    :param symbol: The trading pair symbol (e.g., 'BTCUSDT').
    :param period: The time interval for the data (e.g., '1m', '5m', '1h').
    :param limit: The maximum number of records to fetch (default is 50).
    :return: A list of taker ratios. [ { timestamp, buySellRatio, buyVol, sellVol, ... } ... ]
    """
    return um_futures_client.taker_long_short_ratio(symbol=symbol, period=period, limit=limit)