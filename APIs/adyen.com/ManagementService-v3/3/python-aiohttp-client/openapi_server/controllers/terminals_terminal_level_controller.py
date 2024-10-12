from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_terminals_response import ListTerminalsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.terminal_reassignment_request import TerminalReassignmentRequest
from openapi_server import util


async def get_terminals(request: web.Request, search_query=None, otp_query=None, countries=None, merchant_ids=None, store_ids=None, brand_models=None, page_number=None, page_size=None) -> web.Response:
    """Get a list of terminals

    Returns the payment terminals that the API credential has access to and that match the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API — Terminal actions read

    :param search_query: Returns terminals with an ID that contains the specified string. If present, other query parameters are ignored.
    :type search_query: str
    :param otp_query: Returns one or more terminals associated with the one-time passwords specified in the request. If this query parameter is used, other query parameters are ignored.
    :type otp_query: str
    :param countries: Returns terminals located in the countries specified by their [two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    :type countries: str
    :param merchant_ids: Returns terminals that belong to the merchant accounts specified by their unique merchant account ID.
    :type merchant_ids: str
    :param store_ids: Returns terminals that are assigned to the [stores](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores) specified by their unique store ID.
    :type store_ids: str
    :param brand_models: Returns terminals of the [models](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) specified in the format *brand.model*.
    :type brand_models: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
    :type page_size: int

    """
    return web.Response(status=200)


async def post_terminals_terminal_id_reassign(request: web.Request, terminal_id, body=None) -> web.Response:
    """Reassign a terminal

    Reassigns a payment terminal to a company account, merchant account, merchant account inventory, or a store.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Assign Terminal

    :param terminal_id: The unique identifier of the payment terminal.
    :type terminal_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TerminalReassignmentRequest.from_dict(body)
    return web.Response(status=200)
