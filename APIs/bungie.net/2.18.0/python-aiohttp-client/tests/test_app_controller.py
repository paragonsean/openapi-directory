# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_get_application_api_usage200_response import AppGetApplicationApiUsage200Response
from openapi_server.models.app_get_bungie_applications200_response import AppGetBungieApplications200Response


pytestmark = pytest.mark.asyncio

async def test_app_get_application_api_usage(client):
    """Test case for app_get_application_api_usage

    
    """
    params = [('end', '2013-10-20T19:20:30+01:00'),
                    ('start', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/App/ApiUsage/{application_id}'.format(application_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_get_bungie_applications(client):
    """Test case for app_get_bungie_applications

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/App/FirstParty/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

