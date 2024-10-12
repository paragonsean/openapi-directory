# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_health_data_list_result import EndpointHealthDataListResult
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.event_hub_consumer_group_info import EventHubConsumerGroupInfo
from openapi_server.models.event_hub_consumer_groups_list_result import EventHubConsumerGroupsListResult
from openapi_server.models.iot_hub_description import IotHubDescription
from openapi_server.models.iot_hub_description_list_result import IotHubDescriptionListResult
from openapi_server.models.iot_hub_quota_metric_info_list_result import IotHubQuotaMetricInfoListResult
from openapi_server.models.iot_hub_sku_description_list_result import IotHubSkuDescriptionListResult
from openapi_server.models.job_response import JobResponse
from openapi_server.models.job_response_list_result import JobResponseListResult
from openapi_server.models.registry_statistics import RegistryStatistics
from openapi_server.models.user_subscription_quota_list_result import UserSubscriptionQuotaListResult


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get(client):
    """Test case for iot_hub_resource_get

    Get the non-security related metadata of an IoT hub
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get_endpoint_health(client):
    """Test case for iot_hub_resource_get_endpoint_health

    Get the health for routing endpoints
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{iot_hub_name}/routingEndpointsHealth'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', iot_hub_name='iot_hub_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get_event_hub_consumer_group(client):
    """Test case for iot_hub_resource_get_event_hub_consumer_group

    Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/eventHubEndpoints/{event_hub_endpoint_name}/ConsumerGroups/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', event_hub_endpoint_name='event_hub_endpoint_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get_job(client):
    """Test case for iot_hub_resource_get_job

    Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/jobs/{job_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get_quota_metrics(client):
    """Test case for iot_hub_resource_get_quota_metrics

    Get the quota metrics for an IoT hub
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/quotaMetrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get_stats(client):
    """Test case for iot_hub_resource_get_stats

    Get the statistics from an IoT hub
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/IotHubStats'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get_valid_skus(client):
    """Test case for iot_hub_resource_get_valid_skus

    Get the list of valid SKUs for an IoT hub
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/skus'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_list_by_resource_group(client):
    """Test case for iot_hub_resource_list_by_resource_group

    Get all the IoT hubs in a resource group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_list_by_subscription(client):
    """Test case for iot_hub_resource_list_by_subscription

    Get all the IoT hubs in a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Devices/IotHubs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_list_event_hub_consumer_groups(client):
    """Test case for iot_hub_resource_list_event_hub_consumer_groups

    Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/eventHubEndpoints/{event_hub_endpoint_name}/ConsumerGroups'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', event_hub_endpoint_name='event_hub_endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_list_jobs(client):
    """Test case for iot_hub_resource_list_jobs

    Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/jobs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_provider_common_get_subscription_quota(client):
    """Test case for resource_provider_common_get_subscription_quota

    Get the number of iot hubs in the subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Devices/usages'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

