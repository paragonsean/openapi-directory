from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.terms import Terms
from openapi_server import util


async def list_management_term_add_term(request: web.Request, list_id, term, language) -> web.Response:
    """list_management_term_add_term

    Add a term to the term list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param term: Term to be deleted
    :type term: str
    :param language: Language of the terms.
    :type language: str

    """
    return web.Response(status=200)


async def list_management_term_delete_all_terms(request: web.Request, list_id, language) -> web.Response:
    """list_management_term_delete_all_terms

    Deletes all terms from the list with list Id equal to the list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param language: Language of the terms.
    :type language: str

    """
    return web.Response(status=200)


async def list_management_term_delete_term(request: web.Request, list_id, term, language) -> web.Response:
    """list_management_term_delete_term

    Deletes a term from the list with list Id equal to the list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param term: Term to be deleted
    :type term: str
    :param language: Language of the terms.
    :type language: str

    """
    return web.Response(status=200)


async def list_management_term_get_all_terms(request: web.Request, list_id, language, offset=None, limit=None) -> web.Response:
    """list_management_term_get_all_terms

    Gets all terms from the list with list Id equal to the list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param language: Language of the terms.
    :type language: str
    :param offset: The pagination start index.
    :type offset: int
    :param limit: The max limit.
    :type limit: int

    """
    return web.Response(status=200)
