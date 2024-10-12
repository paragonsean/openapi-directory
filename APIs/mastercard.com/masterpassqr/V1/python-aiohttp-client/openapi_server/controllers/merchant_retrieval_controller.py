from typing import List, Dict
from aiohttp import web

from openapi_server.models.merchant_transfer54_wrapper import MerchantTransfer54Wrapper
from openapi_server.models.merchant_transfers69_wrapper import MerchantTransfers69Wrapper
from openapi_server import util


async def get_merchant_transfer_by_id(request: web.Request, partner_id, transfer_id) -> web.Response:
    """Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.

    Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param transfer_id: Path Param - Valid transfer id
    :type transfer_id: str

    """
    return web.Response(status=200)


async def get_merchant_transfer_by_ref(request: web.Request, partner_id, ref) -> web.Response:
    """Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.

    Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param ref: Query Param - Is the client specified transfer reference when initiating the transfer. Allowable characters are alphanumeric and * , - . _ ~. Details- 6-40 Example- DEF123456
    :type ref: str

    """
    return web.Response(status=200)
