# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.get_compay_settings_list200_response import GetCompaySettingsList200Response


pytestmark = pytest.mark.asyncio

async def test_get_compay_settings_list(client):
    """Test case for get_compay_settings_list

    Get a list of company settings
    """
    params = [('name', 'name_example'),
                    ('description', 'description_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/company_settings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

