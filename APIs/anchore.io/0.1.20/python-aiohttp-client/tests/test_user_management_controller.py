# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_credential import AccessCredential
from openapi_server.models.account import Account
from openapi_server.models.account_creation_request import AccountCreationRequest
from openapi_server.models.account_status import AccountStatus
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.user import User
from openapi_server.models.user_creation_request import UserCreationRequest


pytestmark = pytest.mark.asyncio

async def test_create_account(client):
    """Test case for create_account

    Create a new user. Only avaialble to admin user.
    """
    body = {"name":"name","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_user(client):
    """Test case for create_user

    Create a new user
    """
    body = {"password":"password","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts/{accountname}/users'.format(accountname='accountname_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_user_credential(client):
    """Test case for create_user_credential

    add/replace credential
    """
    body = {"created_at":"created_at","type":"password","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts/{accountname}/users/{username}/credentials'.format(accountname='accountname_example', username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_account(client):
    """Test case for delete_account

    Delete the specified account, only allowed if the account is in the disabled state. All users will be deleted along with the account and all resources will be garbage collected
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts/{accountname}'.format(accountname='accountname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete a specific user credential by username of the credential. Cannot be the credential used to authenticate the request.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts/{accountname}/users/{username}'.format(accountname='accountname_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_credential(client):
    """Test case for delete_user_credential

    Delete a credential by type
    """
    params = [('credential_type', 'credential_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts/{accountname}/users/{username}/credentials'.format(accountname='accountname_example', username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Get info about an user. Only available to admin user. Uses the main user Id, not a username.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{accountname}'.format(accountname='accountname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_user(client):
    """Test case for get_account_user

    Get a specific user in the specified account
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{accountname}/users/{username}'.format(accountname='accountname_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_accounts(client):
    """Test case for list_accounts

    List user summaries. Only available to the system admin user.
    """
    params = [('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_credentials(client):
    """Test case for list_user_credentials

    Get current credential summary
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{accountname}/users/{username}/credentials'.format(accountname='accountname_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_users(client):
    """Test case for list_users

    List accounts for the user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{accountname}/users'.format(accountname='accountname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account_state(client):
    """Test case for update_account_state

    Update the state of an account to either enabled or disabled. For deletion use the DELETE route
    """
    body = {"state":"enabled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/accounts/{accountname}/state'.format(accountname='accountname_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

