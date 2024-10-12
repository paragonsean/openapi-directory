# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apple_pay_session_request import ApplePaySessionRequest
from openapi_server.models.apple_pay_session_response import ApplePaySessionResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.utility_request import UtilityRequest
from openapi_server.models.utility_response import UtilityResponse


pytestmark = pytest.mark.asyncio

async def test_post_apple_pay_sessions(client):
    """Test case for post_apple_pay_sessions

    Get an Apple Pay session
    """
    body = {"merchantIdentifier":"merchantIdentifier","displayName":"displayName","domainName":"domainName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v49/applePay/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_origin_keys(client):
    """Test case for post_origin_keys

    Create originKey values for domains
    """
    body = {"originDomains":["originDomains","originDomains"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v49/originKeys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

