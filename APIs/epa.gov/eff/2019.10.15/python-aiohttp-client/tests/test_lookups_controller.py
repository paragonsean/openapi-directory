# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_lookups_cwa_parameters_get200_response import RestLookupsCwaParametersGet200Response


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_cwa_parameters_get(client):
    """Test case for rest_lookups_cwa_parameters_get

    ECHO CWA Parameter Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.cwa_parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_cwa_parameters_post(client):
    """Test case for rest_lookups_cwa_parameters_post

    ECHO CWA Parameter Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.cwa_parameters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

