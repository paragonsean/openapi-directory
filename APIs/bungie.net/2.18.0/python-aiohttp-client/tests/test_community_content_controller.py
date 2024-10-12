# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.community_content_get_community_content200_response import CommunityContentGetCommunityContent200Response


pytestmark = pytest.mark.asyncio

async def test_community_content_get_community_content(client):
    """Test case for community_content_get_community_content

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/CommunityContent/Get/{sort}/{media_filter}/{page}'.format(media_filter=56, page=56, sort=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

