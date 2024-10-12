# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.link_list_result import LinkListResult
from openapi_server.models.link_resource_format import LinkResourceFormat


pytestmark = pytest.mark.asyncio

async def test_links_create_or_update(client):
    """Test case for links_create_or_update

    
    """
    parameters = {"properties":{"sourceEntityType":"None","sourceEntityTypeName":"sourceEntityTypeName","displayName":{"key":"displayName"},"description":{"key":"description"},"participantPropertyReferences":[{"targetPropertyName":"targetPropertyName","sourcePropertyName":"sourcePropertyName"},{"targetPropertyName":"targetPropertyName","sourcePropertyName":"sourcePropertyName"}],"targetEntityTypeName":"targetEntityTypeName","provisioningState":"Provisioning","linkName":"linkName","mappings":[{"targetPropertyName":"targetPropertyName","linkType":"UpdateAlways","sourcePropertyName":"sourcePropertyName"},{"targetPropertyName":"targetPropertyName","linkType":"UpdateAlways","sourcePropertyName":"sourcePropertyName"}],"targetEntityType":"None","tenantId":"tenantId","operationType":"Upsert","referenceOnly":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/links/{link_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', link_name='link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_links_delete(client):
    """Test case for links_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/links/{link_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', link_name='link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_links_get(client):
    """Test case for links_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/links/{link_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', link_name='link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_links_list_by_hub(client):
    """Test case for links_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/links'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

