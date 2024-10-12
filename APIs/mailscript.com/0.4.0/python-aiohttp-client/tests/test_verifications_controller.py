# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_verification_request import AddVerificationRequest
from openapi_server.models.add_verification_response import AddVerificationResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_verifications_response import GetAllVerificationsResponse
from openapi_server.models.verify_request import VerifyRequest


pytestmark = pytest.mark.asyncio

async def test_add_verification(client):
    """Test case for add_verification

    Start verification process for external email address or sms number
    """
    body = openapi_server.AddVerificationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/verifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_verifications(client):
    """Test case for get_all_verifications

    Get all verificats for the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/verifications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify(client):
    """Test case for verify

    Verify an email address or sms number with a code
    """
    body = openapi_server.VerifyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/verifications/{verification}/verify'.format(verification='verification_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

