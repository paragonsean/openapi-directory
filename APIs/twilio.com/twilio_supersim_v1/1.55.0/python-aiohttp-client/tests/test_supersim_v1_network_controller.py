# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_network_response import ListNetworkResponse
from openapi_server.models.supersim_v1_network import SupersimV1Network


pytestmark = pytest.mark.asyncio

async def test_fetch_network(client):
    """Test case for fetch_network

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Networks/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_network(client):
    """Test case for list_network

    
    """
    params = [('IsoCountry', 'iso_country_example'),
                    ('Mcc', 'mcc_example'),
                    ('Mnc', 'mnc_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Networks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

