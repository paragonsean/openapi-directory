# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analytics200_response import Analytics200Response


pytestmark = pytest.mark.asyncio

async def test_analytics(client):
    """Test case for analytics

    
    """
    params = [('start', 'start_example'),
                    ('end', 'end_example'),
                    ('label', 'label_example'),
                    ('subaccounts', 'subaccounts_example'),
                    ('group_by', 'group_by_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/analytics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

