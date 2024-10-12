from typing import List, Dict
from aiohttp import web

from openapi_server.models.dependent_hosted_number_order_enum_status import DependentHostedNumberOrderEnumStatus
from openapi_server.models.list_dependent_hosted_number_order_response import ListDependentHostedNumberOrderResponse
from openapi_server import util


async def list_dependent_hosted_number_order(request: web.Request, signing_document_sid, status=None, phone_number=None, incoming_phone_number_sid=None, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_dependent_hosted_number_order

    Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

    :param signing_document_sid: A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder.
    :type signing_document_sid: str
    :param status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
    :type status: str
    :param phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
    :type phone_number: str
    :param incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
    :type incoming_phone_number_sid: str
    :param friendly_name: A human readable description of this resource, up to 128 characters.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
