# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.computer_vision_image_create_response import ComputerVisionImageCreateResponse
from openapi_server.models.get_keywords_asset_id_parameter import GetKeywordsAssetIdParameter
from openapi_server.models.image_create_request import ImageCreateRequest
from openapi_server.models.image_create_response import ImageCreateResponse
from openapi_server.models.image_search_results import ImageSearchResults
from openapi_server.models.keyword_data_list import KeywordDataList
from openapi_server.models.language import Language
from openapi_server.models.video_search_results import VideoSearchResults


pytestmark = pytest.mark.asyncio

async def test_get_keywords(client):
    """Test case for get_keywords

    List suggested keywords
    """
    params = [('asset_id', openapi_server.GetKeywordsAssetIdParameter())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/cv/keywords',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_images(client):
    """Test case for get_similar_images

    List similar images
    """
    params = [('asset_id', 'U6ba16262e3bc2db470b8e3cfa8aaab25'),
                    ('license', ["commercial"]),
                    ('safe', True),
                    ('language', openapi_server.Language()),
                    ('page', 1),
                    ('per_page', 20),
                    ('view', minimal)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/cv/similar/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_similar_videos(client):
    """Test case for get_similar_videos

    List similar videos
    """
    params = [('asset_id', 'U6ba16262e3bc2db470b8e3cfa8aaab25'),
                    ('license', ["commercial"]),
                    ('safe', True),
                    ('language', openapi_server.Language()),
                    ('page', 1),
                    ('per_page', 20),
                    ('view', minimal)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/cv/similar/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_ephemeral_image(client):
    """Test case for upload_ephemeral_image

    Upload ephemeral images
    """
    body = {"base64_image":"R0lGODlhgACAAPcAAEwiBLyaLOzNUNmWFNjOrNSuN7x6PPzqeOTMgfKSDMyuTPzwsdi2dHwuBPzbVu"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/images',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_image(client):
    """Test case for upload_image

    Upload images
    """
    body = {"base64_image":"R0lGODlhgACAAPcAAEwiBLyaLOzNUNmWFNjOrNSuN7x6PPzqeOTMgfKSDMyuTPzwsdi2dHwuBPzbVu"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/cv/images',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

