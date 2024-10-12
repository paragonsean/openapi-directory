from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.word_alterations_dto import WordAlterationsDTO
from openapi_server import util


async def alterations_get(request: web.Request, ) -> web.Response:
    """Download alterations from runtime.

    


    """
    return web.Response(status=200)


async def alterations_replace(request: web.Request, word_alterations) -> web.Response:
    """Replace alterations data.

    

    :param word_alterations: New alterations data.
    :type word_alterations: dict | bytes

    """
    word_alterations = WordAlterationsDTO.from_dict(word_alterations)
    return web.Response(status=200)
