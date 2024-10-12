from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_inventory_task_request import CreateInventoryTaskRequest
from openapi_server.models.inventory_task import InventoryTask
from openapi_server.models.inventory_task_collection import InventoryTaskCollection
from openapi_server import util


async def create_inventory_task(request: web.Request, body) -> web.Response:
    """create_inventory_task

    This method creates an inventory-related download task for a specified feed type with optional filter criteria. When using this method, specify the &lt;strong&gt;feedType&lt;/strong&gt;. &lt;br/&gt;&lt;br/&gt;This method returns the location response header containing the &lt;strong&gt;getInventoryTask&lt;/strong&gt; call URI to retrieve the inventory task you just created. The URL includes the eBay-assigned task ID, which you can use to reference the inventory task.&lt;br/&gt;&lt;br/&gt;To retrieve the status of the task, use the &lt;strong&gt;getInventoryTask&lt;/strong&gt; method to retrieve a single task ID or the &lt;strong&gt;getInventoryTasks&lt;/strong&gt; method to retrieve multiple task IDs.&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The scope depends on the feed type. An error message results when an unsupported scope or feed type is specified.&lt;/span&gt;&lt;/p&gt;Presently, this method supports Active Inventory Report. The &lt;strong&gt;ActiveInventoryReport&lt;/strong&gt; returns a report that contains price and quantity information for all of the active listings for a specific seller. A seller can use this information to maintain their inventory on eBay.

    :param body: The request payload containing the version, feedType, and optional filterCriteria.
    :type body: dict | bytes

    """
    body = CreateInventoryTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_inventory_task(request: web.Request, task_id) -> web.Response:
    """get_inventory_task

    This method retrieves the task details and status of the specified inventory-related task. The input is &lt;strong&gt;task_id&lt;/strong&gt;.

    :param task_id: The ID of the task. This ID was generated when the task was created by the &lt;strong&gt;createInventoryTask&lt;/strong&gt; method
    :type task_id: str

    """
    return web.Response(status=200)


async def get_inventory_tasks(request: web.Request, feed_type=None, schedule_id=None, look_back_days=None, date_range=None, limit=None, offset=None) -> web.Response:
    """get_inventory_tasks

    This method searches for multiple tasks of a specific feed type, and includes date filters and pagination.

    :param feed_type: The feed type associated with the inventory task. Either &lt;strong&gt;feed_type&lt;/strong&gt; or &lt;strong&gt;schedule_id&lt;/strong&gt; is required. Do not use with the &lt;strong&gt;schedule_id&lt;/strong&gt; parameter. Presently, only one feed type is available:&lt;ul&gt;&lt;li&gt;&lt;code&gt;LMS_ACTIVE_INVENTORY_REPORT&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;
    :type feed_type: str
    :param schedule_id: The ID of the schedule for which to retrieve the latest result file. This ID is generated when the schedule was created by the &lt;strong&gt;createSchedule&lt;/strong&gt; method. Schedules apply to downloaded reports (&lt;code&gt;LMS_ACTIVE_INVENTORY_REPORT&lt;/code&gt;). Either &lt;strong&gt;schedule_id&lt;/strong&gt; or &lt;strong&gt;feed_type&lt;/strong&gt; is  required. Do not use with the &lt;strong&gt;feed_type&lt;/strong&gt; parameter.
    :type schedule_id: str
    :param look_back_days: The number of previous days in which to search for tasks. Do not use with the &lt;code&gt;date_range&lt;/code&gt; parameter. If both &lt;code&gt;date_range&lt;/code&gt; and &lt;code&gt;look_back_days&lt;/code&gt; are omitted, this parameter&#39;s default value is used.  &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt; 7 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Range: &lt;/b&gt; 1-90 (inclusive)
    :type look_back_days: str
    :param date_range: Specifies the range of task creation dates used to filter the results. The results are filtered to include only tasks with a creation date that is equal to this date or is within specified range. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Maximum date range window size is 90 days.&lt;/span&gt;&lt;/p&gt;&lt;br /&gt;&lt;b&gt;Valid Format (UTC): &lt;/b&gt;&lt;code&gt;yyyy-MM-ddThh:mm:ss.SSSZ..yyyy-MM-ddThh:mm:ss.SSSZ&lt;/code&gt;&lt;br /&gt;&lt;br /&gt;For example: Tasks created on March 31, 2021&lt;br /&gt; &lt;code&gt;2021-03-31T00:00:00.000Z..2021-03-31T00:00:00.000Z&lt;/code&gt;&lt;br /&gt;&lt;br /&gt;
    :type date_range: str
    :param limit: The maximum number of tasks that can be returned on each page of the paginated response. Use this parameter in conjunction with the &lt;strong&gt;offset&lt;/strong&gt; parameter to control the pagination of the output. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This feature employs a zero-based list, where the first item in the list has an offset of &lt;code&gt;0&lt;/code&gt;.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;For example, if &lt;strong&gt;offset&lt;/strong&gt; is set to 10 and &lt;strong&gt;limit&lt;/strong&gt; is set to 10, the call retrieves tasks 11 thru 20 from the result set.&lt;/p&gt;&lt;p&gt;If this parameter is omitted, the default value is used. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt; 10 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt;500
    :type limit: str
    :param offset: The number of tasks to skip in the result set before returning the first task in the paginated response. &lt;p&gt;Combine &lt;strong&gt;offset&lt;/strong&gt; with the &lt;strong&gt;limit&lt;/strong&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;strong&gt;offset&lt;/strong&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;strong&gt;limit&lt;/strong&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;strong&gt;offset&lt;/strong&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;strong&gt;limit&lt;/strong&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set. If this query parameter is not set, the default value is used and the first page of records is returned. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt;0
    :type offset: str

    """
    return web.Response(status=200)
