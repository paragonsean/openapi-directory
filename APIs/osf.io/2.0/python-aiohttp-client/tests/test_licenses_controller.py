# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.license import License


pytestmark = pytest.mark.asyncio

async def test_license_list(client):
    """Test case for license_list

    List all licenses
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/licenses/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_licenses_read(client):
    """Test case for licenses_read

    Retrieve a license
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/license/{license_id}'.format(license_id='license_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

