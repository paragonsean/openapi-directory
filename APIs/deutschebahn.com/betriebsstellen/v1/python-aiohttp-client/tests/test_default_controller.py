# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.station import Station


pytestmark = pytest.mark.asyncio

async def test_betriebsstellen_abbrev_get(client):
    """Test case for betriebsstellen_abbrev_get

    Get information about a specific station or stop by abbrevation
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/betriebsstellen/v1/betriebsstellen/{abbrev}'.format(abbrev='abbrev_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_betriebsstellen_get(client):
    """Test case for betriebsstellen_get

    Get information of stations matching a given text
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/betriebsstellen/v1/betriebsstellen',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

