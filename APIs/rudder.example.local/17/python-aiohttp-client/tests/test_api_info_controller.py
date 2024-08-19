# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_general_informations200_response import ApiGeneralInformations200Response
from openapi_server.models.api_informations200_response import ApiInformations200Response
from openapi_server.models.api_sub_informations200_response import ApiSubInformations200Response


pytestmark = pytest.mark.asyncio

async def test_api_general_informations(client):
    """Test case for api_general_informations

    List all endoints
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_informations(client):
    """Test case for api_informations

    Get information about one API endpoint
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/info/details/{endpoint_name}'.format(endpoint_name='listAcceptedNodes'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_sub_informations(client):
    """Test case for api_sub_informations

    Get information on endpoint in a section
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/info/{section_id}'.format(section_id='nodes'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

