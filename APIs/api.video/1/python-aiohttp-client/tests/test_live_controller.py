# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.live_stream import LiveStream
from openapi_server.models.live_stream_create_payload import LiveStreamCreatePayload
from openapi_server.models.live_stream_list_response import LiveStreamListResponse
from openapi_server.models.live_stream_update_payload import LiveStreamUpdatePayload
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_d_elete_live_streams_live_stream_id(client):
    """Test case for d_elete_live_streams_live_stream_id

    Delete a live stream
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/live-streams/{live_stream_id}'.format(live_stream_id='li400mYKSgQ6xs7taUeSaEKr'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_d_elete_live_streams_live_stream_id_thumbnail(client):
    """Test case for d_elete_live_streams_live_stream_id_thumbnail

    Delete a thumbnail
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/live-streams/{live_stream_id}/thumbnail'.format(live_stream_id='li400mYKSgQ6xs7taUeSaEKr'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_live_streams(client):
    """Test case for g_et_live_streams

    List all live streams
    """
    params = [('streamKey', '30087931-229e-42cf-b5f9-e91bcc1f7332'),
                    ('name', 'My Video'),
                    ('sortBy', 'createdAt'),
                    ('sortOrder', 'desc'),
                    ('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/live-streams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_live_streams_live_stream_id(client):
    """Test case for g_et_live_streams_live_stream_id

    Show live stream
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/live-streams/{live_stream_id}'.format(live_stream_id='li400mYKSgQ6xs7taUeSaEKr'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_atch_live_streams_live_stream_id(client):
    """Test case for p_atch_live_streams_live_stream_id

    Update a live stream
    """
    body = openapi_server.LiveStreamUpdatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/live-streams/{live_stream_id}'.format(live_stream_id='li400mYKSgQ6xs7taUeSaEKr'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_live_streams(client):
    """Test case for p_ost_live_streams

    Create live stream
    """
    body = openapi_server.LiveStreamCreatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/live-streams',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_live_streams_live_stream_id_thumbnail(client):
    """Test case for p_ost_live_streams_live_stream_id_thumbnail

    Upload a thumbnail
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/live-streams/{live_stream_id}/thumbnail'.format(live_stream_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

