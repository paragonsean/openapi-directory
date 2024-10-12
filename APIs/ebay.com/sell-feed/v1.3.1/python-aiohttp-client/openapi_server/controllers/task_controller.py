from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_task_request import CreateTaskRequest
from openapi_server.models.task import Task
from openapi_server.models.task_collection import TaskCollection
from openapi_server import util


async def create_task(request: web.Request, body, x_ebay_c_marketplace_id=None) -> web.Response:
    """create_task

    This method creates an upload task or a download task without filter criteria. When using this method, specify the &lt;b&gt; feedType&lt;/b&gt; and the feed file &lt;b&gt; schemaVersion&lt;/b&gt;. The feed type specified sets the task as a download or an upload task.  &lt;p&gt;For details about the upload and download flows, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html\&quot;&gt;Working with Order Feeds&lt;/a&gt; in the Selling Integration Guide.&lt;/p&gt;&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The scope depends on the feed type. An error message results when an unsupported scope or feed type is specified.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;The following list contains this method&#39;s authorization scopes and their corresponding feed types:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;https://api.ebay.com/oauth/api_scope/sell.inventory: See &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Availabl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;LMS FeedTypes&lt;/a&gt;&lt;/li&gt;&lt;li&gt;https://api.ebay.com/oauth/api_scope/sell.fulfillment: LMS_ORDER_ACK (specify for upload tasks). Also see &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Availabl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;LMS FeedTypes&lt;/a&gt;&lt;/li&gt;&lt;li&gt;https://api.ebay.com/oauth/api_scope/sell.marketing: None*&lt;/li&gt;&lt;li&gt;https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly: None*&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;* Reserved for future release&lt;/p&gt;

    :param body: description not needed
    :type body: dict | bytes
    :param x_ebay_c_marketplace_id: The ID of the eBay marketplace where the item is hosted. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This value is case sensitive.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;For example:&lt;/p&gt;&lt;p&gt;&lt;code&gt;X-EBAY-C-MARKETPLACE-ID:EBAY_US&lt;/code&gt;&lt;/p&gt;&lt;p&gt;This identifies the eBay marketplace that applies to this task. See &lt;a href&#x3D;\&quot;/api-docs/sell/feed/types/bas:MarketplaceIdEnum\&quot;&gt;MarketplaceIdEnum&lt;/a&gt;.&lt;/p&gt;
    :type x_ebay_c_marketplace_id: str

    """
    body = CreateTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_input_file(request: web.Request, task_id) -> web.Response:
    """get_input_file

    This method downloads the file previously uploaded using &lt;strong&gt;uploadFile&lt;/strong&gt;. Specify the task_id from the &lt;strong&gt;uploadFile&lt;/strong&gt; call. &lt;p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; With respect to LMS, this method applies to all feed types except &lt;code&gt;LMS_ORDER_REPORT&lt;/code&gt; and &lt;code&gt;LMS_ACTIVE_INVENTORY_REPORT&lt;/code&gt;. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/lms-feeds.html\&quot;&gt;LMS API Feeds&lt;/a&gt; in the Selling Integration Guide.&lt;/span&gt;&lt;/p&gt;

    :param task_id: The task ID associated with the file to be downloaded.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_result_file(request: web.Request, task_id) -> web.Response:
    """get_result_file

    This method retrieves the generated file that is associated with the specified task ID. The response of this call is a compressed or uncompressed CSV, XML, or JSON file, with the applicable file extension (for example: csv.gz). &lt;p&gt;For details about how this method is used, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html\&quot;&gt;Working with Order Feeds&lt;/a&gt; in the Selling Integration Guide. &lt;/p&gt;&lt;p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; The status of the task to retrieve must be in the COMPLETED or COMPLETED_WITH_ERROR state before this method can retrieve the file. You can use the getTask or getTasks method to retrieve the status of the task.&lt;/span&gt;&lt;/p&gt;

    :param task_id: The ID of the task associated with the file you want to download. This ID was generated when the task was created.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_task(request: web.Request, task_id) -> web.Response:
    """get_task

    This method retrieves the details and status of the specified task. The input is &lt;strong&gt;task_id&lt;/strong&gt;. &lt;br /&gt;&lt;br /&gt;For details of how this method is used, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html\&quot;&gt;Working with Order Feeds&lt;/a&gt; in the Selling Integration Guide. 

    :param task_id: The ID of the task. This ID was generated when the task was created.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_tasks(request: web.Request, date_range=None, feed_type=None, limit=None, look_back_days=None, offset=None, schedule_id=None) -> web.Response:
    """get_tasks

    This method returns the details and status for an array of tasks based on a specified &lt;strong&gt;feed_type&lt;/strong&gt; or &lt;strong&gt;scheduledId&lt;/strong&gt;. Specifying both &lt;strong&gt;feed_type&lt;/strong&gt; and &lt;strong&gt;scheduledId&lt;/strong&gt; results in an error. Since schedules are based on feed types, you can specify a schedule (&lt;strong&gt;schedule_id&lt;/strong&gt;) that returns the needed &lt;strong&gt;feed_type&lt;/strong&gt;.&lt;br /&gt;&lt;br /&gt;If specifying the &lt;strong&gt;feed_type&lt;/strong&gt;, limit which tasks are returned by specifying filters, such as the creation date range or period of time using &lt;strong&gt;look_back_days&lt;/strong&gt;. Also, by specifying the &lt;strong&gt;feed_type&lt;/strong&gt;, both on-demand and scheduled reports are returned.&lt;br /&gt;&lt;br /&gt;If specifying a &lt;strong&gt;scheduledId&lt;/strong&gt;, the schedule template (that the schedule ID is based on) determines which tasks are returned (see &lt;strong&gt;schedule_id&lt;/strong&gt; for additional information). Each &lt;strong&gt;scheduledId&lt;/strong&gt; applies to one &lt;strong&gt;feed_type&lt;/strong&gt;. 

    :param date_range: Specifies the range of task creation dates used to filter the results. The results are filtered to include only tasks with a creation date that is equal to this date or is within specified range. Only tasks that are less than 90 days can be retrieved. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Maximum date range window size is 90 days.&lt;/span&gt;&lt;/p&gt; &lt;br /&gt;&lt;b&gt;Valid Format (UTC):&lt;/b&gt;&lt;code&gt;yyyy-MM-ddThh:mm:ss.SSSZ..yyyy-MM-ddThh:mm:ss.SSSZ &lt;/code&gt;&lt;br /&gt;&lt;br /&gt;For example: Tasks created on September 8, 2019&lt;br /&gt; &lt;code&gt;2019-09-08T00:00:00.000Z..2019-09-09T00:00:00.000Z&lt;/code&gt;
    :type date_range: str
    :param feed_type: The feed type associated with the tasks to be returned. Only use a &lt;strong&gt;feedType&lt;/strong&gt; that is available for your API: &lt;ul&gt;&lt;li&gt;Order Feeds: &lt;code&gt;LMS_ORDER_ACK, LMS_ORDER_REPORT&lt;/code&gt;&lt;/li&gt;&lt;li&gt;Large Merchant Services (LMS) Feeds: See &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Availabl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Available FeedTypes&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;&lt;br/&gt;Do not use with the &lt;strong&gt;schedule_id&lt;/strong&gt; parameter. Since schedules are based on feed types, you can specify a schedule (&lt;strong&gt;schedule_id&lt;/strong&gt;) that returns the needed &lt;strong&gt;feed_type&lt;/strong&gt;.
    :type feed_type: str
    :param limit: The maximum number of tasks that can be returned on each page of the paginated response. Use this parameter in conjunction with the &lt;strong&gt;offset&lt;/strong&gt; parameter to control the pagination of the output. &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This feature employs a zero-based list, where the first item in the list has an offset of &lt;code&gt;0&lt;/code&gt;.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;For example, if &lt;strong&gt;offset&lt;/strong&gt; is set to 10 and &lt;strong&gt;limit&lt;/strong&gt; is set to 10, the call retrieves tasks 11 thru 20 from the result set.&lt;/p&gt;&lt;p&gt;If this parameter is omitted, the default value is used. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt; 10 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt;500
    :type limit: str
    :param look_back_days: The number of previous days in which to search for tasks. Do not use with the &lt;code&gt;date_range&lt;/code&gt; parameter. If both &lt;code&gt;date_range&lt;/code&gt; and &lt;code&gt;look_back_days&lt;/code&gt; are omitted, this parameter&#39;s default value is used.  &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt; 7 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Range: &lt;/b&gt; 1-90 (inclusive)
    :type look_back_days: str
    :param offset: The number of tasks to skip in the result set before returning the first task in the paginated response. &lt;p&gt;Combine &lt;strong&gt;offset&lt;/strong&gt; with the &lt;strong&gt;limit&lt;/strong&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;strong&gt;offset&lt;/strong&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;strong&gt;limit&lt;/strong&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;strong&gt;offset&lt;/strong&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;strong&gt;limit&lt;/strong&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set. If this query parameter is not set, the default value is used and the first page of records is returned. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt;0
    :type offset: str
    :param schedule_id: The schedule ID associated with the task. A schedule periodically generates a report for the feed type specified by the schedule template (see &lt;strong&gt;scheduleTemplateId&lt;/strong&gt; in &lt;strong&gt;createSchedule&lt;/strong&gt;). Do not use with the &lt;strong&gt;feed_type&lt;/strong&gt; parameter. Since schedules are based on feed types, you can specify a schedule (&lt;strong&gt;schedule_id&lt;/strong&gt;) that returns the needed &lt;strong&gt;feed_type&lt;/strong&gt;.
    :type schedule_id: str

    """
    return web.Response(status=200)


async def upload_file(request: web.Request, task_id, creation_date=None, file_name=None, modification_date=None, name=None, parameters=None, read_date=None, size=None, type=None) -> web.Response:
    """upload_file

    This method associates the specified file with the specified task ID and uploads the input file. After the file has been uploaded, the processing of the file begins. &lt;br /&gt;&lt;br /&gt;Reports often take time to generate and it&#39;s common for this method to return an HTTP status of 202, which indicates the report is being generated. Use the &lt;b&gt; getTask&lt;/b&gt; with the task ID or &lt;b&gt; getTasks&lt;/b&gt; to determine the status of a report. &lt;br /&gt;&lt;br /&gt;The status flow is &lt;code&gt;QUEUED&lt;/code&gt; &amp;gt; &lt;code&gt;IN_PROCESS&lt;/code&gt; &amp;gt; &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;COMPLETED_WITH_ERROR&lt;/code&gt;. When the status is &lt;code&gt;COMPLETED&lt;/code&gt; or &lt;code&gt;COMPLETED_WITH_ERROR&lt;/code&gt;, this indicates the file has been processed and the order report can be downloaded. If there are errors, they will be indicated in the report file. &lt;br /&gt;&lt;br /&gt;For details of how this method is used in the upload flow, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/orders/generating-and-retrieving-order-reports.html\&quot;&gt;Working with Order Feeds&lt;/a&gt; in the Selling Integration Guide. &lt;p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; This method applies to all Seller Hub feed types and LMS feed types except &lt;code&gt;LMS_ORDER_REPORT&lt;/code&gt; and &lt;code&gt;LMS_ACTIVE_INVENTORY_REPORT&lt;/code&gt;. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/lms-feeds-quick-reference.html#Availabl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;LMS feed types&lt;/a&gt; and &lt;a href&#x3D;\&quot;/api-docs/sell/static/feed/fx-feeds-quick-reference.html#availabl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Seller Hub feed types&lt;/a&gt;.&lt;/span&gt;&lt;/p&gt;&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You must use a &lt;strong&gt;Content-Type&lt;/strong&gt; header with its value set to \&quot;&lt;strong&gt;multipart/form-data&lt;/strong&gt;\&quot;. See &lt;a href&#x3D;\&quot;/api-docs/sell/feed/resources/task/methods/uploadFile#h2-samples\&quot;&gt;Samples&lt;/a&gt; for information.&lt;/span&gt;&lt;/p&gt;

    :param task_id: The task_id associated with the file that will be uploaded. This ID was generated when the specified task was created.
    :type task_id: str
    :param creation_date: The file creation date. &lt;br /&gt;&lt;br /&gt;&lt;b&gt; Format: &lt;/b&gt; UTC &lt;code&gt;yyyy-MM-ddThh:mm:ss.SSSZ&lt;/code&gt;&lt;p&gt;&lt;b&gt;For example:&lt;/b&gt;&lt;p&gt;Created on September 8, 2019&lt;/p&gt;&lt;p&gt;&lt;code&gt;2019-09-08T00:00:00.000Z&lt;/code&gt;&lt;/p&gt;
    :type creation_date: str
    :param file_name: The name of the file including its extension (for example, xml or csv) to be uploaded.
    :type file_name: str
    :param modification_date: The file modified date. &lt;br /&gt;&lt;br /&gt;&lt;b&gt; Format: &lt;/b&gt; UTC &lt;code&gt;yyyy-MM-ddThh:mm:ss.SSSZ&lt;/code&gt;&lt;p&gt;&lt;b&gt;For example:&lt;/b&gt;&lt;p&gt;Created on September 9, 2019&lt;/p&gt;&lt;p&gt;&lt;code&gt;2019-09-09T00:00:00.000Z&lt;/code&gt;&lt;/p&gt;
    :type modification_date: str
    :param name: A content identifier. The only presently supported name is &lt;code&gt;file&lt;/code&gt;.
    :type name: str
    :param parameters: The parameters you want associated with the file.
    :type parameters: Dict[str, str]
    :param read_date: The date you read the file. &lt;br /&gt;&lt;br /&gt;&lt;b&gt; Format: &lt;/b&gt; UTC &lt;code&gt;yyyy-MM-ddThh:mm:ss.SSSZ&lt;/code&gt;&lt;p&gt;&lt;b&gt;For example:&lt;/b&gt;&lt;p&gt;Created on September 10, 2019&lt;/p&gt;&lt;p&gt;&lt;code&gt;2019-09-10T00:00:00.000Z&lt;/code&gt;&lt;/p&gt;
    :type read_date: str
    :param size: The size of the file.
    :type size: int
    :param type: The file type. The only presently supported type is &lt;code&gt;form-data&lt;/code&gt;.
    :type type: str

    """
    return web.Response(status=200)
