from typing import List, Dict
from aiohttp import web

from openapi_server.models.department import Department
from openapi_server.models.department_list_result import DepartmentListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def departments_get(request: web.Request, api_version, billing_account_name, department_name, expand=None, filter=None) -> web.Response:
    """departments_get

    Get the department by id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param department_name: Department Id.
    :type department_name: str
    :param expand: May be used to expand the enrollmentAccounts.
    :type expand: str
    :param filter: The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def departments_list_by_billing_account_name(request: web.Request, api_version, billing_account_name, expand=None, filter=None) -> web.Response:
    """departments_list_by_billing_account_name

    Lists all departments for a user which he has access to.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the enrollmentAccounts.
    :type expand: str
    :param filter: The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)
