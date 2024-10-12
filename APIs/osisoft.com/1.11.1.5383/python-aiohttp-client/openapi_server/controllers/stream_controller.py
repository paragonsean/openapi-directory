from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.extended_timed_value import ExtendedTimedValue
from openapi_server.models.extended_timed_values import ExtendedTimedValues
from openapi_server.models.items_stream_values import ItemsStreamValues
from openapi_server.models.items_substatus import ItemsSubstatus
from openapi_server.models.items_summary_value import ItemsSummaryValue
from openapi_server.models.stream_updates_register import StreamUpdatesRegister
from openapi_server.models.stream_updates_retrieve import StreamUpdatesRetrieve
from openapi_server.models.timed_value import TimedValue
from openapi_server.models.timed_values import TimedValues
from openapi_server import util


async def stream_get_channel(request: web.Request, web_id, heartbeat_rate=None, include_initial_values=None, web_id_type=None) -> web.Response:
    """Opens a channel that will send messages about any value changes for the specified stream.

    

    :param web_id: The ID of the stream.
    :type web_id: str
    :param heartbeat_rate: HeartbeatRate is an integer multiple of the Polling Interval. It specifies the rate at which a client will receive an empty message if there are no data updates. It can be used to check that the connection is still alive. Zero/negative values correspond to no heartbeat. By default, no empty messages will be sent to the user.
    :type heartbeat_rate: int
    :param include_initial_values: Specified if the channel should send a message with the current value of the stream after the connection is opened. The default is &#39;false&#39;.
    :type include_initial_values: bool
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_get_end(request: web.Request, web_id, desired_units=None, selected_fields=None) -> web.Response:
    """Returns the end-of-stream value of the stream.

    

    :param web_id: The ID of the stream.
    :type web_id: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str

    """
    return web.Response(status=200)


async def stream_get_interpolated(request: web.Request, web_id, desired_units=None, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, selected_fields=None, start_time=None, sync_time=None, sync_time_boundary_type=None, time_zone=None) -> web.Response:
    """Retrieves interpolated values over the specified time range at the specified sampling interval.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of the stream.
    :type web_id: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param interval: The sampling interval, in AFTimeSpan format.
    :type interval: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param sync_time: An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
    :type sync_time: str
    :param sync_time_boundary_type: An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;.
    :type sync_time_boundary_type: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_get_interpolated_at_times(request: web.Request, web_id, time, desired_units=None, filter_expression=None, include_filtered_values=None, selected_fields=None, sort_order=None, time_zone=None) -> web.Response:
    """Retrieves interpolated values over the specified time range at the specified sampling interval.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of the stream.
    :type web_id: str
    :param time: The timestamp at which to retrieve an interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
    :type time: List[str]
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_get_plot(request: web.Request, web_id, desired_units=None, end_time=None, intervals=None, selected_fields=None, start_time=None, time_zone=None) -> web.Response:
    """Retrieves values over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

    For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of the stream.
    :type web_id: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param intervals: The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
    :type intervals: int
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_get_recorded(request: web.Request, web_id, associations=None, boundary_type=None, desired_units=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, start_time=None, time_zone=None) -> web.Response:
    """Returns a list of compressed values for the requested time range from the source provider.

    Returned times are affected by the specified boundary type. If no values are found for the time range and conditions specified then the HTTP response will be success, with a body containing an empty array of Items. When specifying true for the includeFilteredValues parameter, consecutive filtered events are not returned. The first value that would be filtered out is returned with its time and the enumeration value \&quot;Filtered\&quot;. The next value in the collection will be the next compressed value in the specified direction that passes the filter criteria - if any. When both boundaryType and a filterExpression are specified, the events returned for the boundary condition specified are passed through the filter. If the includeFilteredValues parameter is true, the boundary values will be reported at the proper timestamps with the enumeration value \&quot;Filtered\&quot; when the filter conditions are not met at the boundary time. If the includeFilteredValues parameter is false for this case, no event is returned for the boundary time. Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.   If only recorded values with annotations are desired, the filterExpression parameter should include the filter IsSet(&#39;.&#39;, \&quot;a\&quot;).

    :param web_id: The ID of the stream.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned.
    :type associations: str
    :param boundary_type: An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;.
    :type boundary_type: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param max_count: The maximum number of values to be returned. The default is 1000.
    :type max_count: int
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_get_recorded_at_time(request: web.Request, web_id, time, associations=None, desired_units=None, retrieval_mode=None, selected_fields=None, time_zone=None) -> web.Response:
    """Returns a single recorded value based on the passed time and retrieval mode from the stream.

    If only recorded values with annotations are desired, the filterExpression parameter should include the filter IsSet(&#39;.&#39;, \&quot;a\&quot;).

    :param web_id: The ID of the stream.
    :type web_id: str
    :param time: The timestamp at which the value is desired.
    :type time: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned.
    :type associations: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param retrieval_mode: An optional value that determines the value to return when a value doesn&#39;t exist at the exact time specified. The default is &#39;Auto&#39;.
    :type retrieval_mode: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_get_recorded_at_times(request: web.Request, web_id, time, associations=None, desired_units=None, retrieval_mode=None, selected_fields=None, sort_order=None, time_zone=None) -> web.Response:
    """Retrieves recorded values at the specified times.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.   If only recorded values with annotations are desired, the filterExpression parameter should include the filter IsSet(&#39;.&#39;, \&quot;a\&quot;).

    :param web_id: The ID of the stream.
    :type web_id: str
    :param time: The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
    :type time: List[str]
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Annotations to return events with annotation values. If this parameter is not specified, annotation values are not returned.
    :type associations: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param retrieval_mode: An optional value that determines the value to return when a value doesn&#39;t exist at the exact time specified. The default is &#39;Auto&#39;.
    :type retrieval_mode: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_get_summary(request: web.Request, web_id, calculation_basis=None, end_time=None, filter_expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, time_zone=None) -> web.Response:
    """Returns a summary over the specified time range for the stream.

    Count is the only summary type supported on non-numeric streams. Requesting a summary for any other type will generate an error. Time-weighted totals are computed by integrating the rate tag values over the requested time range. If some of the data are bad in the time range, the calculated total is divided by the fraction of the time period for which there are good values. This approach is equivalent to assuming that during the period of bad data, the tag takes on the average values for the entire calculation time range. The PercentGood summary may be used to determine if the calculation results are suitable for the application&#39;s purposes. For time-weighted totals, if the time unit rate of the stream cannot be determined, then the value will be totaled assuming a unit of \&quot;per day\&quot; and no unit of measure will be assigned to the value. If the measured time component of the tag is not based on a day, the user of the data must convert the totalized value to the correct units.

    :param web_id: The ID of the stream.
    :type web_id: str
    :param calculation_basis: Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;.
    :type calculation_basis: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute.
    :type filter_expression: str
    :param sample_interval: When the sampleType is Interval, sampleInterval specifies how often the filter expression is evaluated when computing the summary for an interval.
    :type sample_interval: str
    :param sample_type: Defines the evaluation of an expression over a time range. The default is &#39;ExpressionRecordedValues&#39;.
    :type sample_type: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param summary_duration: The duration of each summary interval. If specified in hours, minutes, seconds, or milliseconds, the summary durations will be evenly spaced UTC time intervals. Longer interval types are interpreted using wall clock rules and are time zone dependent.
    :type summary_duration: str
    :param summary_type: Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType.
    :type summary_type: List[str]
    :param time_type: Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;.
    :type time_type: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_get_value(request: web.Request, web_id, desired_units=None, selected_fields=None, time=None, time_zone=None) -> web.Response:
    """Returns the value of the stream at the specified time. By default, this is usually the current value.

    

    :param web_id: The ID of the stream.
    :type web_id: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param time: An optional time. The default time context is determined from the owning object - for example, the time range of the event frame or transfer which holds this attribute. Otherwise, the implementation of the Data Reference determines the meaning of no context. For Points or simply configured PI Point Data References, this means the snapshot value of the PI Point on the Data Server.
    :type time: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str

    """
    return web.Response(status=200)


async def stream_register_stream_update(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Register for stream updates

    The supplied webId will register for stream updates. For a 201 or 204 response, the returned location header will contain the url for retrieving the next set of stream updates.

    :param web_id: The ID of the stream.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_retrieve_stream_update(request: web.Request, marker, desired_units=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Receive stream updates

    The supplied marker will identify the set of stream updates to retrieve. For a 200 response, the returned location header will contain the url for retrieving the stream updates.

    :param marker: Identifier of stream source and current position
    :type marker: str
    :param desired_units: The name or abbreviation of the desired units of measure for the returned value, as found in the UOM database associated with the attribute. If not specified for an attribute, the attribute&#39;s default unit of measure is used. If the underlying stream is a point, this value may not be specified, as points are not associated with a unit of measure.
    :type desired_units: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_update_value(request: web.Request, web_id, value, buffer_option=None, update_option=None, web_id_type=None) -> web.Response:
    """Updates a value for the specified stream.

    

    :param web_id: The ID of the stream.
    :type web_id: str
    :param value: The value to add or update.
    :type value: dict | bytes
    :param buffer_option: The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;.
    :type buffer_option: str
    :param update_option: The desired AFUpdateOption. The default is &#39;Replace&#39;. This parameter is ignored if the attribute is a configuration item.
    :type update_option: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    value = TimedValue.from_dict(value)
    return web.Response(status=200)


async def stream_update_values(request: web.Request, web_id, values, buffer_option=None, update_option=None) -> web.Response:
    """Updates multiple values for the specified stream.

    

    :param web_id: The ID of the stream.
    :type web_id: str
    :param values: The values to add or update.
    :type values: list | bytes
    :param buffer_option: The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;.
    :type buffer_option: str
    :param update_option: The desired AFUpdateOption. The default is &#39;Replace&#39;.
    :type update_option: str

    """
    values = [TimedValue.from_dict(d) for d in values]
    return web.Response(status=200)
