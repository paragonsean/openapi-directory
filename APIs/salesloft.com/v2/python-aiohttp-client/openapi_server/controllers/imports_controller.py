from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_import import ModelImport
from openapi_server import util


async def v2_imports_id_json_delete(request: web.Request, id, undo=None) -> web.Response:
    """Delete an import

    Deletes an import, by ID only. The associated people can be deleted as part of the deletion process.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

    :param id: Import ID
    :type id: str
    :param undo: Whether to delete people on this Import. Possible values are: [not present], all, single.  &#39;single&#39; will delete people who are only present in this Import. &#39;all&#39; will delete people even if they are present in other Imports. Not specifying this parameter will not delete any people 
    :type undo: str

    """
    return web.Response(status=200)


async def v2_imports_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch an import

    Fetches an import, by ID only.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

    :param id: Import ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_imports_id_json_put(request: web.Request, id, name=None, user_id=None) -> web.Response:
    """Update an import

    Updates an import, by ID only.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

    :param id: Import ID
    :type id: str
    :param name: Name, recommended to be easily identifiable to a user
    :type name: str
    :param user_id: ID of the User that owns this Import
    :type user_id: int

    """
    return web.Response(status=200)


async def v2_imports_json_get(request: web.Request, ids=None, user_ids=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List imports

    Fetches multiple imports. 

    :param ids: IDs of imports to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param user_ids: ID of users to fetch imports for. Using this filter will return an empty array for non-admin users who request other user&#39;s imports
    :type user_ids: List[int]
    :param sort_by: Key to sort on, must be one of: created_at, updated_at. Defaults to created_at
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str
    :param per_page: How many records to show per page in the range [1, 100]. Defaults to 25
    :type per_page: int
    :param page: The current page to fetch results from. Defaults to 1
    :type page: int
    :param include_paging_counts: Whether to include total_pages and total_count in the metadata. Defaults to false
    :type include_paging_counts: bool
    :param limit_paging_counts: Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    :type limit_paging_counts: bool

    """
    return web.Response(status=200)


async def v2_imports_json_post(request: web.Request, name=None, user_id=None) -> web.Response:
    """Create an import

    Creates an import. 

    :param name: Name, recommended to be easily identifiable to a user
    :type name: str
    :param user_id: ID of the User that owns this Import
    :type user_id: int

    """
    return web.Response(status=200)
