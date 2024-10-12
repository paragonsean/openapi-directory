# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.subscription_definitions_response import SubscriptionDefinitionsResponse


pytestmark = pytest.mark.asyncio

async def test_get_communication_preferences_v3_definitions_get_page(client):
    """Test case for get_communication_preferences_v3_definitions_get_page

    Get subscription definitions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/communication-preferences/v3/definitions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

