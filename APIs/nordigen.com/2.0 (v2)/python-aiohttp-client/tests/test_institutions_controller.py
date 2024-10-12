# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.integration import Integration
from openapi_server.models.integration_retrieve import IntegrationRetrieve


pytestmark = pytest.mark.asyncio

async def test_retrieve_all_supported_institutions_in_a_given_country(client):
    """Test case for retrieve_all_supported_institutions_in_a_given_country

    
    """
    params = [('country', 'AT'),
                    ('payments_enabled', 'false')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/institutions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_institution(client):
    """Test case for retrieve_institution

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/institutions/{id}'.format(id='N26_NTSBDEB1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

