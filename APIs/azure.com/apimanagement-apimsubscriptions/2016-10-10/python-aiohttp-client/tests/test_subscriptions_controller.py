# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_collection import SubscriptionCollection
from openapi_server.models.subscription_contract import SubscriptionContract
from openapi_server.models.subscription_create_parameters import SubscriptionCreateParameters
from openapi_server.models.subscription_update_parameters import SubscriptionUpdateParameters
from openapi_server.models.subscriptions_list_default_response import SubscriptionsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_subscriptions_create_or_update(client):
    """Test case for subscriptions_create_or_update

    
    """
    parameters = {"productId":"productId","secondaryKey":"secondaryKey","name":"name","state":"Suspended","userId":"userId","primaryKey":"primaryKey"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_delete(client):
    """Test case for subscriptions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_get(client):
    """Test case for subscriptions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_list(client):
    """Test case for subscriptions_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_regenerate_primary_key(client):
    """Test case for subscriptions_regenerate_primary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}/regeneratePrimaryKey'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_regenerate_secondary_key(client):
    """Test case for subscriptions_regenerate_secondary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}/regenerateSecondaryKey'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_update(client):
    """Test case for subscriptions_update

    
    """
    parameters = {"productId":"productId","secondaryKey":"secondaryKey","stateComment":"stateComment","name":"name","state":"Suspended","userId":"userId","expirationDate":"2000-01-23T04:56:07.000+00:00","primaryKey":"primaryKey"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

