# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_request import AvailabilityRequest
from openapi_server.models.availability_results import AvailabilityResults
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_wayback_v1_available_get(client):
    """Test case for wayback_v1_available_get

    
    """
    params = [('url', 'url_example'),
                    ('timestamp', 'timestamp_example'),
                    ('callback', 'param_callback_example'),
                    ('timeout', 5),
                    ('closest', either),
                    ('status_code', 56),
                    ('tag', 'tag_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/wayback/v1/available',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_wayback_v1_available_post(client):
    """Test case for wayback_v1_available_post

    
    """
    body = {"tag":"tag","url":"url","closest":"either","timestamp":"timestamp"}
    params = [('url', 'url_example'),
                    ('timestamp', 'timestamp_example'),
                    ('callback', 'param_callback_example'),
                    ('timeout', 5),
                    ('closest', either),
                    ('status_code', 56),
                    ('tag', 'tag_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/wayback/v1/available',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

