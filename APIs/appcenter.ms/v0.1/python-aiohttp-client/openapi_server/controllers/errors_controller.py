from typing import List, Dict
from aiohttp import web

from openapi_server.models.diagnostics_stack_trace import DiagnosticsStackTrace
from openapi_server.models.errors_app_builds_list200_response import ErrorsAppBuildsList200Response
from openapi_server.models.errors_available_versions200_response import ErrorsAvailableVersions200Response
from openapi_server.models.errors_counts_per_day200_response import ErrorsCountsPerDay200Response
from openapi_server.models.errors_delete_error200_response import ErrorsDeleteError200Response
from openapi_server.models.errors_error_attachment_text200_response import ErrorsErrorAttachmentText200Response
from openapi_server.models.errors_error_attachments200_response_inner import ErrorsErrorAttachments200ResponseInner
from openapi_server.models.errors_error_groups_search200_response import ErrorsErrorGroupsSearch200Response
from openapi_server.models.errors_error_location200_response import ErrorsErrorLocation200Response
from openapi_server.models.errors_error_search200_response import ErrorsErrorSearch200Response
from openapi_server.models.errors_get_retention_settings200_response import ErrorsGetRetentionSettings200Response
from openapi_server.models.errors_group_details200_response import ErrorsGroupDetails200Response
from openapi_server.models.errors_group_error_free_device_percentages200_response import ErrorsGroupErrorFreeDevicePercentages200Response
from openapi_server.models.errors_group_list200_response import ErrorsGroupList200Response
from openapi_server.models.errors_group_model_counts200_response import ErrorsGroupModelCounts200Response
from openapi_server.models.errors_group_operating_system_counts200_response import ErrorsGroupOperatingSystemCounts200Response
from openapi_server.models.errors_latest_error_details200_response import ErrorsLatestErrorDetails200Response
from openapi_server.models.errors_list_for_group200_response import ErrorsListForGroup200Response
from openapi_server.models.errors_list_session_logs200_response import ErrorsListSessionLogs200Response
from openapi_server.models.errors_update_state_request import ErrorsUpdateStateRequest
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse
from openapi_server import util


async def errors_app_builds_list(request: web.Request, version, start, owner_name, app_name, end=None, top=None, error_type=None) -> web.Response:
    """errors_app_builds_list

    List of app builds

    :param version: 
    :type version: str
    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results till the max number.)
    :type top: int
    :param error_type: Type of error (handled vs unhandled), including All
    :type error_type: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_available_versions(request: web.Request, start, owner_name, app_name, end=None, top=None, skip=None, filter=None, inlinecount=None, error_type=None) -> web.Response:
    """errors_available_versions

    Get all available versions in the time range.

    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results till the max number.)
    :type top: int
    :param skip: The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    :type skip: int
    :param filter: A filter as specified in https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#97-filtering.
    :type filter: str
    :param inlinecount: Controls whether or not to include a count of all the items across all pages.
    :type inlinecount: str
    :param error_type: Type of error (handled vs unhandled), including All
    :type error_type: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_counts_per_day(request: web.Request, start, owner_name, app_name, version=None, end=None, app_build=None, error_type=None) -> web.Response:
    """errors_counts_per_day

    Count of crashes or errors by day in the time range based the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror.

    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param version: 
    :type version: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str
    :param app_build: app build
    :type app_build: str
    :param error_type: Type of error (handled vs unhandled), excluding All
    :type error_type: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_delete_error(request: web.Request, error_group_id, error_id, owner_name, app_name) -> web.Response:
    """errors_delete_error

    Delete a specific error and related attachments and blobs for an app. Searchable data will not be deleted immediately and may take up to 30 days.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param error_id: The id of the error
    :type error_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_error_attachment_location(request: web.Request, error_id, attachment_id, owner_name, app_name) -> web.Response:
    """errors_error_attachment_location

    Error attachment location.

    :param error_id: The id of the error
    :type error_id: str
    :param attachment_id: Error attachment id.
    :type attachment_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_error_attachment_text(request: web.Request, error_id, attachment_id, owner_name, app_name) -> web.Response:
    """errors_error_attachment_text

    Error attachment text.

    :param error_id: The id of the error
    :type error_id: str
    :param attachment_id: Error attachment id.
    :type attachment_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_error_attachments(request: web.Request, error_id, owner_name, app_name) -> web.Response:
    """errors_error_attachments

    List error attachments.

    :param error_id: The id of the error
    :type error_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_error_download(request: web.Request, error_group_id, error_id, owner_name, app_name, format=None) -> web.Response:
    """errors_error_download

    Download details for a specific error.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param error_id: The id of the error
    :type error_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param format: the format of the crash log
    :type format: str

    """
    return web.Response(status=200)


async def errors_error_free_device_percentages(request: web.Request, start, owner_name, app_name, end=None, versions=None, app_build=None, error_type=None) -> web.Response:
    """errors_error_free_device_percentages

    Percentage of error-free devices by day in the time range based on the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror. API will return -1 if crash devices is greater than active devices

    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str
    :param versions: 
    :type versions: List[str]
    :param app_build: app build
    :type app_build: str
    :param error_type: Type of error (handled vs unhandled), excluding All
    :type error_type: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_error_groups_search(request: web.Request, owner_name, app_name, filter=None, q=None, order=None, sort=None, top=None, skip=None) -> web.Response:
    """errors_error_groups_search

    Error groups list based on search parameters

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param filter: A filter as specified in OData notation
    :type filter: str
    :param q: A query string
    :type q: str
    :param order: It controls the order of sorting
    :type order: str
    :param sort: It controls the sort based on specified field
    :type sort: str
    :param top: The maximum number of results to return
    :type top: int
    :param skip: The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    :type skip: int

    """
    return web.Response(status=200)


async def errors_error_location(request: web.Request, error_group_id, error_id, owner_name, app_name) -> web.Response:
    """errors_error_location

    Error location.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param error_id: The id of the error
    :type error_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_error_search(request: web.Request, owner_name, app_name, filter=None, q=None, order=None, sort=None, top=None, skip=None) -> web.Response:
    """errors_error_search

    Errors list based on search parameters

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param filter: A filter as specified in OData notation
    :type filter: str
    :param q: A query string
    :type q: str
    :param order: It controls the order of sorting
    :type order: str
    :param sort: It controls the sort based on specified field
    :type sort: str
    :param top: The maximum number of results to return
    :type top: int
    :param skip: The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    :type skip: int

    """
    return web.Response(status=200)


async def errors_error_stack_trace(request: web.Request, error_group_id, error_id, owner_name, app_name) -> web.Response:
    """errors_error_stack_trace

    Error Stacktrace details.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param error_id: The id of the error
    :type error_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_get_error_details(request: web.Request, error_group_id, error_id, owner_name, app_name) -> web.Response:
    """errors_get_error_details

    Error details.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param error_id: The id of the error
    :type error_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_get_retention_settings(request: web.Request, owner_name, app_name) -> web.Response:
    """gets the retention settings in days

    gets the retention settings in days

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_group_counts_per_day(request: web.Request, error_group_id, start, owner_name, app_name, version=None, end=None) -> web.Response:
    """errors_group_counts_per_day

    Count of errors by day in the time range of the selected error group with selected version

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param version: 
    :type version: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_group_details(request: web.Request, error_group_id, owner_name, app_name) -> web.Response:
    """errors_group_details

    Error group details

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_group_error_free_device_percentages(request: web.Request, error_group_id, start, owner_name, app_name, end=None) -> web.Response:
    """errors_group_error_free_device_percentages

    Percentage of error-free devices by day in the time range. Api will return -1 if crash devices is greater than active devices

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_group_error_stack_trace(request: web.Request, error_group_id, owner_name, app_name) -> web.Response:
    """errors_group_error_stack_trace

    Gets the stack trace for the error group.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_group_list(request: web.Request, start, owner_name, app_name, version=None, app_build=None, group_state=None, end=None, orderby=None, top=None, error_type=None) -> web.Response:
    """errors_group_list

    List of error groups

    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param version: 
    :type version: str
    :param app_build: app build
    :type app_build: str
    :param group_state: 
    :type group_state: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str
    :param orderby: controls the sorting order and sorting based on which column
    :type orderby: str
    :param top: The maximum number of results to return. (0 will fetch all results till the max number.)
    :type top: int
    :param error_type: Type of error (handled vs unhandled), including All
    :type error_type: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_group_model_counts(request: web.Request, error_group_id, owner_name, app_name, top=None) -> web.Response:
    """errors_group_model_counts

    Top models of the selected error group.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param top: The maximum number of results to return. (0 will fetch all results till the max number.)
    :type top: int

    """
    return web.Response(status=200)


async def errors_group_operating_system_counts(request: web.Request, error_group_id, owner_name, app_name, top=None) -> web.Response:
    """errors_group_operating_system_counts

    Top OSes of the selected error group.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param top: The maximum number of results to return. (0 will fetch all results till the max number.)
    :type top: int

    """
    return web.Response(status=200)


async def errors_latest_error_details(request: web.Request, error_group_id, owner_name, app_name) -> web.Response:
    """errors_latest_error_details

    Latest error details.

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def errors_list_for_group(request: web.Request, error_group_id, start, owner_name, app_name, end=None, top=None, model=None, os=None) -> web.Response:
    """errors_list_for_group

    Get all errors for group

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param start: Start date time in data in ISO 8601 date time format
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results till the max number.)
    :type top: int
    :param model: 
    :type model: str
    :param os: 
    :type os: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def errors_list_session_logs(request: web.Request, error_id, owner_name, app_name, _date=None) -> web.Response:
    """errors_list_session_logs

    Get session logs by error ID

    :param error_id: The id of the error
    :type error_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param _date: Date of data requested
    :type _date: str

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)


async def errors_update_state(request: web.Request, error_group_id, owner_name, app_name, body) -> web.Response:
    """errors_update_state

    Update error group state

    :param error_group_id: The id of the error group
    :type error_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The state of the error group
    :type body: dict | bytes

    """
    body = ErrorsUpdateStateRequest.from_dict(body)
    return web.Response(status=200)
