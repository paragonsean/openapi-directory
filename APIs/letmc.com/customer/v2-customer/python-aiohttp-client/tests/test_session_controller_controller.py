# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_session_controller_change_password(client):
    """Test case for session_controller_change_password

    Change the password of a customer given their existing and new password.
    """
    params = [('token', 'token_example'),
                    ('oldPassword', 'old_password_example'),
                    ('newPassword', 'new_password_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/v2/customer/{short_name}/session/password'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_session_controller_create_landlord_login(client):
    """Test case for session_controller_create_landlord_login

    Send a request to the in-tray to create a landlord login.
    """
    params = [('email', 'email_example'),
                    ('title', 'title_example'),
                    ('forename', 'forename_example'),
                    ('surname', 'surname_example'),
                    ('propertyAddress', 'property_address_example'),
                    ('contactDetails', 'contact_details_example'),
                    ('branchID', 'branch_id_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/customer/{short_name}/session/createlandlordlogin'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_session_controller_get_session_info(client):
    """Test case for session_controller_get_session_info

    Gets information about the currently logged on customer.
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/session'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_session_controller_login(client):
    """Test case for session_controller_login

    Login as a customer given their username and password.
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/customer/{short_name}/session'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_session_controller_logout(client):
    """Test case for session_controller_logout

    Logout a customer previously logged in via the Login endpoint.
    """
    params = [('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/customer/{short_name}/session'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_session_controller_reset_password(client):
    """Test case for session_controller_reset_password

    Reset the customer's password. An email will be sent out to reset.
    """
    params = [('email', 'email_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/customer/{short_name}/session/resetpassword'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

