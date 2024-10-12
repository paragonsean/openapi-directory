from typing import List, Dict
from aiohttp import web

from openapi_server.models.qod_response import QODResponse
from openapi_server import util


async def qod_categories_get(request: web.Request, language=None, detailed=None) -> web.Response:
    """qod_categories_get

    Gets a list of &#x60;Quote of the Day&#x60; Categories. 

    :param language: Language of the QOD category. The language must be supported in our QOD system.
    :type language: str
    :param detailed: Return detailed information of the categories. Note the data format changes between the two values of this switch.
    :type detailed: bool

    """
    return web.Response(status=200)


async def qod_get(request: web.Request, category=None, language=None, id=None) -> web.Response:
    """qod_get

    Gets &#x60;Quote of the Day&#x60; (QOD). Optional &#x60;category&#x60; param determines the category of returned quote of the day 

    :param category: QOD Category (Used in public QOD only)
    :type category: str
    :param language: Language of the QOD. The language must be supported in our QOD system.
    :type language: str
    :param id: QOD defition id (Used in private QOD only)
    :type id: str

    """
    return web.Response(status=200)


async def qod_languages_get(request: web.Request, ) -> web.Response:
    """qod_languages_get

    Gets a list of supported languages for &#x60;Quote of the Day&#x60;.  


    """
    return web.Response(status=200)
