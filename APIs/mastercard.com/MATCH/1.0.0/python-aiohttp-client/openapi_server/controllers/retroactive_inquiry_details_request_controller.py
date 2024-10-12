from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.retro_inquiry_request_schema import RetroInquiryRequestSchema
from openapi_server.models.retro_inquiry_response_schema import RetroInquiryResponseSchema
from openapi_server import util


async def fraud_merchant_v3_retro_retro_inquiry_details_post(request: web.Request, acquirer_id, retro_inquiry_request) -> web.Response:
    """Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination.

    Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination. 

    :param acquirer_id: The Member ICA number which is used to validate that the application has permission to hit the MATCH database. This number must be obtained from a participating MATCH acquiring bank or entity before a developer can access the MATCH resource.
    :type acquirer_id: str
    :param retro_inquiry_request: The retro inquiry request object
    :type retro_inquiry_request: dict | bytes

    """
    retro_inquiry_request = RetroInquiryRequestSchema.from_dict(retro_inquiry_request)
    return web.Response(status=200)
