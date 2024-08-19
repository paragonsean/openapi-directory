# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.containers_messages_get200_response import ContainersMessagesGet200Response
from openapi_server.models.containers_version_get_info import ContainersVersionGetInfo


pytestmark = pytest.mark.asyncio

async def test_containers_messages_get(client):
    """Test case for containers_messages_get

    List messages for the user
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/messages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_version_get(client):
    """Test case for containers_version_get

    List latest API version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

