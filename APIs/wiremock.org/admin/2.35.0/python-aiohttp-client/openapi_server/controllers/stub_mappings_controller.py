from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_mappings_find_by_metadata_post_request import AdminMappingsFindByMetadataPostRequest
from openapi_server.models.admin_mappings_get200_response import AdminMappingsGet200Response
from openapi_server.models.admin_mappings_get200_response_mappings_inner import AdminMappingsGet200ResponseMappingsInner
from openapi_server import util


async def admin_mappings_delete(request: web.Request, ) -> web.Response:
    """Delete all stub mappings

    


    """
    return web.Response(status=200)


async def admin_mappings_find_by_metadata_post(request: web.Request, body) -> web.Response:
    """admin_mappings_find_by_metadata_post

    Find stubs by matching on their metadata

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsFindByMetadataPostRequest.from_dict(body)
    return web.Response(status=200)


async def admin_mappings_get(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get all stub mappings

    

    :param limit: The maximum number of results to return
    :type limit: int
    :param offset: The start index of the results to return
    :type offset: int

    """
    return web.Response(status=200)


async def admin_mappings_import_post(request: web.Request, ) -> web.Response:
    """Import stub mappings

    Import given stub mappings to the backing store


    """
    return web.Response(status=200)


async def admin_mappings_post(request: web.Request, body=None) -> web.Response:
    """Create a new stub mapping

    

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsGet200ResponseMappingsInner.from_dict(body)
    return web.Response(status=200)


async def admin_mappings_remove_by_metadata_post(request: web.Request, body=None) -> web.Response:
    """Delete stub mappings matching metadata

    

    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsFindByMetadataPostRequest.from_dict(body)
    return web.Response(status=200)


async def admin_mappings_reset_post(request: web.Request, ) -> web.Response:
    """Reset stub mappings

    Restores stub mappings to the defaults defined back in the backing store


    """
    return web.Response(status=200)


async def admin_mappings_save_post(request: web.Request, ) -> web.Response:
    """Persist stub mappings

    Save all persistent stub mappings to the backing store


    """
    return web.Response(status=200)


async def admin_mappings_stub_mapping_id_delete(request: web.Request, stub_mapping_id) -> web.Response:
    """Delete a stub mapping

    

    :param stub_mapping_id: The UUID of stub mapping
    :type stub_mapping_id: str

    """
    return web.Response(status=200)


async def admin_mappings_stub_mapping_id_get(request: web.Request, stub_mapping_id) -> web.Response:
    """Get stub mapping by ID

    

    :param stub_mapping_id: The UUID of stub mapping
    :type stub_mapping_id: str

    """
    return web.Response(status=200)


async def admin_mappings_stub_mapping_id_put(request: web.Request, stub_mapping_id, body=None) -> web.Response:
    """Update a stub mapping

    

    :param stub_mapping_id: The UUID of stub mapping
    :type stub_mapping_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AdminMappingsGet200ResponseMappingsInner.from_dict(body)
    return web.Response(status=200)
