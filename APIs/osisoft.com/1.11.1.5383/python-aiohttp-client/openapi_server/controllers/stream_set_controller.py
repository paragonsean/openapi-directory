from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_items_substatus import ItemsItemsSubstatus
from openapi_server.models.items_stream_summaries import ItemsStreamSummaries
from openapi_server.models.items_stream_updates_register import ItemsStreamUpdatesRegister
from openapi_server.models.items_stream_updates_retrieve import ItemsStreamUpdatesRetrieve
from openapi_server.models.items_stream_value import ItemsStreamValue
from openapi_server.models.items_stream_values import ItemsStreamValues
from openapi_server.models.items_substatus import ItemsSubstatus
from openapi_server.models.stream_value import StreamValue
from openapi_server.models.stream_values import StreamValues
from openapi_server import util


async def stream_set_get_channel(request: web.Request, web_id, category_name=None, heartbeat_rate=None, include_initial_values=None, name_filter=None, search_full_hierarchy=None, show_excluded=None, show_hidden=None, template_name=None, web_id_type=None) -> web.Response:
    """Opens a channel that will send messages about any value changes for the attributes of an Element, Event Frame, or Attribute.

    

    :param web_id: The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param heartbeat_rate: Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat.
    :type heartbeat_rate: int
    :param include_initial_values: Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;.
    :type include_initial_values: bool
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_channel_ad_hoc(request: web.Request, web_id, heartbeat_rate=None, include_initial_values=None, web_id_type=None) -> web.Response:
    """Opens a channel that will send messages about any value changes for the specified streams.

    

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param heartbeat_rate: Specifies the maximum number of consecutive empty messages that can be elapsed with no new data updates from the PI System, after which the client receives an empty payload. It helps to check if the connection is still alive. Zero/negative values correspond to no heartbeat, and the default value is no heartbeat.
    :type heartbeat_rate: int
    :param include_initial_values: Specified if the channel should send a message with the current values of all the streams after the connection is opened. The default is &#39;false&#39;.
    :type include_initial_values: bool
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_end(request: web.Request, web_id, category_name=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, template_name=None, web_id_type=None) -> web.Response:
    """Returns End of stream values of the attributes for an Element, Event Frame or Attribute

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_end_ad_hoc(request: web.Request, web_id, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None) -> web.Response:
    """Returns End Of Stream values for attributes of the specified streams

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_interpolated(request: web.Request, web_id, category_name=None, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, sync_time=None, sync_time_boundary_type=None, template_name=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns interpolated values of attributes for an element, event frame or attribute over the specified time range at the specified sampling interval.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param interval: The sampling interval, in AFTimeSpan format.
    :type interval: str
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param sync_time: An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
    :type sync_time: str
    :param sync_time_boundary_type: An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;.
    :type sync_time_boundary_type: str
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_interpolated_ad_hoc(request: web.Request, web_id, end_time=None, filter_expression=None, include_filtered_values=None, interval=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, sync_time=None, sync_time_boundary_type=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns interpolated values of the specified streams over the specified time range at the specified sampling interval.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param end_time: An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param interval: The sampling interval, in AFTimeSpan format.
    :type interval: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39;.
    :type start_time: str
    :param sync_time: An optional start time anchor, in AFTime format. When specified, interpolated data retrieval will use the sync time as the origin for calculating the interval times.
    :type sync_time: str
    :param sync_time_boundary_type: An optional string specifying the boundary type to use when applying a syncTime. The allowed values are &#39;Inside&#39; and &#39;Outside&#39;. The default is &#39;Inside&#39;.
    :type sync_time_boundary_type: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_interpolated_at_times(request: web.Request, web_id, time, category_name=None, filter_expression=None, include_filtered_values=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_order=None, template_name=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns interpolated values of attributes for an element, event frame or attribute at the specified times.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param time: The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
    :type time: List[str]
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. If the attribute does not support filtering, the filter will be ignored. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_interpolated_at_times_ad_hoc(request: web.Request, time, web_id, filter_expression=None, include_filtered_values=None, selected_fields=None, sort_order=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns interpolated values of the specified streams at the specified times.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param time: The timestamp at which to retrieve a interpolated value. Multiple timestamps may be specified with multiple instances of the parameter.
    :type time: List[str]
    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
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
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_joined(request: web.Request, base_web_id, subordinate_web_id, boundary_type=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, start_time=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns the base stream&#39;s recorded values and subordinate streams&#39; interpolated values at times matching the recorded values&#39; timestamps.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream. The first stream in the response is always the X-Axis.

    :param base_web_id: The ID of the base stream which is used for retrieving the recorded values.
    :type base_web_id: str
    :param subordinate_web_id: The ID of a stream whose values will be joined on the times with the values of the base stream. Multiple streams may be specified with multiple instances of the parameter.
    :type subordinate_web_id: List[str]
    :param boundary_type: An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;.
    :type boundary_type: str
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
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either place, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_plot(request: web.Request, web_id, category_name=None, end_time=None, intervals=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, template_name=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns values of attributes for an element, event frame or attribute over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

    For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param intervals: The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
    :type intervals: int
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_plot_ad_hoc(request: web.Request, web_id, end_time=None, intervals=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns values of attributes for the specified streams over the specified time range suitable for plotting over the number of intervals (typically represents pixels).

    For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state). Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param end_time: An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param intervals: The number of intervals to plot over. Typically, this would be the number of horizontal pixels in the trend. The default is &#39;24&#39;. For each interval, the data available is examined and significant values are returned. Each interval can produce up to 5 values if they are unique, the first value in the interval, the last value, the highest value, the lowest value and at most one exceptional point (bad status or digital state).
    :type intervals: int
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39;.
    :type start_time: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_recorded(request: web.Request, web_id, boundary_type=None, category_name=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_time=None, template_name=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns recorded values of the attributes for an element, event frame, or attribute.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param boundary_type: An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;.
    :type boundary_type: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param max_count: The maximum number of values to be returned. The default is 1000.
    :type max_count: int
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_recorded_ad_hoc(request: web.Request, web_id, boundary_type=None, end_time=None, filter_expression=None, include_filtered_values=None, max_count=None, selected_fields=None, sort_field=None, sort_order=None, start_time=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns recorded values of the specified streams.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param boundary_type: An optional value that determines how the times and values of the returned end points are determined. The default is &#39;Inside&#39;.
    :type boundary_type: str
    :param end_time: An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: An optional string containing a filter expression. Expression variables are relative to the data point. Use &#39;.&#39; to reference the containing attribute. The default is no filtering.
    :type filter_expression: str
    :param include_filtered_values: Specify &#39;true&#39; to indicate that values which fail the filter criteria are present in the returned data at the times where they occurred with a value set to a &#39;Filtered&#39; enumeration value with bad status. Repeated consecutive failures are omitted.
    :type include_filtered_values: bool
    :param max_count: The maximum number of values to be returned. The default is 1000.
    :type max_count: int
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39;.
    :type start_time: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_recorded_at_time(request: web.Request, web_id, time, category_name=None, name_filter=None, retrieval_mode=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, template_name=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns recorded values of the attributes for an element, event frame, or attribute.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param time: The timestamp at which the values are desired.
    :type time: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param retrieval_mode: An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;.
    :type retrieval_mode: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_recorded_at_time_ad_hoc(request: web.Request, time, web_id, retrieval_mode=None, selected_fields=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns recorded values based on the passed time and retrieval mode.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param time: The timestamp at which the values are desired.
    :type time: str
    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param retrieval_mode: An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;.
    :type retrieval_mode: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_recorded_at_times(request: web.Request, web_id, time, category_name=None, name_filter=None, retrieval_mode=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_order=None, template_name=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns recorded values of attributes for an element, event frame or attribute at the specified times.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param time: The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
    :type time: List[str]
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param retrieval_mode: An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;.
    :type retrieval_mode: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_recorded_at_times_ad_hoc(request: web.Request, time, web_id, retrieval_mode=None, selected_fields=None, sort_order=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns recorded values of the specified streams at the specified times.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param time: The timestamp at which to retrieve a recorded value. Multiple timestamps may be specified with multiple instances of the parameter.
    :type time: List[str]
    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param retrieval_mode: An optional value that determines the values to return when values don&#39;t exist at the exact time specified. The default is &#39;Auto&#39;.
    :type retrieval_mode: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_summaries(request: web.Request, web_id, calculation_basis=None, category_name=None, end_time=None, filter_expression=None, name_filter=None, sample_interval=None, sample_type=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, start_time=None, summary_duration=None, summary_type=None, template_name=None, time_type=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns summary values of the attributes for an element, event frame or attribute.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an element, event frame or attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param calculation_basis: Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;.
    :type calculation_basis: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering.
    :type filter_expression: str
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param sample_interval: A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;.
    :type sample_interval: str
    :param sample_type: A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;.
    :type sample_type: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param summary_duration: The duration of each summary interval.
    :type summary_duration: str
    :param summary_type: Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType.
    :type summary_type: List[str]
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time_type: Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;.
    :type time_type: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_summaries_ad_hoc(request: web.Request, web_id, calculation_basis=None, end_time=None, filter_expression=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns summary values of the specified streams.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param calculation_basis: Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;.
    :type calculation_basis: str
    :param end_time: An optional end time. The default is &#39;*&#39;. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param filter_expression: A string containing a filter expression. Expression variables are relative to the attribute. Use &#39;.&#39; to reference the containing attribute. The default is no filtering.
    :type filter_expression: str
    :param sample_interval: A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;.
    :type sample_interval: str
    :param sample_type: A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;.
    :type sample_type: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39;.
    :type start_time: str
    :param summary_duration: The duration of each summary interval.
    :type summary_duration: str
    :param summary_type: Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType.
    :type summary_type: List[str]
    :param time_type: Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;.
    :type time_type: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_values(request: web.Request, web_id, category_name=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, template_name=None, time=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns values of the attributes for an Element, Event Frame or Attribute at the specified time.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of an Element, Event Frame or Attribute, which is the base element or parent of all the stream attributes.
    :type web_id: str
    :param category_name: Specify that included attributes must have this category. The default is no category filter.
    :type category_name: str
    :param name_filter: The name query string used for filtering attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param template_name: Specify that included attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param time: An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.
    :type time: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_get_values_ad_hoc(request: web.Request, web_id, selected_fields=None, sort_field=None, sort_order=None, time=None, time_zone=None, web_id_type=None) -> web.Response:
    """Returns values of the specified streams.

    Any time series value in the response that contains an &#39;Errors&#39; property indicates PI Web API encountered a handled error during the transfer of the response stream.

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. For better performance, by default no sorting is applied. &#39;Name&#39; is the only supported field by which to sort.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;
    :type sort_order: str
    :param time: An AF time string, which is used as the time context to get stream values if it is provided. By default, it is not specified, and the default time context of the AF object will be used.
    :type time: str
    :param time_zone: The time zone in which the time string will be interpreted. This parameter will be ignored if a time zone is specified in the time string. If no time zone is specified in either places, the PI Web API server time zone will be used.
    :type time_zone: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_register_stream_set_updates(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Register for stream updates

    The supplied webIds will register for stream updates. For a 200 response, the returned location header will contain the url for retrieving the next set of stream updates.

    :param web_id: The ID of a stream. Multiple streams may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_retrieve_stream_set_updates(request: web.Request, marker, selected_fields=None, web_id_type=None) -> web.Response:
    """Receive stream updates

    The supplied markers will identify the set of stream updates to retrieve. For a 200 response, the returned location header will contain the url for retrieving the stream updates.

    :param marker: Identifier of stream source and current position. Multiple markers may be specified with multiple instances of the parameter.
    :type marker: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def stream_set_update_value(request: web.Request, web_id, values, buffer_option=None, update_option=None) -> web.Response:
    """Updates a single value for the specified streams.

    

    :param web_id: The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
    :type web_id: str
    :param values: The values to add or update.
    :type values: list | bytes
    :param buffer_option: The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;.
    :type buffer_option: str
    :param update_option: The desired AFUpdateOption. The default is &#39;Replace&#39;.
    :type update_option: str

    """
    values = [StreamValue.from_dict(d) for d in values]
    return web.Response(status=200)


async def stream_set_update_value_ad_hoc(request: web.Request, values, buffer_option=None, update_option=None) -> web.Response:
    """Updates a single value for the specified streams.

    

    :param values: The values to add or update.
    :type values: list | bytes
    :param buffer_option: The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;.
    :type buffer_option: str
    :param update_option: The desired AFUpdateOption. The default is &#39;Replace&#39;.
    :type update_option: str

    """
    values = [StreamValue.from_dict(d) for d in values]
    return web.Response(status=200)


async def stream_set_update_values(request: web.Request, web_id, values, buffer_option=None, update_option=None) -> web.Response:
    """Updates multiple values for the specified streams.

    

    :param web_id: The ID of the parent element, event frame, or attribute. Attributes specified in the body must be descendants of the specified object.
    :type web_id: str
    :param values: The values to add or update.
    :type values: list | bytes
    :param buffer_option: The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;.
    :type buffer_option: str
    :param update_option: The desired AFUpdateOption. The default is &#39;Replace&#39;.
    :type update_option: str

    """
    values = [StreamValues.from_dict(d) for d in values]
    return web.Response(status=200)


async def stream_set_update_values_ad_hoc(request: web.Request, values, buffer_option=None, update_option=None) -> web.Response:
    """Updates multiple values for the specified streams.

    

    :param values: The values to add or update.
    :type values: list | bytes
    :param buffer_option: The desired AFBufferOption. The default is &#39;BufferIfPossible&#39;.
    :type buffer_option: str
    :param update_option: The desired AFUpdateOption. The default is &#39;Replace&#39;.
    :type update_option: str

    """
    values = [StreamValues.from_dict(d) for d in values]
    return web.Response(status=200)
