# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.workspace_list import WorkspaceList


pytestmark = pytest.mark.asyncio

async def test_workspaces_list(client):
    """Test case for workspaces_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBI/workspaceCollections/{workspace_collection_name}/workspaces'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_collection_name='workspace_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

