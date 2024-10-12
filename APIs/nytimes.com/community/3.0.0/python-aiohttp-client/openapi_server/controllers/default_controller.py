from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_user_content_by_date_json200_response import GETUserContentByDateJson200Response
from openapi_server.models.get_user_content_recent_json200_response import GETUserContentRecentJson200Response
from openapi_server.models.get_user_content_url_json200_response import GETUserContentUrlJson200Response
from openapi_server.models.get_user_content_user_json200_response import GETUserContentUserJson200Response
from openapi_server import util


async def g_et_user_content_by_date_json(request: web.Request, _date=None) -> web.Response:
    """Comments by Date

    

    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def g_et_user_content_recent_json(request: web.Request, ) -> web.Response:
    """Recent User Comments

    


    """
    return web.Response(status=200)


async def g_et_user_content_url_json(request: web.Request, url=None) -> web.Response:
    """Comments by URL

    

    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def g_et_user_content_user_json(request: web.Request, user_id=None) -> web.Response:
    """Comments by User

    

    :param user_id: 
    :type user_id: int

    """
    return web.Response(status=200)
