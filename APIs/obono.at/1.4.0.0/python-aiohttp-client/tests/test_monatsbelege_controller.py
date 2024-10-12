# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.monatsbeleg import Monatsbeleg


pytestmark = pytest.mark.asyncio

async def test_get_monatsbelege(client):
    """Test case for get_monatsbelege

    
    """
    params = [('year', 56),
                    ('month', 56)]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/registrierkassen/{registrierkasse_uuid}/monatsbelege'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

