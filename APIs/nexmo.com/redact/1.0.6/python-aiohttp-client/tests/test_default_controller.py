# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_invalid_id import ErrorInvalidId
from openapi_server.models.error_throttled import ErrorThrottled
from openapi_server.models.error_unauthorized import ErrorUnauthorized
from openapi_server.models.redact_message403_response import RedactMessage403Response
from openapi_server.models.redact_message422_response import RedactMessage422Response
from openapi_server.models.redact_transaction import RedactTransaction


pytestmark = pytest.mark.asyncio

async def test_redact_message(client):
    """Test case for redact_message

    Redact a specific message
    """
    body = {"product":"sms","id":"209ab3c7536542b91e8b5aef032f6861","type":"outbound"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/redact/transaction',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

