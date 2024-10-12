from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field import CustomField
from openapi_server.models.custom_field_edit import CustomFieldEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def custom_fields_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing CustomField.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomField
    :type id: int

    """
    return web.Response(status=200)


async def custom_fields_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single CustomField.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomField
    :type id: int

    """
    return web.Response(status=200)


async def custom_fields_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a CustomField.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomField
    :type id: int
    :param body: CustomField parameters.
    :type body: dict | bytes

    """
    body = CustomFieldEdit.from_dict(body)
    return web.Response(status=200)


async def custom_fields_id_select_options_custom_field_select_option_id_json_delete(request: web.Request, login, authtoken, id, custom_field_select_option_id) -> web.Response:
    """Delete an existing CustomFieldSelectOption.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomField
    :type id: int
    :param custom_field_select_option_id: Id of the CustomFieldSelectOption
    :type custom_field_select_option_id: int

    """
    return web.Response(status=200)


async def custom_fields_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve all Store&#39;s Custom Fields.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def custom_fields_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Custom Field.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Custom Field parameters.
    :type body: dict | bytes

    """
    body = CustomFieldEdit.from_dict(body)
    return web.Response(status=200)
