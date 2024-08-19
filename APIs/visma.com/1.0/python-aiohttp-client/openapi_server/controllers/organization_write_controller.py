from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.organization_details_output_model import OrganizationDetailsOutputModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server import util


async def organization_details_patch_organization_details(request: web.Request, body=None) -> web.Response:
    """Update (Patch) a organization details or a part of it

    

    :param body: 
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)
