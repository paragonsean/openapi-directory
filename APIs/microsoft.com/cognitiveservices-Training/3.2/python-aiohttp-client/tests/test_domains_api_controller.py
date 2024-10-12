# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.domain import Domain


pytestmark = pytest.mark.asyncio

async def test_get_domain(client):
    """Test case for get_domain

    Get information about a specific domain.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/domains/{domain_id}'.format(domain_id='b30a91ae-e3c1-4f73-a81e-c270bff27c39'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domains(client):
    """Test case for get_domains

    Get a list of the available domains.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v3.2/training/domains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

