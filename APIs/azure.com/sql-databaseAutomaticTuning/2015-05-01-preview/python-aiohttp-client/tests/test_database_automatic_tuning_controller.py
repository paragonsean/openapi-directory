# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database_automatic_tuning import DatabaseAutomaticTuning


pytestmark = pytest.mark.asyncio

async def test_database_automatic_tuning_get(client):
    """Test case for database_automatic_tuning_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/automaticTuning/current'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_automatic_tuning_update(client):
    """Test case for database_automatic_tuning_update

    
    """
    parameters = {"properties":{"desiredState":"Inherit","options":{"key":{"desiredState":"Off","actualState":"Off","reasonCode":0,"reasonDesc":"Default"}},"actualState":"Inherit"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/automaticTuning/current'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

