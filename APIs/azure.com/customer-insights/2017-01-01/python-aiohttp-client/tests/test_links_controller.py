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
    parameters = {"properties":{"sourceInteractionType":"sourceInteractionType","mappings":[{"isProfileTypeId":True,"interactionTypePropertyName":"interactionTypePropertyName","linkType":"UpdateAlways","profileTypePropertyName":"profileTypePropertyName"},{"isProfileTypeId":True,"interactionTypePropertyName":"interactionTypePropertyName","linkType":"UpdateAlways","profileTypePropertyName":"profileTypePropertyName"}],"targetProfileType":"targetProfileType","displayName":{"key":"displayName"},"tenantId":"tenantId","description":{"key":"description"},"operationType":"Upsert","participantPropertyReferences":[{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"},{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"}],"provisioningState":"Provisioning","referenceOnly":True,"linkName":"linkName"}}
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

