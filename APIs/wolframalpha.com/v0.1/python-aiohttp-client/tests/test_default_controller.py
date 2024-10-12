# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_wolfram_alpha_results(client):
    """Test case for get_wolfram_alpha_results

    Get Wolfram|Alpha results
    """
    params = [('input', 'input_example')]
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/llm-api',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wolfram_cloud_results(client):
    """Test case for get_wolfram_cloud_results

    Evaluate Wolfram Language code
    """
    params = [('input', 'input_example')]
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cloud-plugin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

