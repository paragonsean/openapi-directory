from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_order_task_request import CreateOrderTaskRequest
from openapi_server.models.order_task import OrderTask
from openapi_server.models.order_task_collection import OrderTaskCollection
from openapi_server import util


async def create_order_task(request: web.Request, body) -> web.Response:
    """create_order_task

    This method creates an order download task with filter criteria for the order report. When using this method, specify the &lt;b&gt; feedType&lt;/b&gt;, &lt;b&gt; schemaVersion&lt;/b&gt;, and &lt;b&gt; filterCriteria&lt;/b&gt; for the report. The method returns the &lt;b&gt; location&lt;/b&gt; response header containing the getOrderTask call URI to retrieve the order task you just created. The URL includes the eBay-assigned task ID, which you can use to reference the order task. &lt;br /&gt;&lt;br /&gt;To retrieve the status of the task, use the &lt;b&gt; getOrderTask&lt;/b&gt; method to retrieve a single task ID or the &lt;b&gt;getOrderTasks&lt;/b&gt; method to retrieve multiple order task IDs.&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The scope depends on the feed type. An error message results when an unsupported scope or feed type is specified.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;The following list contains this method&#39;s authorization scope and its corresponding feed type:&lt;ul&gt;&lt;li&gt;https://api.ebay.com/oauth/api_scope/sell.fulfillment: LMS_ORDER_REPORT&lt;/li&gt;&lt;/ul&gt; &lt;/p&gt;&lt;p&gt;For details about how this method is used, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/general-feed-tasks.html\&quot;&gt;General feed types&lt;/a&gt; in the Selling Integration Guide. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; At this time, the &lt;strong&gt;createOrderTask&lt;/strong&gt; method only supports order creation date filters and not modified order date filters. Do not include the &lt;strong&gt;modifiedDateRange&lt;/strong&gt; filter in your request payload.&lt;/span&gt;&lt;/p&gt;

    :param body: description not needed
    :type body: dict | bytes

    """
    body = CreateOrderTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_order_task(request: web.Request, task_id) -> web.Response:
    """get_order_task

    This method retrieves the task details and status of the specified task. The input is &lt;strong&gt;task_id&lt;/strong&gt;. &lt;p&gt;For details about how this method is used, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html\&quot;&gt;Working with Order Feeds&lt;/a&gt; in the Selling Integration Guide.  &lt;/p&gt;

    :param task_id: The ID of the task. This ID is generated when the task was created by the &lt;b&gt; createOrderTask&lt;/b&gt; method.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_order_tasks(request: web.Request, date_range=None, feed_type=None, limit=None, look_back_days=None, offset=None, schedule_id=None) -> web.Response:
    """get_order_tasks

    This method returns the details and status for an array of order tasks based on a specified &lt;strong&gt;feed_type&lt;/strong&gt; or &lt;strong&gt;schedule_id&lt;/strong&gt;. Specifying both &lt;strong&gt;feed_type&lt;/strong&gt; and &lt;strong&gt;schedule_id&lt;/strong&gt; results in an error. Since schedules are based on feed types, you can specify a schedule (&lt;strong&gt;schedule_id&lt;/strong&gt;) that returns the needed &lt;strong&gt;feed_type&lt;/strong&gt;.&lt;br /&gt;&lt;br /&gt;If specifying the &lt;strong&gt;feed_type&lt;/strong&gt;, limit which order tasks are returned by specifying filters such as the creation date range or period of time using &lt;strong&gt;look_back_days&lt;/strong&gt;. &lt;br /&gt;&lt;br /&gt;If specifying a &lt;strong&gt;schedule_id&lt;/strong&gt;, the schedule template (that the &lt;strong&gt;schedule_id&lt;/strong&gt; is based on) determines which order tasks are returned (see &lt;strong&gt;schedule_id&lt;/strong&gt; for additional information). Each &lt;strong&gt;schedule_id&lt;/strong&gt; applies to one &lt;strong&gt;feed_type&lt;/strong&gt;.

    :param date_range: The order tasks creation date range. This range is used to filter the results. The filtered results are filtered to include only tasks with a creation date that is equal to this date or is within specified range. Only orders less than 90 days old can be retrieved. Do not use with the &lt;strong&gt;look_back_days&lt;/strong&gt; parameter. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Format: &lt;/b&gt;UTC   &lt;br /&gt;&lt;br /&gt; &lt;b&gt; For example: &lt;/b&gt; &lt;br /&gt;&lt;br /&gt;Tasks within a range  &lt;br /&gt; &lt;code&gt;yyyy-MM-ddThh:mm:ss.SSSZ..yyyy-MM-ddThh:mm:ss.SSSZ &lt;/code&gt; &lt;br /&gt;&lt;br /&gt; Tasks created on September 8, 2019&lt;br /&gt; &lt;code&gt;2019-09-08T00:00:00.000Z..2019-09-09T00:00:00.000Z&lt;/code&gt;&lt;br /&gt;
    :type date_range: str
    :param feed_type: The feed type associated with the task. The only presently supported value is &lt;code&gt;LMS_ORDER_REPORT&lt;/code&gt;. Do not use with the &lt;strong&gt;schedule_id&lt;/strong&gt; parameter. Since schedules are based on feed types, you can specify a schedule (&lt;strong&gt;schedule_id&lt;/strong&gt;) that returns the needed &lt;strong&gt;feed_type&lt;/strong&gt;.
    :type feed_type: str
    :param limit: The maximum number of order tasks that can be returned on each page of the paginated response. Use this parameter in conjunction with the &lt;strong&gt;offset&lt;/strong&gt; parameter to control the pagination of the output. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This feature employs a zero-based list, where the first item in the list has an offset of &lt;code&gt;0&lt;/code&gt;.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;For example, if &lt;strong&gt;offset&lt;/strong&gt; is set to 10 and &lt;strong&gt;limit&lt;/strong&gt; is set to 10, the call retrieves order tasks 11 thru 20 from the result set.&lt;/p&gt;&lt;p&gt;If this parameter is omitted, the default value is used.&lt;/p&gt;&lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 10 &lt;p&gt;&lt;b&gt;Maximum:&lt;/b&gt; 500&lt;/p&gt;
    :type limit: str
    :param look_back_days: The number of previous days in which to search for tasks. Do not use with the &lt;strong&gt;date_range&lt;/strong&gt; parameter. If both &lt;strong&gt;date_range&lt;/strong&gt; and &lt;strong&gt;look_back_days&lt;/strong&gt; are omitted, this parameter&#39;s default value is used.  &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt; 7 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Range: &lt;/b&gt; 1-90 (inclusive)  
    :type look_back_days: str
    :param offset: The number of order tasks to skip in the result set before returning the first order in the paginated response. &lt;p&gt;Combine &lt;strong&gt;offset&lt;/strong&gt; with the &lt;strong&gt;limit&lt;/strong&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;strong&gt;offset&lt;/strong&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;strong&gt;limit&lt;/strong&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;strong&gt;offset&lt;/strong&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;strong&gt;limit&lt;/strong&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set. If this query parameter is not set, the default value is used and the first page of records is returned.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt;0
    :type offset: str
    :param schedule_id: The schedule ID associated with the order task. A schedule periodically generates a report for the feed type specified by the schedule template (see &lt;strong&gt;scheduleTemplateId&lt;/strong&gt; in &lt;strong&gt;createSchedule&lt;/strong&gt;). Do not use with the &lt;strong&gt;feed_type&lt;/strong&gt; parameter. Since schedules are based on feed types, you can specify a schedule (&lt;strong&gt;schedule_id&lt;/strong&gt;) that returns the needed &lt;strong&gt;feed_type&lt;/strong&gt;.
    :type schedule_id: str

    """
    return web.Response(status=200)
