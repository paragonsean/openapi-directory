from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_get_token_balance_output import BatchGetTokenBalanceOutput
from openapi_server.models.batch_get_token_balance_request import BatchGetTokenBalanceRequest
from openapi_server.models.get_token_balance_output import GetTokenBalanceOutput
from openapi_server.models.get_token_balance_request import GetTokenBalanceRequest
from openapi_server.models.get_transaction_output import GetTransactionOutput
from openapi_server.models.get_transaction_request import GetTransactionRequest
from openapi_server.models.list_token_balances_output import ListTokenBalancesOutput
from openapi_server.models.list_token_balances_request import ListTokenBalancesRequest
from openapi_server.models.list_transaction_events_output import ListTransactionEventsOutput
from openapi_server.models.list_transaction_events_request import ListTransactionEventsRequest
from openapi_server.models.list_transactions_output import ListTransactionsOutput
from openapi_server.models.list_transactions_request import ListTransactionsRequest
from openapi_server import util


async def batch_get_token_balance(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_token_balance

    &lt;p&gt;Gets the token balance for a batch of tokens by using the &lt;code&gt;GetTokenBalance&lt;/code&gt; action for every token in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the native tokens BTC,ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchGetTokenBalanceRequest.from_dict(body)
    return web.Response(status=200)


async def get_token_balance(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_token_balance

    &lt;p&gt;Gets the balance of a specific token, including native tokens, for a given address (wallet or contract) on the blockchain.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the native tokens BTC,ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetTokenBalanceRequest.from_dict(body)
    return web.Response(status=200)


async def get_transaction(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_transaction

    Get the details of a transaction.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def list_token_balances(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_token_balances

    &lt;p&gt;This action returns the following for a given a blockchain network:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Lists all token balances owned by an address (either a contact address or a wallet address).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lists all token balances for all tokens created by a contract.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lists all token balances for a given token.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;You must always specify the network property of the &lt;code&gt;tokenFilter&lt;/code&gt; when using this operation.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTokenBalancesRequest.from_dict(body)
    return web.Response(status=200)


async def list_transaction_events(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_transaction_events

    An array of &lt;code&gt;TransactionEvent&lt;/code&gt; objects. Each object contains details about the transaction event.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTransactionEventsRequest.from_dict(body)
    return web.Response(status=200)


async def list_transactions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_transactions

    Lists all of the transactions on a given wallet address or to a specific contract.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTransactionsRequest.from_dict(body)
    return web.Response(status=200)
