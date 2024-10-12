from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def trivia_categories_get(request: web.Request, start=None) -> web.Response:
    """trivia_categories_get

    Get a random Trivia.

    :param start: start
    :type start: int

    """
    return web.Response(status=200)


async def trivia_delete(request: web.Request, id) -> web.Response:
    """trivia_delete

    Create a random Trivia entry.

    :param id: Trivia ID
    :type id: str

    """
    return web.Response(status=200)


async def trivia_get(request: web.Request, id=None) -> web.Response:
    """trivia_get

    Get a Trivia entry for a given id. Retrieves a trivia question and answer based on the id.

    :param id: ID of the trivia to fetch
    :type id: str

    """
    return web.Response(status=200)


async def trivia_put(request: web.Request, question, category, answer) -> web.Response:
    """trivia_put

    Create a random Trivia entry.

    :param question: Trivia Question
    :type question: str
    :param category: Category of the trivia
    :type category: str
    :param answer: Answer(s) to the trivia question
    :type answer: str

    """
    return web.Response(status=200)


async def trivia_random_get(request: web.Request, category=None) -> web.Response:
    """trivia_random_get

    Get a random trivia for a given category(optional)

    :param category: Category to get the trivia from
    :type category: str

    """
    return web.Response(status=200)


async def trivia_search_get(request: web.Request, query=None, category=None) -> web.Response:
    """trivia_search_get

    Search for random trivia which has the text in the query, for a given category(optional).

    :param query: Text to search for in the trivia
    :type query: str
    :param category: Category to get the trivia from
    :type category: str

    """
    return web.Response(status=200)
