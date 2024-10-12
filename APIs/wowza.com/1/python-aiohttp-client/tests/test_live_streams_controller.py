# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_live_stream200_response import CreateLiveStream200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.live_stream_create_input import LiveStreamCreateInput
from openapi_server.models.live_stream_update_input import LiveStreamUpdateInput
from openapi_server.models.live_streams import LiveStreams
from openapi_server.models.regenerate_connection_code_live_stream200_response import RegenerateConnectionCodeLiveStream200Response
from openapi_server.models.reset_live_stream200_response import ResetLiveStream200Response
from openapi_server.models.show_live_stream_state200_response import ShowLiveStreamState200Response
from openapi_server.models.show_live_stream_stats200_response import ShowLiveStreamStats200Response
from openapi_server.models.show_live_stream_thumbnail_url200_response import ShowLiveStreamThumbnailUrl200Response
from openapi_server.models.start_live_stream200_response import StartLiveStream200Response


pytestmark = pytest.mark.asyncio

async def test_create_live_stream(client):
    """Test case for create_live_stream

    Create a live stream
    """
    live_stream = openapi_server.LiveStreamCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/live_streams',
        headers=headers,
        json=live_stream,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_live_stream(client):
    """Test case for delete_live_stream

    Delete a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/live_streams/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_live_streams(client):
    """Test case for list_live_streams

    Fetch all live streams
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/live_streams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regenerate_connection_code_live_stream(client):
    """Test case for regenerate_connection_code_live_stream

    Regenerate the connection code for a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/live_streams/{id}/regenerate_connection_code'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_live_stream(client):
    """Test case for reset_live_stream

    Reset a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/live_streams/{id}/reset'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_live_stream(client):
    """Test case for show_live_stream

    Fetch a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/live_streams/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_live_stream_state(client):
    """Test case for show_live_stream_state

    Fetch the state of a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/live_streams/{id}/state'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_live_stream_stats(client):
    """Test case for show_live_stream_stats

    Fetch metrics for an active live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/live_streams/{id}/stats'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_live_stream_thumbnail_url(client):
    """Test case for show_live_stream_thumbnail_url

    Fetch the thumbnail URL of a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/live_streams/{id}/thumbnail_url'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_live_stream(client):
    """Test case for start_live_stream

    Start a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/live_streams/{id}/start'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_live_stream(client):
    """Test case for stop_live_stream

    Stop a live stream
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/live_streams/{id}/stop'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_live_stream(client):
    """Test case for update_live_stream

    Update a live stream
    """
    live_stream = openapi_server.LiveStreamUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/live_streams/{id}'.format(id='id_example'),
        headers=headers,
        json=live_stream,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

