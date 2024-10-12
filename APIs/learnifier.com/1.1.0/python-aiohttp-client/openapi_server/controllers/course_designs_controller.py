from typing import List, Dict
from aiohttp import web

from openapi_server.models.course_design import CourseDesign
from openapi_server.models.error import Error
from openapi_server import util


async def coursedesigns_get(request: web.Request, ) -> web.Response:
    """Lists all global course design templates

    Lists all global course design templates. Only api callers that have full access can call this method.


    """
    return web.Response(status=200)
