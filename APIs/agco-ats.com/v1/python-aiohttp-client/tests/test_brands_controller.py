# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError


pytestmark = pytest.mark.asyncio

async def test_brands_brands(client):
    """Test case for brands_brands

    Gets a list of Brands.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Brands',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

