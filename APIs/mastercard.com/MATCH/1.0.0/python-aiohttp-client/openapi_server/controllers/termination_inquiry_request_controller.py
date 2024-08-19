from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.termination_inquiry_request_schema import TerminationInquiryRequestSchema
from openapi_server.models.termination_inquiry_schema import TerminationInquirySchema
from openapi_server import util


async def fraud_merchant_v3_termination_inquiry_post(request: web.Request, page_offset, page_length, termination_inquiry_request) -> web.Response:
    """Returns information on merchants that have been terminated and merchants that have inquired upon. Provides the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (if opted).

    Returns information on merchants that have been terminated and merchants which have been inquired upon. MATCH can provide the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (If opted) 

    :param page_offset: The zero-based offset to start at. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
    :type page_offset: 
    :param page_length: The maximum number of items to retrieve within the current \&quot;page\&quot; of results.
    :type page_length: 
    :param termination_inquiry_request: Body of the Termination Inquiry Request
    :type termination_inquiry_request: dict | bytes

    """
    termination_inquiry_request = TerminationInquiryRequestSchema.from_dict(termination_inquiry_request)
    return web.Response(status=200)
