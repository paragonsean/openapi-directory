# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_create_or_update_request import SubscriptionCreateOrUpdateRequest
from openapi_server.models.subscription_get200_response import SubscriptionGet200Response
from openapi_server.models.subscription_list200_response import SubscriptionList200Response
from openapi_server.models.subscription_list_default_response import SubscriptionListDefaultResponse
from openapi_server.models.subscription_update_request import SubscriptionUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_subscription_create_or_update(client):
    """Test case for subscription_create_or_update

    
    """
    parameters = openapi_server.SubscriptionCreateOrUpdateRequest()
    params = [('notify', True),
                    ('api-version', 'api_version_example'),
                    ('appType', portal)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
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

async def test_subscription_delete(client):
    """Test case for subscription_delete

    
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

async def test_subscription_get(client):
    """Test case for subscription_get

    
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

async def test_subscription_get_entity_tag(client):
    """Test case for subscription_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_list(client):
    """Test case for subscription_list

    
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

async def test_subscription_update(client):
    """Test case for subscription_update

    
    """
    parameters = openapi_server.SubscriptionUpdateRequest()
    params = [('notify', True),
                    ('api-version', 'api_version_example'),
                    ('appType', portal)]
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

