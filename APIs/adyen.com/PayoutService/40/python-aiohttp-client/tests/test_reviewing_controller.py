# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.modify_request import ModifyRequest
from openapi_server.models.modify_response import ModifyResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_confirm_third_party(client):
    """Test case for post_confirm_third_party

    Confirm a payout
    """
    body = {"originalReference":"originalReference","merchantAccount":"merchantAccount","additionalData":{"key":"additionalData"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payout/v40/confirmThirdParty',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_decline_third_party(client):
    """Test case for post_decline_third_party

    Cancel a payout
    """
    body = {"originalReference":"originalReference","merchantAccount":"merchantAccount","additionalData":{"key":"additionalData"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payout/v40/declineThirdParty',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

