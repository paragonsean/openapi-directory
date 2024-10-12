from typing import List, Dict
from aiohttp import web

from openapi_server.models.analytics_crash_counts200_response import AnalyticsCrashCounts200Response
from openapi_server.models.analytics_crash_free_device_percentages200_response import AnalyticsCrashFreeDevicePercentages200Response
from openapi_server.models.analytics_crash_group_model_counts200_response import AnalyticsCrashGroupModelCounts200Response
from openapi_server.models.analytics_crash_group_operating_system_counts200_response import AnalyticsCrashGroupOperatingSystemCounts200Response
from openapi_server.models.analytics_crash_groups_totals200_response_inner import AnalyticsCrashGroupsTotals200ResponseInner
from openapi_server.models.analytics_crash_groups_totals200_response_inner_overall import AnalyticsCrashGroupsTotals200ResponseInnerOverall
from openapi_server.models.analytics_crash_groups_totals_request import AnalyticsCrashGroupsTotalsRequest
from openapi_server.models.analytics_device_counts200_response import AnalyticsDeviceCounts200Response
from openapi_server.models.analytics_device_counts200_response_daily_inner import AnalyticsDeviceCounts200ResponseDailyInner
from openapi_server.models.analytics_device_counts_default_response import AnalyticsDeviceCountsDefaultResponse
from openapi_server.models.analytics_distribution_release_counts200_response import AnalyticsDistributionReleaseCounts200Response
from openapi_server.models.analytics_distribution_release_counts_request import AnalyticsDistributionReleaseCountsRequest
from openapi_server.models.analytics_event_count200_response import AnalyticsEventCount200Response
from openapi_server.models.analytics_event_device_count200_response import AnalyticsEventDeviceCount200Response
from openapi_server.models.analytics_event_per_device_count200_response import AnalyticsEventPerDeviceCount200Response
from openapi_server.models.analytics_event_per_session_count200_response import AnalyticsEventPerSessionCount200Response
from openapi_server.models.analytics_event_properties200_response import AnalyticsEventProperties200Response
from openapi_server.models.analytics_event_property_counts200_response import AnalyticsEventPropertyCounts200Response
from openapi_server.models.analytics_events200_response import AnalyticsEvents200Response
from openapi_server.models.analytics_generic_log_flow200_response import AnalyticsGenericLogFlow200Response
from openapi_server.models.analytics_get_audience200_response import AnalyticsGetAudience200Response
from openapi_server.models.analytics_language_counts200_response import AnalyticsLanguageCounts200Response
from openapi_server.models.analytics_list_audiences200_response import AnalyticsListAudiences200Response
from openapi_server.models.analytics_list_custom_properties200_response import AnalyticsListCustomProperties200Response
from openapi_server.models.analytics_list_device_property_values200_response import AnalyticsListDevicePropertyValues200Response
from openapi_server.models.analytics_log_flow200_response import AnalyticsLogFlow200Response
from openapi_server.models.analytics_model_counts200_response import AnalyticsModelCounts200Response
from openapi_server.models.analytics_operating_system_counts200_response import AnalyticsOperatingSystemCounts200Response
from openapi_server.models.analytics_per_device_counts200_response import AnalyticsPerDeviceCounts200Response
from openapi_server.models.analytics_place_counts200_response import AnalyticsPlaceCounts200Response
from openapi_server.models.analytics_session_durations_distribution200_response import AnalyticsSessionDurationsDistribution200Response
from openapi_server.models.analytics_test_audience200_response import AnalyticsTestAudience200Response
from openapi_server.models.analytics_test_audience_request import AnalyticsTestAudienceRequest
from openapi_server.models.analytics_versions200_response import AnalyticsVersions200Response
from openapi_server.models.crashes_list_session_logs200_response import CrashesListSessionLogs200Response
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse
from openapi_server import util


async def analytics_audience_name_exists(request: web.Request, audience_name, owner_name, app_name) -> web.Response:
    """analytics_audience_name_exists

    Returns whether audience definition exists.

    :param audience_name: The name of the audience
    :type audience_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_crash_counts(request: web.Request, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """Available for UWP apps only.

    Count of crashes by day in the time range based the selected versions. Available for UWP apps only.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_crash_free_device_percentages(request: web.Request, start, version, owner_name, app_name, end=None) -> web.Response:
    """analytics_crash_free_device_percentages

    Percentage of crash-free device by day in the time range based on the selected versions. Api will return -1 if crash devices is greater than active devices.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param version: 
    :type version: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_crash_group_counts(request: web.Request, crash_group_id, version, start, owner_name, app_name, end=None) -> web.Response:
    """Available for UWP apps only.

    Count of crashes by day in the time range of the selected crash group with selected version. Available for UWP apps only.

    :param crash_group_id: The id of the crash group.
    :type crash_group_id: str
    :param version: 
    :type version: str
    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_crash_group_model_counts(request: web.Request, crash_group_id, version, owner_name, app_name, top=None) -> web.Response:
    """Available for UWP apps only.

    Top models of the selected crash group with selected version. Available for UWP apps only.

    :param crash_group_id: The id of the crash group.
    :type crash_group_id: str
    :param version: 
    :type version: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int

    """
    return web.Response(status=200)


async def analytics_crash_group_operating_system_counts(request: web.Request, crash_group_id, version, owner_name, app_name, top=None) -> web.Response:
    """Available for UWP apps only.

    Top OSes of the selected crash group with selected version. Available for UWP apps only.

    :param crash_group_id: The id of the crash group.
    :type crash_group_id: str
    :param version: 
    :type version: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int

    """
    return web.Response(status=200)


async def analytics_crash_group_totals(request: web.Request, crash_group_id, version, owner_name, app_name) -> web.Response:
    """Available for UWP apps only.

    Overall crashes and affected users count of the selected crash group with selected version. Available for UWP apps only.

    :param crash_group_id: The id of the crash group.
    :type crash_group_id: str
    :param version: 
    :type version: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_crash_groups_totals(request: web.Request, owner_name, app_name, body) -> web.Response:
    """analytics_crash_groups_totals

    Overall crashes and affected users count of the selected crash groups with selected versions.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = AnalyticsCrashGroupsTotalsRequest.from_dict(body)
    return web.Response(status=200)


async def analytics_create_or_update_audience(request: web.Request, audience_name, owner_name, app_name, body) -> web.Response:
    """analytics_create_or_update_audience

    Creates or updates audience definition.

    :param audience_name: The name of the audience
    :type audience_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Audience definition
    :type body: dict | bytes

    """
    body = AnalyticsTestAudienceRequest.from_dict(body)
    return web.Response(status=200)


async def analytics_delete_audience(request: web.Request, audience_name, owner_name, app_name) -> web.Response:
    """analytics_delete_audience

    Deletes audience definition.

    :param audience_name: The name of the audience
    :type audience_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_device_counts(request: web.Request, start, owner_name, app_name, end=None, versions=None, app_build=None) -> web.Response:
    """analytics_device_counts

    Count of active devices by interval in the time range.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]
    :param app_build: Application build number. If build number is specified than multiple versions are not allowed.
    :type app_build: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_distribution_release_counts(request: web.Request, owner_name, app_name, body) -> web.Response:
    """analytics_distribution_release_counts

    Count of total downloads for the provided distribution releases.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The releases to retrieve.
    :type body: dict | bytes

    """
    body = AnalyticsDistributionReleaseCountsRequest.from_dict(body)
    return web.Response(status=200)


async def analytics_event_count(request: web.Request, event_name, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """analytics_event_count

    Count of events by interval in the time range.

    :param event_name: The id of the event.
    :type event_name: str
    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_event_device_count(request: web.Request, event_name, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """analytics_event_device_count

    Count of devices for an event by interval in the time range.

    :param event_name: The id of the event.
    :type event_name: str
    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_event_per_device_count(request: web.Request, event_name, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """analytics_event_per_device_count

    Count of events per device by interval in the time range.

    :param event_name: The id of the event.
    :type event_name: str
    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_event_per_session_count(request: web.Request, event_name, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """analytics_event_per_session_count

    Count of events per session by interval in the time range.

    :param event_name: The id of the event.
    :type event_name: str
    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_event_properties(request: web.Request, event_name, owner_name, app_name) -> web.Response:
    """analytics_event_properties

    Event properties.

    :param event_name: The id of the event.
    :type event_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_event_property_counts(request: web.Request, event_name, event_property_name, start, owner_name, app_name, end=None, versions=None, top=None) -> web.Response:
    """analytics_event_property_counts

    Event properties value counts during the time range in descending order.

    :param event_name: The id of the event.
    :type event_name: str
    :param event_property_name: The id of the event property.
    :type event_property_name: str
    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]
    :param top: The number of property values to return. Set to 0 in order to fetch all results available.
    :type top: int

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_events(request: web.Request, start, owner_name, app_name, end=None, versions=None, event_name=None, top=None, skip=None, inlinecount=None, orderby=None) -> web.Response:
    """analytics_events

    Count of active events in the time range ordered by event.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]
    :param event_name: To select the specific events.
    :type event_name: List[str]
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int
    :param skip: The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    :type skip: int
    :param inlinecount: Controls whether or not to include a count of all the items across all pages.
    :type inlinecount: str
    :param orderby: controls the sorting order and sorting based on which column
    :type orderby: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_events_delete(request: web.Request, event_name, owner_name, app_name) -> web.Response:
    """analytics_events_delete

    Delete the set of Events with the specified event names.

    :param event_name: The id of the event.
    :type event_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_events_delete_logs(request: web.Request, event_name, owner_name, app_name) -> web.Response:
    """analytics_events_delete_logs

    Delete the set of Events with the specified event names.

    :param event_name: The id of the event.
    :type event_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_generic_log_flow(request: web.Request, owner_name, app_name, start=None) -> web.Response:
    """analytics_generic_log_flow

    Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param start: Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone.
    :type start: str

    """
    start = util.deserialize_datetime(start)
    return web.Response(status=200)


async def analytics_get_audience(request: web.Request, audience_name, owner_name, app_name) -> web.Response:
    """analytics_get_audience

    Gets audience definition.

    :param audience_name: The name of the audience
    :type audience_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_language_counts(request: web.Request, start, owner_name, app_name, end=None, top=None, versions=None) -> web.Response:
    """analytics_language_counts

    Languages in the time range.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_list_audiences(request: web.Request, owner_name, app_name, include_disabled=None) -> web.Response:
    """analytics_list_audiences

    Get list of audiences.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param include_disabled: Include disabled audience definitions
    :type include_disabled: bool

    """
    return web.Response(status=200)


async def analytics_list_custom_properties(request: web.Request, owner_name, app_name) -> web.Response:
    """analytics_list_custom_properties

    Get list of custom properties.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_list_device_properties(request: web.Request, owner_name, app_name) -> web.Response:
    """analytics_list_device_properties

    Get list of device properties.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def analytics_list_device_property_values(request: web.Request, property_name, owner_name, app_name, contains=None) -> web.Response:
    """analytics_list_device_property_values

    Get list of device property values.

    :param property_name: Device property
    :type property_name: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param contains: Contains string
    :type contains: str

    """
    return web.Response(status=200)


async def analytics_log_flow(request: web.Request, owner_name, app_name, start=None) -> web.Response:
    """analytics_log_flow

    Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param start: Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone.
    :type start: str

    """
    start = util.deserialize_datetime(start)
    return web.Response(status=200)


async def analytics_model_counts(request: web.Request, start, owner_name, app_name, end=None, top=None, versions=None) -> web.Response:
    """analytics_model_counts

    Models in the time range.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_operating_system_counts(request: web.Request, start, owner_name, app_name, end=None, top=None, versions=None) -> web.Response:
    """analytics_operating_system_counts

    OSes in the time range.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_per_device_counts(request: web.Request, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """analytics_per_device_counts

    Count of sessions per device in the time range.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_place_counts(request: web.Request, start, owner_name, app_name, end=None, top=None, versions=None) -> web.Response:
    """analytics_place_counts

    Places in the time range.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_session_counts(request: web.Request, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """analytics_session_counts

    Count of sessions in the time range.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_session_durations_distribution(request: web.Request, start, owner_name, app_name, end=None, versions=None) -> web.Response:
    """analytics_session_durations_distribution

    Gets session duration.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def analytics_test_audience(request: web.Request, owner_name, app_name, body) -> web.Response:
    """analytics_test_audience

    Tests audience definition.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Audience definition
    :type body: dict | bytes

    """
    body = AnalyticsTestAudienceRequest.from_dict(body)
    return web.Response(status=200)


async def analytics_versions(request: web.Request, start, owner_name, app_name, end=None, top=None, versions=None) -> web.Response:
    """analytics_versions

    Count of active versions in the time range ordered by version.

    :param start: Start date time in data in ISO 8601 date time format.
    :type start: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param end: Last date time in data in ISO 8601 date time format.
    :type end: str
    :param top: The maximum number of results to return. (0 will fetch all results)
    :type top: int
    :param versions: To select specific application versions
    :type versions: List[str]

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def app_block_logs(request: web.Request, owner_name, app_name) -> web.Response:
    """app_block_logs

    **Warning, this operation is not reversible.**   A successful call to this API will permanently stop ingesting any logs received via SDK by app_id, and cannot be restored. We advise caution when using this API, it is designed to permanently disable an app_id. 

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_list_session_logs(request: web.Request, crash_id, owner_name, app_name, _date=None) -> web.Response:
    """crashes_list_session_logs

    Get session logs by crash ID

    :param crash_id: The id of the a crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param _date: Date of data requested
    :type _date: str

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)


async def devices_block_logs(request: web.Request, install_id, owner_name, app_name) -> web.Response:
    """devices_block_logs

    **Warning, this operation is not reversible.**   A successful call to this API will permanently stop ingesting any logs received via SDK for the given installation ID, and cannot be restored. We advise caution when using this API, it is designed to permanently disable collection from a specific installation of the app on a device, usually following the request from a user. 

    :param install_id: The id of the device
    :type install_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)
