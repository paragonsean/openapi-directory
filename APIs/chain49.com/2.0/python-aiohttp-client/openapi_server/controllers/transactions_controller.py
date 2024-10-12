from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_mempool_v2200_response import GetMempoolV2200Response
from openapi_server.models.get_transaction_v2200_response import GetTransactionV2200Response
from openapi_server.models.post_send_tx_v2200_response import PostSendTxV2200Response
from openapi_server import util


async def get_mempool_v2(request: web.Request, blockchain, page=None, page_size=None) -> web.Response:
    """Get Mempool V2

    Get a list of transaction IDs currently in the mempool of the node (meaning unconfirmed transactions not included in any block yet)  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param page: specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
    :type page: int
    :param page_size: number of transactions returned by call (default and maximum 1000)
    :type page_size: int

    """
    return web.Response(status=200)


async def get_send_tx_v2(request: web.Request, blockchain, hex) -> web.Response:
    """Send transaction (in URL) V2

    Sends new transaction to backend  It is recommended to use POST for sending transactions as there is a limit on how much data can be sent in the URL itself.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param hex: Transaction hex data
    :type hex: str

    """
    return web.Response(status=200)


async def get_transaction_v2(request: web.Request, blockchain, tx_id) -> web.Response:
    """Get transaction V2

    Get transaction returns \&quot;normalized\&quot; data about transaction, which has the same general structure for all supported coins. It does not return coin specific fields (for example information about Zcash shielded addresses).  A note about the blockTime field: for already mined transaction (confirmations &gt; 0), the field blockTime contains time of the block for transactions in mempool (confirmations &#x3D;&#x3D; 0), the field contains time when the running instance of Blockbook was first time notified about the transaction. This time may be different in different instances of Blockbook.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param tx_id: Transaction ID
    :type tx_id: str

    """
    return web.Response(status=200)


async def get_tx_specific_v2(request: web.Request, blockchain, tx_id) -> web.Response:
    """Get transaction (as is from Backend) V2

    Returns transaction data in the exact format as returned by backend, including all coin specific fields

    :param blockchain: Blockchain name
    :type blockchain: str
    :param tx_id: Transaction ID
    :type tx_id: str

    """
    return web.Response(status=200)


async def post_send_tx_v2(request: web.Request, blockchain, body=None) -> web.Response:
    """Send transaction (POST) V2

    Sends new transaction to backend for broadcasting  The trailing slash &#39;/&#39; at the end is mandatory 

    :param blockchain: Blockchain name
    :type blockchain: str
    :param body: Transaction hex as plain text
    :type body: 

    """
    return web.Response(status=200)
