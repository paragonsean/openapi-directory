from typing import List, Dict
from aiohttp import web

from openapi_server.models.game_summary_model import GameSummaryModel
from openapi_server.models.message_model import MessageModel
from openapi_server import util


async def get_game_summary_using_get(request: web.Request, api_key, stage, start_date, end_date) -> web.Response:
    """getGameSummary

    

    :param api_key: apiKey
    :type api_key: str
    :param stage: stage
    :type stage: str
    :param start_date: yyyy-MM-dd
    :type start_date: str
    :param end_date: yyyy-MM-dd
    :type end_date: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)
