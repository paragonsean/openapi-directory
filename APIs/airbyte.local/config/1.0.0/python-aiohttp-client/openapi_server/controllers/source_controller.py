from typing import List, Dict
from aiohttp import web

from openapi_server.models.actor_catalog_with_updated_at import ActorCatalogWithUpdatedAt
from openapi_server.models.check_connection_read import CheckConnectionRead
from openapi_server.models.discover_catalog_result import DiscoverCatalogResult
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.source_clone_request_body import SourceCloneRequestBody
from openapi_server.models.source_create import SourceCreate
from openapi_server.models.source_discover_schema_read import SourceDiscoverSchemaRead
from openapi_server.models.source_discover_schema_request_body import SourceDiscoverSchemaRequestBody
from openapi_server.models.source_discover_schema_write_request_body import SourceDiscoverSchemaWriteRequestBody
from openapi_server.models.source_id_request_body import SourceIdRequestBody
from openapi_server.models.source_read import SourceRead
from openapi_server.models.source_read_list import SourceReadList
from openapi_server.models.source_search import SourceSearch
from openapi_server.models.source_update import SourceUpdate
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_server import util


async def check_connection_to_source(request: web.Request, body) -> web.Response:
    """Check connection to the source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def check_connection_to_source_for_update(request: web.Request, body) -> web.Response:
    """Check connection for a proposed update to a source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceUpdate.from_dict(body)
    return web.Response(status=200)


async def clone_source(request: web.Request, body) -> web.Response:
    """Clone source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceCloneRequestBody.from_dict(body)
    return web.Response(status=200)


async def create_source(request: web.Request, body) -> web.Response:
    """Create a source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceCreate.from_dict(body)
    return web.Response(status=200)


async def delete_source(request: web.Request, body) -> web.Response:
    """Delete a source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def discover_schema_for_source(request: web.Request, body) -> web.Response:
    """Discover the schema catalog of the source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDiscoverSchemaRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_most_recent_source_actor_catalog(request: web.Request, body) -> web.Response:
    """Get most recent ActorCatalog for source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_source(request: web.Request, body) -> web.Response:
    """Get source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def list_sources_for_workspace(request: web.Request, body) -> web.Response:
    """List sources for workspace

    List sources for workspace. Does not return deleted sources.

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def search_sources(request: web.Request, body) -> web.Response:
    """Search sources

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceSearch.from_dict(body)
    return web.Response(status=200)


async def update_source(request: web.Request, body) -> web.Response:
    """Update a source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceUpdate.from_dict(body)
    return web.Response(status=200)


async def write_discover_catalog_result(request: web.Request, body) -> web.Response:
    """Should only called from worker, to write result from discover activity back to DB.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDiscoverSchemaWriteRequestBody.from_dict(body)
    return web.Response(status=200)
