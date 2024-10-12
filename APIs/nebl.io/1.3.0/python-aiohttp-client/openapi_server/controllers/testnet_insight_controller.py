from typing import List, Dict
from aiohttp import web

from openapi_server.models.broadcast_tx_response import BroadcastTxResponse
from openapi_server.models.error import Error
from openapi_server.models.get_address_response import GetAddressResponse
from openapi_server.models.get_address_utxos_response_inner import GetAddressUtxosResponseInner
from openapi_server.models.get_block_index_response import GetBlockIndexResponse
from openapi_server.models.get_block_response import GetBlockResponse
from openapi_server.models.get_raw_tx_response import GetRawTxResponse
from openapi_server.models.get_sync_response import GetSyncResponse
from openapi_server.models.get_tx_response import GetTxResponse
from openapi_server.models.get_txs_response import GetTxsResponse
from openapi_server.models.send_tx_request import SendTxRequest
from openapi_server import util


async def testnet_get_address(request: web.Request, address) -> web.Response:
    """Returns address object

    Returns NEBL address object containing information on a specific address

    :param address: Address
    :type address: str

    """
    return web.Response(status=200)


async def testnet_get_address_balance(request: web.Request, address) -> web.Response:
    """Returns address balance in sats

    Returns NEBL address balance in satoshis

    :param address: Address
    :type address: str

    """
    return web.Response(status=200)


async def testnet_get_address_total_received(request: web.Request, address) -> web.Response:
    """Returns total received by address in sats

    Returns total NEBL received by address in satoshis

    :param address: Address
    :type address: str

    """
    return web.Response(status=200)


async def testnet_get_address_total_sent(request: web.Request, address) -> web.Response:
    """Returns total sent by address in sats

    Returns total NEBL sent by address in satoshis

    :param address: Address
    :type address: str

    """
    return web.Response(status=200)


async def testnet_get_address_unconfirmed_balance(request: web.Request, address) -> web.Response:
    """Returns address unconfirmed balance in sats

    Returns NEBL address unconfirmed balance in satoshis

    :param address: Address
    :type address: str

    """
    return web.Response(status=200)


async def testnet_get_address_utxos(request: web.Request, address) -> web.Response:
    """Returns all UTXOs at a given address

    Returns information on each Unspent Transaction Output contained at an address

    :param address: Address
    :type address: str

    """
    return web.Response(status=200)


async def testnet_get_block(request: web.Request, blockhash) -> web.Response:
    """Returns information regarding a Neblio block

    Returns blockchain data for a given block based upon the block hash

    :param blockhash: Block Hash
    :type blockhash: str

    """
    return web.Response(status=200)


async def testnet_get_block_index(request: web.Request, blockindex) -> web.Response:
    """Returns block hash of block

    Returns the block hash of a block at a given block index

    :param blockindex: Block Index
    :type blockindex: 

    """
    return web.Response(status=200)


async def testnet_get_raw_tx(request: web.Request, txid) -> web.Response:
    """Returns raw transaction hex

    Returns raw transaction hex representing a NEBL transaction

    :param txid: Transaction ID
    :type txid: str

    """
    return web.Response(status=200)


async def testnet_get_status(request: web.Request, q=None) -> web.Response:
    """Utility API for calling several blockchain node functions

    Utility API for calling several blockchain node functions - getInfo, getDifficulty, getBestBlockHash, getLastBlockHash

    :param q: Function to call, getInfo, getDifficulty, getBestBlockHash, or getLastBlockHash
    :type q: str

    """
    return web.Response(status=200)


async def testnet_get_sync(request: web.Request, ) -> web.Response:
    """Get node sync status

    Returns information on the node&#39;s sync progress


    """
    return web.Response(status=200)


async def testnet_get_tx(request: web.Request, txid) -> web.Response:
    """Returns transaction object

    Returns NEBL transaction object representing a NEBL transaction

    :param txid: Transaction ID
    :type txid: str

    """
    return web.Response(status=200)


async def testnet_get_txs(request: web.Request, address=None, block=None, page_num=None) -> web.Response:
    """Get transactions by block or address

    Returns all transactions by block or address

    :param address: Address
    :type address: str
    :param block: Block Hash
    :type block: str
    :param page_num: Page number to display
    :type page_num: 

    """
    return web.Response(status=200)


async def testnet_send_tx(request: web.Request, body) -> web.Response:
    """Broadcasts a signed raw transaction to the network (not NTP1 specific)

    Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

    :param body: Object representing a transaction to broadcast
    :type body: dict | bytes

    """
    body = SendTxRequest.from_dict(body)
    return web.Response(status=200)
