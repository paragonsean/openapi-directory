# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.about import About
from openapi_server.models.ec import Ec


pytestmark = pytest.mark.asyncio

async def test_about_get(client):
    """Test case for about_get

    Metadata about this API&#58; version number, release date and available languages.  Metadata requests are NOT billed. 
    """
    params = [('outputFormat', 'output_format_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/about',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ec_get(client):
    """Test case for ec_get

    The entropy calculator - alias ec -, analyzes a password and calculates its entropy.  Entropy calculator requests are billed. 
    """
    params = [('password', 'password_example'),
                    ('outputFormat', 'output_format_example'),
                    ('penalty', 3.4),
                    ('reqId', 'req_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/ec',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

