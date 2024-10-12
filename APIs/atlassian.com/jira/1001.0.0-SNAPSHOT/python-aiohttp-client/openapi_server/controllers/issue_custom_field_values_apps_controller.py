from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field_value_update_details import CustomFieldValueUpdateDetails
from openapi_server.models.multiple_custom_field_values_update_details import MultipleCustomFieldValuesUpdateDetails
from openapi_server import util


async def update_custom_field_value(request: web.Request, field_id_or_key, body, generate_changelog=None) -> web.Response:
    """Update custom field value

    Updates the value of a custom field on one or more issues. Custom fields can only be updated by the Forge app that created them.  **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

    :param field_id_or_key: The ID or key of the custom field. For example, &#x60;customfield_10010&#x60;.
    :type field_id_or_key: str
    :param body: 
    :type body: dict | bytes
    :param generate_changelog: Whether to generate a changelog for this update.
    :type generate_changelog: bool

    """
    body = CustomFieldValueUpdateDetails.from_dict(body)
    return web.Response(status=200)


async def update_multiple_custom_field_values(request: web.Request, body, generate_changelog=None) -> web.Response:
    """Update custom fields

    Updates the value of one or more custom fields on one or more issues. Combinations of custom field and issue should be unique within the request. Custom fields can only be updated by the Forge app that created them.  **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

    :param body: 
    :type body: dict | bytes
    :param generate_changelog: Whether to generate a changelog for this update.
    :type generate_changelog: bool

    """
    body = MultipleCustomFieldValuesUpdateDetails.from_dict(body)
    return web.Response(status=200)
