from typing import List, Dict
from aiohttp import web

from openapi_server.models.browser_json_response import BrowserJsonResponse
from openapi_server.models.info_response import InfoResponse
from openapi_server.models.search_data import SearchData
from openapi_server import util


async def api_delete_pic_post(request: web.Request, id_search=None, id_pic=None) -> web.Response:
    """Remove an image from a search request

    

    :param id_search: 
    :type id_search: str
    :param id_pic: 
    :type id_pic: str

    """
    return web.Response(status=200)


async def api_info_post(request: web.Request, ) -> web.Response:
    """Returns remaining search credits, search engine online status, and number of indexed faces

    


    """
    return web.Response(status=200)


async def api_search_post(request: web.Request, body=None) -> web.Response:
    """api_search_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = SearchData.from_dict(body)
    return web.Response(status=200)


async def api_upload_pic_post(request: web.Request, id_search=None, images=None) -> web.Response:
    """api_upload_pic_post

    

    :param id_search: 
    :type id_search: str
    :param images: 
    :type images: List[str]

    """
    return web.Response(status=200)
