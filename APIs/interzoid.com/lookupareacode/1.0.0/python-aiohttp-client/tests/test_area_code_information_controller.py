# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getareacode200_response import Getareacode200Response


pytestmark = pytest.mark.asyncio

async def test_getareacode(client):
    """Test case for getareacode

    Gets telephone area code information
    """
    params = [('license', 'license_example'),
                    ('areacode', 'areacode_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getareacode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

