from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_category import ActivityCategory
from openapi_server.models.activity_model import ActivityModel
from openapi_server.models.activity_participant_model import ActivityParticipantModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.recurrence_type import RecurrenceType
from openapi_server import util


async def activities_get_activities(request: web.Request, page_token=None, row_count=None, closed=None, activity_categories=None, customer_guids=None, include_tasks_with_no_customer=None, project_guids=None, include_tasks_with_no_project=None, project_business_unit_guids=None, project_owner_guids=None, user_guids=None, include_as_member=None, user_keyword_guids=None, start_date_time=None, end_date_time=None, project_task_status_guids=None, phase_guids=None, include_sub_phases=None, contact_guids=None, has_duration=None, has_hours=None, is_unassigned=None, changed_since=None, use_strict_start_and_end_date_time=None, activity_type_guids=None, recurrence_type=None) -> web.Response:
    """Get all activities of an organization

    Start and end date times accept values of DateTimeOffset type, based on UTF-8 encoding.

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param closed: Optional: Which activities to fetch - open/closed, Default all.
    :type closed: bool
    :param activity_categories: Optional: activity category for the activities to be fetched. Should be one of Personal/Absences/CalendarEntry/SalesEvent/Task. Default all.
    :type activity_categories: list | bytes
    :param customer_guids: Optional: ID of customer. Default all.
    :type customer_guids: List[str]
    :param include_tasks_with_no_customer: Optional: Include the activities that don&#39;t have customer. Default is true.
    :type include_tasks_with_no_customer: bool
    :param project_guids: Optional: ID of the project for the activities to be fetched. If not provided, returns for all projects. Default all.
    :type project_guids: List[str]
    :param include_tasks_with_no_project: Optional: Include the activities that don&#39;t have project. Default is true.
    :type include_tasks_with_no_project: bool
    :param project_business_unit_guids: Optional: ID of the business unit of the project based on which activities should be filtered. If not provided, returns for all business units. Default all.
    :type project_business_unit_guids: List[str]
    :param project_owner_guids: Optional: ID of the project manager. If not provided, returns for all project managers. Default all.
    :type project_owner_guids: List[str]
    :param user_guids: Optional: ID of the user for the activities to be fetched. If not provided, returns for all users. Default all.
    :type user_guids: List[str]
    :param include_as_member: Optional: Include the activities that the user is a member. Effective if userGuid is provided. Default is to not include.
    :type include_as_member: bool
    :param user_keyword_guids: Optional: User keyword Ids of activity owner to search for.
    :type user_keyword_guids: List[str]
    :param start_date_time: Optional: starting date and time from which to get the activities in user&#39;s timezone. Finds all activities that end after the date time. Format \&quot;2017-04-12T13%3A20%3A00%2b02%3A00\&quot;. Default all.
    :type start_date_time: str
    :param end_date_time: Optional: ending date and time to which to get the activities in user&#39;s timezone. Finds all activities that start before or on the date time. Format \&quot;2017-04-12T13%3A20%3A00%2b02%3A00\&quot;. Default all. If activities for one day are fetched, give start date time with time as 00:00 with the offset of the timezone and end time as 23:59:59 with the offset.
    :type end_date_time: str
    :param project_task_status_guids: Optional: ID of the project task status. Default all.
    :type project_task_status_guids: List[str]
    :param phase_guids: Optional: ID of the phase for the activities to be fetched. If not provided, returns for all phases. Default all.
    :type phase_guids: List[str]
    :param include_sub_phases: Optional: If one phase guid is given include activities also from sub phases. If multiple phase guids are given, returns activities only for those regardless of this parameter. Default false.
    :type include_sub_phases: bool
    :param contact_guids: Optional: ID of the contact for the activities to be fetched. If not provided, returns for all users. Default all.
    :type contact_guids: List[str]
    :param has_duration: Optional: has duration flag for the activity. Default all.
    :type has_duration: bool
    :param has_hours: Optional: has any work hour entries associated with the activity. Default all.
    :type has_hours: bool
    :param is_unassigned: Optional: is the activity unassigned. Default all.
    :type is_unassigned: bool
    :param changed_since: Optional: Get activities that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param use_strict_start_and_end_date_time: Optional: If given as true returns activities that start after start time and end before end time. If given as false returns activities that start before end time and end after start time. Limit are included in both cases. Default false.
    :type use_strict_start_and_end_date_time: bool
    :param activity_type_guids: Optional: ID of the project activity type. Default all.
    :type activity_type_guids: List[str]
    :param recurrence_type: Optional: Type of the recurrence. Default returns all not recurring activities, instances and exceptions. (None &#x3D; not recurring activity)
    :type recurrence_type: dict | bytes

    """
    activity_categories = [ActivityCategory.from_dict(d) for d in activity_categories]
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    changed_since = util.deserialize_datetime(changed_since)
    recurrence_type = .from_dict(recurrence_type)
    return web.Response(status=200)


async def activities_get_activity(request: web.Request, guid) -> web.Response:
    """Get activity by ID

    

    :param guid: GUID used to get the activity.
    :type guid: str

    """
    return web.Response(status=200)


async def activity_participants_get_activity_participant(request: web.Request, guid) -> web.Response:
    """Get activity participant

    

    :param guid: ID of the participant
    :type guid: str

    """
    return web.Response(status=200)


async def activity_participants_get_activity_participants(request: web.Request, activity_guid) -> web.Response:
    """Get participants for an activity

    

    :param activity_guid: ID of the activity
    :type activity_guid: str

    """
    return web.Response(status=200)
