# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.authorization_error import AuthorizationError
from openapi_server.models.veteran_status_confirmation import VeteranStatusConfirmation
from openapi_server.models.veteran_status_request import VeteranStatusRequest


pytestmark = pytest.mark.asyncio

async def test_get_veteran_status(client):
    """Test case for get_veteran_status

    Get confirmation about an individual's Veteran status according to the VA
    """
    body = {"gender":"M","birth_date":"1965-01-01","last_name":"Doe","middle_name":"Theodore","first_name":"John","ssn":"555-55-5555"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/services/veteran_confirmation/v0/status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

