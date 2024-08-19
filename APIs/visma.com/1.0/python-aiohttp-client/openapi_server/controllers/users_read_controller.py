from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flextime_adjustment_output_model import FlextimeAdjustmentOutputModel
from openapi_server.models.flextime_model import FlextimeModel
from openapi_server.models.get_users_purpose import GetUsersPurpose
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.project_member_cost_exception_output_model import ProjectMemberCostExceptionOutputModel
from openapi_server.models.user_custom_value_output_model import UserCustomValueOutputModel
from openapi_server.models.user_keyword_model import UserKeywordModel
from openapi_server.models.user_output_model import UserOutputModel
from openapi_server.models.work_contract_output_model import WorkContractOutputModel
from openapi_server.models.workday_model import WorkdayModel
from openapi_server import util


async def flextime_adjustments_get_flextime_adjustment(request: web.Request, guid) -> web.Response:
    """Get Flextime Adjustment by ID.

    

    :param guid: GUID used to get the Flextime Adjustment.
    :type guid: str

    """
    return web.Response(status=200)


async def flextime_adjustments_get_flextime_adjustments(request: web.Request, user_guid, page_token=None, row_count=None) -> web.Response:
    """Get the Flextime Adjustments.

    

    :param user_guid: ID of the user for whom to get the adjustments.
    :type user_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    return web.Response(status=200)


async def flextime_get_flextime(request: web.Request, user_guid, event_date=None) -> web.Response:
    """Get the flextime balance for a user for a specified date. Total balance is returned for the given date. Month balance is the balance for the month of the given date. Values are returned only if the advanced time tracking add-on is active.

    

    :param user_guid: Id of the user.
    :type user_guid: str
    :param event_date: Date for which to get the balance. Max 12 months into the future.
    :type event_date: str

    """
    event_date = util.deserialize_datetime(event_date)
    return web.Response(status=200)


async def keywords_get_user_keywords(request: web.Request, user_guid, active=None, sortings=None) -> web.Response:
    """Get all the keywords for user.

    

    :param user_guid: ID of the user for who keywords are requested.
    :type user_guid: str
    :param active: If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    :type active: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def project_member_cost_exceptions_get_project_member_cost_exceptions_for_user(request: web.Request, user_guid, is_project_closed=None, first_row=None, row_count=None) -> web.Response:
    """Get all cost exceptions of project members for user.

    

    :param user_guid: Guid of the user.
    :type user_guid: str
    :param is_project_closed: Search only for open or closed projects. Default all projects.
    :type is_project_closed: bool
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    return web.Response(status=200)


async def user_custom_values_get_user_custom_value(request: web.Request, guid) -> web.Response:
    """Get user custom value by ID.

    

    :param guid: Id used to get the user custom value.
    :type guid: str

    """
    return web.Response(status=200)


async def user_custom_values_get_user_custom_values(request: web.Request, user_guid, page_token=None, row_count=None, is_active=None, targets=None, changed_since=None) -> web.Response:
    """Get the user custom values.

    

    :param user_guid: ID of the user.
    :type user_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_active: Optional: Get only values of active or inactive user custom properties.
    :type is_active: bool
    :param targets: Optional: List of target for which to get the values.
    :type targets: List[str]
    :param changed_since: Optional: Get user custom values that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def users_get_user(request: web.Request, guid) -> web.Response:
    """Get user by ID.

    

    :param guid: GUID used to get the user.
    :type guid: str

    """
    return web.Response(status=200)


async def users_get_users(request: web.Request, page_token=None, row_count=None, is_active=None, business_unit_guids=None, keyword_guids=None, changed_since=None, supervisor_user_guids=None, code=None, email=None, purpose=None) -> web.Response:
    """Get users

    

    :param page_token: 
    :type page_token: str
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param is_active: If not given, return all users, if given as true return only active users, if given as false returns only inactive users
    :type is_active: bool
    :param business_unit_guids: Optional: ID of the business unit of the user. If not provided, returns for all business units. Default all.
    :type business_unit_guids: List[str]
    :param keyword_guids: Optional: ID of the keyword of the user. If not provided, returns for all keywords. Default all.
    :type keyword_guids: List[str]
    :param changed_since: Optional: Get users that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param supervisor_user_guids: Optional: ID of the supervisor to get subordinates for.
    :type supervisor_user_guids: List[str]
    :param code: Optional: Code of the user.
    :type code: str
    :param email: Optional: Email address of the user.
    :type email: str
    :param purpose: Optional: Filter users by purpose.
    :type purpose: dict | bytes

    """
    changed_since = util.deserialize_datetime(changed_since)
    purpose = .from_dict(purpose)
    return web.Response(status=200)


async def work_contracts_get_current_work_contract_for_user(request: web.Request, user_guid) -> web.Response:
    """Gets current work contract for the user

    

    :param user_guid: Id of the user
    :type user_guid: str

    """
    return web.Response(status=200)


async def work_contracts_get_work_contract_0(request: web.Request, guid) -> web.Response:
    """Get work contract by ID.

    

    :param guid: Id used to get the work contract.
    :type guid: str

    """
    return web.Response(status=200)


async def work_contracts_get_work_contracts_for_user(request: web.Request, user_guid) -> web.Response:
    """Get all the work contracts for the user.

    

    :param user_guid: Id of the user.
    :type user_guid: str

    """
    return web.Response(status=200)


async def workdays_get_workdays(request: web.Request, user_guid, start_date, end_date) -> web.Response:
    """Get workdays for a user.

    

    :param user_guid: ID of the user.
    :type user_guid: str
    :param start_date: Start date of the workdays.
    :type start_date: str
    :param end_date: End date of the workdays.
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
