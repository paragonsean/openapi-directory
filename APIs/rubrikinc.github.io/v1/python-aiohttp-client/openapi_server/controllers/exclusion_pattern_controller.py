from typing import List, Dict
from aiohttp import web

from openapi_server.models.exclusion_pattern_create_config import ExclusionPatternCreateConfig
from openapi_server.models.exclusion_pattern_detail import ExclusionPatternDetail
from openapi_server.models.exclusion_pattern_detail_list import ExclusionPatternDetailList
from openapi_server.models.exclusion_pattern_detail_list_response import ExclusionPatternDetailListResponse
from openapi_server.models.exclusion_pattern_update_config import ExclusionPatternUpdateConfig
from openapi_server import util


async def bulk_create_exclusion_pattern(request: web.Request, body) -> web.Response:
    """Bulk create exclusion patterns

    Bulk create exclusion patterns.

    :param body: Create configuration parameters for a exclusion pattern.
    :type body: list | bytes

    """
    body = [ExclusionPatternCreateConfig.from_dict(d) for d in body]
    return web.Response(status=200)


async def bulk_delete_exclusion_pattern(request: web.Request, ids) -> web.Response:
    """Bulk delete the provided mutable exclusion patterns

    Bulk deletes the mutable patterns in a specified set of exclusion patterns.

    :param ids: The ID of each exclusion pattern to delete.
    :type ids: List[str]

    """
    return web.Response(status=200)


async def create_exclusion_pattern(request: web.Request, body) -> web.Response:
    """Create an exclusion pattern

    Create a exclusion pattern.

    :param body: Create configuration parameters for a exclusion pattern.
    :type body: dict | bytes

    """
    body = ExclusionPatternCreateConfig.from_dict(body)
    return web.Response(status=200)


async def delete_exclusion_pattern(request: web.Request, id) -> web.Response:
    """Delete a mutable exclusion pattern

    Deletes an exclusion pattern if that pattern is mutable.

    :param id: ID of the exclusion pattern.
    :type id: str

    """
    return web.Response(status=200)


async def get_exclusion_pattern(request: web.Request, id) -> web.Response:
    """Get details of a exclusion pattern

    Get details of a exclusion pattern.

    :param id: ID of the exclusion pattern.
    :type id: str

    """
    return web.Response(status=200)


async def query_exclusion_pattern(request: web.Request, pattern=None, is_mutable=None, source_id=None, primary_cluster_id=None, limit=None, offset=None, sort_by=None, sort_order=None) -> web.Response:
    """Get a summary of all exclusion patterns

    Get a summary of all exclusion patterns.

    :param pattern: Filter a response by making an infix comparison of the exclusion patttern in the response with the specified value.
    :type pattern: str
    :param is_mutable: Filter a response based on the mutability of the pattern.
    :type is_mutable: bool
    :param source_id: Filter a response based on the protectable object to which the exclusion pattern applies.
    :type source_id: str
    :param primary_cluster_id: Limit a response to the results that have the specified primary cluster value.
    :type primary_cluster_id: str
    :param limit: Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
    :type limit: int
    :param offset: Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
    :type offset: int
    :param sort_by: Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def update_exclusion_pattern(request: web.Request, id, body) -> web.Response:
    """Update a mutable exclusion pattern

    Update mutable exclusion pattern with specified properties. The exclusion pattern which is mutable can be modified.

    :param id: ID of exclusion pattern.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = ExclusionPatternUpdateConfig.from_dict(body)
    return web.Response(status=200)
