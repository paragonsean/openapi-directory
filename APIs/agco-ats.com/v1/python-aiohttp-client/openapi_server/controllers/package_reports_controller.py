from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.update_system_models_package_report import UpdateSystemModelsPackageReport
from openapi_server import util


async def api_v2_clients_client_id_package_reports_put(request: web.Request, client_id, body) -> web.Response:
    """Submit a package report

    No Documentation Found.

    :param client_id: The Client ID
    :type client_id: str
    :param body: The Package Report
    :type body: dict | bytes

    """
    body = UpdateSystemModelsPackageReport.from_dict(body)
    return web.Response(status=200)


async def package_reports_batch(request: web.Request, client_id, body) -> web.Response:
    """Submit a batch of package reports

    No Documentation Found.

    :param client_id: The Client ID
    :type client_id: str
    :param body: The Package Reports
    :type body: list | bytes

    """
    body = [UpdateSystemModelsPackageReport.from_dict(d) for d in body]
    return web.Response(status=200)


async def package_reports_default(request: web.Request, client_id) -> web.Response:
    """Get the package reports for a client.

    No Documentation Found.

    :param client_id: The Client ID
    :type client_id: str

    """
    return web.Response(status=200)
