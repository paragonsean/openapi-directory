# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_validation200_response import EmailValidation200Response
from openapi_server.models.email_validation400_response import EmailValidation400Response


pytestmark = pytest.mark.asyncio

async def test_email_validation(client):
    """Test case for email_validation

    Email Validation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/json/email/{your_api_key_here}/{user_email_here}'.format(your_api_key_here='asd24#sdfs322#', user_email_here='example@example.com'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

