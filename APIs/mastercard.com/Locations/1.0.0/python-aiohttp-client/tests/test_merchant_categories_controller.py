# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.categories_response import CategoriesResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_merchants_v1_category_get(client):
    """Test case for merchants_v1_category_get

    Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/merchants/v1/category',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

