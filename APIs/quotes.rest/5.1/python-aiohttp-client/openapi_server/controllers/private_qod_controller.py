from typing import List, Dict
from aiohttp import web

from openapi_server.models.qod_response import QODResponse
from openapi_server.models.quote_response import QuoteResponse
from openapi_server.models.success_response import SuccessResponse
from openapi_server import util


async def qod_get_0(request: web.Request, category=None, language=None, id=None) -> web.Response:
    """qod_get_0

    Gets &#x60;Quote of the Day&#x60; (QOD). Optional &#x60;category&#x60; param determines the category of returned quote of the day 

    :param category: QOD Category (Used in public QOD only)
    :type category: str
    :param language: Language of the QOD. The language must be supported in our QOD system.
    :type language: str
    :param id: QOD defition id (Used in private QOD only)
    :type id: str

    """
    return web.Response(status=200)


async def qod_patch(request: web.Request, title, repeat_after=None, authors=None, private=None, language=None, sfw=None) -> web.Response:
    """qod_patch

    Update an existing private &#x60;Quote of the Day&#x60; definition. 

    :param title: Title of the Quote of the day category
    :type title: str
    :param repeat_after: How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
    :type repeat_after: int
    :param authors: Comma seperated author names. Quotes will be chosen from one of these authors.
    :type authors: str
    :param private: Should apply the filters to the private collection. Default is public quotes in the platform.
    :type private: bool
    :param language: Quotes language.
    :type language: str
    :param sfw: Consider only quotes marked as \&quot;sfw\&quot; (Safe for work).
    :type sfw: bool

    """
    return web.Response(status=200)


async def qod_put(request: web.Request, title, repeat_after=None, authors=None, private=None, language=None, sfw=None) -> web.Response:
    """qod_put

    Create a private &#x60;Quote of the Day&#x60; service.  

    :param title: Title of the Quote of the day category
    :type title: str
    :param repeat_after: How many days after the quotes can repeat? If you are setting this up from your private collection make sure you have more quotes that meet the filter conditions than the days you specify here.
    :type repeat_after: int
    :param authors: Comma seperated author names. Quotes will be chosen from one of these authors.
    :type authors: str
    :param private: Should apply the filters to the private collection. Default is public quotes in the platform.
    :type private: bool
    :param language: Quotes language.
    :type language: str
    :param sfw: Consider only quotes marked as \&quot;sfw\&quot; (Safe for work).
    :type sfw: bool

    """
    return web.Response(status=200)
