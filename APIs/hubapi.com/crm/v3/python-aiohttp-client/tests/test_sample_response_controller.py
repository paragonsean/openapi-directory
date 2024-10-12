# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.integrator_card_payload_response import IntegratorCardPayloadResponse


pytestmark = pytest.mark.asyncio

async def test_get_crm_v3_extensions_cards_sample_response(client):
    """Test case for get_crm_v3_extensions_cards_sample_response

    Get sample card detail response
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/crm/v3/extensions/cards/sample-response',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

