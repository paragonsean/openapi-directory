from typing import List, Dict
from aiohttp import web

from openapi_server.models.concept_item_model_public import ConceptItemModelPublic
from openapi_server import util


async def get_concept(request: web.Request, id) -> web.Response:
    """get_concept

    

    :param id: concept id
    :type id: str

    """
    return web.Response(status=200)


async def get_concepts(request: web.Request, ids=None, types=None) -> web.Response:
    """get_concepts

    

    :param ids: ids
    :type ids: str
    :param types: types
    :type types: str

    """
    return web.Response(status=200)
