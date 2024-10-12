# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.graph_error import GraphError
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_signed_in_user_get(client):
    """Test case for signed_in_user_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/me'.format(tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_signed_in_user_list_owned_objects(client):
    """Test case for signed_in_user_list_owned_objects

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/me/ownedObjects'.format(tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

