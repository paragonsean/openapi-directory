# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.convertcurrency200_response import Convertcurrency200Response


pytestmark = pytest.mark.asyncio

async def test_convertcurrency(client):
    """Test case for convertcurrency

    Converts amount in one currency to that of another
    """
    params = [('license', 'license_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example'),
                    ('amount', 'amount_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/convertcurrency',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

