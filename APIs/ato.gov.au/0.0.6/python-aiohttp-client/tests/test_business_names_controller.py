# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.business_name import BusinessName
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_business_names_get(client):
    """Test case for business_names_get

    Retrieve a list of business names
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/business-names',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

