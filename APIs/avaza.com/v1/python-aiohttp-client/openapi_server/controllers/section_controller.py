from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_section import NewSection
from openapi_server.models.section_details import SectionDetails
from openapi_server.models.section_list import SectionList
from openapi_server import util


async def section_delete(request: web.Request, section_id) -> web.Response:
    """Delete a Section

    

    :param section_id: 
    :type section_id: int

    """
    return web.Response(status=200)


async def section_get(request: web.Request, project_id) -> web.Response:
    """Gets list of Sections

    

    :param project_id: Get sections for Project with ProjectID
    :type project_id: int

    """
    return web.Response(status=200)


async def section_post(request: web.Request, model) -> web.Response:
    """Create a Section

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewSection.from_dict(model)
    return web.Response(status=200)
