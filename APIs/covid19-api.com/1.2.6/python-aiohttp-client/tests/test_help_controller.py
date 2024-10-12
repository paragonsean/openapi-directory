# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_list_of_countries200_response_inner import GetListOfCountries200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_list_of_countries(client):
    """Test case for get_list_of_countries

    getListOfCountries
    """
    params = [('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/help/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

