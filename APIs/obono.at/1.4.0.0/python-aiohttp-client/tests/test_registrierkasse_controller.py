# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.registrierkasse import Registrierkasse


pytestmark = pytest.mark.asyncio

async def test_get_dep(client):
    """Test case for get_dep

    
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/registrierkassen/{registrierkasse_uuid}/dep'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registrierkasse(client):
    """Test case for get_registrierkasse

    
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/registrierkassen/{registrierkasse_uuid}'.format(registrierkasse_uuid='registrierkasse_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

