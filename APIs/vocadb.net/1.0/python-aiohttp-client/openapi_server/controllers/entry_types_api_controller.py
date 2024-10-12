from typing import List, Dict
from aiohttp import web

from openapi_server.models.entry_type import EntryType
from openapi_server.models.tag_for_api_contract import TagForApiContract
from openapi_server.models.tag_optional_fields import TagOptionalFields
from openapi_server import util


async def api_entry_types_entry_type_sub_type_tag_get(request: web.Request, entry_type, sub_type, fields=None) -> web.Response:
    """api_entry_types_entry_type_sub_type_tag_get

    

    :param entry_type: 
    :type entry_type: dict | bytes
    :param sub_type: 
    :type sub_type: str
    :param fields: 
    :type fields: dict | bytes

    """
    entry_type = .from_dict(entry_type)
    fields = .from_dict(fields)
    return web.Response(status=200)
