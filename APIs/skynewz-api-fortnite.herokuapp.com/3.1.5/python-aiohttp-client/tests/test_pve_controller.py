# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_pve_info_get(client):
    """Test case for pve_info_get

    Get Fortnite PVE Info (storm, etc)
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pve/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pve_user_username_get(client):
    """Test case for pve_user_username_get

    Get PVE Stat by given username
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/pve/user/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

