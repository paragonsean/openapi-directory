# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.send_referral_email_request_body import SendReferralEmailRequestBody


pytestmark = pytest.mark.asyncio

async def test_send_referral_email(client):
    """Test case for send_referral_email

    Send referral email to a given address
    """
    body = {"emails":["emails","emails"],"message":"I use ExaVault for secure file sending, and so should you. Follow my link to sign up for a trial."}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/email/referral',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_welcome_email(client):
    """Test case for send_welcome_email

    Resend welcome email to specific user
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/email/welcome/{username}'.format(username='exampleuser'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

