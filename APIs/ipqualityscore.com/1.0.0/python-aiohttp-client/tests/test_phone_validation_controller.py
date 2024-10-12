# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_validation400_response import EmailValidation400Response
from openapi_server.models.phone_validation200_response import PhoneValidation200Response


pytestmark = pytest.mark.asyncio

async def test_phone_validation(client):
    """Test case for phone_validation

    Phone Validation
    """
    params = [('country', 'UK')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/json/phone/{your_api_key_here}/{user_phone_here}'.format(your_api_key_here='asd24#sdfs322#', user_phone_here='18007132618'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

