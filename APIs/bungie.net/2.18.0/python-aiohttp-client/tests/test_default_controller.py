# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_available_locales200_response import GetAvailableLocales200Response
from openapi_server.models.get_common_settings200_response import GetCommonSettings200Response
from openapi_server.models.get_global_alerts200_response import GetGlobalAlerts200Response
from openapi_server.models.get_user_system_overrides200_response import GetUserSystemOverrides200Response


pytestmark = pytest.mark.asyncio

async def test_get_available_locales(client):
    """Test case for get_available_locales

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GetAvailableLocales/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_common_settings(client):
    """Test case for get_common_settings

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Settings/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_global_alerts(client):
    """Test case for get_global_alerts

    
    """
    params = [('includestreaming', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GlobalAlerts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_system_overrides(client):
    """Test case for get_user_system_overrides

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/UserSystemOverrides/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

