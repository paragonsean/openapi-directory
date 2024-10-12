# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_content_filtering_request import UpdateNetworkContentFilteringRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_content_filtering(client):
    """Test case for get_network_content_filtering

    Return the content filtering settings for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/contentFiltering'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_content_filtering(client):
    """Test case for update_network_content_filtering

    Update the content filtering settings for an MX network
    """
    body = openapi_server.UpdateNetworkContentFilteringRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/contentFiltering'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

