from typing import List, Dict
from aiohttp import web

from openapi_server.models.person_stage import PersonStage
from openapi_server import util


async def v2_person_stages_id_json_delete(request: web.Request, id) -> web.Response:
    """Delete an person stage

    Deletes a person stage. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

    :param id: Stage ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_person_stages_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a person stage

    Fetches a person stage, by ID only. 

    :param id: Stage ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_person_stages_id_json_put(request: web.Request, id, name) -> web.Response:
    """Update a person stage

    Updates a person stage. 

    :param id: Stage ID
    :type id: str
    :param name: The name of the stage.
    :type name: str

    """
    return web.Response(status=200)


async def v2_person_stages_json_get(request: web.Request, ids=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List person stages

    Fetches multiple person stage records. The records can be filtered, paged, and sorted according to the respective parameters. 

    :param ids: IDs of person stages to fetch.
    :type ids: List[int]
    :param sort_by: Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
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


async def v2_person_stages_json_post(request: web.Request, name) -> web.Response:
    """Create a person stage

    Creates a person stage. 

    :param name: The name of the new stage
    :type name: str

    """
    return web.Response(status=200)
