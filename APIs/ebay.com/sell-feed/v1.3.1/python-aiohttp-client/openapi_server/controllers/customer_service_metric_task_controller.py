from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_service_metrics_task_request import CreateServiceMetricsTaskRequest
from openapi_server.models.customer_service_metric_task_collection import CustomerServiceMetricTaskCollection
from openapi_server.models.service_metrics_task import ServiceMetricsTask
from openapi_server import util


async def create_customer_service_metric_task(request: web.Request, accept_language, body) -> web.Response:
    """create_customer_service_metric_task

    &lt;p&gt;Use this method to create a customer service metrics download task with filter criteria for the customer service metrics report. When using this method, specify the &lt;strong&gt;feedType&lt;/strong&gt; and &lt;strong&gt;filterCriteria&lt;/strong&gt; including both &lt;strong&gt;evaluationMarketplaceId&lt;/strong&gt; and &lt;strong&gt;customerServiceMetricType&lt;/strong&gt; for the report. The method returns the location response header containing the call URI to use with &lt;strong&gt;getCustomerServiceMetricTask&lt;/strong&gt; to retrieve status and details on the task.&lt;/p&gt;&lt;p&gt;Only CURRENT Customer Service Metrics reports can be generated with the Sell Feed API. PROJECTED reports are not supported at this time. See the &lt;a href&#x3D;\&quot;/api-docs/sell/analytics/resources/customer_service_metric/methods/getCustomerServiceMetric\&quot;&gt;getCustomerServiceMetric&lt;/a&gt; method document in the Analytics API for more information about these two types of reports.&lt;/p&gt;&lt;p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; Before calling this API, retrieve the summary of the seller&#39;s performance and rating for the customer service metric by calling &lt;strong&gt;getCustomerServiceMetric&lt;/strong&gt; (part of the &lt;a href&#x3D;\&quot;/api-docs/sell/analytics/resources/methods\&quot;&gt;Analytics API&lt;/a&gt;). You can then populate the create task request fields with the values from the response. This technique eliminates failed tasks that request a report for a &lt;strong&gt;customerServiceMetricType&lt;/strong&gt; and &lt;strong&gt;evaluationMarketplaceId&lt;/strong&gt; that are without evaluation.&lt;/span&gt;&lt;/p&gt;

    :param accept_language: Use this header to specify the natural language in which the authenticated user desires the response.
    :type accept_language: str
    :param body: Request payload containing version, feedType, and optional filterCriteria.
    :type body: dict | bytes

    """
    body = CreateServiceMetricsTaskRequest.from_dict(body)
    return web.Response(status=200)


async def get_customer_service_metric_task(request: web.Request, task_id) -> web.Response:
    """get_customer_service_metric_task

    &lt;p&gt;Use this method to retrieve customer service metric task details for the specified task. The input is &lt;strong&gt;task_id&lt;/strong&gt;.&lt;/p&gt;

    :param task_id: Use this path parameter to specify the task ID value for the customer service metric task to retrieve.
    :type task_id: str

    """
    return web.Response(status=200)


async def get_customer_service_metric_tasks(request: web.Request, date_range=None, feed_type=None, limit=None, look_back_days=None, offset=None) -> web.Response:
    """get_customer_service_metric_tasks

    Use this method to return an array of customer service metric tasks. You can limit the tasks returned by specifying a date range. &lt;/p&gt; &lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; You can pass in either the &lt;code&gt;look_back_days &lt;/code&gt;or&lt;code&gt; date_range&lt;/code&gt;, but not both.&lt;/span&gt;&lt;/p&gt;

    :param date_range: The task creation date range. The results are filtered to include only tasks with a creation date that is equal to the dates specified or is within the specified range. Do not use with the &lt;code&gt;look_back_days&lt;/code&gt; parameter.&lt;p&gt;&lt;strong&gt;Format: &lt;/strong&gt;UTC&lt;/p&gt;&lt;p&gt;For example, tasks within a range: &lt;/p&gt;&lt;p&gt;&lt;code&gt;yyyy-MM-ddThh:mm:ss.SSSZ..yyyy-MM-ddThh:mm:ss.SSSZ &lt;/code&gt;&lt;/p&gt;&lt;p&gt;Tasks created on March 8, 2020&lt;/p&gt;&lt;p&gt;&lt;code&gt;2020-03-08T00:00.00.000Z..2020-03-09T00:00:00.000Z&lt;/code&gt;&lt;/p&gt;&lt;p&gt;&lt;b&gt;Maximum: &lt;/b&gt;90 days&lt;/p&gt;
    :type date_range: str
    :param feed_type: The feed type associated with the task. The only presently supported value is &lt;code&gt;CUSTOMER_SERVICE_METRICS_REPORT&lt;/code&gt;.
    :type feed_type: str
    :param limit: The number of customer service metric tasks to return per page of the result set. Use this parameter in conjunction with the offset parameter to control the pagination of the output. &lt;p&gt;For example, if &lt;strong&gt;offset&lt;/strong&gt; is set to 10 and &lt;strong&gt;limit&lt;/strong&gt; is set to 10, the call retrieves tasks 11 thru 20 from the result set.&lt;/p&gt;&lt;p&gt;If this parameter is omitted, the default value is used.&lt;/p&gt;&lt;p&gt; &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt;This feature employs a zero-based list, where the first item in the list has an offset of &lt;code&gt;0&lt;/code&gt;.&lt;/span&gt;&lt;/p&gt;&lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 10 &lt;p&gt;&lt;b&gt;Maximum:&lt;/b&gt; 500&lt;/p&gt;
    :type limit: str
    :param look_back_days: The number of previous days in which to search for tasks. Do not use with the &lt;code&gt;date_range&lt;/code&gt; parameter. If both &lt;code&gt;date_range&lt;/code&gt; and &lt;code&gt;look_back_days&lt;/code&gt; are omitted, this parameter&#39;s default value is used. &lt;p&gt;&lt;b&gt;Default value:&lt;/b&gt; 7&lt;/p&gt;&lt;p&gt;&lt;b&gt;Range:&lt;/b&gt; 1-90 (inclusive)&lt;/p&gt;
    :type look_back_days: str
    :param offset: The number of customer service metric tasks to skip in the result set before returning the first task in the paginated response. &lt;p&gt;Combine &lt;strong&gt;offset&lt;/strong&gt; with the &lt;strong&gt;limit&lt;/strong&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;strong&gt;offset&lt;/strong&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;strong&gt;limit&lt;/strong&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;strong&gt;offset&lt;/strong&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;strong&gt;limit&lt;/strong&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt;0
    :type offset: str

    """
    return web.Response(status=200)
