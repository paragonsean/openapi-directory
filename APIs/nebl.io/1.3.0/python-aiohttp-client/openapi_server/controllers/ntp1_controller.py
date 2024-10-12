from typing import List, Dict
from aiohttp import web

from openapi_server.models.broadcast_tx_request import BroadcastTxRequest
from openapi_server.models.broadcast_tx_response import BroadcastTxResponse
from openapi_server.models.burn_token_request import BurnTokenRequest
from openapi_server.models.burn_token_response import BurnTokenResponse
from openapi_server.models.error import Error
from openapi_server.models.get_address_info_response import GetAddressInfoResponse
from openapi_server.models.get_token_holders_response import GetTokenHoldersResponse
from openapi_server.models.get_token_id_response import GetTokenIdResponse
from openapi_server.models.get_token_metadata_response import GetTokenMetadataResponse
from openapi_server.models.get_transaction_info_response import GetTransactionInfoResponse
from openapi_server.models.issue_token_request import IssueTokenRequest
from openapi_server.models.issue_token_response import IssueTokenResponse
from openapi_server.models.send_token_request import SendTokenRequest
from openapi_server.models.send_token_response import SendTokenResponse
from openapi_server import util


async def broadcast_tx(request: web.Request, body) -> web.Response:
    """Broadcasts a signed raw transaction to the network

    Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

    :param body: Object representing a transaction to broadcast
    :type body: dict | bytes

    """
    body = BroadcastTxRequest.from_dict(body)
    return web.Response(status=200)


async def burn_token(request: web.Request, body) -> web.Response:
    """Builds a transaction that burns an NTP1 Token

    Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain. 

    :param body: Object representing the token to be burned
    :type body: dict | bytes

    """
    body = BurnTokenRequest.from_dict(body)
    return web.Response(status=200)


async def get_address_info(request: web.Request, address) -> web.Response:
    """Information On a Neblio Address

    Returns both NEBL and NTP1 token UTXOs held at the given address. 

    :param address: Neblio Address to get information on.
    :type address: str

    """
    return web.Response(status=200)


async def get_token_holders(request: web.Request, tokenid) -> web.Response:
    """Get Addresses Holding a Token

    Returns the the the addresses holding a token and how many tokens are held 

    :param tokenid: TokenId to request metadata for
    :type tokenid: str

    """
    return web.Response(status=200)


async def get_token_id(request: web.Request, tokensymbol) -> web.Response:
    """Returns the tokenId representing a token

    Translates a token symbol to a tokenId if a token exists with that symbol on the network 

    :param tokensymbol: Token symbol
    :type tokensymbol: str

    """
    return web.Response(status=200)


async def get_token_metadata(request: web.Request, tokenid, verbosity=None) -> web.Response:
    """Get Metadata of Token

    Returns the metadata associated with a token. 

    :param tokenid: TokenId to request metadata for
    :type tokenid: str
    :param verbosity: 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
    :type verbosity: 

    """
    return web.Response(status=200)


async def get_token_metadata_of_utxo(request: web.Request, tokenid, utxo, verbosity=None) -> web.Response:
    """Get UTXO Metadata of Token

    Returns the metadata associated with a token for that specific utxo instead of the issuance transaction. 

    :param tokenid: TokenId to request metadata for
    :type tokenid: str
    :param utxo: Specific UTXO to request metadata for
    :type utxo: str
    :param verbosity: 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses
    :type verbosity: 

    """
    return web.Response(status=200)


async def get_transaction_info(request: web.Request, txid) -> web.Response:
    """Information On an NTP1 Transaction

    Returns detailed information regarding an NTP1 transaction. 

    :param txid: Neblio txid to get information on.
    :type txid: str

    """
    return web.Response(status=200)


async def issue_token(request: web.Request, body) -> web.Response:
    """Builds a transaction that issues a new NTP1 Token

    Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain. 

    :param body: Object representing the token to be created
    :type body: dict | bytes

    """
    body = IssueTokenRequest.from_dict(body)
    return web.Response(status=200)


async def send_token(request: web.Request, body) -> web.Response:
    """Builds a transaction that sends an NTP1 Token

    Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain. 

    :param body: Object representing the token to be sent
    :type body: dict | bytes

    """
    body = SendTokenRequest.from_dict(body)
    return web.Response(status=200)
