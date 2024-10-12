# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.check_push_request import CheckPushRequest
from openapi_server.models.check_push_response import CheckPushResponse
from openapi_server.models.check_sqs_request import CheckSQSRequest
from openapi_server.models.check_sqs_response import CheckSQSResponse


pytestmark = pytest.mark.asyncio

async def test_check_push_0(client):
    """Test case for check_push_0

    Check push
    """
    body = {"skip_devices":True,"firebase_template":"firebase_template","user_id":"user_id","apn_template":"apn_template","push_provider_name":"push_provider_name","push_provider_type":"firebase","firebase_data_template":"firebase_data_template","message_id":"message_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_push',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_sqs_0(client):
    """Test case for check_sqs_0

    Check SQS
    """
    body = {"sqs_key":"sqs_key","sqs_url":"sqs_url","sqs_secret":"sqs_secret"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/check_sqs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

