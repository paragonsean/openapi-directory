from typing import List, Dict
from aiohttp import web

from openapi_server.models.attachment import Attachment
from openapi_server.models.attachment_edit import AttachmentEdit
from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def products_id_attachments_attachment_id_json_delete(request: web.Request, login, authtoken, id, attachment_id) -> web.Response:
    """Delete a Product Attachment.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param attachment_id: Id of the Product Attachment
    :type attachment_id: int

    """
    return web.Response(status=200)


async def products_id_attachments_attachment_id_json_get(request: web.Request, login, authtoken, id, attachment_id) -> web.Response:
    """Retrieve a single Product Attachment.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param attachment_id: Id of the Product Attachment
    :type attachment_id: int

    """
    return web.Response(status=200)


async def products_id_attachments_count_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Count all Product Attachments.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_attachments_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve all Product Attachments.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_attachments_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Create a new Product Attachment.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param body: Product Attachment parameters.
    :type body: dict | bytes

    """
    body = AttachmentEdit.from_dict(body)
    return web.Response(status=200)
