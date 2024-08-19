from typing import List, Dict
from aiohttp import web

from openapi_server.models.card import Card
from openapi_server.models.card_resume import CardResume
from openapi_server import util


async def cards(request: web.Request, ) -> web.Response:
    """fetch the list of cards

    desc


    """
    return web.Response(status=200)


async def find_pets_by_tags(request: web.Request, card_id) -> web.Response:
    """Finds Card by Global ID

    Find a defined card thatusing its global id

    :param card_id: Tags to filter by
    :type card_id: str

    """
    return web.Response(status=200)


async def sets_set_card_local_id_get(request: web.Request, set, card_local_id) -> web.Response:
    """sets_set_card_local_id_get

    

    :param set: 
    :type set: str
    :param card_local_id: 
    :type card_local_id: str

    """
    return web.Response(status=200)
