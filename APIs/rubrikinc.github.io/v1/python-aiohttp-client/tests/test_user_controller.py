# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.local_user_account_lockout_config import LocalUserAccountLockoutConfig
from openapi_server.models.local_user_account_lockout_status import LocalUserAccountLockoutStatus
from openapi_server.models.totp_config_update_request import TotpConfigUpdateRequest
from openapi_server.models.totp_secret import TotpSecret
from openapi_server.models.totp_status import TotpStatus


pytestmark = pytest.mark.asyncio

async def test_generate_totp_secret(client):
    """Test case for generate_totp_secret

    Generate a TOTP secret key for the given user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/user/{id}/totp/new_secret'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_totp_status(client):
    """Test case for get_totp_status

    Get the TOTP status for the given user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user/{id}/totp/status'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_account_lockout_settings(client):
    """Test case for get_user_account_lockout_settings

    Get the local user account lockout settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user/lockout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_manage_user_account_lockout_settings(client):
    """Test case for manage_user_account_lockout_settings

    Update the local user account lockout settings
    """
    body = {"maxFailedLoginsForLocalUser":6,"accountLockoutDurationInMinutes":0,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/user/lockout',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_totp(client):
    """Test case for reset_totp

    Reset the TOTP for the given user
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/user/{id}/totp/config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_totp(client):
    """Test case for setup_totp

    Configure the TOTP secret for the given user
    """
    body = {"otpForValidation":"otpForValidation","secret":"secret"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/user/{id}/totp/config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlock_user(client):
    """Test case for unlock_user

    Unlock a user account
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/user/{id}/unlock'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

