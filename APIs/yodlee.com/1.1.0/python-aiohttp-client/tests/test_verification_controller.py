# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_verification_request import UpdateVerificationRequest
from openapi_server.models.verification_request import VerificationRequest
from openapi_server.models.verification_response import VerificationResponse
from openapi_server.models.verification_status_response import VerificationStatusResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_get_verification_status(client):
    """Test case for get_verification_status

    Get Verification Status
    """
    params = [('accountId', 'account_id_example'),
                    ('providerAccountId', 'provider_account_id_example'),
                    ('verificationType', 'verification_type_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/verification',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_initiate_matching_or_challenge_deposite_verification(client):
    """Test case for initiate_matching_or_challenge_deposite_verification

    Initiaite Matching Service and Challenge Deposit
    """
    body = {"verification":{"accountId":0,"reason":"DATA_NOT_AVAILABLE","verificationStatus":"INITIATED","providerAccountId":6,"verificationType":"MATCHING","account":{"accountName":"accountName","accountType":"SAVINGS","accountNumber":"accountNumber","bankTransferCode":{"id":"id","type":"BSB"}},"verificationDate":"verificationDate","verificationId":1}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/verification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_challenge_deposit(client):
    """Test case for verify_challenge_deposit

    Verify Challenge Deposit
    """
    body = {"verification":{"accountId":0,"reason":"DATA_NOT_AVAILABLE","verificationStatus":"INITIATED","providerAccountId":6,"verificationType":"MATCHING","account":{"accountName":"accountName","accountType":"SAVINGS","accountNumber":"accountNumber","bankTransferCode":{"id":"id","type":"BSB"}},"transaction":[{"amount":{"amount":0.8008281904610115,"currency":"AUD"},"baseType":"CREDIT"},{"amount":{"amount":0.8008281904610115,"currency":"AUD"},"baseType":"CREDIT"}],"verificationDate":"verificationDate","verificationId":1}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/verification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

