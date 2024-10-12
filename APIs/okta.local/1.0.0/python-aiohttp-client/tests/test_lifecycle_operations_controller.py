# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_activate_user(client):
    """Test case for activate_user

    Activate User
    """
    params = [('sendEmail', 'false')]
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/activate'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_deactivate_user(client):
    """Test case for deactivate_user

    Deactivate User
    """
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/deactivate'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_reset_password(client):
    """Test case for reset_password

    Reset Password
    """
    params = [('sendEmail', 'false')]
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/reset_password'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_set_temp_password(client):
    """Test case for set_temp_password

    Set Temp Password
    """
    params = [('tempPassword', 'true')]
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/expire_password'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_suspend_user(client):
    """Test case for suspend_user

    Suspend User
    """
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/suspend'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_unlock_user(client):
    """Test case for unlock_user

    Unlock User
    """
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/unlock'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_unsuspend_user(client):
    """Test case for unsuspend_user

    Unsuspend User
    """
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/unsuspend'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

