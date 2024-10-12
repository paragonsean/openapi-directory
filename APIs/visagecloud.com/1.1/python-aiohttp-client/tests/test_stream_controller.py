# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_response import RestResponse


pytestmark = pytest.mark.asyncio

async def test_add_stream_using_post(client):
    """Test case for add_stream_using_post

    Create new stream with given name
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('name', 'name_example'),
                    ('url', 'url_example'),
                    ('method', WEBRTC_PUSH),
                    ('username', 'username_example'),
                    ('password', 'password_example'),
                    ('skipFramesWithNoFaces', True),
                    ('retentionTime', 605000),
                    ('storeOriginalFrames', False),
                    ('storeAttendanceFaces', False),
                    ('storeAttendanceFrames', False),
                    ('isActive', False),
                    ('associatedCollections', ['associated_collections_example']),
                    ('attributes', 'attributes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/stream/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cleanup_stream_using_patch(client):
    """Test case for cleanup_stream_using_patch

    Cleanup frames older than specified timeframe
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamId', 'stream_id_example'),
                    ('interval', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/rest/v1.1/stream/cleanup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_frame_image_using_get(client):
    """Test case for get_frame_image_using_get

    Get individual frame image
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamId', 'stream_id_example'),
                    ('timestamp', 56)]
    headers = { 
        'Accept': 'image/jpeg',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/stream/frameImage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_n_attedance_using_get(client):
    """Test case for get_last_n_attedance_using_get

    Get last N recognized individuals from stream
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamIds', ['stream_ids_example']),
                    ('count', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/stream/attendance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_n_frames_using_get(client):
    """Test case for get_last_n_frames_using_get

    Get last processed N frames from stream
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamId', 'stream_id_example'),
                    ('count', 10),
                    ('collectionId', 'collection_id_example'),
                    ('labels', ['labels_example']),
                    ('attributeFilters', ['attribute_filters_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/stream/frames',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stream_using_get(client):
    """Test case for get_stream_using_get

    Get an existing stream with a given ID
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/stream/{stream_id}'.format(stream_id='stream_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_stream_using_delete(client):
    """Test case for remove_stream_using_delete

    Delete existing stream
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/stream/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_stream_using_patch(client):
    """Test case for start_stream_using_patch

    Start existing stream
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamId', 'stream_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/rest/v1.1/stream/start',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_stream_using_patch(client):
    """Test case for stop_stream_using_patch

    Stop existing stream
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamId', 'stream_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/rest/v1.1/stream/stop',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_streams_by_account_using_get(client):
    """Test case for streams_by_account_using_get

    Show status of all streams from account
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/stream/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_stream_using_patch(client):
    """Test case for update_stream_using_patch

    Update an existing stream with a given ID
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('name', 'name_example'),
                    ('url', 'url_example'),
                    ('method', 'method_example'),
                    ('username', 'username_example'),
                    ('password', 'password_example'),
                    ('skipFramesWithNoFaces', True),
                    ('retentionTime', 56),
                    ('storeOriginalFrames', True),
                    ('storeAttendanceFaces', True),
                    ('storeAttendanceFrames', True),
                    ('isActive', True),
                    ('associatedCollections', ['associated_collections_example']),
                    ('attributes', 'attributes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/rest/v1.1/stream/{stream_id}'.format(stream_id='stream_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

