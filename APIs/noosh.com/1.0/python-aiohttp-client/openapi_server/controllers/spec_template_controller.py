from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.spec_template_expand_vo import SpecTemplateExpandVO
from openapi_server.models.spec_template_list_vo import SpecTemplateListVO
from openapi_server import util


async def get_spec_template(request: web.Request, workgroup_id, spec_template_id) -> web.Response:
    """Get a specific Spec Template

    Get a specific Spec Template

    :param workgroup_id: 
    :type workgroup_id: str
    :param spec_template_id: 
    :type spec_template_id: str

    """
    return web.Response(status=200)


async def get_spec_template_list(request: web.Request, workgroup_id) -> web.Response:
    """List Spec Templates of Workgroup Level 

    List Spec Templates of Workgroup Level 

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)
