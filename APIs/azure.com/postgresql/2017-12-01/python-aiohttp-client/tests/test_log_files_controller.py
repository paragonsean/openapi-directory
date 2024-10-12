# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.log_file_list_result import LogFileListResult


pytestmark = pytest.mark.asyncio

async def test_log_files_list_by_server(client):
    """Test case for log_files_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DBforPostgreSQL/servers/{server_name}/logFiles'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

