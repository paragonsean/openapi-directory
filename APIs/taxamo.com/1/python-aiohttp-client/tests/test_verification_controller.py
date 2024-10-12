# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_sms_token_in import CreateSMSTokenIn
from openapi_server.models.create_sms_token_out import CreateSMSTokenOut
from openapi_server.models.verify_sms_token_out import VerifySMSTokenOut


pytestmark = pytest.mark.asyncio

async def test_create_sms_token(client):
    """Test case for create_sms_token

    Create SMS token
    """
    input = openapi_server.CreateSMSTokenIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/verification/sms',
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_sms_token(client):
    """Test case for verify_sms_token

    Verify SMS token
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/verification/sms/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

