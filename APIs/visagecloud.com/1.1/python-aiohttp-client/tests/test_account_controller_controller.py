# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_response import RestResponse


pytestmark = pytest.mark.asyncio

async def test_change_password_using_post(client):
    """Test case for change_password_using_post

    Change password for an account using old password
    """
    params = [('email', 'email_example'),
                    ('oldPassword', 'old_password_example'),
                    ('newPassword', 'new_password_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/account/changePassword',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_by_access_key_using_get(client):
    """Test case for get_account_by_access_key_using_get

    Get account information by accessKey and secretKey
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/account/account',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_billing_per_account_using_get(client):
    """Test case for get_billing_per_account_using_get

    Get billing information by accessKey and secretKey
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('dateTemplate', 'date_template_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/account/billing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login_with_email_using_post(client):
    """Test case for login_with_email_using_post

    Get account information including accessKey and secretKey by email and password
    """
    params = [('email', 'email_example'),
                    ('password', 'password_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/account/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

