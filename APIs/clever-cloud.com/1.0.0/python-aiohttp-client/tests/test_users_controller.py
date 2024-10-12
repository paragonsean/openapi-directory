# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.user import User
from openapi_server.models.wannabe_user import WannabeUser


pytestmark = pytest.mark.asyncio

async def test_get_users_id_0(client):
    """Test case for get_users_id_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_id_applications_1(client):
    """Test case for get_users_id_applications_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{id}/applications'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_user_id_git_info_0(client):
    """Test case for get_users_user_id_git_info_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/git-info'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users_0(client):
    """Test case for post_users_0

    
    """
    body = {"zipcode":"zipcode","country":"country","password":"password","address":"address","city":"city","phone":"phone","terms":False,"name":"name","lang":"lang","email":"email"}
    params = [('invitationKey', 'invitation_key_example'),
                    ('addonBetaInvitationKey', 'addon_beta_invitation_key_example'),
                    ('email', 'email_example'),
                    ('pass', '_pass_example'),
                    ('url_next', 'url_next_example'),
                    ('terms', 'terms_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/users',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

