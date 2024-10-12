from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_sentences_from_book200_response import GetSentencesFromBook200Response
from openapi_server.models.get_specific_sentence200_response import GetSpecificSentence200Response
from openapi_server import util


async def get_sentences(request: web.Request, limit=None) -> web.Response:
    """A random sentence

    

    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_sentences_from_book(request: web.Request, id, limit=None) -> web.Response:
    """Random sentences from a specific book

    

    :param id: Book ID
    :type id: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_specific_sentence(request: web.Request, id) -> web.Response:
    """A specific sentence

    

    :param id: Sentence ID
    :type id: str

    """
    return web.Response(status=200)
