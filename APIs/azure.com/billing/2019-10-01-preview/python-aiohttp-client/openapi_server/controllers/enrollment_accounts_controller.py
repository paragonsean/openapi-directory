from typing import List, Dict
from aiohttp import web

from openapi_server.models.enrollment_account import EnrollmentAccount
from openapi_server.models.enrollment_account_list_result import EnrollmentAccountListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def enrollment_accounts_get_by_enrollment_account_id(request: web.Request, api_version, billing_account_name, enrollment_account_name, expand=None, filter=None) -> web.Response:
    """enrollment_accounts_get_by_enrollment_account_id

    Get the enrollment account by id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param enrollment_account_name: Enrollment Account Id.
    :type enrollment_account_name: str
    :param expand: May be used to expand the Department.
    :type expand: str
    :param filter: The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def enrollment_accounts_list_by_billing_account_name(request: web.Request, api_version, billing_account_name, expand=None, filter=None) -> web.Response:
    """enrollment_accounts_list_by_billing_account_name

    Lists all Enrollment Accounts for a user which he has access to.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the department.
    :type expand: str
    :param filter: The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)
