# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_settings import AccountSettings
from openapi_server.models.register_email_request import RegisterEmailRequest
from openapi_server.models.register_email_response import RegisterEmailResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_change_account_settings(client):
    """Test case for change_account_settings

    Change Account Settings
    """
    params = [('api_key', 'abcd1234'),
                    ('api_secret', 'ABCDEFGH01234abc')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'dr_call_back_url': 'dr_call_back_url_example',
        'mo_call_back_url': 'mo_call_back_url_example'
        }
    response = await client.request(
        method='POST',
        path='/account/settings',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_sender(client):
    """Test case for register_sender

    Register an email sender
    """
    body = openapi_server.RegisterEmailRequest()
    params = [('api_key', 'abcd1234'),
                    ('api_secret', 'ABCDEFGH01234abc')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/account/register-sender',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

