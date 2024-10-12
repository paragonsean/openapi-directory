from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_all_licenses200_response import ListAllLicenses200Response
from openapi_server.models.list_all_licenses_request import ListAllLicensesRequest
from openapi_server import util


async def list_all_licenses(request: web.Request, org_id, sort_by=None, order=None, body=None) -> web.Response:
    """List all licenses

    

    :param org_id: The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param sort_by: The field to sort results by.
    :type sort_by: str
    :param order: The direction to sort results by.
    :type order: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListAllLicensesRequest.from_dict(body)
    return web.Response(status=200)
