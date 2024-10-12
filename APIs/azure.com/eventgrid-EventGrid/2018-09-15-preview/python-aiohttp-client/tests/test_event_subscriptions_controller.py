# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_subscription import EventSubscription
from openapi_server.models.event_subscription_full_url import EventSubscriptionFullUrl
from openapi_server.models.event_subscription_update_parameters import EventSubscriptionUpdateParameters
from openapi_server.models.event_subscriptions_list_result import EventSubscriptionsListResult


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_create_or_update(client):
    """Test case for event_subscriptions_create_or_update

    Create or update an event subscription
    """
    event_subscription_info = {"properties":{"expirationTimeUtc":"2000-01-23T04:56:07.000+00:00","filter":{"includedEventTypes":["includedEventTypes","includedEventTypes"],"subjectEndsWith":"subjectEndsWith","subjectBeginsWith":"subjectBeginsWith","advancedFilters":[{"operatorType":"NumberIn","key":"key"},{"operatorType":"NumberIn","key":"key"}],"isSubjectCaseSensitive":False},"deadLetterDestination":{"endpointType":"StorageBlob"},"retryPolicy":{"maxDeliveryAttempts":6,"eventTimeToLiveInMinutes":0},"destination":{"endpointType":"WebHook"},"eventDeliverySchema":"EventGridSchema","topic":"topic","provisioningState":"Creating","labels":["labels","labels"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{event_subscription_name}'.format(scope='scope_example', event_subscription_name='event_subscription_name_example'),
        headers=headers,
        json=event_subscription_info,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_delete(client):
    """Test case for event_subscriptions_delete

    Delete an event subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{event_subscription_name}'.format(scope='scope_example', event_subscription_name='event_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_get(client):
    """Test case for event_subscriptions_get

    Get an event subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{event_subscription_name}'.format(scope='scope_example', event_subscription_name='event_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_get_full_url(client):
    """Test case for event_subscriptions_get_full_url

    Get full URL of an event subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{event_subscription_name}/getFullUrl'.format(scope='scope_example', event_subscription_name='event_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_by_domain_topic(client):
    """Test case for event_subscriptions_list_by_domain_topic

    List all event subscriptions for a specific domain topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/domains/{domain_name}/topics/{topic_name}/providers/Microsoft.EventGrid/eventSubscriptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', domain_name='domain_name_example', topic_name='topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_by_resource(client):
    """Test case for event_subscriptions_list_by_resource

    List all event subscriptions for a specific topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/{provider_namespace}/{resource_type_name}/{resource_name}/providers/Microsoft.EventGrid/eventSubscriptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provider_namespace='provider_namespace_example', resource_type_name='resource_type_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_global_by_resource_group(client):
    """Test case for event_subscriptions_list_global_by_resource_group

    List all global event subscriptions under an Azure subscription and resource group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/eventSubscriptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_global_by_resource_group_for_topic_type(client):
    """Test case for event_subscriptions_list_global_by_resource_group_for_topic_type

    List all global event subscriptions under a resource group for a topic type
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topicTypes/{topic_type_name}/eventSubscriptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', topic_type_name='topic_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_global_by_subscription(client):
    """Test case for event_subscriptions_list_global_by_subscription

    Get an aggregated list of all global event subscriptions under an Azure subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.EventGrid/eventSubscriptions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_global_by_subscription_for_topic_type(client):
    """Test case for event_subscriptions_list_global_by_subscription_for_topic_type

    List all global event subscriptions for a topic type
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.EventGrid/topicTypes/{topic_type_name}/eventSubscriptions'.format(subscription_id='subscription_id_example', topic_type_name='topic_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_regional_by_resource_group(client):
    """Test case for event_subscriptions_list_regional_by_resource_group

    List all regional event subscriptions under an Azure subscription and resource group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/locations/{location}/eventSubscriptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_regional_by_resource_group_for_topic_type(client):
    """Test case for event_subscriptions_list_regional_by_resource_group_for_topic_type

    List all regional event subscriptions under an Azure subscription and resource group for a topic type
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/locations/{location}/topicTypes/{topic_type_name}/eventSubscriptions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', topic_type_name='topic_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_regional_by_subscription(client):
    """Test case for event_subscriptions_list_regional_by_subscription

    List all regional event subscriptions under an Azure subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.EventGrid/locations/{location}/eventSubscriptions'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_list_regional_by_subscription_for_topic_type(client):
    """Test case for event_subscriptions_list_regional_by_subscription_for_topic_type

    List all regional event subscriptions under an Azure subscription for a topic type
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.EventGrid/locations/{location}/topicTypes/{topic_type_name}/eventSubscriptions'.format(subscription_id='subscription_id_example', location='location_example', topic_type_name='topic_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_subscriptions_update(client):
    """Test case for event_subscriptions_update

    Update an event subscription
    """
    event_subscription_update_parameters = {"expirationTimeUtc":"2000-01-23T04:56:07.000+00:00","filter":{"includedEventTypes":["includedEventTypes","includedEventTypes"],"subjectEndsWith":"subjectEndsWith","subjectBeginsWith":"subjectBeginsWith","advancedFilters":[{"operatorType":"NumberIn","key":"key"},{"operatorType":"NumberIn","key":"key"}],"isSubjectCaseSensitive":False},"deadLetterDestination":{"endpointType":"StorageBlob"},"retryPolicy":{"maxDeliveryAttempts":6,"eventTimeToLiveInMinutes":0},"destination":{"endpointType":"WebHook"},"eventDeliverySchema":"EventGridSchema","labels":["labels","labels"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/{scope}/providers/Microsoft.EventGrid/eventSubscriptions/{event_subscription_name}'.format(scope='scope_example', event_subscription_name='event_subscription_name_example'),
        headers=headers,
        json=event_subscription_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

