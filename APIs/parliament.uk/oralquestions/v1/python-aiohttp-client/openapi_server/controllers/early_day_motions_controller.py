from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response_list_published_written_question import ApiResponseListPublishedWrittenQuestion
from openapi_server.models.api_response_object import ApiResponseObject
from openapi_server import util


async def early_day_motions_list_get(request: web.Request, parameters_edm_ids=None, parameters_u_in_with_amendment_suffix=None, parameters_search_term=None, parameters_current_status_date_start=None, parameters_current_status_date_end=None, parameters_is_prayer=None, parameters_member_id=None, parameters_include_sponsored_by_member=None, parameters_tabled_start_date=None, parameters_tabled_end_date=None, parameters_statuses=None, parameters_order_by=None, parameters_skip=None, parameters_take=None) -> web.Response:
    """Returns a list of Early Day Motions

    Get a list of Early Day Motions which meet the specified criteria. Only supports Published and Withdrawn status.

    :param parameters_edm_ids: Early Day Motions with an ID in the list provided.
    :type parameters_edm_ids: List[int]
    :param parameters_u_in_with_amendment_suffix: Early Day Motions with an UINWithAmendmentSuffix provided.
    :type parameters_u_in_with_amendment_suffix: str
    :param parameters_search_term: Early Day Motions where the title includes the search term provided.
    :type parameters_search_term: str
    :param parameters_current_status_date_start: Early Day Motions where the current status has been set on or after the date provided. Date format YYYY-MM-DD.
    :type parameters_current_status_date_start: str
    :param parameters_current_status_date_end: Early Day Motions where the current status has been set on or before the date provided. Date format YYYY-MM-DD.
    :type parameters_current_status_date_end: str
    :param parameters_is_prayer: Early Day Motions which are a prayer against a Negative Statutory Instrument.
    :type parameters_is_prayer: bool
    :param parameters_member_id: Return Early Day Motions tabled by Member with ID provided.
    :type parameters_member_id: int
    :param parameters_include_sponsored_by_member: Include Early Day Motions sponsored by Member specified
    :type parameters_include_sponsored_by_member: bool
    :param parameters_tabled_start_date: Early Day Motions where the date tabled is on or after the date provided. Date format YYYY-MM-DD.
    :type parameters_tabled_start_date: str
    :param parameters_tabled_end_date: Early Day Motions where the date tabled is on or before the date provided. Date format YYYY-MM-DD.
    :type parameters_tabled_end_date: str
    :param parameters_statuses: Early Day Motions where current status is in the selected list.
    :type parameters_statuses: List[str]
    :param parameters_order_by: Order results by date tabled, title or signature count. Default is date tabled.
    :type parameters_order_by: str
    :param parameters_skip: The number of records to skip from the first, default is 0.
    :type parameters_skip: int
    :param parameters_take: The number of records to return, default is 25, maximum is 100.
    :type parameters_take: int

    """
    parameters_current_status_date_start = util.deserialize_datetime(parameters_current_status_date_start)
    parameters_current_status_date_end = util.deserialize_datetime(parameters_current_status_date_end)
    parameters_tabled_start_date = util.deserialize_datetime(parameters_tabled_start_date)
    parameters_tabled_end_date = util.deserialize_datetime(parameters_tabled_end_date)
    return web.Response(status=200)


async def published_early_day_motion_get(request: web.Request, id) -> web.Response:
    """Returns a single Early Day Motion by ID

    Get a single Early Day Motion which has the ID specified.

    :param id: Early Day Motion with the ID specified.
    :type id: int

    """
    return web.Response(status=200)
