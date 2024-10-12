from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_block import GetBlock
from openapi_server.models.get_block_request import GetBlockRequest
from openapi_server.models.get_ethereum_balance import GetEthereumBalance
from openapi_server.models.get_ethereum_balance_request import GetEthereumBalanceRequest
from openapi_server.models.get_exchange_rate import GetExchangeRate
from openapi_server.models.get_exchange_rate_request import GetExchangeRateRequest
from openapi_server.models.get_gas_price import GetGasPrice
from openapi_server.models.get_last_block_number import GetLastBlockNumber
from openapi_server.models.get_token import GetToken
from openapi_server.models.get_token_balance import GetTokenBalance
from openapi_server.models.get_token_balance_request import GetTokenBalanceRequest
from openapi_server.models.get_token_request import GetTokenRequest
from openapi_server.models.get_transactions import GetTransactions
from openapi_server.models.get_transactions_request import GetTransactionsRequest
from openapi_server import util


async def get_block(request: web.Request, authorization, body) -> web.Response:
    """getBlock

    Returns information of an ethereum block with or without transactions

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetBlockRequest.from_dict(body)
    return web.Response(status=200)


async def get_ethereum_balance(request: web.Request, authorization, body) -> web.Response:
    """getEthereumBalance

    Returns the ethereum balance of a given address.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetEthereumBalanceRequest.from_dict(body)
    return web.Response(status=200)


async def get_exchange_rate(request: web.Request, authorization, body) -> web.Response:
    """getExchangeRate

    Returns the current Ethereum price in Euro or US Dollar.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetExchangeRateRequest.from_dict(body)
    return web.Response(status=200)


async def get_gas_price(request: web.Request, content_type, authorization) -> web.Response:
    """getGasPrice

    Returns the current gas price in GWEI.

    :param content_type: 
    :type content_type: str
    :param authorization: API Key
    :type authorization: str

    """
    return web.Response(status=200)


async def get_last_block_number(request: web.Request, content_type, authorization) -> web.Response:
    """getLastBlockNumber

    Returns the block number of the last mined ethereum block.

    :param content_type: 
    :type content_type: str
    :param authorization: API Key
    :type authorization: str

    """
    return web.Response(status=200)


async def get_token(request: web.Request, authorization, body) -> web.Response:
    """getToken

    Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetTokenRequest.from_dict(body)
    return web.Response(status=200)


async def get_token_balance(request: web.Request, authorization, body) -> web.Response:
    """getTokenBalance

    Returns the token balance of a given address.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetTokenBalanceRequest.from_dict(body)
    return web.Response(status=200)


async def get_transactions(request: web.Request, authorization, body) -> web.Response:
    """getTransactions

    Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetTransactionsRequest.from_dict(body)
    return web.Response(status=200)
