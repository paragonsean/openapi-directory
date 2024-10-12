from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server.models.page_of_variant_sets import PageOfVariantSets
from openapi_server.models.variant_set import VariantSet
from openapi_server import util


async def delete_variant_set_item(request: web.Request, id) -> web.Response:
    """Deletes variant set

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_variant_analyze(request: web.Request, id) -> web.Response:
    """Returns list of matches

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_variant_set_item(request: web.Request, id) -> web.Response:
    """Returns a variant set

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_variant_sets_archive_collection(request: web.Request, year, month, day, page=None, per_page=None) -> web.Response:
    """Returns list of variant sets from a specified time period

    

    :param year: 
    :type year: int
    :param month: 
    :type month: int
    :param day: 
    :type day: int
    :param page: Page number
    :type page: int
    :param per_page: Results per page {error_msg}
    :type per_page: int

    """
    return web.Response(status=200)


async def get_variant_sets_collection(request: web.Request, page=None, per_page=None) -> web.Response:
    """Returns list of variant sets

    

    :param page: Page number
    :type page: int
    :param per_page: Results per page {error_msg}
    :type per_page: int

    """
    return web.Response(status=200)


async def post_variant_sets_collection(request: web.Request, body) -> web.Response:
    """Creates a new variant set

    

    :param body: 
    :type body: dict | bytes

    """
    body = VariantSet.from_dict(body)
    return web.Response(status=200)


async def put_variant_set_item(request: web.Request, id, body) -> web.Response:
    """Updates a variant set

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VariantSet.from_dict(body)
    return web.Response(status=200)
