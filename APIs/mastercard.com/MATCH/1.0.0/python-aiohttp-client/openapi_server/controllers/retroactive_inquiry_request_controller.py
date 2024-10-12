from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.retro_request_schema import RetroRequestSchema
from openapi_server.models.retro_response_schema import RetroResponseSchema
from openapi_server import util


async def fraud_merchant_v3_retro_retro_list_post(request: web.Request, retro_request) -> web.Response:
    """Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service.

    Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service. 

    :param retro_request: The retro request object
    :type retro_request: dict | bytes

    """
    retro_request = RetroRequestSchema.from_dict(retro_request)
    return web.Response(status=200)
