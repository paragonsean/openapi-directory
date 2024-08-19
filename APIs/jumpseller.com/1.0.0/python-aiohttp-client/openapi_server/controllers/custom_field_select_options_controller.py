from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field_select_option import CustomFieldSelectOption
from openapi_server.models.custom_field_select_option_edit import CustomFieldSelectOptionEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def custom_fields_id_select_options_custom_field_select_option_id_json_get(request: web.Request, login, authtoken, id, custom_field_select_option_id) -> web.Response:
    """Retrieve a single SelectOption from a CustomField.

    

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


async def custom_fields_id_select_options_custom_field_select_option_id_json_put(request: web.Request, login, authtoken, id, custom_field_select_option_id, body) -> web.Response:
    """Update a SelectOption from a CustomField.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomField
    :type id: int
    :param custom_field_select_option_id: Id of the CustomFieldSelectOption
    :type custom_field_select_option_id: int
    :param body: CustomFieldSelectOption parameters.
    :type body: dict | bytes

    """
    body = CustomFieldSelectOptionEdit.from_dict(body)
    return web.Response(status=200)


async def custom_fields_id_select_options_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve all Store&#39;s Custom Fields.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the CustomField
    :type id: int

    """
    return web.Response(status=200)


async def custom_fields_id_select_options_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Create a new Custom Field Select Option.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Automatically added
    :type id: str
    :param body: Custom Field Select Option parameters.
    :type body: dict | bytes

    """
    body = CustomFieldSelectOptionEdit.from_dict(body)
    return web.Response(status=200)
