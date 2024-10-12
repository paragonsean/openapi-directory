# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getglobalnumberinfo200_response import Getglobalnumberinfo200Response


pytestmark = pytest.mark.asyncio

async def test_getglobalnumberinfo(client):
    """Test case for getglobalnumberinfo

    Get demographic information for a global telephone number
    """
    params = [('license', 'license_example'),
                    ('intlnumber', 'intlnumber_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getglobalnumberinfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

