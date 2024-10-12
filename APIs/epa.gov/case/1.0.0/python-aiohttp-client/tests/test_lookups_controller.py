# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_lookups_icis_law_sections_get200_response import RestLookupsIcisLawSectionsGet200Response


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_icis_law_sections_get(client):
    """Test case for rest_lookups_icis_law_sections_get

    ECHO ICIS Law Sections Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('statute_code', 'statute_code_example'),
                    ('status_flag', 'status_flag_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example'),
                    ('sort_order', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.icis_law_sections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_icis_law_sections_post(client):
    """Test case for rest_lookups_icis_law_sections_post

    ECHO ICIS Law Sections Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'statute_code': 'statute_code_example',
        'status_flag': 'status_flag_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example',
        'sort_order': 3.4
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.icis_law_sections',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

