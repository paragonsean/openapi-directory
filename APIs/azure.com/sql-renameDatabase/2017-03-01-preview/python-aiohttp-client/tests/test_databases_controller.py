# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_move_definition import ResourceMoveDefinition


pytestmark = pytest.mark.asyncio

async def test_databases_rename(client):
    """Test case for databases_rename

    
    """
    parameters = {"id":"id"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/move'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

