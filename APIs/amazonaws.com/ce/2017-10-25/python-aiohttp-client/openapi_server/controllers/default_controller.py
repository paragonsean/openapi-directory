from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_anomaly_monitor_request import CreateAnomalyMonitorRequest
from openapi_server.models.create_anomaly_monitor_response import CreateAnomalyMonitorResponse
from openapi_server.models.create_anomaly_subscription_request import CreateAnomalySubscriptionRequest
from openapi_server.models.create_anomaly_subscription_response import CreateAnomalySubscriptionResponse
from openapi_server.models.create_cost_category_definition_request import CreateCostCategoryDefinitionRequest
from openapi_server.models.create_cost_category_definition_response import CreateCostCategoryDefinitionResponse
from openapi_server.models.delete_anomaly_monitor_request import DeleteAnomalyMonitorRequest
from openapi_server.models.delete_anomaly_subscription_request import DeleteAnomalySubscriptionRequest
from openapi_server.models.delete_cost_category_definition_request import DeleteCostCategoryDefinitionRequest
from openapi_server.models.delete_cost_category_definition_response import DeleteCostCategoryDefinitionResponse
from openapi_server.models.describe_cost_category_definition_request import DescribeCostCategoryDefinitionRequest
from openapi_server.models.describe_cost_category_definition_response import DescribeCostCategoryDefinitionResponse
from openapi_server.models.get_anomalies_request import GetAnomaliesRequest
from openapi_server.models.get_anomalies_response import GetAnomaliesResponse
from openapi_server.models.get_anomaly_monitors_request import GetAnomalyMonitorsRequest
from openapi_server.models.get_anomaly_monitors_response import GetAnomalyMonitorsResponse
from openapi_server.models.get_anomaly_subscriptions_request import GetAnomalySubscriptionsRequest
from openapi_server.models.get_anomaly_subscriptions_response import GetAnomalySubscriptionsResponse
from openapi_server.models.get_cost_and_usage_request import GetCostAndUsageRequest
from openapi_server.models.get_cost_and_usage_response import GetCostAndUsageResponse
from openapi_server.models.get_cost_and_usage_with_resources_request import GetCostAndUsageWithResourcesRequest
from openapi_server.models.get_cost_and_usage_with_resources_response import GetCostAndUsageWithResourcesResponse
from openapi_server.models.get_cost_categories_request import GetCostCategoriesRequest
from openapi_server.models.get_cost_categories_response import GetCostCategoriesResponse
from openapi_server.models.get_cost_forecast_request import GetCostForecastRequest
from openapi_server.models.get_cost_forecast_response import GetCostForecastResponse
from openapi_server.models.get_dimension_values_request import GetDimensionValuesRequest
from openapi_server.models.get_dimension_values_response import GetDimensionValuesResponse
from openapi_server.models.get_reservation_coverage_request import GetReservationCoverageRequest
from openapi_server.models.get_reservation_coverage_response import GetReservationCoverageResponse
from openapi_server.models.get_reservation_purchase_recommendation_request import GetReservationPurchaseRecommendationRequest
from openapi_server.models.get_reservation_purchase_recommendation_response import GetReservationPurchaseRecommendationResponse
from openapi_server.models.get_reservation_utilization_request import GetReservationUtilizationRequest
from openapi_server.models.get_reservation_utilization_response import GetReservationUtilizationResponse
from openapi_server.models.get_rightsizing_recommendation_request import GetRightsizingRecommendationRequest
from openapi_server.models.get_rightsizing_recommendation_response import GetRightsizingRecommendationResponse
from openapi_server.models.get_savings_plan_purchase_recommendation_details_request import GetSavingsPlanPurchaseRecommendationDetailsRequest
from openapi_server.models.get_savings_plan_purchase_recommendation_details_response import GetSavingsPlanPurchaseRecommendationDetailsResponse
from openapi_server.models.get_savings_plans_coverage_request import GetSavingsPlansCoverageRequest
from openapi_server.models.get_savings_plans_coverage_response import GetSavingsPlansCoverageResponse
from openapi_server.models.get_savings_plans_purchase_recommendation_request import GetSavingsPlansPurchaseRecommendationRequest
from openapi_server.models.get_savings_plans_purchase_recommendation_response import GetSavingsPlansPurchaseRecommendationResponse
from openapi_server.models.get_savings_plans_utilization_details_request import GetSavingsPlansUtilizationDetailsRequest
from openapi_server.models.get_savings_plans_utilization_details_response import GetSavingsPlansUtilizationDetailsResponse
from openapi_server.models.get_savings_plans_utilization_request import GetSavingsPlansUtilizationRequest
from openapi_server.models.get_savings_plans_utilization_response import GetSavingsPlansUtilizationResponse
from openapi_server.models.get_tags_request import GetTagsRequest
from openapi_server.models.get_tags_response import GetTagsResponse
from openapi_server.models.get_usage_forecast_request import GetUsageForecastRequest
from openapi_server.models.get_usage_forecast_response import GetUsageForecastResponse
from openapi_server.models.list_cost_allocation_tags_request import ListCostAllocationTagsRequest
from openapi_server.models.list_cost_allocation_tags_response import ListCostAllocationTagsResponse
from openapi_server.models.list_cost_category_definitions_request import ListCostCategoryDefinitionsRequest
from openapi_server.models.list_cost_category_definitions_response import ListCostCategoryDefinitionsResponse
from openapi_server.models.list_savings_plans_purchase_recommendation_generation_request import ListSavingsPlansPurchaseRecommendationGenerationRequest
from openapi_server.models.list_savings_plans_purchase_recommendation_generation_response import ListSavingsPlansPurchaseRecommendationGenerationResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.provide_anomaly_feedback_request import ProvideAnomalyFeedbackRequest
from openapi_server.models.provide_anomaly_feedback_response import ProvideAnomalyFeedbackResponse
from openapi_server.models.start_savings_plans_purchase_recommendation_generation_response import StartSavingsPlansPurchaseRecommendationGenerationResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_anomaly_monitor_request import UpdateAnomalyMonitorRequest
from openapi_server.models.update_anomaly_monitor_response import UpdateAnomalyMonitorResponse
from openapi_server.models.update_anomaly_subscription_request import UpdateAnomalySubscriptionRequest
from openapi_server.models.update_anomaly_subscription_response import UpdateAnomalySubscriptionResponse
from openapi_server.models.update_cost_allocation_tags_status_request import UpdateCostAllocationTagsStatusRequest
from openapi_server.models.update_cost_allocation_tags_status_response import UpdateCostAllocationTagsStatusResponse
from openapi_server.models.update_cost_category_definition_request import UpdateCostCategoryDefinitionRequest
from openapi_server.models.update_cost_category_definition_response import UpdateCostCategoryDefinitionResponse
from openapi_server import util


async def create_anomaly_monitor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_anomaly_monitor

    Creates a new cost anomaly detection monitor with the requested type and monitor specification. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateAnomalyMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def create_anomaly_subscription(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_anomaly_subscription

    Adds an alert subscription to a cost anomaly detection monitor. You can use each subscription to define subscribers with email or SNS notifications. Email subscribers can set an absolute or percentage threshold and a time frequency for receiving notifications. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateAnomalySubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def create_cost_category_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cost_category_definition

    Creates a new Cost Category with the requested name and rules.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateCostCategoryDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_anomaly_monitor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_anomaly_monitor

    Deletes a cost anomaly monitor. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteAnomalyMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def delete_anomaly_subscription(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_anomaly_subscription

    Deletes a cost anomaly subscription. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteAnomalySubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_cost_category_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_cost_category_definition

    Deletes a Cost Category. Expenses from this month going forward will no longer be categorized with this Cost Category.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteCostCategoryDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def describe_cost_category_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cost_category_definition

    &lt;p&gt;Returns the name, Amazon Resource Name (ARN), rules, definition, and effective dates of a Cost Category that&#39;s defined in the account.&lt;/p&gt; &lt;p&gt;You have the option to use &lt;code&gt;EffectiveOn&lt;/code&gt; to return a Cost Category that&#39;s active on a specific date. If there&#39;s no &lt;code&gt;EffectiveOn&lt;/code&gt; specified, you see a Cost Category that&#39;s effective on the current date. If Cost Category is still effective, &lt;code&gt;EffectiveEnd&lt;/code&gt; is omitted in the response. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeCostCategoryDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def get_anomalies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_anomalies

    Retrieves all of the cost anomalies detected on your account during the time period that&#39;s specified by the &lt;code&gt;DateInterval&lt;/code&gt; object. Anomalies are available for up to 90 days.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetAnomaliesRequest.from_dict(body)
    return web.Response(status=200)


async def get_anomaly_monitors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_anomaly_monitors

    Retrieves the cost anomaly monitor definitions for your account. You can filter using a list of cost anomaly monitor Amazon Resource Names (ARNs). 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetAnomalyMonitorsRequest.from_dict(body)
    return web.Response(status=200)


async def get_anomaly_subscriptions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_anomaly_subscriptions

    Retrieves the cost anomaly subscription objects for your account. You can filter using a list of cost anomaly monitor Amazon Resource Names (ARNs). 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetAnomalySubscriptionsRequest.from_dict(body)
    return web.Response(status=200)


async def get_cost_and_usage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cost_and_usage

    &lt;p&gt;Retrieves cost and usage metrics for your account. You can specify which cost and usage-related metric that you want the request to return. For example, you can specify &lt;code&gt;BlendedCosts&lt;/code&gt; or &lt;code&gt;UsageQuantity&lt;/code&gt;. You can also filter and group your data by various dimensions, such as &lt;code&gt;SERVICE&lt;/code&gt; or &lt;code&gt;AZ&lt;/code&gt;, in a specific time range. For a complete list of valid dimensions, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html\&quot;&gt;GetDimensionValues&lt;/a&gt; operation. Management account in an organization in Organizations have access to all member accounts.&lt;/p&gt; &lt;p&gt;For information about filter limitations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html\&quot;&gt;Quotas and restrictions&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetCostAndUsageRequest.from_dict(body)
    return web.Response(status=200)


async def get_cost_and_usage_with_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cost_and_usage_with_resources

    &lt;p&gt;Retrieves cost and usage metrics with resources for your account. You can specify which cost and usage-related metric, such as &lt;code&gt;BlendedCosts&lt;/code&gt; or &lt;code&gt;UsageQuantity&lt;/code&gt;, that you want the request to return. You can also filter and group your data by various dimensions, such as &lt;code&gt;SERVICE&lt;/code&gt; or &lt;code&gt;AZ&lt;/code&gt;, in a specific time range. For a complete list of valid dimensions, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html\&quot;&gt;GetDimensionValues&lt;/a&gt; operation. Management account in an organization in Organizations have access to all member accounts. This API is currently available for the Amazon Elastic Compute Cloud – Compute service only.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This is an opt-in only feature. You can enable this feature from the Cost Explorer Settings page. For information about how to access the Settings page, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-access.html\&quot;&gt;Controlling Access for Cost Explorer&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetCostAndUsageWithResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def get_cost_categories(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cost_categories

    &lt;p&gt;Retrieves an array of Cost Category names and values incurred cost.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If some Cost Category names and values are not associated with any cost, they will not be returned by this API.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetCostCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def get_cost_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cost_forecast

    Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the forecast time period that you select, based on your past costs. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetCostForecastRequest.from_dict(body)
    return web.Response(status=200)


async def get_dimension_values(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dimension_values

    Retrieves all available filter values for a specified filter over a period of time. You can search the dimension values for an arbitrary string. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetDimensionValuesRequest.from_dict(body)
    return web.Response(status=200)


async def get_reservation_coverage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_reservation_coverage

    &lt;p&gt;Retrieves the reservation coverage for your account, which you can use to see how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon Redshift usage is covered by a reservation. An organization&#39;s management account can see the coverage of the associated member accounts. This supports dimensions, Cost Categories, and nested expressions. For any time period, you can filter data about reservation usage by the following dimensions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;AZ&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;CACHE_ENGINE&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DATABASE_ENGINE&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DEPLOYMENT_OPTION&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;INSTANCE_TYPE&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;LINKED_ACCOUNT&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;OPERATING_SYSTEM&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;PLATFORM&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;REGION&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;SERVICE&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;TAG&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;TENANCY&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To determine valid values for a dimension, use the &lt;code&gt;GetDimensionValues&lt;/code&gt; operation. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetReservationCoverageRequest.from_dict(body)
    return web.Response(status=200)


async def get_reservation_purchase_recommendation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_reservation_purchase_recommendation

    &lt;p&gt;Gets recommendations for reservation purchases. These recommendations might help you to reduce your costs. Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand pricing.&lt;/p&gt; &lt;p&gt;Amazon Web Services generates your recommendations by identifying your On-Demand usage during a specific time period and collecting your usage into categories that are eligible for a reservation. After Amazon Web Services has these categories, it simulates every combination of reservations in each category of usage to identify the best number of each type of Reserved Instance (RI) to purchase to maximize your estimated savings. &lt;/p&gt; &lt;p&gt;For example, Amazon Web Services automatically aggregates your Amazon EC2 Linux, shared tenancy, and c4 family usage in the US West (Oregon) Region and recommends that you buy size-flexible regional reservations to apply to the c4 family usage. Amazon Web Services recommends the smallest size instance in an instance family. This makes it easier to purchase a size-flexible Reserved Instance (RI). Amazon Web Services also shows the equal number of normalized units. This way, you can purchase any instance size that you want. For this example, your RI recommendation is for &lt;code&gt;c4.large&lt;/code&gt; because that is the smallest size instance in the c4 instance family.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetReservationPurchaseRecommendationRequest.from_dict(body)
    return web.Response(status=200)


async def get_reservation_utilization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_reservation_utilization

    Retrieves the reservation utilization for your account. Management account in an organization have access to member accounts. You can filter data by dimensions in a time period. You can use &lt;code&gt;GetDimensionValues&lt;/code&gt; to determine the possible dimension values. Currently, you can group only by &lt;code&gt;SUBSCRIPTION_ID&lt;/code&gt;. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetReservationUtilizationRequest.from_dict(body)
    return web.Response(status=200)


async def get_rightsizing_recommendation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_rightsizing_recommendation

    &lt;p&gt;Creates recommendations that help you save cost by identifying idle and underutilized Amazon EC2 instances.&lt;/p&gt; &lt;p&gt;Recommendations are generated to either downsize or terminate instances, along with providing savings detail and metrics. For more information about calculation and function, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html\&quot;&gt;Optimizing Your Cost with Rightsizing Recommendations&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetRightsizingRecommendationRequest.from_dict(body)
    return web.Response(status=200)


async def get_savings_plan_purchase_recommendation_details(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_savings_plan_purchase_recommendation_details

    Retrieves the details for a Savings Plan recommendation. These details include the hourly data-points that construct the new cost, coverage, and utilization charts.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetSavingsPlanPurchaseRecommendationDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def get_savings_plans_coverage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_savings_plans_coverage

    &lt;p&gt;Retrieves the Savings Plans covered for your account. This enables you to see how much of your cost is covered by a Savings Plan. An organization’s management account can see the coverage of the associated member accounts. This supports dimensions, Cost Categories, and nested expressions. For any time period, you can filter data for Savings Plans usage with the following dimensions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LINKED_ACCOUNT&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;REGION&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SERVICE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;INSTANCE_FAMILY&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To determine valid values for a dimension, use the &lt;code&gt;GetDimensionValues&lt;/code&gt; operation.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetSavingsPlansCoverageRequest.from_dict(body)
    return web.Response(status=200)


async def get_savings_plans_purchase_recommendation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_savings_plans_purchase_recommendation

    Retrieves the Savings Plans recommendations for your account. First use &lt;code&gt;StartSavingsPlansPurchaseRecommendationGeneration&lt;/code&gt; to generate a new set of recommendations, and then use &lt;code&gt;GetSavingsPlansPurchaseRecommendation&lt;/code&gt; to retrieve them.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetSavingsPlansPurchaseRecommendationRequest.from_dict(body)
    return web.Response(status=200)


async def get_savings_plans_utilization(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_savings_plans_utilization

    &lt;p&gt;Retrieves the Savings Plans utilization for your account across date ranges with daily or monthly granularity. Management account in an organization have access to member accounts. You can use &lt;code&gt;GetDimensionValues&lt;/code&gt; in &lt;code&gt;SAVINGS_PLANS&lt;/code&gt; to determine the possible dimension values.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t group by any dimension values for &lt;code&gt;GetSavingsPlansUtilization&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetSavingsPlansUtilizationRequest.from_dict(body)
    return web.Response(status=200)


async def get_savings_plans_utilization_details(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_savings_plans_utilization_details

    &lt;p&gt;Retrieves attribute data along with aggregate utilization and savings data for a given time period. This doesn&#39;t support granular or grouped data (daily/monthly) in response. You can&#39;t retrieve data by dates in a single response similar to &lt;code&gt;GetSavingsPlanUtilization&lt;/code&gt;, but you have the option to make multiple calls to &lt;code&gt;GetSavingsPlanUtilizationDetails&lt;/code&gt; by providing individual dates. You can use &lt;code&gt;GetDimensionValues&lt;/code&gt; in &lt;code&gt;SAVINGS_PLANS&lt;/code&gt; to determine the possible dimension values.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;GetSavingsPlanUtilizationDetails&lt;/code&gt; internally groups data by &lt;code&gt;SavingsPlansArn&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetSavingsPlansUtilizationDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def get_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_tags

    Queries for available tag keys and tag values for a specified period. You can search the tag values for an arbitrary string. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetTagsRequest.from_dict(body)
    return web.Response(status=200)


async def get_usage_forecast(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_usage_forecast

    Retrieves a forecast for how much Amazon Web Services predicts that you will use over the forecast time period that you select, based on your past usage. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetUsageForecastRequest.from_dict(body)
    return web.Response(status=200)


async def list_cost_allocation_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_cost_allocation_tags

    Get a list of cost allocation tags. All inputs in the API are optional and serve as filters. By default, all cost allocation tags are returned. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListCostAllocationTagsRequest.from_dict(body)
    return web.Response(status=200)


async def list_cost_category_definitions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_cost_category_definitions

    Returns the name, Amazon Resource Name (ARN), &lt;code&gt;NumberOfRules&lt;/code&gt; and effective dates of all Cost Categories defined in the account. You have the option to use &lt;code&gt;EffectiveOn&lt;/code&gt; to return a list of Cost Categories that were active on a specific date. If there is no &lt;code&gt;EffectiveOn&lt;/code&gt; specified, you’ll see Cost Categories that are effective on the current date. If Cost Category is still effective, &lt;code&gt;EffectiveEnd&lt;/code&gt; is omitted in the response. &lt;code&gt;ListCostCategoryDefinitions&lt;/code&gt; supports pagination. The request can have a &lt;code&gt;MaxResults&lt;/code&gt; range up to 100.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListCostCategoryDefinitionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_savings_plans_purchase_recommendation_generation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_savings_plans_purchase_recommendation_generation

    Retrieves a list of your historical recommendation generations within the past 30 days.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListSavingsPlansPurchaseRecommendationGenerationRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Returns a list of resource tags associated with the resource specified by the Amazon Resource Name (ARN). 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def provide_anomaly_feedback(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """provide_anomaly_feedback

    Modifies the feedback property of a given cost anomaly. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ProvideAnomalyFeedbackRequest.from_dict(body)
    return web.Response(status=200)


async def start_savings_plans_purchase_recommendation_generation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_savings_plans_purchase_recommendation_generation

    &lt;p&gt;Requests a Savings Plans recommendation generation. This enables you to calculate a fresh set of Savings Plans recommendations that takes your latest usage data and current Savings Plans inventory into account. You can refresh Savings Plans recommendations up to three times daily for a consolidated billing family.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;StartSavingsPlansPurchaseRecommendationGeneration&lt;/code&gt; has no request syntax because no input parameters are needed to support this operation.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;An API operation for adding one or more tags (key-value pairs) to a resource.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;Although the maximum number of array members is 200, user-tag maximum is 50. The remaining are reserved for Amazon Web Services use.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from a resource. Specify only tag keys in your request. Don&#39;t specify the value. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_anomaly_monitor(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_anomaly_monitor

    Updates an existing cost anomaly monitor. The changes made are applied going forward, and doesn&#39;t change anomalies detected in the past. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateAnomalyMonitorRequest.from_dict(body)
    return web.Response(status=200)


async def update_anomaly_subscription(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_anomaly_subscription

    &lt;p&gt;Updates an existing cost anomaly subscription. Specify the fields that you want to update. Omitted fields are unchanged.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The JSON below describes the generic construct for each type. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalySubscription.html#API_UpdateAnomalySubscription_RequestParameters\&quot;&gt;Request Parameters&lt;/a&gt; for possible values as they apply to &lt;code&gt;AnomalySubscription&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateAnomalySubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def update_cost_allocation_tags_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cost_allocation_tags_status

    Updates status for cost allocation tags in bulk, with maximum batch size of 20. If the tag status that&#39;s updated is the same as the existing tag status, the request doesn&#39;t fail. Instead, it doesn&#39;t have any effect on the tag status (for example, activating the active tag). 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateCostAllocationTagsStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_cost_category_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cost_category_definition

    Updates an existing Cost Category. Changes made to the Cost Category rules will be used to categorize the current month’s expenses and future expenses. This won’t change categorization for the previous months.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateCostCategoryDefinitionRequest.from_dict(body)
    return web.Response(status=200)
