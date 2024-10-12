from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_range_info import DeleteRangeInfo
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.schedule_info import ScheduleInfo
from openapi_server.models.team_duty_summary_info import TeamDutySummaryInfo
from openapi_server import util


async def teams_team_id_duty_reports_file_name_get(request: web.Request, team_id, file_name) -> web.Response:
    """Download duty report with a specific fileName

    

    :param team_id: ID of team you want to download the duty report for.
    :type team_id: str
    :param file_name: Filename of the csv to download.
    :type file_name: str

    """
    return web.Response(status=200)


async def teams_team_id_duty_reports_get(request: web.Request, team_id) -> web.Response:
    """Get Information about downloadable reports

    

    :param team_id: ID of team you want to get the duty report file infos for.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_dutysummary_get(request: web.Request, team_id, last_two_duties=None) -> web.Response:
    """Get duty assistant info for a team

    

    :param team_id: ID of the team the duty belongs to.
    :type team_id: str
    :param last_two_duties: 
    :type last_two_duties: bool

    """
    return web.Response(status=200)


async def teams_team_id_schedules_delete_range_post(request: web.Request, team_id, body=None) -> web.Response:
    """Delete duty schedules in range

    

    :param team_id: Team ID you want to delete
    :type team_id: str
    :param body: Information with date range to delete from to
    :type body: dict | bytes

    """
    body = DeleteRangeInfo.from_dict(body)
    return web.Response(status=200)


async def teams_team_id_schedules_duty_id_delete(request: web.Request, team_id, duty_id) -> web.Response:
    """Delete a specific duty.

    

    :param team_id: ID of the team the duty belongs to.
    :type team_id: str
    :param duty_id: ID of the duty to be deleted.
    :type duty_id: str

    """
    return web.Response(status=200)


async def teams_team_id_schedules_get(request: web.Request, team_id, user_id=None, min_date=None, limit=None) -> web.Response:
    """Returns information about all duties that belong to the team.

    

    :param team_id: Id of the team the schedules user belongs to
    :type team_id: str
    :param user_id: 
    :type user_id: str
    :param min_date: 
    :type min_date: str
    :param limit: 
    :type limit: int

    """
    min_date = util.deserialize_datetime(min_date)
    return web.Response(status=200)


async def teams_team_id_schedules_multiple_post(request: web.Request, team_id, override_existing=None, body=None) -> web.Response:
    """Save multiple schedules. It is possible to override existing schedules if you wish

    

    :param team_id: Team ID to set
    :type team_id: str
    :param override_existing: Override or cut existing schedules if set to true.
    :type override_existing: bool
    :param body: List of schedules to save
    :type body: list | bytes

    """
    body = [ScheduleInfo.from_dict(d) for d in body]
    return web.Response(status=200)


async def teams_team_id_schedules_post(request: web.Request, team_id, body=None) -> web.Response:
    """Create/Update given duty schedule.

    

    :param team_id: Id of the team the duty is to be assigned to.
    :type team_id: str
    :param body: information about the duty schedule to be created
    :type body: dict | bytes

    """
    body = ScheduleInfo.from_dict(body)
    return web.Response(status=200)


async def teams_team_id_schedules_schedule_id_get(request: web.Request, team_id, schedule_id) -> web.Response:
    """Returns information of the duty schedule with the specified Id.

    

    :param team_id: Id of the team the duty belongs to
    :type team_id: str
    :param schedule_id: Id of the requested duty schedule.
    :type schedule_id: str

    """
    return web.Response(status=200)
