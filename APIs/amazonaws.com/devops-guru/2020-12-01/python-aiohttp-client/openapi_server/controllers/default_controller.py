from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_notification_channel_request import AddNotificationChannelRequest
from openapi_server.models.add_notification_channel_response import AddNotificationChannelResponse
from openapi_server.models.describe_account_health_response import DescribeAccountHealthResponse
from openapi_server.models.describe_account_overview_request import DescribeAccountOverviewRequest
from openapi_server.models.describe_account_overview_response import DescribeAccountOverviewResponse
from openapi_server.models.describe_anomaly_response import DescribeAnomalyResponse
from openapi_server.models.describe_event_sources_config_response import DescribeEventSourcesConfigResponse
from openapi_server.models.describe_feedback_request import DescribeFeedbackRequest
from openapi_server.models.describe_feedback_response import DescribeFeedbackResponse
from openapi_server.models.describe_insight_response import DescribeInsightResponse
from openapi_server.models.describe_organization_health_request import DescribeOrganizationHealthRequest
from openapi_server.models.describe_organization_health_response import DescribeOrganizationHealthResponse
from openapi_server.models.describe_organization_overview_request import DescribeOrganizationOverviewRequest
from openapi_server.models.describe_organization_overview_response import DescribeOrganizationOverviewResponse
from openapi_server.models.describe_organization_resource_collection_health_request import DescribeOrganizationResourceCollectionHealthRequest
from openapi_server.models.describe_organization_resource_collection_health_response import DescribeOrganizationResourceCollectionHealthResponse
from openapi_server.models.describe_resource_collection_health_response import DescribeResourceCollectionHealthResponse
from openapi_server.models.describe_service_integration_response import DescribeServiceIntegrationResponse
from openapi_server.models.get_cost_estimation_response import GetCostEstimationResponse
from openapi_server.models.get_resource_collection_response import GetResourceCollectionResponse
from openapi_server.models.list_anomalies_for_insight_request import ListAnomaliesForInsightRequest
from openapi_server.models.list_anomalies_for_insight_response import ListAnomaliesForInsightResponse
from openapi_server.models.list_anomalous_log_groups_request import ListAnomalousLogGroupsRequest
from openapi_server.models.list_anomalous_log_groups_response import ListAnomalousLogGroupsResponse
from openapi_server.models.list_events_request import ListEventsRequest
from openapi_server.models.list_events_response import ListEventsResponse
from openapi_server.models.list_insights_request import ListInsightsRequest
from openapi_server.models.list_insights_response import ListInsightsResponse
from openapi_server.models.list_monitored_resources_request import ListMonitoredResourcesRequest
from openapi_server.models.list_monitored_resources_response import ListMonitoredResourcesResponse
from openapi_server.models.list_notification_channels_request import ListNotificationChannelsRequest
from openapi_server.models.list_notification_channels_response import ListNotificationChannelsResponse
from openapi_server.models.list_organization_insights_request import ListOrganizationInsightsRequest
from openapi_server.models.list_organization_insights_response import ListOrganizationInsightsResponse
from openapi_server.models.list_recommendations_request import ListRecommendationsRequest
from openapi_server.models.list_recommendations_response import ListRecommendationsResponse
from openapi_server.models.put_feedback_request import PutFeedbackRequest
from openapi_server.models.search_insights_request import SearchInsightsRequest
from openapi_server.models.search_insights_response import SearchInsightsResponse
from openapi_server.models.search_organization_insights_request import SearchOrganizationInsightsRequest
from openapi_server.models.search_organization_insights_response import SearchOrganizationInsightsResponse
from openapi_server.models.start_cost_estimation_request import StartCostEstimationRequest
from openapi_server.models.update_event_sources_config_request import UpdateEventSourcesConfigRequest
from openapi_server.models.update_resource_collection_request import UpdateResourceCollectionRequest
from openapi_server.models.update_service_integration_request import UpdateServiceIntegrationRequest
from openapi_server import util


async def add_notification_channel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_notification_channel

    &lt;p&gt; Adds a notification channel to DevOps Guru. A notification channel is used to notify you about important DevOps Guru events, such as when an insight is generated. &lt;/p&gt; &lt;p&gt;If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html\&quot;&gt;Permissions for Amazon SNS topics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you use an Amazon SNS topic that is encrypted by an Amazon Web Services Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html\&quot;&gt;Permissions for Amazon Web Services KMS–encrypted Amazon SNS topics&lt;/a&gt;.&lt;/p&gt;

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
    body = AddNotificationChannelRequest.from_dict(body)
    return web.Response(status=200)


async def delete_insight(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_insight

    Deletes the insight along with the associated anomalies, events and recommendations.

    :param id: The ID of the insight.
    :type id: str
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


async def describe_account_health(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account_health

     Returns the number of open reactive insights, the number of open proactive insights, and the number of metrics analyzed in your Amazon Web Services account. Use these numbers to gauge the health of operations in your Amazon Web Services account. 

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


async def describe_account_overview(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account_overview

     For the time range passed in, returns the number of open reactive insight that were created, the number of open proactive insights that were created, and the Mean Time to Recover (MTTR) for all closed reactive insights. 

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
    body = DescribeAccountOverviewRequest.from_dict(body)
    return web.Response(status=200)


async def describe_anomaly(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, account_id=None) -> web.Response:
    """describe_anomaly

     Returns details about an anomaly that you specify using its ID. 

    :param id:  The ID of the anomaly. 
    :type id: str
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
    :param account_id: The ID of the member account.
    :type account_id: str

    """
    return web.Response(status=200)


async def describe_event_sources_config(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_event_sources_config

    Returns the integration status of services that are integrated with DevOps Guru as Consumer via EventBridge. The one service that can be integrated with DevOps Guru is Amazon CodeGuru Profiler, which can produce proactive recommendations which can be stored and viewed in DevOps Guru.

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


async def describe_feedback(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_feedback

     Returns the most recent feedback submitted in the current Amazon Web Services account and Region. 

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
    body = DescribeFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def describe_insight(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, account_id=None) -> web.Response:
    """describe_insight

     Returns details about an insight that you specify using its ID. 

    :param id:  The ID of the insight. 
    :type id: str
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
    :param account_id: The ID of the member account in the organization.
    :type account_id: str

    """
    return web.Response(status=200)


async def describe_organization_health(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_organization_health

    Returns active insights, predictive insights, and resource hours analyzed in last hour.

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
    body = DescribeOrganizationHealthRequest.from_dict(body)
    return web.Response(status=200)


async def describe_organization_overview(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_organization_overview

    Returns an overview of your organization&#39;s history based on the specified time range. The overview includes the total reactive and proactive insights.

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
    body = DescribeOrganizationOverviewRequest.from_dict(body)
    return web.Response(status=200)


async def describe_organization_resource_collection_health(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """describe_organization_resource_collection_health

    Provides an overview of your system&#39;s health. If additional member accounts are part of your organization, you can filter those accounts using the &lt;code&gt;AccountIds&lt;/code&gt; field.

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeOrganizationResourceCollectionHealthRequest.from_dict(body)
    return web.Response(status=200)


async def describe_resource_collection_health(request: web.Request, resource_collection_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """describe_resource_collection_health

     Returns the number of open proactive insights, open reactive insights, and the Mean Time to Recover (MTTR) for all closed insights in resource collections in your account. You specify the type of Amazon Web Services resources collection. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks. 

    :param resource_collection_type:  An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks. 
    :type resource_collection_type: str
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
    :param next_token: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
    :type next_token: str

    """
    return web.Response(status=200)


async def describe_service_integration(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_service_integration

     Returns the integration status of services that are integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon Web Services Systems Manager, which can be used to create an OpsItem for each generated insight. 

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


async def get_cost_estimation(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """get_cost_estimation

    Returns an estimate of the monthly cost for DevOps Guru to analyze your Amazon Web Services resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html\&quot;&gt;Estimate your Amazon DevOps Guru costs&lt;/a&gt; and &lt;a href&#x3D;\&quot;http://aws.amazon.com/devops-guru/pricing/\&quot;&gt;Amazon DevOps Guru pricing&lt;/a&gt;.

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
    :param next_token: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
    :type next_token: str

    """
    return web.Response(status=200)


async def get_resource_collection(request: web.Request, resource_collection_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """get_resource_collection

     Returns lists Amazon Web Services resources that are of the specified resource collection type. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks. 

    :param resource_collection_type:  The type of Amazon Web Services resource collections to return. The one valid value is &lt;code&gt;CLOUD_FORMATION&lt;/code&gt; for Amazon Web Services CloudFormation stacks. 
    :type resource_collection_type: str
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
    :param next_token: The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_anomalies_for_insight(request: web.Request, insight_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_anomalies_for_insight

     Returns a list of the anomalies that belong to an insight that you specify using its ID. 

    :param insight_id:  The ID of the insight. The returned anomalies belong to this insight. 
    :type insight_id: str
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
    body = ListAnomaliesForInsightRequest.from_dict(body)
    return web.Response(status=200)


async def list_anomalous_log_groups(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_anomalous_log_groups

     Returns the list of log groups that contain log anomalies. 

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
    body = ListAnomalousLogGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_events(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_events

     Returns a list of the events emitted by the resources that are evaluated by DevOps Guru. You can use filters to specify which events are returned. 

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
    body = ListEventsRequest.from_dict(body)
    return web.Response(status=200)


async def list_insights(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_insights

     Returns a list of insights in your Amazon Web Services account. You can specify which insights are returned by their start time and status (&lt;code&gt;ONGOING&lt;/code&gt;, &lt;code&gt;CLOSED&lt;/code&gt;, or &lt;code&gt;ANY&lt;/code&gt;). 

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
    body = ListInsightsRequest.from_dict(body)
    return web.Response(status=200)


async def list_monitored_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_monitored_resources

     Returns the list of all log groups that are being monitored and tagged by DevOps Guru. 

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
    body = ListMonitoredResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_notification_channels(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_notification_channels

     Returns a list of notification channels configured for DevOps Guru. Each notification channel is used to notify you when DevOps Guru generates an insight that contains information about how to improve your operations. The one supported notification channel is Amazon Simple Notification Service (Amazon SNS). 

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListNotificationChannelsRequest.from_dict(body)
    return web.Response(status=200)


async def list_organization_insights(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_organization_insights

    Returns a list of insights associated with the account or OU Id.

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
    body = ListOrganizationInsightsRequest.from_dict(body)
    return web.Response(status=200)


async def list_recommendations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """list_recommendations

     Returns a list of a specified insight&#39;s recommendations. Each recommendation includes a list of related metrics and a list of related events. 

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
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def put_feedback(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_feedback

     Collects customer feedback about the specified insight. 

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
    body = PutFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def remove_notification_channel(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_notification_channel

     Removes a notification channel from DevOps Guru. A notification channel is used to notify you when DevOps Guru generates an insight that contains information about how to improve your operations. 

    :param id:  The ID of the notification channel to be removed. 
    :type id: str
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


async def search_insights(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_insights

    &lt;p&gt; Returns a list of insights in your Amazon Web Services account. You can specify which insights are returned by their start time, one or more statuses (&lt;code&gt;ONGOING&lt;/code&gt; or &lt;code&gt;CLOSED&lt;/code&gt;), one or more severities (&lt;code&gt;LOW&lt;/code&gt;, &lt;code&gt;MEDIUM&lt;/code&gt;, and &lt;code&gt;HIGH&lt;/code&gt;), and type (&lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt;). &lt;/p&gt; &lt;p&gt; Use the &lt;code&gt;Filters&lt;/code&gt; parameter to specify status and severity search parameters. Use the &lt;code&gt;Type&lt;/code&gt; parameter to specify &lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt; in your search. &lt;/p&gt;

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
    body = SearchInsightsRequest.from_dict(body)
    return web.Response(status=200)


async def search_organization_insights(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_organization_insights

    &lt;p&gt; Returns a list of insights in your organization. You can specify which insights are returned by their start time, one or more statuses (&lt;code&gt;ONGOING&lt;/code&gt;, &lt;code&gt;CLOSED&lt;/code&gt;, and &lt;code&gt;CLOSED&lt;/code&gt;), one or more severities (&lt;code&gt;LOW&lt;/code&gt;, &lt;code&gt;MEDIUM&lt;/code&gt;, and &lt;code&gt;HIGH&lt;/code&gt;), and type (&lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt;). &lt;/p&gt; &lt;p&gt; Use the &lt;code&gt;Filters&lt;/code&gt; parameter to specify status and severity search parameters. Use the &lt;code&gt;Type&lt;/code&gt; parameter to specify &lt;code&gt;REACTIVE&lt;/code&gt; or &lt;code&gt;PROACTIVE&lt;/code&gt; in your search. &lt;/p&gt;

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
    body = SearchOrganizationInsightsRequest.from_dict(body)
    return web.Response(status=200)


async def start_cost_estimation(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_cost_estimation

    Starts the creation of an estimate of the monthly cost to analyze your Amazon Web Services resources.

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
    body = StartCostEstimationRequest.from_dict(body)
    return web.Response(status=200)


async def update_event_sources_config(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_event_sources_config

    Enables or disables integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon CodeGuru Profiler, which can produce proactive recommendations which can be stored and viewed in DevOps Guru.

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
    body = UpdateEventSourcesConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_resource_collection(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_resource_collection

     Updates the collection of resources that DevOps Guru analyzes. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks. This method also creates the IAM role required for you to use DevOps Guru. 

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
    body = UpdateResourceCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_service_integration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_integration

     Enables or disables integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon Web Services Systems Manager, which can be used to create an OpsItem for each generated insight. 

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
    body = UpdateServiceIntegrationRequest.from_dict(body)
    return web.Response(status=200)
