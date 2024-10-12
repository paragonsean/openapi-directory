# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.interaction_list_result import InteractionListResult
from openapi_server.models.interaction_resource_format import InteractionResourceFormat
from openapi_server.models.suggest_relationship_links_response import SuggestRelationshipLinksResponse


pytestmark = pytest.mark.asyncio

async def test_interactions_create_or_update(client):
    """Test case for interactions_create_or_update

    
    """
    parameters = {"properties":{"participantProfiles":[{"role":"role","profileTypeName":"profileTypeName","displayName":{"key":"displayName"},"description":{"key":"description"},"participantPropertyReferences":[{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"},{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"}],"participantName":"participantName"},{"role":"role","profileTypeName":"profileTypeName","displayName":{"key":"displayName"},"description":{"key":"description"},"participantPropertyReferences":[{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"},{"profilePropertyName":"profilePropertyName","interactionPropertyName":"interactionPropertyName"}],"participantName":"participantName"}],"primaryParticipantProfilePropertyName":"primaryParticipantProfilePropertyName","dataSourcePrecedenceRules":[{"dataSource":{"name":"name","id":0,"dataSourceType":"Connector","dataSourceReferenceId":"dataSourceReferenceId","status":"None"},"precedence":6},{"dataSource":{"name":"name","id":0,"dataSourceType":"Connector","dataSourceReferenceId":"dataSourceReferenceId","status":"None"},"precedence":6}],"isActivity":True,"defaultDataSource":{"name":"name","id":0,"dataSourceType":"Connector","dataSourceReferenceId":"dataSourceReferenceId","status":"None"},"idPropertyNames":["idPropertyNames","idPropertyNames"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/interactions/{interaction_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', interaction_name='interaction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_interactions_get(client):
    """Test case for interactions_get

    
    """
    params = [('locale-code', 'en-us'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/interactions/{interaction_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', interaction_name='interaction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_interactions_list_by_hub(client):
    """Test case for interactions_list_by_hub

    
    """
    params = [('locale-code', 'en-us'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/interactions'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_interactions_suggest_relationship_links(client):
    """Test case for interactions_suggest_relationship_links

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/interactions/{interaction_name}/suggestRelationshipLinks'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', interaction_name='interaction_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

