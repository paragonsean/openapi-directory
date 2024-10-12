# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.get_tracking_snippet200_response import GetTrackingSnippet200Response


pytestmark = pytest.mark.asyncio

async def test_get_tracking_snippet(client):
    """Test case for get_tracking_snippet

    Get snippet for a website
    """
    params = [('domain', 'domain_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/tracking/snippet',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

