# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tax_list import TaxList


pytestmark = pytest.mark.asyncio

async def test_tax_get(client):
    """Test case for tax_get

    Get List of Taxes configured in the Avaza account.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Tax',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

