from typing import List, Dict
from aiohttp import web

from openapi_server.models.erskine_may_chapter_overview import ErskineMayChapterOverview
from openapi_server import util


async def api_chapter_chapter_number_get(request: web.Request, chapter_number) -> web.Response:
    """Returns a single chapter overview by chapter number.

    

    :param chapter_number: Chapter overview with the chapter number specified
    :type chapter_number: int

    """
    return web.Response(status=200)
