# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.download_history_data_list import DownloadHistoryDataList
from openapi_server.models.editorial_video_category_results import EditorialVideoCategoryResults
from openapi_server.models.editorial_video_content import EditorialVideoContent
from openapi_server.models.editorial_video_search_results import EditorialVideoSearchResults
from openapi_server.models.license_editorial_content_results import LicenseEditorialContentResults
from openapi_server.models.license_editorial_video_content_request import LicenseEditorialVideoContentRequest


pytestmark = pytest.mark.asyncio

async def test_get_editorial_video(client):
    """Test case for get_editorial_video

    Get editorial video content details
    """
    params = [('country', 'USA'),
                    ('search_id', '00000000-0000-0000-0000-000000000000')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/videos/{id}'.format(id='9926131a'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_editorial_video_license_list(client):
    """Test case for get_editorial_video_license_list

    List editorial video licenses
    """
    params = [('video_id', '12345678'),
                    ('license', 'premier_editorial_all_media'),
                    ('page', 1),
                    ('per_page', 20),
                    ('sort', newest),
                    ('username', 'aUniqueUsername'),
                    ('start_date', '2021-03-29T13:25:13.521Z'),
                    ('end_date', '2021-03-29T13:25:13.521Z'),
                    ('download_availability', all),
                    ('team_history', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/videos/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_license_editorial_video(client):
    """Test case for license_editorial_video

    License editorial video content
    """
    body = {"country":"USA","editorial":[{"editorial_id":"10679854a","license":"premier_editorial_video_digital_only","metadata":{"purchase_order":"12345"},"size":"original"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/editorial/videos/licenses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_editorial_video_categories(client):
    """Test case for list_editorial_video_categories

    List editorial video categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/videos/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_editorial_videos(client):
    """Test case for search_editorial_videos

    Search editorial video content
    """
    params = [('query', 'The Academy Awards'),
                    ('sort', relevant),
                    ('category', 'Alone,Performing'),
                    ('country', 'USA'),
                    ('supplier_code', ['supplier_code_example']),
                    ('date_start', '2020-05-29'),
                    ('date_end', '2021-05-29'),
                    ('resolution', '4k'),
                    ('fps', 24),
                    ('per_page', 20),
                    ('cursor', 'eyJ2IjoxLCJzIjoxfQ==')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/editorial/videos/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

