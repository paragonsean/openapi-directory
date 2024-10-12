# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getcompanymatch200_response import Getcompanymatch200Response


pytestmark = pytest.mark.asyncio

async def test_getcompanymatch(client):
    """Test case for getcompanymatch

    Gets a similarity key for matching purposes for company name data
    """
    params = [('license', 'license_example'),
                    ('company', 'company_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getcompanymatch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

