from typing import List, Dict
from aiohttp import web

from openapi_server.models.saved_list_view import SavedListView
from openapi_server import util


async def v2_saved_list_views_id_json_delete(request: web.Request, id) -> web.Response:
    """Delete a saved list view

    Deletes a saved list view. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

    :param id: Saved List View ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_saved_list_views_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a saved list view

    Fetches a saved list view, by ID only. 

    :param id: Saved List View ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_saved_list_views_id_json_put(request: web.Request, id, is_default=None, name=None, view_params=None) -> web.Response:
    """Update a saved list view

    Updates a saved list view. 

    :param id: Saved List View ID
    :type id: str
    :param is_default: Whether the saved list view is the default
    :type is_default: bool
    :param name: The name of the saved list view
    :type name: str
    :param view_params: JSON object of list view parameters
    :type view_params: str

    """
    return web.Response(status=200)


async def v2_saved_list_views_json_get(request: web.Request, ids=None, view=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List saved list views

    Fetches multiple saved list view records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of saved list views to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param view: Type of saved list views to fetch.
    :type view: str
    :param sort_by: Key to sort on, must be one of: name. Defaults to name
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


async def v2_saved_list_views_json_post(request: web.Request, name, view, is_default=None, view_params=None) -> web.Response:
    """Create a saved list view

    Creates a saved list view. 

    :param name: The name of the saved list view
    :type name: str
    :param view: The type of objects in the saved list view.  Value must be one of: people, companies, or recordings
    :type view: str
    :param is_default: Whether the saved list view is the default
    :type is_default: bool
    :param view_params: JSON object of list view parameters
    :type view_params: str

    """
    return web.Response(status=200)
