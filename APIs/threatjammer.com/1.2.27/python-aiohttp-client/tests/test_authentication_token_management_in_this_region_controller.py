# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_collection_output import ActivityCollectionOutput
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.token_output import TokenOutput


pytestmark = pytest.mark.asyncio

async def test_query_token_activity_v1_token_activity_get(client):
    """Test case for query_token_activity_v1_token_activity_get

    Get the activity information of the token in the region.
    """
    params = [('page', 1),
                    ('page_size', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/token/activity',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_token_info_v1_token_get(client):
    """Test case for query_token_info_v1_token_get

    Get the information of the user's token in the region.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

