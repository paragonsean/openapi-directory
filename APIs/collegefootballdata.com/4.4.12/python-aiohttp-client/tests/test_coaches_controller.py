# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.coach import Coach


pytestmark = pytest.mark.asyncio

async def test_get_coaches(client):
    """Test case for get_coaches

    Coaching records and history
    """
    params = [('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example'),
                    ('team', 'team_example'),
                    ('year', 56),
                    ('minYear', 56),
                    ('maxYear', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/coaches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

