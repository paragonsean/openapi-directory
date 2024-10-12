# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_contact_request_body import CheckContactRequestBody
from openapi_server.models.check_contact_response import CheckContactResponse


pytestmark = pytest.mark.asyncio

async def test_check_contact(client):
    """Test case for check_contact

    Check-Contact
    """
    body = {"blocking":"wait","contacts":["{{Recipient-WA-ID}}"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/contacts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

