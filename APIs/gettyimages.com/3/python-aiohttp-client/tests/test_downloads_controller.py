# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.download_file_type import DownloadFileType
from openapi_server.models.get_downloads_response import GetDownloadsResponse
from openapi_server.models.premium_access_download_data import PremiumAccessDownloadData
from openapi_server.models.product_type_for_downloads import ProductTypeForDownloads


pytestmark = pytest.mark.asyncio

async def test_v3_downloads_get(client):
    """Test case for v3_downloads_get

    Returns information about a customer's downloaded assets.
    """
    params = [('date_from', '2013-10-20T19:20:30+01:00'),
                    ('date_to', '2013-10-20T19:20:30+01:00'),
                    ('use_time', False),
                    ('page', 1),
                    ('page_size', 30),
                    ('product_type', openapi_server.ProductTypeForDownloads()),
                    ('company_downloads', False)]
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
        path='/v3/downloads',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_downloads_images_id_post(client):
    """Test case for v3_downloads_images_id_post

    Download an image
    """
    body = {"download_notes":"download_notes","project_code":"project_code"}
    params = [('auto_download', True),
                    ('file_type', openapi_server.DownloadFileType()),
                    ('height', 'height_example'),
                    ('product_id', 56),
                    ('product_type', openapi_server.ProductTypeForDownloads()),
                    ('use_team_credits', False)]
    headers = { 
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/downloads/images/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_downloads_videos_id_post(client):
    """Test case for v3_downloads_videos_id_post

    Download a video
    """
    body = {"download_notes":"download_notes","project_code":"project_code"}
    params = [('auto_download', False),
                    ('size', 'size_example'),
                    ('product_id', 56),
                    ('product_type', openapi_server.ProductTypeForDownloads()),
                    ('use_team_credits', True)]
    headers = { 
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/downloads/videos/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

