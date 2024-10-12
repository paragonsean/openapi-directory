# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_add_member_setup import AccountAddMemberSetup
from openapi_server.models.account_update_member_setup import AccountUpdateMemberSetup
from openapi_server.models.error import Error
from openapi_server.models.member import Member


pytestmark = pytest.mark.asyncio

async def test_add_member_to_account(client):
    """Test case for add_member_to_account

    
    """
    account_add_member_setup = openapi_server.AccountAddMemberSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{account_slug}/members'.format(account_slug='account_slug_example'),
        headers=headers,
        json=account_add_member_setup,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_member(client):
    """Test case for get_account_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{account_slug}/members/{member_id}'.format(account_slug='account_slug_example', member_id='member_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_members_for_account(client):
    """Test case for list_members_for_account

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{account_slug}/members'.format(account_slug='account_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_account_member(client):
    """Test case for remove_account_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/{account_slug}/members/{member_id}'.format(account_slug='account_slug_example', member_id='member_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account_member(client):
    """Test case for update_account_member

    
    """
    account_update_member_setup = openapi_server.AccountUpdateMemberSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/{account_slug}/members/{member_id}'.format(account_slug='account_slug_example', member_id='member_id_example'),
        headers=headers,
        json=account_update_member_setup,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

