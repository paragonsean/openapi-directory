from typing import List, Dict
from aiohttp import web

from openapi_server.models.contacts_contact_id_contact_custom_field_values_get200_response import ContactsContactIdContactCustomFieldValuesGet200Response
from openapi_server import util


async def contacts_contact_id_contact_custom_field_values_get(request: web.Request, contact_id) -> web.Response:
    """Get a list of contact custom field values

    

    :param contact_id: Automatically added
    :type contact_id: str

    """
    return web.Response(status=200)
