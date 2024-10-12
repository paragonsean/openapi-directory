# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.password_reset_email_request import PasswordResetEmailRequest
from openapi_server.models.password_reset_request import PasswordResetRequest
from openapi_server.models.service_error import ServiceError
from openapi_server.models.subscription_details import SubscriptionDetails


pytestmark = pytest.mark.asyncio

async def test_forgot_password(client):
    """Test case for forgot_password

    
    """
    body = {"email":"email"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/request-password-reset',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_data(client):
    """Test case for get_subscription_data

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/check-subscription/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_password(client):
    """Test case for reset_password

    
    """
    body = {"password":"password","resetToken":"resetToken"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/reset-password',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_email(client):
    """Test case for verify_email

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'verifyEmailAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/verify-email',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

