from typing import List, Dict
from aiohttp import web

from openapi_server.models.erskine_may_section_detail import ErskineMaySectionDetail
from openapi_server.models.erskine_may_section_overview import ErskineMaySectionOverview
from openapi_server import util


async def api_section_section_id_get(request: web.Request, section_id) -> web.Response:
    """Returns a section by section id.

    

    :param section_id: Section by id.
    :type section_id: int

    """
    return web.Response(status=200)


async def api_section_section_idstep_get(request: web.Request, section_id, step) -> web.Response:
    """Returns a section overview by section id and step.

    

    :param section_id: Section by id.
    :type section_id: int
    :param step: Number of sections to step over from given section.
    :type step: int

    """
    return web.Response(status=200)
