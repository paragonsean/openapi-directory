# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_subscription import CustomerSubscription
from openapi_server.models.customer_subscription_list import CustomerSubscriptionList
from openapi_server.models.customer_subscriptions_list_default_response import CustomerSubscriptionsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_customer_subscriptions_create(client):
    """Test case for customer_subscriptions_create

    
    """
    customer_creation_parameters = {"properties":{"tenantId":"tenantId"}}
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/customerSubscriptions/{customer_subscription_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example', customer_subscription_name='customer_subscription_name_example'),
        headers=headers,
        json=customer_creation_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_subscriptions_delete(client):
    """Test case for customer_subscriptions_delete

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/customerSubscriptions/{customer_subscription_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example', customer_subscription_name='customer_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_subscriptions_get(client):
    """Test case for customer_subscriptions_get

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/customerSubscriptions/{customer_subscription_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example', customer_subscription_name='customer_subscription_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_subscriptions_list(client):
    """Test case for customer_subscriptions_list

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/customerSubscriptions'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

