# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branding_options import BrandingOptions


pytestmark = pytest.mark.asyncio

async def test_get_branding_css(client):
    """Test case for get_branding_css

    Gets branding css.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Branding/Css',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_branding_css2(client):
    """Test case for get_branding_css2

    Gets branding css.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Branding/Css.css',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_branding_options(client):
    """Test case for get_branding_options

    Gets branding configuration.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Branding/Configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

