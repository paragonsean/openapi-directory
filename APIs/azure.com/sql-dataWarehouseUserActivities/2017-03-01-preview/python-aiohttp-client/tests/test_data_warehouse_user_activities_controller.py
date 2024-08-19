# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_warehouse_user_activities import DataWarehouseUserActivities


pytestmark = pytest.mark.asyncio

async def test_data_warehouse_user_activities_get(client):
    """Test case for data_warehouse_user_activities_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/dataWarehouseUserActivities/{data_warehouse_user_activity_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', data_warehouse_user_activity_name='data_warehouse_user_activity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

