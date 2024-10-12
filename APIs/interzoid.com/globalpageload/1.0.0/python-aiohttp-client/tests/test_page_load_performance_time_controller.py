# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.globalpageload200_response import Globalpageload200Response


pytestmark = pytest.mark.asyncio

async def test_globalpageload(client):
    """Test case for globalpageload

    Gets page load (or an API call) performance from a specified global geography such as Paris, Tokyo, Virginia, Mumbai, Frankfurt, London, Seoul, California, Sao Paolo, and many more.
    """
    params = [('license', 'license_example'),
                    ('origin', 'origin_example'),
                    ('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/globalpageload',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

