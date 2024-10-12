# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_create_anomaly_monitor(client):
    """Test case for create_anomaly_monitor

    
    """
    body = {"ResourceTags":"","AnomalyMonitor":{"LastUpdatedDate":"","CreationDate":"","LastEvaluatedDate":"","MonitorType":"","MonitorArn":"","MonitorName":"","MonitorSpecification":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"MonitorDimension":"","DimensionalValueCount":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.CreateAnomalyMonitor',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_anomaly_subscription(client):
    """Test case for create_anomaly_subscription

    
    """
    body = {"ResourceTags":"","AnomalySubscription":{"MonitorArnList":"","AccountId":"","Frequency":"","SubscriptionName":"","Subscribers":"","SubscriptionArn":"","Threshold":"","ThresholdExpression":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.CreateAnomalySubscription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_cost_category_definition(client):
    """Test case for create_cost_category_definition

    
    """
    body = {"DefaultValue":"DefaultValue","ResourceTags":"","EffectiveStart":"","SplitChargeRules":"","RuleVersion":"CostCategoryExpression.v1","Rules":"","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.CreateCostCategoryDefinition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_anomaly_monitor(client):
    """Test case for delete_anomaly_monitor

    
    """
    body = {"MonitorArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.DeleteAnomalyMonitor',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_anomaly_subscription(client):
    """Test case for delete_anomaly_subscription

    
    """
    body = {"SubscriptionArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.DeleteAnomalySubscription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cost_category_definition(client):
    """Test case for delete_cost_category_definition

    
    """
    body = {"CostCategoryArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.DeleteCostCategoryDefinition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_cost_category_definition(client):
    """Test case for describe_cost_category_definition

    
    """
    body = {"CostCategoryArn":"","EffectiveOn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.DescribeCostCategoryDefinition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_anomalies(client):
    """Test case for get_anomalies

    
    """
    body = {"TotalImpact":{"StartValue":"","EndValue":"","NumericOperator":""},"Feedback":"","MonitorArn":"","NextPageToken":"","MaxResults":"","DateInterval":{"StartDate":"","EndDate":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetAnomalies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_anomaly_monitors(client):
    """Test case for get_anomaly_monitors

    
    """
    body = {"MonitorArnList":"","NextPageToken":"","MaxResults":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetAnomalyMonitors',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_anomaly_subscriptions(client):
    """Test case for get_anomaly_subscriptions

    
    """
    body = {"MonitorArn":"","NextPageToken":"","SubscriptionArnList":"","MaxResults":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetAnomalySubscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cost_and_usage(client):
    """Test case for get_cost_and_usage

    
    """
    body = {"Metrics":"","GroupBy":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"NextPageToken":"","Granularity":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetCostAndUsage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cost_and_usage_with_resources(client):
    """Test case for get_cost_and_usage_with_resources

    
    """
    body = {"Metrics":"","GroupBy":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"NextPageToken":"","Granularity":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetCostAndUsageWithResources',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cost_categories(client):
    """Test case for get_cost_categories

    
    """
    body = {"Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"CostCategoryName":"CostCategoryName","SortBy":"","NextPageToken":"","MaxResults":"","SearchString":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetCostCategories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cost_forecast(client):
    """Test case for get_cost_forecast

    
    """
    body = {"Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"Metric":"","Granularity":"","PredictionIntervalLevel":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetCostForecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dimension_values(client):
    """Test case for get_dimension_values

    
    """
    body = {"Context":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"SortBy":"","NextPageToken":"","MaxResults":"","Dimension":"","SearchString":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetDimensionValues',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reservation_coverage(client):
    """Test case for get_reservation_coverage

    
    """
    body = {"Metrics":"","GroupBy":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"NextPageToken":"","SortBy":{"SortOrder":"","Key":""},"MaxResults":"","Granularity":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetReservationCoverage',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reservation_purchase_recommendation(client):
    """Test case for get_reservation_purchase_recommendation

    
    """
    body = {"ServiceSpecification":{"EC2Specification":{"OfferingClass":""}},"AccountId":"","PageSize":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"LookbackPeriodInDays":"","NextPageToken":"","Service":"","PaymentOption":"","TermInYears":"","AccountScope":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetReservationPurchaseRecommendation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reservation_utilization(client):
    """Test case for get_reservation_utilization

    
    """
    body = {"GroupBy":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"SortBy":{"SortOrder":"","Key":""},"NextPageToken":"","MaxResults":"","Granularity":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetReservationUtilization',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rightsizing_recommendation(client):
    """Test case for get_rightsizing_recommendation

    
    """
    body = {"Configuration":{"BenefitsConsidered":"","RecommendationTarget":""},"PageSize":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"NextPageToken":"","Service":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetRightsizingRecommendation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_savings_plan_purchase_recommendation_details(client):
    """Test case for get_savings_plan_purchase_recommendation_details

    
    """
    body = {"RecommendationDetailId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetSavingsPlanPurchaseRecommendationDetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_savings_plans_coverage(client):
    """Test case for get_savings_plans_coverage

    
    """
    body = {"Metrics":"","GroupBy":"","NextToken":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"SortBy":{"SortOrder":"","Key":""},"MaxResults":"","Granularity":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetSavingsPlansCoverage',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_savings_plans_purchase_recommendation(client):
    """Test case for get_savings_plans_purchase_recommendation

    
    """
    body = {"PageSize":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"SavingsPlansType":"","NextPageToken":"","LookbackPeriodInDays":"","PaymentOption":"","TermInYears":"","AccountScope":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetSavingsPlansPurchaseRecommendation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_savings_plans_utilization(client):
    """Test case for get_savings_plans_utilization

    
    """
    body = {"Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"SortBy":{"SortOrder":"","Key":""},"Granularity":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetSavingsPlansUtilization',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_savings_plans_utilization_details(client):
    """Test case for get_savings_plans_utilization_details

    
    """
    body = {"NextToken":"","Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"SortBy":{"SortOrder":"","Key":""},"MaxResults":"","DataType":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetSavingsPlansUtilizationDetails',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags(client):
    """Test case for get_tags

    
    """
    body = {"Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"SortBy":"","NextPageToken":"","MaxResults":"","TagKey":"","SearchString":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetTags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_usage_forecast(client):
    """Test case for get_usage_forecast

    
    """
    body = {"Filter":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"TimePeriod":{"Start":"","End":""},"Metric":"","Granularity":"","PredictionIntervalLevel":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.GetUsageForecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cost_allocation_tags(client):
    """Test case for list_cost_allocation_tags

    
    """
    body = {"Status":"","Type":"","NextToken":"","MaxResults":"","TagKeys":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.ListCostAllocationTags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cost_category_definitions(client):
    """Test case for list_cost_category_definitions

    
    """
    body = {"NextToken":"","MaxResults":"","EffectiveOn":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.ListCostCategoryDefinitions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_savings_plans_purchase_recommendation_generation(client):
    """Test case for list_savings_plans_purchase_recommendation_generation

    
    """
    body = {"RecommendationIds":"","PageSize":"","NextPageToken":"","GenerationStatus":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.ListSavingsPlansPurchaseRecommendationGeneration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    body = {"ResourceArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.ListTagsForResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provide_anomaly_feedback(client):
    """Test case for provide_anomaly_feedback

    
    """
    body = {"AnomalyId":"","Feedback":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.ProvideAnomalyFeedback',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_savings_plans_purchase_recommendation_generation(client):
    """Test case for start_savings_plans_purchase_recommendation_generation

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.StartSavingsPlansPurchaseRecommendationGeneration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"ResourceArn":"","ResourceTags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.TagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"ResourceArn":"","ResourceTagKeys":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.UntagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_anomaly_monitor(client):
    """Test case for update_anomaly_monitor

    
    """
    body = {"MonitorArn":"","MonitorName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.UpdateAnomalyMonitor',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_anomaly_subscription(client):
    """Test case for update_anomaly_subscription

    
    """
    body = {"MonitorArnList":"","Frequency":"","SubscriptionName":"","Subscribers":"","SubscriptionArn":"","Threshold":"","ThresholdExpression":{"Not":{"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}},"Or":"","And":"","Dimensions":{"MatchOptions":"","Values":"","Key":""},"CostCategories":{"MatchOptions":"","Values":"","Key":"Key"},"Tags":{"MatchOptions":"","Values":"","Key":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.UpdateAnomalySubscription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cost_allocation_tags_status(client):
    """Test case for update_cost_allocation_tags_status

    
    """
    body = {"CostAllocationTagsStatus":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.UpdateCostAllocationTagsStatus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_cost_category_definition(client):
    """Test case for update_cost_category_definition

    
    """
    body = {"CostCategoryArn":"","DefaultValue":"DefaultValue","EffectiveStart":"","SplitChargeRules":"","RuleVersion":"CostCategoryExpression.v1","Rules":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSInsightsIndexService.UpdateCostCategoryDefinition',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

