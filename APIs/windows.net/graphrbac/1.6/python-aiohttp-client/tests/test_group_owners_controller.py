# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.graph_error import GraphError


pytestmark = pytest.mark.asyncio

async def test_groups_list_owners(client):
    """Test case for groups_list_owners

    Directory objects that are owners of the group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/groups/{object_id}/owners'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

