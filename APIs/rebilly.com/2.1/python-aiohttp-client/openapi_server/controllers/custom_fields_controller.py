from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field import CustomField
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server import util


async def get_custom_field(request: web.Request, resource, name, organization_id=None) -> web.Response:
    """Retrieve a Custom Field

    Retrieve a schema of the given Custom Field for the given resource type. 

    :param resource: The resource type string.
    :type resource: str
    :param name: The custom field&#39;s identifier string.
    :type name: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_custom_field_collection(request: web.Request, resource, organization_id=None, limit=None, offset=None) -> web.Response:
    """Retrieve Custom Fields

    Retrieve a schema of Custom Fields for the given resource type. 

    :param resource: The resource type string.
    :type resource: str
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str
    :param limit: The collection items limit.
    :type limit: int
    :param offset: The collection items offset.
    :type offset: int

    """
    return web.Response(status=200)


async def put_custom_field(request: web.Request, resource, name, body, organization_id=None) -> web.Response:
    """Create or alter a Custom Field

    Create or alter a schema of the given Custom Field for the given resource. type. 

    :param resource: The resource type string.
    :type resource: str
    :param name: The custom field&#39;s identifier string.
    :type name: str
    :param body: Custom Fields schema of the given resource type.
    :type body: dict | bytes
    :param organization_id: Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    :type organization_id: str

    """
    body = CustomField.from_dict(body)
    return web.Response(status=200)
