from typing import List, Dict
from aiohttp import web

from openapi_server.models.enrollment_account import EnrollmentAccount
from openapi_server.models.enrollment_account_list_result import EnrollmentAccountListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def enrollment_accounts_get(request: web.Request, name, api_version) -> web.Response:
    """enrollment_accounts_get

    Gets a enrollment account by name.

    :param name: Enrollment Account name.
    :type name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def enrollment_accounts_list(request: web.Request, api_version) -> web.Response:
    """enrollment_accounts_list

    Lists the enrollment accounts the caller has access to.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
