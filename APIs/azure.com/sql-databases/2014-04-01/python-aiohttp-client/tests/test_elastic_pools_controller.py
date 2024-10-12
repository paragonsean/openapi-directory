# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database import Database


pytestmark = pytest.mark.asyncio

async def test_databases_get_by_elastic_pool(client):
    """Test case for databases_get_by_elastic_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}/databases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

