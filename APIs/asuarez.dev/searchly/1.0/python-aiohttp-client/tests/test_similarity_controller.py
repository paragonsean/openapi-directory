# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response_similarity import APIResponseSimilarity
from openapi_server.models.src_searchly_api_v1_controllers_similarity_by_content_request import SrcSearchlyApiV1ControllersSimilarityByContentRequest


pytestmark = pytest.mark.asyncio

async def test_src_searchly_api_v1_controllers_similarity_by_content(client):
    """Test case for src_searchly_api_v1_controllers_similarity_by_content

    API endpoint to search similarity using content
    """
    body = openapi_server.SrcSearchlyApiV1ControllersSimilarityByContentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/similarity/by_content',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_src_searchly_api_v1_controllers_similarity_by_song(client):
    """Test case for src_searchly_api_v1_controllers_similarity_by_song

    API endpoint to search similarity using a song identifier
    """
    params = [('song_id', 234)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/similarity/by_song',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

