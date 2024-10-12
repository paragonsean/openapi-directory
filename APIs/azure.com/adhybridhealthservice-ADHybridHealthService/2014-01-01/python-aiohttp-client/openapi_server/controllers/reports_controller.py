from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_report_users_entries import ErrorReportUsersEntries
from openapi_server.models.risky_ip_blob_uris import RiskyIPBlobUris
from openapi_server import util


async def services_list_all_risky_ip_download_report(request: web.Request, service_name, api_version) -> web.Response:
    """services_list_all_risky_ip_download_report

    Gets all Risky IP report URIs for the last 7 days.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_current_risky_ip_download_report(request: web.Request, service_name, api_version) -> web.Response:
    """services_list_current_risky_ip_download_report

    Initiate the generation of a new Risky IP report. Returns the URI for the new one.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list_user_bad_password_report(request: web.Request, service_name, api_version, data_source=None) -> web.Response:
    """services_list_user_bad_password_report

    Gets the bad password login attempt report for an user

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param data_source: The source of data, if its test data or customer data.
    :type data_source: str

    """
    return web.Response(status=200)
