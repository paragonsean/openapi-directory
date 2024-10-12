from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.image import Image
from openapi_server.models.image_edit import ImageEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def products_id_images_count_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Count all Product Images.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_images_image_id_json_delete(request: web.Request, login, authtoken, id, image_id) -> web.Response:
    """Delete a Product Image.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param image_id: Id of the Product Image
    :type image_id: int

    """
    return web.Response(status=200)


async def products_id_images_image_id_json_get(request: web.Request, login, authtoken, id, image_id) -> web.Response:
    """Retrieve a single Product Image.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param image_id: Id of the Product Image
    :type image_id: int

    """
    return web.Response(status=200)


async def products_id_images_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve all Product Images.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_images_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Create a new Product Image.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param body: Product Image parameters.
    :type body: dict | bytes

    """
    body = ImageEdit.from_dict(body)
    return web.Response(status=200)
