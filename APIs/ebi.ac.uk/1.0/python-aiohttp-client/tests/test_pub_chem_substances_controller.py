# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pubchem_substances import PubchemSubstances


pytestmark = pytest.mark.asyncio

async def test_get_substances_using_get(client):
    """Test case for get_substances_using_get

    Get pubchem substances
    """
    params = [('cid', ['cid_example']),
                    ('limit', 10),
                    ('page', 0),
                    ('sid', ['sid_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/pubchem/substances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

