from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field_definition import CustomFieldDefinition
from openapi_server.models.error import Error
from openapi_server import util


async def get_all_custom_fields_by_category(request: web.Request, company_id, category) -> web.Response:
    """Get All Custom Fields

    Get All Custom Fields for the selected company

    :param company_id: Company Id
    :type company_id: str
    :param category: Custom Fields Category
    :type category: str

    """
    return web.Response(status=200)
