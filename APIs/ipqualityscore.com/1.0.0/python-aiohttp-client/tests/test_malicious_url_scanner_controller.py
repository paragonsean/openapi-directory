# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_validation400_response import EmailValidation400Response
from openapi_server.models.malicious_url_scanner200_response import MaliciousUrlScanner200Response


pytestmark = pytest.mark.asyncio

async def test_malicious_url_scanner(client):
    """Test case for malicious_url_scanner

    Malicious URL Scanner
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/json/url/{your_api_key_here}/{url_here}'.format(your_api_key_here='asd24#sdfs322#', url_here='https%3A%2F%2Fgoogle.com'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

