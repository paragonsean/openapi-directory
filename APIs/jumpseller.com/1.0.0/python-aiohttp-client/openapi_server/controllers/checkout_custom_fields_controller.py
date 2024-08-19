from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_custom_field import CheckoutCustomField
from openapi_server.models.checkout_custom_field_edit import CheckoutCustomFieldEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def checkout_custom_fields_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing CheckoutCustomField.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CheckoutCustomField
    :type id: int

    """
    return web.Response(status=200)


async def checkout_custom_fields_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single CheckoutCustomField.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CheckoutCustomField
    :type id: int

    """
    return web.Response(status=200)


async def checkout_custom_fields_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a CheckoutCustomField.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CheckoutCustomField
    :type id: int
    :param body: CheckoutCustomField parameters.
    :type body: dict | bytes

    """
    body = CheckoutCustomFieldEdit.from_dict(body)
    return web.Response(status=200)


async def checkout_custom_fields_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Checkout Custom Fields.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: List restriction
    :type limit: int
    :param page: List page
    :type page: int

    """
    return web.Response(status=200)


async def checkout_custom_fields_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new CheckoutCustomField.

    Type values can be: input, selection, checkbox, date or text. Area values can be: contact, billing_shipping or other.

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: CheckoutCustomField parameters.
    :type body: dict | bytes

    """
    body = CheckoutCustomFieldEdit.from_dict(body)
    return web.Response(status=200)
