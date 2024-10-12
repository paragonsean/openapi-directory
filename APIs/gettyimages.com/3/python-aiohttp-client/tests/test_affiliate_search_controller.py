# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.affiliate_image_search_response import AffiliateImageSearchResponse
from openapi_server.models.affiliate_search_style import AffiliateSearchStyle
from openapi_server.models.affiliate_video_search_response import AffiliateVideoSearchResponse


pytestmark = pytest.mark.asyncio

async def test_v3_affiliates_search_images_get(client):
    """Test case for v3_affiliates_search_images_get

    
    """
    params = [('phrase', 'phrase_example'),
                    ('style', openapi_server.AffiliateSearchStyle())]
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
        path='/v3/affiliates/search/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_affiliates_search_videos_get(client):
    """Test case for v3_affiliates_search_videos_get

    
    """
    params = [('phrase', 'phrase_example')]
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
        path='/v3/affiliates/search/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

