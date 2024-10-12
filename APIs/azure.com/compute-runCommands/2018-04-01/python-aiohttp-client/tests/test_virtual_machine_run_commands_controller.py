# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.run_command_document import RunCommandDocument
from openapi_server.models.run_command_list_result import RunCommandListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_run_commands_get(client):
    """Test case for virtual_machine_run_commands_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/runCommands/{command_id}'.format(location='location_example', command_id='command_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_run_commands_list(client):
    """Test case for virtual_machine_run_commands_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/runCommands'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

