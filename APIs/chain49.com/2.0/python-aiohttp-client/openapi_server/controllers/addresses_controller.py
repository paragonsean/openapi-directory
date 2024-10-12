from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_balance_history_v2200_response_inner import GetBalanceHistoryV2200ResponseInner
from openapi_server.models.get_xpub_v2200_response import GetXpubV2200Response
from openapi_server import util


async def get_address_v2(request: web.Request, blockchain, address, page=None, page_size=None, from_block=None, to_block=None, details=None, contract=None, secondary=None) -> web.Response:
    """Get address V2

    Returns balances and transactions of an address. The returned transactions are sorted by block height, newest blocks first.  The **details** query parameter can specify the level of details returned by the request (default: \&quot;txids\&quot;). Possible values are:  **basic**: return only xpub balances, without any derived addresses and transactions  **tokens**: basic + tokens (addresses) derived from the xpub, subject to tokens parameter  **tokenBalances**: basic + tokens (addresses) derived from the xpub with balances, subject to tokens parameter  **txids**: tokenBalances + list of txids, subject to from, to filter and paging  **txs**: tokenBalances + list of transaction with details, subject to from, to filter and paging 

    :param blockchain: Blockchain name
    :type blockchain: str
    :param address: Wallet address
    :type address: str
    :param page: specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
    :type page: int
    :param page_size: number of transactions returned by call (default and maximum 1000)
    :type page_size: int
    :param from_block: filter of the returned transactions from block height to block height (default no filter)
    :type from_block: int
    :param to_block: filter of the returned transactions from block height to block height (default no filter)
    :type to_block: int
    :param details: specifies level of details returned by request
    :type details: str
    :param contract: return only transactions which affect specified contract (applicable only to coins which support contracts)
    :type contract: str
    :param secondary: specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values
    :type secondary: str

    """
    return web.Response(status=200)


async def get_balance_history_v2(request: web.Request, blockchain, address_or_xpub, from_date=None, to_date=None, fiatcurrency=None, group_by=None) -> web.Response:
    """Get Balance History V2

    Returns a balance history for the specified XPUB or address  The value of sentToSelf is the amount sent from the same address to the same address or within addresses of xpub.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param address_or_xpub: Address or XPUB
    :type address_or_xpub: str
    :param from_date: specifies a start date as a Unix timestamp
    :type from_date: str
    :param to_date: specifies an end date as a Unix timestamp
    :type to_date: str
    :param fiatcurrency: if specified, the response will contain secondary (fiat) rate at the time of transaction. If not, all available currencies will be returned
    :type fiatcurrency: str
    :param group_by: an interval in seconds, to group results by. Default is 3600 seconds
    :type group_by: 

    """
    return web.Response(status=200)


async def get_utxov2(request: web.Request, blockchain, address_or_xpub, confirmed=None) -> web.Response:
    """Get UTXO V2

    Returns array of unspent transaction outputs of address or xpub, applicable only for Bitcoin-type coins. By default, the list contains both confirmed and unconfirmed transactions. The query parameter confirmed&#x3D;true disables return of unconfirmed transactions. The returned utxos are sorted by block height, newest blocks first. For xpubs or output descriptors, the response also contains address and derivation path of the utxo.    Unconfirmed utxos do not have field height, the field confirmations has value 0 and may contain field lockTime, if not zero.  Coinbase utxos have field coinbase set to true, however due to performance reasons only up to minimum coinbase confirmations limit (100). After this limit, utxos are not detected as coinbase.

    :param blockchain: Blockchain name
    :type blockchain: str
    :param address_or_xpub: Address or XPUB
    :type address_or_xpub: str
    :param confirmed: confirmed&#x3D;true disables return of unconfirmed transactions
    :type confirmed: bool

    """
    return web.Response(status=200)


async def get_xpub_v2(request: web.Request, blockchain, xpub, page=None, page_size=None, from_block=None, to_block=None, details=None, tokens=None, secondary=None) -> web.Response:
    """Get xpub V2

    Returns balances and transactions of an xpub or output descriptor, applicable only for Bitcoin-type coins.  Blockbook supports BIP44, BIP49, BIP84 and BIP86 (Taproot) derivation schemes, using either xpubs or output descriptors (see https://github.com/bitcoin/bitcoin/blob/master/doc/descriptors.md)  Note: usedTokens always returns total number of used addresses of xpub.  Detailed documentation found here: https://github.com/trezor/blockbook/blob/master/docs/api.md#get-xpub

    :param blockchain: Blockchain name
    :type blockchain: str
    :param xpub: xpub or output descriptor, applicable only for Bitcoin-type coins
    :type xpub: str
    :param page: specifies page of returned transactions, starting from 1. If out of range, Blockbook returns the closest possible page.
    :type page: int
    :param page_size: number of transactions returned by call (default and maximum 1000)
    :type page_size: int
    :param from_block: filter of the returned transactions from block height to block height (default no filter)
    :type from_block: int
    :param to_block: filter of the returned transactions from block height to block height (default no filter)
    :type to_block: int
    :param details: specifies level of details returned by request
    :type details: str
    :param tokens: specifies what tokens (xpub addresses) are returned by the request (default nonzero)
    :type tokens: str
    :param secondary: specifies secondary (fiat) currency in which the token and total balances are returned in addition to crypto values
    :type secondary: str

    """
    return web.Response(status=200)
