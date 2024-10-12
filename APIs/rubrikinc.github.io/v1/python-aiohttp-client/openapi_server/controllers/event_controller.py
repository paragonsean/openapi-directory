from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_log_summary_v1_list_response import ActivityLogSummaryV1ListResponse
from openapi_server.models.event_csv_download_response import EventCsvDownloadResponse
from openapi_server.models.events_and_series_summaries_v1 import EventsAndSeriesSummariesV1
from openapi_server import util


async def get_events_csv_download_link(request: web.Request, limit=None, event_series_status=None, event_status=None, event_type=None, event_severity=None, object_ids=None, object_type=None, object_name=None, after_id=None, before_date=None, after_date=None, order_by_time=None) -> web.Response:
    """Download summary of events as a CSV file

    Download summary of the related events that match the value specified in the following categories: event type, status, object name or ID, eventSeriesId, object type, and limit events by dates.

    :param limit: Maximum number of events to retrieve. Default value is 100.
    :type limit: int
    :param event_series_status: Filter by the current status of the event series.
    :type event_series_status: str
    :param event_status: Filter by the status of the latest event in the event series.
    :type event_status: str
    :param event_type: Filter by the type of the latest event in the event series.
    :type event_type: str
    :param event_severity: Filter by the severity of the latest event in the event series.
    :type event_severity: str
    :param object_ids: Filter the object IDs in the latest event series by matches to a comma-separated list of object IDs.
    :type object_ids: List[str]
    :param object_type: Filter the events in the event series by a specified object type.
    :type object_type: str
    :param object_name: Filter latest events according to the provided name using prefix search for resources and exact search for usernames.
    :type object_name: str
    :param after_id: An (event_series_id, time) tuple. When specified, returns all event series whose latest event timestamp comes after the time value of after_id based on the sort order defined by the order_by_time parameter.
    :type after_id: str
    :param before_date: Filter out event series that have events occurring after the specified date.
    :type before_date: str
    :param after_date: Filter out event series that have events occurring before the specified date.
    :type after_date: str
    :param order_by_time: The events in a series are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is desc.
    :type order_by_time: str

    """
    before_date = util.deserialize_datetime(before_date)
    after_date = util.deserialize_datetime(after_date)
    return web.Response(status=200)


async def query_event_v1(request: web.Request, limit=None, after_id=None, before_date=None, after_date=None, order_by_time=None, should_include_event_series=None) -> web.Response:
    """Get information for all events

    Returns information for all events. Only Global or Read Only Admins and Support users have authorization to use this endpoint. Accepts filters. For similar functionality to the previous /internal/event endpoint, use the /v1/event/latest endpoint.

    :param limit: Maximum number of events retrieved.
    :type limit: int
    :param after_id: An (event_id, time) tuple. When specified, returns all events with timestamps that come after the time value of after_id based on the sort order defined by the order_by_time parameter.
    :type after_id: str
    :param before_date: Filter the events occurring after the specified date.
    :type before_date: str
    :param after_date: Filter the events occurring before the specified date.
    :type after_date: str
    :param order_by_time: The events are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is asc.
    :type order_by_time: str
    :param should_include_event_series: A Boolean value that determines whether to include event series summary for every event. If set to &#39;true&#39;, a list of event series summary will be returned and each summary has an empty list of events. If set to &#39;false&#39;, an empty list of event series summary will be returned. The default value is &#39;false&#39;. Setting it to &#39;true&#39; will increase the response time.
    :type should_include_event_series: bool

    """
    before_date = util.deserialize_datetime(before_date)
    after_date = util.deserialize_datetime(after_date)
    return web.Response(status=200)


async def query_latest_events_v1(request: web.Request, limit=None, event_series_status=None, event_status=None, event_type=None, event_severity=None, object_ids=None, object_type=None, object_name=None, after_id=None, before_date=None, after_date=None, order_by_time=None, should_include_event_series=None) -> web.Response:
    """Get latest events with their associated event series information

    Get the latest event, event series status, and the number of warning events for all event series. This endpoint has similar/enhanced functionality to the previously deprecated /internal/event endpoint.

    :param limit: Maximum number of events retrieved.
    :type limit: int
    :param event_series_status: Filter by the current status of the event series.
    :type event_series_status: str
    :param event_status: Filter by the status of the latest event in the event series.
    :type event_status: str
    :param event_type: Filter by the type of the latest event in the event series.
    :type event_type: str
    :param event_severity: Filter by the severity of the latest event in the event series.
    :type event_severity: str
    :param object_ids: Filter the object IDs in the latest event series by matches to a comma-separated list of object IDs.
    :type object_ids: List[str]
    :param object_type: Filter the events in the event series by a specified object type.
    :type object_type: str
    :param object_name: Filter latest events according to the provided name using prefix search for resources and exact search for usernames.
    :type object_name: str
    :param after_id: An (event_series_id, time) tuple. When specified, returns all event series whose latest event timestamp comes after the time value of after_id based on the sort order defined by the order_by_time parameter.
    :type after_id: str
    :param before_date: Filter out event series that have events occurring after the specified date.
    :type before_date: str
    :param after_date: Filter out event series that have events occurring before the specified date.
    :type after_date: str
    :param order_by_time: The events in a series are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is desc.
    :type order_by_time: str
    :param should_include_event_series: A Boolean value that determines whether to include all events in the event series. The default value is &#39;false&#39;. Setting it to &#39;true&#39; will significantly increase the response time.
    :type should_include_event_series: bool

    """
    before_date = util.deserialize_datetime(before_date)
    after_date = util.deserialize_datetime(after_date)
    return web.Response(status=200)
