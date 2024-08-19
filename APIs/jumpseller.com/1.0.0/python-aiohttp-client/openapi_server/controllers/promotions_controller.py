from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.promotion import Promotion
from openapi_server.models.promotion_edit import PromotionEdit
from openapi_server import util


async def promotions_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing Promotion.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Promotion
    :type id: int

    """
    return web.Response(status=200)


async def promotions_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Promotion.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Promotion
    :type id: int

    """
    return web.Response(status=200)


async def promotions_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a Promotion.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Promotion
    :type id: int
    :param body: Promotion parameters.
    :type body: dict | bytes

    """
    body = PromotionEdit.from_dict(body)
    return web.Response(status=200)


async def promotions_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Promotions.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: Promotions&#39; list restriction (default: 50 | max: 200).
    :type limit: int
    :param page: Promotions&#39; list page (default: 1).
    :type page: int

    """
    return web.Response(status=200)


async def promotions_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Promotion.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Promotion parameters.
    :type body: dict | bytes

    """
    body = PromotionEdit.from_dict(body)
    return web.Response(status=200)
