from typing import List, Dict
from aiohttp import web

from openapi_server.models.cadence_membership import CadenceMembership
from openapi_server import util


async def v2_cadence_memberships_id_json_delete(request: web.Request, id) -> web.Response:
    """Delete a cadence membership

    Cadence Membership 

    :param id: CadenceMembership ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_cadence_memberships_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a cadence membership

    Fetches a cadence membership, by ID only. 

    :param id: CadenceMembership ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_cadence_memberships_json_get(request: web.Request, ids=None, person_id=None, cadence_id=None, updated_at=None, currently_on_cadence=None, sort_by=None, sort_direction=None, per_page=None, page=None, include_paging_counts=None, limit_paging_counts=None) -> web.Response:
    """List cadence memberships

    Fetches multiple cadence membership records. The records can be filtered, paged, and sorted according to the respective parameters. A cadence membership is the association between a person and their current and historical time on a cadence. Cadence membership records are mutable and change over time. If a person is added to a cadence and re-added to the same cadence in the future, there is a single membership record. 

    :param ids: IDs of cadence memberships to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful
    :type ids: List[int]
    :param person_id: ID of the person to find cadence memberships for
    :type person_id: int
    :param cadence_id: ID of the cadence to find cadence memberships for
    :type cadence_id: int
    :param updated_at: Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]} 
    :type updated_at: List[str]
    :param currently_on_cadence: If true, return only cadence memberships for people currently on cadences.  If false, return cadence memberships for people who have been removed from or have completed a cadence.
    :type currently_on_cadence: bool
    :param sort_by: Key to sort on, must be one of: added_at, updated_at. Defaults to updated_at
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


async def v2_cadence_memberships_json_post(request: web.Request, person_id, cadence_id, user_id=None, step_id=None) -> web.Response:
    """Create a cadence membership

    Adds a person to a cadence. person_id and cadence_id are required, and must be visible to the authenticated user. user_id will default to the authenticated user, but can be set to any visible user on the authenticated team.  A person cannot be added to a cadence on behalf of a teammate unless the cadence is a team cadence, the cadence is owned by the teammate, or the teammate has the Personal Cadence Admin permission. 

    :param person_id: ID of the person to create a cadence membership for
    :type person_id: int
    :param cadence_id: ID of the cadence to create a cadence membership for
    :type cadence_id: int
    :param user_id: ID of the user to create a cadence membership for. The associated cadence must be owned by the user, or it must be a team cadence
    :type user_id: int
    :param step_id: ID of the step on which the person should start the cadence. Start on first step is the default behavior without this parameter.
    :type step_id: int

    """
    return web.Response(status=200)
