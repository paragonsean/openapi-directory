# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.repo_license import RepoLicense


pytestmark = pytest.mark.asyncio

async def test_get_v3_licenses(client):
    """Test case for get_v3_licenses

    Get the list of the available license template
    """
    params = [('popular', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_licenses_name(client):
    """Test case for get_v3_licenses_name

    Get the text for a specific license
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/licenses/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

