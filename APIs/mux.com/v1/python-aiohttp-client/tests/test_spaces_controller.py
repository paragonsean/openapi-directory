# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.broadcast_response import BroadcastResponse
from openapi_server.models.create_broadcast_request import CreateBroadcastRequest
from openapi_server.models.create_space_request import CreateSpaceRequest
from openapi_server.models.list_spaces_response import ListSpacesResponse
from openapi_server.models.space_response import SpaceResponse
from openapi_server.models.start_space_broadcast_response import StartSpaceBroadcastResponse
from openapi_server.models.stop_space_broadcast_response import StopSpaceBroadcastResponse


pytestmark = pytest.mark.asyncio

async def test_create_space(client):
    """Test case for create_space

    Create a space
    """
    body = {"passthrough":"passthrough","broadcasts":[{"layout":"gallery","background":"background","passthrough":"passthrough","live_stream_id":"live_stream_id","resolution":"1920x1080"},{"layout":"gallery","background":"background","passthrough":"passthrough","live_stream_id":"live_stream_id","resolution":"1920x1080"}],"type":"server"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/spaces',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_space_broadcast(client):
    """Test case for create_space_broadcast

    Create a space broadcast
    """
    body = {"layout":"gallery","background":"background","passthrough":"passthrough","live_stream_id":"live_stream_id","resolution":"1920x1080"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/spaces/{space_id}/broadcasts'.format(space_id='space_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_space(client):
    """Test case for delete_space

    Delete a space
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/spaces/{space_id}'.format(space_id='space_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_space_broadcast(client):
    """Test case for delete_space_broadcast

    Delete a space broadcast
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/spaces/{space_id}/broadcasts/{broadcast_id}'.format(space_id='space_id_example', broadcast_id='broadcast_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_space(client):
    """Test case for get_space

    Retrieve a space
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/spaces/{space_id}'.format(space_id='space_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_space_broadcast(client):
    """Test case for get_space_broadcast

    Retrieve space broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/spaces/{space_id}/broadcasts/{broadcast_id}'.format(space_id='space_id_example', broadcast_id='broadcast_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_spaces(client):
    """Test case for list_spaces

    List spaces
    """
    params = [('limit', 25),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/spaces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_space_broadcast(client):
    """Test case for start_space_broadcast

    Start a space broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/spaces/{space_id}/broadcasts/{broadcast_id}/start'.format(space_id='space_id_example', broadcast_id='broadcast_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_space_broadcast(client):
    """Test case for stop_space_broadcast

    Stop a space broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/spaces/{space_id}/broadcasts/{broadcast_id}/stop'.format(space_id='space_id_example', broadcast_id='broadcast_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

