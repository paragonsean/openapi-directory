from typing import List, Dict
from aiohttp import web

from openapi_server.models.assign_terminals_request import AssignTerminalsRequest
from openapi_server.models.assign_terminals_response import AssignTerminalsResponse
from openapi_server.models.find_terminal_request import FindTerminalRequest
from openapi_server.models.find_terminal_response import FindTerminalResponse
from openapi_server.models.get_stores_under_account_request import GetStoresUnderAccountRequest
from openapi_server.models.get_stores_under_account_response import GetStoresUnderAccountResponse
from openapi_server.models.get_terminal_details_request import GetTerminalDetailsRequest
from openapi_server.models.get_terminal_details_response import GetTerminalDetailsResponse
from openapi_server.models.get_terminals_under_account_request import GetTerminalsUnderAccountRequest
from openapi_server.models.get_terminals_under_account_response import GetTerminalsUnderAccountResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_assign_terminals(request: web.Request, body=None) -> web.Response:
    """Assign terminals

    Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company inventory.

    :param body: 
    :type body: dict | bytes

    """
    body = AssignTerminalsRequest.from_dict(body)
    return web.Response(status=200)


async def post_find_terminal(request: web.Request, body=None) -> web.Response:
    """Get the account or store of a terminal

    Returns the company account, merchant account, or store that a payment terminal is assigned to.

    :param body: 
    :type body: dict | bytes

    """
    body = FindTerminalRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_stores_under_account(request: web.Request, body=None) -> web.Response:
    """Get the stores of an account

    Returns a list of stores associated with a company account or a merchant account, including the status of each store.

    :param body: 
    :type body: dict | bytes

    """
    body = GetStoresUnderAccountRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_terminal_details(request: web.Request, body=None) -> web.Response:
    """Get the details of a terminal

    Returns the details of a payment terminal, including where the terminal is assigned to. The response returns the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.

    :param body: 
    :type body: dict | bytes

    """
    body = GetTerminalDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_terminals_under_account(request: web.Request, body=None) -> web.Response:
    """Get the list of terminals

    Returns a list of payment terminals associated with a company account, merchant account, or store. The response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).

    :param body: 
    :type body: dict | bytes

    """
    body = GetTerminalsUnderAccountRequest.from_dict(body)
    return web.Response(status=200)
