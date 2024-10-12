# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getemailinfo200_response import Getemailinfo200Response


pytestmark = pytest.mark.asyncio

async def test_getemailinfo(client):
    """Test case for getemailinfo

    Gets email validation information for an email address
    """
    params = [('license', 'license_example'),
                    ('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getemailinfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

