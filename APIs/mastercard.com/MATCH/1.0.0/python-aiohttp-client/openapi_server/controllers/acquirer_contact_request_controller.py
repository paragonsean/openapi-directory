from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact_request_schema import ContactRequestSchema
from openapi_server.models.contact_response_schema import ContactResponseSchema
from openapi_server.models.errors_response import ErrorsResponse
from openapi_server import util


async def fraud_merchant_v3_common_contact_details_post(request: web.Request, contact_request) -> web.Response:
    """Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH.

    Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH. 

    :param contact_request: The contact request object
    :type contact_request: dict | bytes

    """
    contact_request = ContactRequestSchema.from_dict(contact_request)
    return web.Response(status=200)
