from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_game_model import DeletedGameModel
from openapi_server.models.game_endpoints_model import GameEndpointsModel
from openapi_server.models.game_model import GameModel
from openapi_server.models.message_model import MessageModel
from openapi_server import util


async def get_games_endpoints_using_get(request: web.Request, api_key) -> web.Response:
    """getGamesEndpoints

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def list_deleted_using_get(request: web.Request, ) -> web.Response:
    """listDeleted

    


    """
    return web.Response(status=200)


async def list_using_get(request: web.Request, ) -> web.Response:
    """list

    


    """
    return web.Response(status=200)


async def restore_deleted_game_using_post(request: web.Request, api_key) -> web.Response:
    """restoreDeletedGame

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)
