# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_v2_get_user_clan_invite_setting200_response import GroupV2GetUserClanInviteSetting200Response
from openapi_server.models.social_get_friend_list200_response import SocialGetFriendList200Response
from openapi_server.models.social_get_friend_request_list200_response import SocialGetFriendRequestList200Response
from openapi_server.models.social_get_platform_friend_list200_response import SocialGetPlatformFriendList200Response


pytestmark = pytest.mark.asyncio

async def test_social_accept_friend_request(client):
    """Test case for social_accept_friend_request

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Social/Friends/Requests/Accept/{membership_id}'.format(membership_id='membership_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_social_decline_friend_request(client):
    """Test case for social_decline_friend_request

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Social/Friends/Requests/Decline/{membership_id}'.format(membership_id='membership_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_social_get_friend_list(client):
    """Test case for social_get_friend_list

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Social/Friends/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_social_get_friend_request_list(client):
    """Test case for social_get_friend_request_list

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Social/Friends/Requests/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_social_get_platform_friend_list(client):
    """Test case for social_get_platform_friend_list

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Social/PlatformFriends/{friend_platform}/{page}'.format(friend_platform=56, page='page_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_social_issue_friend_request(client):
    """Test case for social_issue_friend_request

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Social/Friends/Add/{membership_id}'.format(membership_id='membership_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_social_remove_friend(client):
    """Test case for social_remove_friend

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Social/Friends/Remove/{membership_id}'.format(membership_id='membership_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_social_remove_friend_request(client):
    """Test case for social_remove_friend_request

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Social/Friends/Requests/Remove/{membership_id}'.format(membership_id='membership_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

