from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_organization_openapi_spec_1(request: web.Request, organization_id) -> web.Response:
    """Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

    Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)
