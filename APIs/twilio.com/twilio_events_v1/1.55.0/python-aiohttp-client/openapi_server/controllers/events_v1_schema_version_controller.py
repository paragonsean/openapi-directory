from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_schema_schema_version import EventsV1SchemaSchemaVersion
from openapi_server.models.list_schema_version_response import ListSchemaVersionResponse
from openapi_server import util


async def fetch_schema_version(request: web.Request, id, schema_version) -> web.Response:
    """fetch_schema_version

    Fetch a specific schema and version.

    :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
    :type id: str
    :param schema_version: The version of the schema
    :type schema_version: int

    """
    return web.Response(status=200)


async def list_schema_version(request: web.Request, id, page_size=None, page=None, page_token=None) -> web.Response:
    """list_schema_version

    Retrieve a paginated list of versions of the schema.

    :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
    :type id: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
