from typing import List, Dict
from aiohttp import web

from openapi_server.models.automation_entity import AutomationEntity
from openapi_server import util


async def delete_automations_id(request: web.Request, id) -> web.Response:
    """Delete Automation

    Delete Automation

    :param id: Automation ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_automations(request: web.Request, cursor=None, per_page=None, sort_by=None, automation=None, filter=None, filter_gt=None, filter_gteq=None, filter_lt=None, filter_lteq=None, with_deleted=None) -> web.Response:
    """List Automations

    List Automations

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[automation]&#x3D;desc&#x60;). Valid fields are &#x60;automation&#x60;, &#x60;disabled&#x60;, &#x60;last_modified_at&#x60; or &#x60;name&#x60;.
    :type sort_by: dict | bytes
    :param automation: If set, return records where the specified field is equal to the supplied value.
    :type automation: str
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;disabled&#x60;, &#x60;last_modified_at&#x60; or &#x60;automation&#x60;. Valid field combinations are &#x60;[ automation, disabled ]&#x60; and &#x60;[ disabled, automation ]&#x60;.
    :type filter: dict | bytes
    :param filter_gt: If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;last_modified_at&#x60;.
    :type filter_gt: dict | bytes
    :param filter_gteq: If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;last_modified_at&#x60;.
    :type filter_gteq: dict | bytes
    :param filter_lt: If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;last_modified_at&#x60;.
    :type filter_lt: dict | bytes
    :param filter_lteq: If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;last_modified_at&#x60;.
    :type filter_lteq: dict | bytes
    :param with_deleted: Set to true to include deleted automations in the results.
    :type with_deleted: bool

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_gt = .from_dict(filter_gt)
    filter_gteq = .from_dict(filter_gteq)
    filter_lt = .from_dict(filter_lt)
    filter_lteq = .from_dict(filter_lteq)
    return web.Response(status=200)


async def get_automations_id(request: web.Request, id) -> web.Response:
    """Show Automation

    Show Automation

    :param id: Automation ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_automations_id(request: web.Request, id, automation=None, description=None, destination=None, destination_replace_from=None, destination_replace_to=None, destinations=None, disabled=None, group_ids=None, interval=None, name=None, path=None, recurring_day=None, schedule=None, source=None, sync_ids=None, trigger=None, trigger_actions=None, user_ids=None, value=None) -> web.Response:
    """Update Automation

    Update Automation

    :param id: Automation ID.
    :type id: int
    :param automation: Automation type
    :type automation: str
    :param description: Description for the this Automation.
    :type description: str
    :param destination: DEPRECATED: Destination Path. Use &#x60;destinations&#x60; instead.
    :type destination: str
    :param destination_replace_from: If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;.
    :type destination_replace_from: str
    :param destination_replace_to: If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here.
    :type destination_replace_to: str
    :param destinations: A list of String destination paths or Hash of folder_path and optional file_path.
    :type destinations: List[str]
    :param disabled: If true, this automation will not run.
    :type disabled: bool
    :param group_ids: A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    :type group_ids: str
    :param interval: How often to run this automation? One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60;
    :type interval: str
    :param name: Name for this automation.
    :type name: str
    :param path: Path on which this Automation runs.  Supports globs.
    :type path: str
    :param recurring_day: If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;.
    :type recurring_day: int
    :param schedule: Custom schedule for running this automation.
    :type schedule: dict | bytes
    :param source: Source Path
    :type source: str
    :param sync_ids: A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    :type sync_ids: str
    :param trigger: How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;.
    :type trigger: str
    :param trigger_actions: If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy
    :type trigger_actions: List[str]
    :param user_ids: A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    :type user_ids: str
    :param value: A Hash of attributes specific to the automation type.
    :type value: dict | bytes

    """
    schedule = object.from_dict(schedule)
    value = object.from_dict(value)
    return web.Response(status=200)


async def post_automations(request: web.Request, automation, description=None, destination=None, destination_replace_from=None, destination_replace_to=None, destinations=None, disabled=None, group_ids=None, interval=None, name=None, path=None, recurring_day=None, schedule=None, source=None, sync_ids=None, trigger=None, trigger_actions=None, user_ids=None, value=None) -> web.Response:
    """Create Automation

    Create Automation

    :param automation: Automation type
    :type automation: str
    :param description: Description for the this Automation.
    :type description: str
    :param destination: DEPRECATED: Destination Path. Use &#x60;destinations&#x60; instead.
    :type destination: str
    :param destination_replace_from: If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;.
    :type destination_replace_from: str
    :param destination_replace_to: If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here.
    :type destination_replace_to: str
    :param destinations: A list of String destination paths or Hash of folder_path and optional file_path.
    :type destinations: List[str]
    :param disabled: If true, this automation will not run.
    :type disabled: bool
    :param group_ids: A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    :type group_ids: str
    :param interval: How often to run this automation? One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60;
    :type interval: str
    :param name: Name for this automation.
    :type name: str
    :param path: Path on which this Automation runs.  Supports globs.
    :type path: str
    :param recurring_day: If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;.
    :type recurring_day: int
    :param schedule: Custom schedule for running this automation.
    :type schedule: dict | bytes
    :param source: Source Path
    :type source: str
    :param sync_ids: A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    :type sync_ids: str
    :param trigger: How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;.
    :type trigger: str
    :param trigger_actions: If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy
    :type trigger_actions: List[str]
    :param user_ids: A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    :type user_ids: str
    :param value: A Hash of attributes specific to the automation type.
    :type value: dict | bytes

    """
    schedule = object.from_dict(schedule)
    value = object.from_dict(value)
    return web.Response(status=200)
