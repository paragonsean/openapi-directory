# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service import Service


pytestmark = pytest.mark.asyncio

async def test_all_lines(client):
    """Test case for all_lines

    Get all environments
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/lines',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_for_a_line(client):
    """Test case for services_for_a_line

    Get all services for an environment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/lines/{line}/services'.format(line='line_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

