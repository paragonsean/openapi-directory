from typing import List, Dict
from aiohttp import web

from openapi_server.models.section_format_get200_response import SectionFormatGet200Response
from openapi_server import util


async def section_format_get(request: web.Request, section, format, param_callback=None) -> web.Response:
    """Top Stories

    The Top Stories API returns a list of articles and associated images currently on the specified section.  Support JSON and JSONP. 

    :param section: The section the story appears in.
    :type section: str
    :param format: if this is JSONP or JSON
    :type format: str
    :param param_callback: The name of the function the API call results will be passed to. Required when using JSONP. This parameter has only one valid value per section. The format is {section_name}TopStoriesCallback. 
    :type param_callback: str

    """
    return web.Response(status=200)
