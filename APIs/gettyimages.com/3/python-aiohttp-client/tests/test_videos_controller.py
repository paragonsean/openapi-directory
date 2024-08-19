# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_download_history_results import AssetDownloadHistoryResults
from openapi_server.models.associated_video_detail_field_values import AssociatedVideoDetailFieldValues
from openapi_server.models.video_detail_field_values import VideoDetailFieldValues


pytestmark = pytest.mark.asyncio

async def test_v3_videos_get(client):
    """Test case for v3_videos_get

    Get metadata for multiple videos by supplying multiple video ids
    """
    params = [('ids', ['ids_example']),
                    ('fields', [openapi_server.VideoDetailFieldValues()])]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_videos_id_downloadhistory_get(client):
    """Test case for v3_videos_id_downloadhistory_get

    Returns information about a customer's download history for a specific asset
    """
    params = [('company_downloads', True)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/videos/{id}/downloadhistory'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_videos_id_get(client):
    """Test case for v3_videos_id_get

    Get metadata for a single video by supplying one video id
    """
    params = [('fields', [openapi_server.VideoDetailFieldValues()])]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/videos/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_videos_id_same_series_get(client):
    """Test case for v3_videos_id_same_series_get

    Retrieve creative videos from the same series
    """
    params = [('fields', [openapi_server.AssociatedVideoDetailFieldValues()]),
                    ('page', 1),
                    ('page_size', 30)]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/videos/{id}/same-series'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_videos_id_similar_get(client):
    """Test case for v3_videos_id_similar_get

    Retrieve similar videos
    """
    params = [('fields', [openapi_server.AssociatedVideoDetailFieldValues()]),
                    ('page', 1),
                    ('page_size', 30)]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/videos/{id}/similar'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

