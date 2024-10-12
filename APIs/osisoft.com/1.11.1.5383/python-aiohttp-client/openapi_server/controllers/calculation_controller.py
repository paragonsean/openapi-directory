from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_summary_value import ItemsSummaryValue
from openapi_server.models.timed_values import TimedValues
from openapi_server import util


async def calculation_get_at_intervals(request: web.Request, expression, end_time=None, sample_interval=None, selected_fields=None, start_time=None, web_id=None) -> web.Response:
    """Returns results of evaluating the expression over the time range from the start time to the end time at a defined interval.

    

    :param expression: A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    :type expression: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param sample_interval: A time span specifies how often the filter expression is evaluated when computing the summary for an interval.
    :type sample_interval: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param web_id: The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    :type web_id: str

    """
    return web.Response(status=200)


async def calculation_get_at_recorded(request: web.Request, expression, end_time=None, selected_fields=None, start_time=None, web_id=None) -> web.Response:
    """Returns the result of evaluating the expression at each point in time over the time range from the start time to the end time where a recorded value exists for a member of the expression.

    

    :param expression: A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    :type expression: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param web_id: The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    :type web_id: str

    """
    return web.Response(status=200)


async def calculation_get_at_times(request: web.Request, expression, time, selected_fields=None, sort_order=None, web_id=None) -> web.Response:
    """Returns the result of evaluating the expression at the specified timestamps.

    

    :param expression: A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    :type expression: str
    :param time: A list of timestamps at which to calculate the expression.
    :type time: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param web_id: The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    :type web_id: str

    """
    return web.Response(status=200)


async def calculation_get_summary(request: web.Request, expression, calculation_basis=None, end_time=None, sample_interval=None, sample_type=None, selected_fields=None, start_time=None, summary_duration=None, summary_type=None, time_type=None, web_id=None) -> web.Response:
    """Returns the result of evaluating the expression over the time range from the start time to the end time. The time range is first divided into a number of summary intervals. Then the calculation is performed for the specified summaries over each interval.

    

    :param expression: A string containing the expression to be evaluated. The syntax for the expression generally follows the Performance Equation syntax as described in the PI Server documentation, with the exception that expressions which target AF objects use attribute names in place of tag names in the equation.
    :type expression: str
    :param calculation_basis: Specifies the method of evaluating the data over the time range. The default is &#39;TimeWeighted&#39;.
    :type calculation_basis: str
    :param end_time: An optional end time. The default is &#39;*&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s end time, or &#39;*&#39; if that is not set. Note that if endTime is earlier than startTime, the resulting values will be in time-descending order.
    :type end_time: str
    :param sample_interval: A time span specifies how often the filter expression is evaluated when computing the summary for an interval, if the sampleType is &#39;Interval&#39;.
    :type sample_interval: str
    :param sample_type: A flag which specifies one or more summaries to compute for each interval over the time range. The default is &#39;ExpressionRecordedValues&#39;.
    :type sample_type: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_time: An optional start time. The default is &#39;*-1d&#39; for element attributes and points. For event frame attributes, the default is the event frame&#39;s start time, or &#39;*-1d&#39; if that is not set.
    :type start_time: str
    :param summary_duration: The duration of each summary interval.
    :type summary_duration: str
    :param summary_type: Specifies the kinds of summaries to produce over the range. The default is &#39;Total&#39;. Multiple summary types may be specified by using multiple instances of summaryType.
    :type summary_type: List[str]
    :param time_type: Specifies how to calculate the timestamp for each interval. The default is &#39;Auto&#39;.
    :type time_type: str
    :param web_id: The ID of the target object of the expression. A target object can be a Data Server, a database, an element, an event frame or an attribute. References to attributes or points are based on the target. If this parameter is not provided, the target object is set to null.
    :type web_id: str

    """
    return web.Response(status=200)
