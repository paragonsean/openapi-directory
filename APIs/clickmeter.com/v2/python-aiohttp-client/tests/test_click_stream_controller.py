# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_responses_entities_response_api_core_dto_click_stream_hit import ApiCoreResponsesEntitiesResponseApiCoreDtoClickStreamHit


pytestmark = pytest.mark.asyncio

async def test_click_stream_get(client):
    """Test case for click_stream_get

    Retrieve the latest list of events of this account. Limited to last 100.
    """
    params = [('group', 56),
                    ('datapoint', 56),
                    ('conversion', 56),
                    ('pageSize', 50),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/clickstream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

