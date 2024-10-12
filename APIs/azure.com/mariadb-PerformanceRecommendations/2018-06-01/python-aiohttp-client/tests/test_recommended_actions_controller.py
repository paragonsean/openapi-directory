# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recommendation_action import RecommendationAction
from openapi_server.models.recommendation_actions_result_list import RecommendationActionsResultList


pytestmark = pytest.mark.asyncio

async def test_recommended_actions_get(client):
    """Test case for recommended_actions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMariaDB/servers/{server_name}/advisors/{advisor_name}/recommendedActions/{recommended_action_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', advisor_name='advisor_name_example', recommended_action_name='recommended_action_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommended_actions_list_by_server(client):
    """Test case for recommended_actions_list_by_server

    
    """
    params = [('api-version', 'api_version_example'),
                    ('sessionId', 'session_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMariaDB/servers/{server_name}/advisors/{advisor_name}/recommendedActions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', advisor_name='advisor_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

