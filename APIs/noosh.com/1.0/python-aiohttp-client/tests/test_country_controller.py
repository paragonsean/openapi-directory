# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country_list_vo import CountryListVO
from openapi_server.models.http_status_vo import HTTPStatusVO


pytestmark = pytest.mark.asyncio

async def test_get_country_list(client):
    """Test case for get_country_list

    List all countries
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

