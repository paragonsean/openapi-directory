# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advisor import Advisor


pytestmark = pytest.mark.asyncio

async def test_find_advisor_by_id(client):
    """Test case for find_advisor_by_id

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/advisors/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

