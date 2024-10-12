# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branding_conf import BrandingConf
from openapi_server.models.get_branding_conf200_response import GetBrandingConf200Response
from openapi_server.models.update_b_randing_conf200_response import UpdateBRandingConf200Response


pytestmark = pytest.mark.asyncio

async def test_get_branding_conf(client):
    """Test case for get_branding_conf

    Get branding configuration
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/branding',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_branding_conf(client):
    """Test case for reload_branding_conf

    Reload branding file
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/branding/reload',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_b_randing_conf(client):
    """Test case for update_b_randing_conf

    Update web interface customization
    """
    body = openapi_server.BrandingConf()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/branding',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

