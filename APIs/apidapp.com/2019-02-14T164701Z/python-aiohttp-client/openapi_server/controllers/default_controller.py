from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def account_id_get(request: web.Request, id) -> web.Response:
    """account_id_get

    Get account balance

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def account_id_options(request: web.Request, id) -> web.Response:
    """account_id_options

    

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def account_options(request: web.Request, ) -> web.Response:
    """account_options

    


    """
    return web.Response(status=200)


async def account_post(request: web.Request, ) -> web.Response:
    """account_post

    Create new account


    """
    return web.Response(status=200)


async def block_get(request: web.Request, ) -> web.Response:
    """block_get

    Access detailed block information


    """
    return web.Response(status=200)


async def block_id_get(request: web.Request, id) -> web.Response:
    """block_id_get

    Get information about particular block

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def block_id_options(request: web.Request, id) -> web.Response:
    """block_id_options

    

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def block_id_transaction_get(request: web.Request, id) -> web.Response:
    """block_id_transaction_get

    Get transaction count within block

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def block_id_transaction_index_get(request: web.Request, index, id) -> web.Response:
    """block_id_transaction_index_get

    Get information about particular transaction within block

    :param index: 
    :type index: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def block_id_transaction_index_options(request: web.Request, id, index) -> web.Response:
    """block_id_transaction_index_options

    

    :param id: Automatically added
    :type id: str
    :param index: Automatically added
    :type index: str

    """
    return web.Response(status=200)


async def block_id_transaction_options(request: web.Request, id) -> web.Response:
    """block_id_transaction_options

    

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def block_options(request: web.Request, ) -> web.Response:
    """block_options

    


    """
    return web.Response(status=200)


async def blockchain_get(request: web.Request, ) -> web.Response:
    """blockchain_get

    Get a list of supported blockchains


    """
    return web.Response(status=200)


async def blockchain_id_get(request: web.Request, id) -> web.Response:
    """blockchain_id_get

    Get information about blockchain woth given id

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def blockchain_id_options(request: web.Request, id) -> web.Response:
    """blockchain_id_options

    

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def blockchain_options(request: web.Request, ) -> web.Response:
    """blockchain_options

    


    """
    return web.Response(status=200)


async def contract_id_get(request: web.Request, id) -> web.Response:
    """contract_id_get

    Get contract balance

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def contract_id_options(request: web.Request, id) -> web.Response:
    """contract_id_options

    

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def contract_id_post(request: web.Request, id) -> web.Response:
    """contract_id_post

    Call the contract

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def contract_options(request: web.Request, ) -> web.Response:
    """contract_options

    


    """
    return web.Response(status=200)


async def contract_post(request: web.Request, ) -> web.Response:
    """contract_post

    Create a new smart contract


    """
    return web.Response(status=200)


async def echo_options(request: web.Request, ) -> web.Response:
    """echo_options

    


    """
    return web.Response(status=200)


async def erc20_address_get(request: web.Request, address) -> web.Response:
    """erc20_address_get

    Get information amout token balance in the account

    :param address: 
    :type address: str

    """
    return web.Response(status=200)


async def erc20_address_options(request: web.Request, address) -> web.Response:
    """erc20_address_options

    

    :param address: Automatically added
    :type address: str

    """
    return web.Response(status=200)


async def erc20_address_post(request: web.Request, address) -> web.Response:
    """erc20_address_post

    Transfer tokens to another account

    :param address: 
    :type address: str

    """
    return web.Response(status=200)


async def erc20_get(request: web.Request, ) -> web.Response:
    """erc20_get

    Get token information such as name, total amount in circulation, etc


    """
    return web.Response(status=200)


async def erc20_options(request: web.Request, ) -> web.Response:
    """erc20_options

    


    """
    return web.Response(status=200)


async def erc20_post(request: web.Request, ) -> web.Response:
    """erc20_post

    


    """
    return web.Response(status=200)


async def key_get(request: web.Request, token=None) -> web.Response:
    """key_get

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def key_key_delete(request: web.Request, key) -> web.Response:
    """key_key_delete

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def key_key_options(request: web.Request, key) -> web.Response:
    """key_key_options

    

    :param key: Automatically added
    :type key: str

    """
    return web.Response(status=200)


async def key_options(request: web.Request, ) -> web.Response:
    """key_options

    


    """
    return web.Response(status=200)


async def key_post(request: web.Request, ) -> web.Response:
    """key_post

    


    """
    return web.Response(status=200)


async def root_options(request: web.Request, ) -> web.Response:
    """root_options

    


    """
    return web.Response(status=200)


async def transaction_hash_get(request: web.Request, hash) -> web.Response:
    """transaction_hash_get

    Get information about transaction by the transaction hash value

    :param hash: 
    :type hash: str

    """
    return web.Response(status=200)


async def transaction_hash_options(request: web.Request, hash) -> web.Response:
    """transaction_hash_options

    

    :param hash: Automatically added
    :type hash: str

    """
    return web.Response(status=200)


async def transaction_hash_receipt_get(request: web.Request, hash) -> web.Response:
    """transaction_hash_receipt_get

    Get receipt detail information

    :param hash: 
    :type hash: str

    """
    return web.Response(status=200)


async def transaction_hash_receipt_options(request: web.Request, hash) -> web.Response:
    """transaction_hash_receipt_options

    

    :param hash: Automatically added
    :type hash: str

    """
    return web.Response(status=200)


async def transaction_options(request: web.Request, ) -> web.Response:
    """transaction_options

    


    """
    return web.Response(status=200)


async def transaction_post(request: web.Request, ) -> web.Response:
    """transaction_post

    Create a new transaction. Transfer Ether between accounts


    """
    return web.Response(status=200)


async def version_get(request: web.Request, ) -> web.Response:
    """version_get

    Get API version info


    """
    return web.Response(status=200)


async def version_options(request: web.Request, ) -> web.Response:
    """version_options

    


    """
    return web.Response(status=200)


async def wallet_account_get(request: web.Request, ) -> web.Response:
    """wallet_account_get

    


    """
    return web.Response(status=200)


async def wallet_account_id_contract_post(request: web.Request, id) -> web.Response:
    """wallet_account_id_contract_post

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def wallet_account_id_erc20_post(request: web.Request, id) -> web.Response:
    """wallet_account_id_erc20_post

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def wallet_account_id_get(request: web.Request, id) -> web.Response:
    """wallet_account_id_get

    Get account balance

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def wallet_account_id_options(request: web.Request, id) -> web.Response:
    """wallet_account_id_options

    

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def wallet_account_id_pay_options(request: web.Request, id) -> web.Response:
    """wallet_account_id_pay_options

    

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def wallet_account_id_pay_post(request: web.Request, id) -> web.Response:
    """wallet_account_id_pay_post

    Send payment from the account held within the wallet

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def wallet_account_options(request: web.Request, ) -> web.Response:
    """wallet_account_options

    


    """
    return web.Response(status=200)


async def wallet_account_post(request: web.Request, ) -> web.Response:
    """wallet_account_post

    


    """
    return web.Response(status=200)


async def wallet_get(request: web.Request, ) -> web.Response:
    """wallet_get

    Get current account balance


    """
    return web.Response(status=200)


async def wallet_options(request: web.Request, ) -> web.Response:
    """wallet_options

    


    """
    return web.Response(status=200)


async def wallet_post(request: web.Request, ) -> web.Response:
    """wallet_post

    Create personal wallet


    """
    return web.Response(status=200)
