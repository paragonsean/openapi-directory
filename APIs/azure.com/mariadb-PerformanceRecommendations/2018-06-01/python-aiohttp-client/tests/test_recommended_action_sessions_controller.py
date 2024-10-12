# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_create_recommended_action_session(client):
    """Test case for create_recommended_action_session

    
    """
    params = [('api-version', 'api_version_example'),
                    ('databaseName', 'database_name_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforMariaDB/servers/{server_name}/advisors/{advisor_name}/createRecommendedActionSession'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', advisor_name='advisor_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

