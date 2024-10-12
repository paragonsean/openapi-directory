from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_import_request import BulkImportRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.import_response import ImportResponse
from openapi_server import util


async def get_latest_import_status(request: web.Request, organization_uuid) -> web.Response:
    """Get status for latest import

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str

    """
    return web.Response(status=200)


async def get_status_by_uuid(request: web.Request, organization_uuid, import_uuid) -> web.Response:
    """Get status for an import

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param import_uuid: 
    :type import_uuid: str
    :type import_uuid: str

    """
    return web.Response(status=200)


async def import_library_v2(request: web.Request, organization_uuid, body) -> web.Response:
    """Import library items

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = BulkImportRequest.from_dict(body)
    return web.Response(status=200)
