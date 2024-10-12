from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_terminated_merchant_request_schema import AddTerminatedMerchantRequestSchema
from openapi_server.models.add_terminated_merchant_response_schema import AddTerminatedMerchantResponseSchema
from openapi_server.models.errors_response import ErrorsResponse
from openapi_server import util


async def fraud_merchant_v3_add_merchant_post(request: web.Request, add_terminated_merchant_request_schema) -> web.Response:
    """Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing.

    Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing. 

    :param add_terminated_merchant_request_schema: Body of the Add Terminated Merchant Request
    :type add_terminated_merchant_request_schema: dict | bytes

    """
    add_terminated_merchant_request_schema = AddTerminatedMerchantRequestSchema.from_dict(add_terminated_merchant_request_schema)
    return web.Response(status=200)
