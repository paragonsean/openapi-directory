from typing import List, Dict
from aiohttp import web

from openapi_server.models.game_region_options_dto import GameRegionOptionsDTO
from openapi_server.models.message_model import MessageModel
from openapi_server.models.region_result import RegionResult
from openapi_server import util


async def get_game_region_options_using_get(request: web.Request, game_api_key) -> web.Response:
    """getGameRegionOptions

    

    :param game_api_key: gameApiKey
    :type game_api_key: str

    """
    return web.Response(status=200)


async def get_region_options_using_get(request: web.Request, ) -> web.Response:
    """getRegionOptions

    


    """
    return web.Response(status=200)


async def set_game_region_using_post(request: web.Request, game_api_key, region_code) -> web.Response:
    """setGameRegion

    

    :param game_api_key: gameApiKey
    :type game_api_key: str
    :param region_code: regionCode
    :type region_code: str

    """
    return web.Response(status=200)
