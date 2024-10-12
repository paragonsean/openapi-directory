# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.conversation_rate import ConversationRate
from openapi_server.models.currency import Currency
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_conversion_rate(client):
    """Test case for get_conversion_rate

    Get currencies exchange rate.
    """
    params = [('from', openapi_server.Currency()),
                    ('to', openapi_server.Currency())]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/currencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

