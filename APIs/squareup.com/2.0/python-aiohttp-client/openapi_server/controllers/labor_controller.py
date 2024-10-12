from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_break_type_request import CreateBreakTypeRequest
from openapi_server.models.create_break_type_response import CreateBreakTypeResponse
from openapi_server.models.create_shift_request import CreateShiftRequest
from openapi_server.models.create_shift_response import CreateShiftResponse
from openapi_server.models.delete_break_type_response import DeleteBreakTypeResponse
from openapi_server.models.delete_shift_response import DeleteShiftResponse
from openapi_server.models.get_break_type_response import GetBreakTypeResponse
from openapi_server.models.get_employee_wage_response import GetEmployeeWageResponse
from openapi_server.models.get_shift_response import GetShiftResponse
from openapi_server.models.get_team_member_wage_response import GetTeamMemberWageResponse
from openapi_server.models.list_break_types_response import ListBreakTypesResponse
from openapi_server.models.list_employee_wages_response import ListEmployeeWagesResponse
from openapi_server.models.list_team_member_wages_response import ListTeamMemberWagesResponse
from openapi_server.models.list_workweek_configs_response import ListWorkweekConfigsResponse
from openapi_server.models.search_shifts_request import SearchShiftsRequest
from openapi_server.models.search_shifts_response import SearchShiftsResponse
from openapi_server.models.update_break_type_request import UpdateBreakTypeRequest
from openapi_server.models.update_break_type_response import UpdateBreakTypeResponse
from openapi_server.models.update_shift_request import UpdateShiftRequest
from openapi_server.models.update_shift_response import UpdateShiftResponse
from openapi_server.models.update_workweek_config_request import UpdateWorkweekConfigRequest
from openapi_server.models.update_workweek_config_response import UpdateWorkweekConfigResponse
from openapi_server import util


async def create_break_type(request: web.Request, body) -> web.Response:
    """CreateBreakType

    Creates a new &#x60;BreakType&#x60;.  A &#x60;BreakType&#x60; is a template for creating &#x60;Break&#x60; objects. You must provide the following values in your request to this endpoint:  - &#x60;location_id&#x60; - &#x60;break_name&#x60; - &#x60;expected_duration&#x60; - &#x60;is_paid&#x60;  You can only have three &#x60;BreakType&#x60; instances per location. If you attempt to add a fourth &#x60;BreakType&#x60; for a location, an &#x60;INVALID_REQUEST_ERROR&#x60; \&quot;Exceeded limit of 3 breaks per location.\&quot; is returned.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateBreakTypeRequest.from_dict(body)
    return web.Response(status=200)


async def create_shift(request: web.Request, body) -> web.Response:
    """CreateShift

    Creates a new &#x60;Shift&#x60;.  A &#x60;Shift&#x60; represents a complete workday for a single employee. You must provide the following values in your request to this endpoint:  - &#x60;location_id&#x60; - &#x60;employee_id&#x60; - &#x60;start_at&#x60;  An attempt to create a new &#x60;Shift&#x60; can result in a &#x60;BAD_REQUEST&#x60; error when: - The &#x60;status&#x60; of the new &#x60;Shift&#x60; is &#x60;OPEN&#x60; and the employee has another shift with an &#x60;OPEN&#x60; status. - The &#x60;start_at&#x60; date is in the future. - The &#x60;start_at&#x60; or &#x60;end_at&#x60; date overlaps another shift for the same employee. - The &#x60;Break&#x60; instances are set in the request and a break &#x60;start_at&#x60; is before the &#x60;Shift.start_at&#x60;, a break &#x60;end_at&#x60; is after the &#x60;Shift.end_at&#x60;, or both.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateShiftRequest.from_dict(body)
    return web.Response(status=200)


async def delete_break_type(request: web.Request, id) -> web.Response:
    """DeleteBreakType

    Deletes an existing &#x60;BreakType&#x60;.  A &#x60;BreakType&#x60; can be deleted even if it is referenced from a &#x60;Shift&#x60;.

    :param id: The UUID for the &#x60;BreakType&#x60; being deleted.
    :type id: str

    """
    return web.Response(status=200)


async def delete_shift(request: web.Request, id) -> web.Response:
    """DeleteShift

    Deletes a &#x60;Shift&#x60;.

    :param id: The UUID for the &#x60;Shift&#x60; being deleted.
    :type id: str

    """
    return web.Response(status=200)


async def get_break_type(request: web.Request, id) -> web.Response:
    """GetBreakType

    Returns a single &#x60;BreakType&#x60; specified by &#x60;id&#x60;.

    :param id: The UUID for the &#x60;BreakType&#x60; being retrieved.
    :type id: str

    """
    return web.Response(status=200)


async def get_employee_wage(request: web.Request, id) -> web.Response:
    """GetEmployeeWage

    Returns a single &#x60;EmployeeWage&#x60; specified by &#x60;id&#x60;.

    :param id: The UUID for the &#x60;EmployeeWage&#x60; being retrieved.
    :type id: str

    """
    return web.Response(status=200)


async def get_shift(request: web.Request, id) -> web.Response:
    """GetShift

    Returns a single &#x60;Shift&#x60; specified by &#x60;id&#x60;.

    :param id: The UUID for the &#x60;Shift&#x60; being retrieved.
    :type id: str

    """
    return web.Response(status=200)


async def get_team_member_wage(request: web.Request, id) -> web.Response:
    """GetTeamMemberWage

    Returns a single &#x60;TeamMemberWage&#x60; specified by &#x60;id &#x60;.

    :param id: The UUID for the &#x60;TeamMemberWage&#x60; being retrieved.
    :type id: str

    """
    return web.Response(status=200)


async def list_break_types(request: web.Request, location_id=None, limit=None, cursor=None) -> web.Response:
    """ListBreakTypes

    Returns a paginated list of &#x60;BreakType&#x60; instances for a business.

    :param location_id: Filter the returned &#x60;BreakType&#x60; results to only those that are associated with the specified location.
    :type location_id: str
    :param limit: The maximum number of &#x60;BreakType&#x60; results to return per page. The number can range between 1 and 200. The default is 200.
    :type limit: int
    :param cursor: A pointer to the next page of &#x60;BreakType&#x60; results to fetch.
    :type cursor: str

    """
    return web.Response(status=200)


async def list_employee_wages(request: web.Request, employee_id=None, limit=None, cursor=None) -> web.Response:
    """ListEmployeeWages

    Returns a paginated list of &#x60;EmployeeWage&#x60; instances for a business.

    :param employee_id: Filter the returned wages to only those that are associated with the specified employee.
    :type employee_id: str
    :param limit: The maximum number of &#x60;EmployeeWage&#x60; results to return per page. The number can range between 1 and 200. The default is 200.
    :type limit: int
    :param cursor: A pointer to the next page of &#x60;EmployeeWage&#x60; results to fetch.
    :type cursor: str

    """
    return web.Response(status=200)


async def list_team_member_wages(request: web.Request, team_member_id=None, limit=None, cursor=None) -> web.Response:
    """ListTeamMemberWages

    Returns a paginated list of &#x60;TeamMemberWage&#x60; instances for a business.

    :param team_member_id: Filter the returned wages to only those that are associated with the specified team member.
    :type team_member_id: str
    :param limit: The maximum number of &#x60;TeamMemberWage&#x60; results to return per page. The number can range between 1 and 200. The default is 200.
    :type limit: int
    :param cursor: A pointer to the next page of &#x60;EmployeeWage&#x60; results to fetch.
    :type cursor: str

    """
    return web.Response(status=200)


async def list_workweek_configs(request: web.Request, limit=None, cursor=None) -> web.Response:
    """ListWorkweekConfigs

    Returns a list of &#x60;WorkweekConfig&#x60; instances for a business.

    :param limit: The maximum number of &#x60;WorkweekConfigs&#x60; results to return per page.
    :type limit: int
    :param cursor: A pointer to the next page of &#x60;WorkweekConfig&#x60; results to fetch.
    :type cursor: str

    """
    return web.Response(status=200)


async def search_shifts(request: web.Request, body) -> web.Response:
    """SearchShifts

    Returns a paginated list of &#x60;Shift&#x60; records for a business. The list to be returned can be filtered by: - Location IDs. - Employee IDs. - Shift status (&#x60;OPEN&#x60; and &#x60;CLOSED&#x60;). - Shift start. - Shift end. - Workday details.  The list can be sorted by: - &#x60;start_at&#x60;. - &#x60;end_at&#x60;. - &#x60;created_at&#x60;. - &#x60;updated_at&#x60;.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchShiftsRequest.from_dict(body)
    return web.Response(status=200)


async def update_break_type(request: web.Request, id, body) -> web.Response:
    """UpdateBreakType

    Updates an existing &#x60;BreakType&#x60;.

    :param id:  The UUID for the &#x60;BreakType&#x60; being updated.
    :type id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateBreakTypeRequest.from_dict(body)
    return web.Response(status=200)


async def update_shift(request: web.Request, id, body) -> web.Response:
    """UpdateShift

    Updates an existing &#x60;Shift&#x60;.  When adding a &#x60;Break&#x60; to a &#x60;Shift&#x60;, any earlier &#x60;Break&#x60; instances in the &#x60;Shift&#x60; have the &#x60;end_at&#x60; property set to a valid RFC-3339 datetime string.  When closing a &#x60;Shift&#x60;, all &#x60;Break&#x60; instances in the &#x60;Shift&#x60; must be complete with &#x60;end_at&#x60; set on each &#x60;Break&#x60;.

    :param id: The ID of the object being updated.
    :type id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateShiftRequest.from_dict(body)
    return web.Response(status=200)


async def update_workweek_config(request: web.Request, id, body) -> web.Response:
    """UpdateWorkweekConfig

    Updates a &#x60;WorkweekConfig&#x60;.

    :param id: The UUID for the &#x60;WorkweekConfig&#x60; object being updated.
    :type id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateWorkweekConfigRequest.from_dict(body)
    return web.Response(status=200)
