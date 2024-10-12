from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_delay_get200_response import GetDelayGet200Response
from openapi_server.models.get_list_page_get200_response import GetListPageGet200Response
from openapi_server.models.skin_info import SkinInfo
from openapi_server import util


async def get_delay_get(request: web.Request, user_agent) -> web.Response:
    """get_delay_get

    

    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str

    """
    return web.Response(status=200)


async def get_id_id_get(request: web.Request, id, user_agent) -> web.Response:
    """get_id_id_get

    Deprecated. Use /get/uuid instead.

    :param id: 
    :type id: 
    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str

    """
    return web.Response(status=200)


async def get_list_page_get(request: web.Request, page, user_agent) -> web.Response:
    """get_list_page_get

    

    :param page: For reference pagination, the uuid of the last skin in the previous page. For numeric pagination (deprecated), the page number or &#39;start&#39;.
    :type page: 
    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str

    """
    return web.Response(status=200)


async def get_uuid_uuid_get(request: web.Request, uuid, user_agent) -> web.Response:
    """get_uuid_uuid_get

    

    :param uuid: 
    :type uuid: str
    :type uuid: str
    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str

    """
    return web.Response(status=200)
