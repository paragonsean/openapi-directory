# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verify_v2_service_verification_check import VerifyV2ServiceVerificationCheck


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_verification_check(client):
    """Test case for create_verification_check

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'amount': 'amount_example',
        'code': 'code_example',
        'payee': 'payee_example',
        'to': 'to_example',
        'verification_sid': 'verification_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/VerificationCheck'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

