from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_create_rum_metric_definitions_request import BatchCreateRumMetricDefinitionsRequest
from openapi_server.models.batch_create_rum_metric_definitions_response import BatchCreateRumMetricDefinitionsResponse
from openapi_server.models.batch_delete_rum_metric_definitions_response import BatchDeleteRumMetricDefinitionsResponse
from openapi_server.models.batch_get_rum_metric_definitions_response import BatchGetRumMetricDefinitionsResponse
from openapi_server.models.create_app_monitor_request import CreateAppMonitorRequest
from openapi_server.models.create_app_monitor_response import CreateAppMonitorResponse
from openapi_server.models.get_app_monitor_data_request import GetAppMonitorDataRequest
from openapi_server.models.get_app_monitor_data_response import GetAppMonitorDataResponse
from openapi_server.models.get_app_monitor_response import GetAppMonitorResponse
from openapi_server.models.list_app_monitors_response import ListAppMonitorsResponse
from openapi_server.models.list_rum_metrics_destinations_response import ListRumMetricsDestinationsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_rum_events_request import PutRumEventsRequest
from openapi_server.models.put_rum_metrics_destination_request import PutRumMetricsDestinationRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_app_monitor_request import UpdateAppMonitorRequest
from openapi_server.models.update_rum_metric_definition_request import UpdateRumMetricDefinitionRequest
from openapi_server import util


async def batch_create_rum_metric_definitions(request: web.Request, app_monitor_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_create_rum_metric_definitions

    &lt;p&gt;Specifies the extended metrics and custom metrics that you want a CloudWatch RUM app monitor to send to a destination. Valid destinations include CloudWatch and Evidently.&lt;/p&gt; &lt;p&gt;By default, RUM app monitors send some metrics to CloudWatch. These default metrics are listed in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-metrics.html\&quot;&gt;CloudWatch metrics that you can collect with CloudWatch RUM&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In addition to these default metrics, you can choose to send extended metrics or custom metrics or both.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Extended metrics enable you to send metrics with additional dimensions not included in the default metrics. You can also send extended metrics to Evidently as well as CloudWatch. The valid dimension names for the additional dimensions for extended metrics are &lt;code&gt;BrowserName&lt;/code&gt;, &lt;code&gt;CountryCode&lt;/code&gt;, &lt;code&gt;DeviceType&lt;/code&gt;, &lt;code&gt;FileType&lt;/code&gt;, &lt;code&gt;OSName&lt;/code&gt;, and &lt;code&gt;PageId&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html\&quot;&gt; Extended metrics that you can send to CloudWatch and CloudWatch Evidently&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Custom metrics are metrics that you define. You can send custom metrics to CloudWatch or to CloudWatch Evidently or to both. With custom metrics, you can use any metric name and namespace, and to derive the metrics you can use any custom events, built-in events, custom attributes, or default attributes. &lt;/p&gt; &lt;p&gt;You can&#39;t send custom metrics to the &lt;code&gt;AWS/RUM&lt;/code&gt; namespace. You must send custom metrics to a custom namespace that you define. The namespace that you use can&#39;t start with &lt;code&gt;AWS/&lt;/code&gt;. CloudWatch RUM prepends &lt;code&gt;RUM/CustomMetrics/&lt;/code&gt; to the custom namespace that you define, so the final namespace for your metrics in CloudWatch is &lt;code&gt;RUM/CustomMetrics/&lt;i&gt;your-custom-namespace&lt;/i&gt; &lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The maximum number of metric definitions that you can specify in one &lt;code&gt;BatchCreateRumMetricDefinitions&lt;/code&gt; operation is 200.&lt;/p&gt; &lt;p&gt;The maximum number of metric definitions that one destination can contain is 2000.&lt;/p&gt; &lt;p&gt;Extended metrics sent to CloudWatch and RUM custom metrics are charged as CloudWatch custom metrics. Each combination of additional dimension name and dimension value counts as a custom metric. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You must have already created a destination for the metrics before you send them. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html\&quot;&gt;PutRumMetricsDestination&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If some metric definitions specified in a &lt;code&gt;BatchCreateRumMetricDefinitions&lt;/code&gt; operations are not valid, those metric definitions fail and return errors, but all valid metric definitions in the same operation still succeed.&lt;/p&gt;

    :param app_monitor_name: The name of the CloudWatch RUM app monitor that is to send the metrics.
    :type app_monitor_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchCreateRumMetricDefinitionsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_rum_metric_definitions(request: web.Request, app_monitor_name, destination, metric_definition_ids, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, destination_arn=None) -> web.Response:
    """batch_delete_rum_metric_definitions

    &lt;p&gt;Removes the specified metrics from being sent to an extended metrics destination.&lt;/p&gt; &lt;p&gt;If some metric definition IDs specified in a &lt;code&gt;BatchDeleteRumMetricDefinitions&lt;/code&gt; operations are not valid, those metric definitions fail and return errors, but all valid metric definition IDs in the same operation are still deleted.&lt;/p&gt; &lt;p&gt;The maximum number of metric definitions that you can specify in one &lt;code&gt;BatchDeleteRumMetricDefinitions&lt;/code&gt; operation is 200.&lt;/p&gt;

    :param app_monitor_name: The name of the CloudWatch RUM app monitor that is sending these metrics.
    :type app_monitor_name: str
    :param destination: Defines the destination where you want to stop sending the specified metrics. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;. If you specify &lt;code&gt;Evidently&lt;/code&gt;, you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.
    :type destination: str
    :param metric_definition_ids: An array of structures which define the metrics that you want to stop sending.
    :type metric_definition_ids: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param destination_arn: &lt;p&gt;This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter. &lt;/p&gt; &lt;p&gt;This parameter specifies the ARN of the Evidently experiment that was receiving the metrics that are being deleted.&lt;/p&gt;
    :type destination_arn: str

    """
    return web.Response(status=200)


async def batch_get_rum_metric_definitions(request: web.Request, app_monitor_name, destination, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, destination_arn=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """batch_get_rum_metric_definitions

    Retrieves the list of metrics and dimensions that a RUM app monitor is sending to a single destination.

    :param app_monitor_name: The name of the CloudWatch RUM app monitor that is sending the metrics.
    :type app_monitor_name: str
    :param destination: The type of destination that you want to view metrics for. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;.
    :type destination: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param destination_arn: &lt;p&gt;This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter.&lt;/p&gt; &lt;p&gt;This parameter specifies the ARN of the Evidently experiment that corresponds to the destination.&lt;/p&gt;
    :type destination_arn: str
    :param max_results: &lt;p&gt;The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.&lt;/p&gt; &lt;p&gt;To retrieve the remaining results, make another call with the returned &lt;code&gt;NextToken&lt;/code&gt; value. &lt;/p&gt;
    :type max_results: int
    :param next_token: Use the token returned by the previous operation to request the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def create_app_monitor(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_monitor

    &lt;p&gt;Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from your application and sends that data to RUM. The data includes performance and reliability information such as page load time, client-side errors, and user behavior.&lt;/p&gt; &lt;p&gt;You use this operation only to create a new app monitor. To update an existing app monitor, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html\&quot;&gt;UpdateAppMonitor&lt;/a&gt; instead.&lt;/p&gt; &lt;p&gt;After you create an app monitor, sign in to the CloudWatch RUM console to get the JavaScript code snippet to add to your web application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html\&quot;&gt;How do I find a code snippet that I&#39;ve already generated?&lt;/a&gt; &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app_monitor(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_monitor

    Deletes an existing app monitor. This immediately stops the collection of data.

    :param name: The name of the app monitor to delete.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_rum_metrics_destination(request: web.Request, app_monitor_name, destination, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, destination_arn=None) -> web.Response:
    """delete_rum_metrics_destination

    Deletes a destination for CloudWatch RUM extended metrics, so that the specified app monitor stops sending extended metrics to that destination.

    :param app_monitor_name: The name of the app monitor that is sending metrics to the destination that you want to delete.
    :type app_monitor_name: str
    :param destination: The type of destination to delete. Valid values are &lt;code&gt;CloudWatch&lt;/code&gt; and &lt;code&gt;Evidently&lt;/code&gt;.
    :type destination: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param destination_arn: This parameter is required if &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;Evidently&lt;/code&gt;. If &lt;code&gt;Destination&lt;/code&gt; is &lt;code&gt;CloudWatch&lt;/code&gt;, do not use this parameter. This parameter specifies the ARN of the Evidently experiment that corresponds to the destination to delete.
    :type destination_arn: str

    """
    return web.Response(status=200)


async def get_app_monitor(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_app_monitor

    Retrieves the complete configuration information for one app monitor.

    :param name: The app monitor to retrieve information for.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_app_monitor_data(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_app_monitor_data

    Retrieves the raw performance events that RUM has collected from your web application, so that you can do your own processing or analysis of this data.

    :param name: The name of the app monitor that collected the data that you want to retrieve.
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetAppMonitorDataRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_monitors(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_app_monitors

    Returns a list of the Amazon CloudWatch RUM app monitors in the account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.
    :type max_results: int
    :param next_token: Use the token returned by the previous operation to request the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_rum_metrics_destinations(request: web.Request, app_monitor_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_rum_metrics_destinations

    &lt;p&gt;Returns a list of destinations that you have created to receive RUM extended metrics, for the specified app monitor.&lt;/p&gt; &lt;p&gt;For more information about extended metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AddRumMetrcs.html\&quot;&gt;AddRumMetrics&lt;/a&gt;.&lt;/p&gt;

    :param app_monitor_name: The name of the app monitor associated with the destinations that you want to retrieve.
    :type app_monitor_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: &lt;p&gt;The maximum number of results to return in one operation. The default is 50. The maximum that you can specify is 100.&lt;/p&gt; &lt;p&gt;To retrieve the remaining results, make another call with the returned &lt;code&gt;NextToken&lt;/code&gt; value. &lt;/p&gt;
    :type max_results: int
    :param next_token: Use the token returned by the previous operation to request the next page of results.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with a CloudWatch RUM resource.

    :param resource_arn: The ARN of the resource that you want to see the tags of.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def put_rum_events(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_rum_events

    &lt;p&gt;Sends telemetry events about your application performance and user behavior to CloudWatch RUM. The code snippet that RUM generates for you to add to your application includes &lt;code&gt;PutRumEvents&lt;/code&gt; operations to send this data to RUM.&lt;/p&gt; &lt;p&gt;Each &lt;code&gt;PutRumEvents&lt;/code&gt; operation can send a batch of events from one user session.&lt;/p&gt;

    :param id: The ID of the app monitor that is sending this data.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutRumEventsRequest.from_dict(body)
    return web.Response(status=200)


async def put_rum_metrics_destination(request: web.Request, app_monitor_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_rum_metrics_destination

    &lt;p&gt;Creates or updates a destination to receive extended metrics from CloudWatch RUM. You can send extended metrics to CloudWatch or to a CloudWatch Evidently experiment.&lt;/p&gt; &lt;p&gt;For more information about extended metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html\&quot;&gt;BatchCreateRumMetricDefinitions&lt;/a&gt;.&lt;/p&gt;

    :param app_monitor_name: The name of the CloudWatch RUM app monitor that will send the metrics.
    :type app_monitor_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutRumMetricsDestinationRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM resource. Currently, the only resources that can be tagged app monitors.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt;

    :param resource_arn: The ARN of the CloudWatch RUM resource that you&#39;re adding tags to.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from the specified resource.

    :param resource_arn: The ARN of the CloudWatch RUM resource that you&#39;re removing tags from.
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the resource.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_app_monitor(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_monitor

    &lt;p&gt;Updates the configuration of an existing app monitor. When you use this operation, only the parts of the app monitor configuration that you specify in this operation are changed. For any parameters that you omit, the existing values are kept.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation to change the tags of an existing app monitor. To change the tags of an existing app monitor, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To create a new app monitor, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html\&quot;&gt;CreateAppMonitor&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you update an app monitor, sign in to the CloudWatch RUM console to get the updated JavaScript code snippet to add to your web application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html\&quot;&gt;How do I find a code snippet that I&#39;ve already generated?&lt;/a&gt; &lt;/p&gt;

    :param name: The name of the app monitor to update.
    :type name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAppMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def update_rum_metric_definition(request: web.Request, app_monitor_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rum_metric_definition

    Modifies one existing metric definition for CloudWatch RUM extended metrics. For more information about extended metrics, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html\&quot;&gt;BatchCreateRumMetricsDefinitions&lt;/a&gt;.

    :param app_monitor_name: The name of the CloudWatch RUM app monitor that sends these metrics.
    :type app_monitor_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRumMetricDefinitionRequest.from_dict(body)
    return web.Response(status=200)
