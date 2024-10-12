# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.relationship_link_list_result import RelationshipLinkListResult
from openapi_server.models.relationship_link_resource_format import RelationshipLinkResourceFormat


pytestmark = pytest.mark.asyncio

async def test_relationship_links_create_or_update(client):
    """Test case for relationship_links_create_or_update

    
    """
    parameters = {"properties":{"relationshipName":"relationshipName","mappings":[{"relationshipFieldName":"relationshipFieldName","linkType":"UpdateAlways","interactionFieldName":"interactionFieldName"},{"relationshipFieldName":"relationshipFieldName","linkType":"UpdateAlways","interactionFieldName":"interactionFieldName"}],"interactionType":"interactionType","displayName":{"key":"displayName"},"relationshipGuidId":"relationshipGuidId","profilePropertyReferences":[{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"},{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"}],"tenantId":"tenantId","description":{"key":"description"},"provisioningState":"Provisioning","relatedProfilePropertyReferences":[{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"},{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"}],"linkName":"linkName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationshipLinks/{relationship_link_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', relationship_link_name='relationship_link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relationship_links_delete(client):
    """Test case for relationship_links_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationshipLinks/{relationship_link_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', relationship_link_name='relationship_link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relationship_links_get(client):
    """Test case for relationship_links_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationshipLinks/{relationship_link_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', relationship_link_name='relationship_link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relationship_links_list_by_hub(client):
    """Test case for relationship_links_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationshipLinks'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

