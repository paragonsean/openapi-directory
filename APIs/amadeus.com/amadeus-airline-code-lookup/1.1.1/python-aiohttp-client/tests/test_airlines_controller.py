# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success_things import SuccessThings


pytestmark = pytest.mark.asyncio

async def test_getairlines(client):
    """Test case for getairlines

    Return airlines information.
    """
    params = [('airlineCodes', 'BA')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/airlines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

