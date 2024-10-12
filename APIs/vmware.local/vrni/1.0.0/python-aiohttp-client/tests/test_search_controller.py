# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.paged_list_response_with_time import PagedListResponseWithTime
from openapi_server.models.search_request import SearchRequest


pytestmark = pytest.mark.asyncio

async def test_search_entities(client):
    """Test case for search_entities

    Search entities
    """
    body = {"cursor":"cursor","filter":"filter","entity_type":"Group","size":0,"time_range":{"start_time":5,"end_time":1},"sort_by":{"field":"field","order":"ASC"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

