# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.segment import Segment


pytestmark = pytest.mark.asyncio

async def test_api_v2_segments_get(client):
    """Test case for api_v2_segments_get

    Returns the segments matching the query parameters.
    """
    params = [('episodeId', 56),
                    ('segmentNumber', 56),
                    ('pageStart', 0),
                    ('pageSize', 500),
                    ('orderById', 'order_by_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/segments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_segments_id_content_get(client):
    """Test case for api_v2_segments_id_content_get

    UNDER DEVELOPMENT - Returns the audio content segment matching the given ID.
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/segments/{id}/content'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_segments_id_delete(client):
    """Test case for api_v2_segments_id_delete

    Deletes the segment with the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/segments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_segments_id_get(client):
    """Test case for api_v2_segments_id_get

    Returns the segment matching the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/segments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_api_v2_segments_post(client):
    """Test case for api_v2_segments_post

    Creates a new segment.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'cd_drive_uri': 'cd_drive_uri_example',
        'episode_id': 56,
        'in_cue': 'in_cue_example',
        'out_cue': 'out_cue_example',
        'segment_number': 56
        }
    response = await client.request(
        method='POST',
        path='/api/v2/segments',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

