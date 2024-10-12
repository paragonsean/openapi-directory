from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tenant_backfill_status_result import TenantBackfillStatusResult
from openapi_server import util


async def start_tenant_backfill(request: web.Request, api_version) -> web.Response:
    """start_tenant_backfill

    Starts backfilling subscriptions for the Tenant.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def tenant_backfill_status(request: web.Request, api_version) -> web.Response:
    """tenant_backfill_status

    Gets tenant backfill status

    :param api_version: Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
