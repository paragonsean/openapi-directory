# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get2_lists_id_response import Get2ListsIdResponse
from openapi_server.models.get2_users_id_followed_lists_response import Get2UsersIdFollowedListsResponse
from openapi_server.models.get2_users_id_list_memberships_response import Get2UsersIdListMembershipsResponse
from openapi_server.models.get2_users_id_owned_lists_response import Get2UsersIdOwnedListsResponse
from openapi_server.models.get2_users_id_pinned_lists_response import Get2UsersIdPinnedListsResponse
from openapi_server.models.list_add_user_request import ListAddUserRequest
from openapi_server.models.list_create_request import ListCreateRequest
from openapi_server.models.list_create_response import ListCreateResponse
from openapi_server.models.list_delete_response import ListDeleteResponse
from openapi_server.models.list_followed_request import ListFollowedRequest
from openapi_server.models.list_followed_response import ListFollowedResponse
from openapi_server.models.list_mutate_response import ListMutateResponse
from openapi_server.models.list_pinned_request import ListPinnedRequest
from openapi_server.models.list_pinned_response import ListPinnedResponse
from openapi_server.models.list_unpin_response import ListUnpinResponse
from openapi_server.models.list_update_request import ListUpdateRequest
from openapi_server.models.list_update_response import ListUpdateResponse
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_get_user_list_memberships(client):
    """Test case for get_user_list_memberships

    Get a User's List Memberships
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('list.fields', ['[\"created_at\",\"description\",\"follower_count\",\"id\",\"member_count\",\"name\",\"owner_id\",\"private\"]']),
                    ('expansions', ['[\"owner_id\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/list_memberships'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_add_member(client):
    """Test case for list_add_member

    Add a List member
    """
    body = {"user_id":"2244994945"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/lists/{id}/members'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_id_create(client):
    """Test case for list_id_create

    Create List
    """
    body = {"private":False,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/lists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_id_delete(client):
    """Test case for list_id_delete

    Delete List
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/lists/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_id_get(client):
    """Test case for list_id_get

    List lookup by List ID.
    """
    params = [('list.fields', ['[\"created_at\",\"description\",\"follower_count\",\"id\",\"member_count\",\"name\",\"owner_id\",\"private\"]']),
                    ('expansions', ['[\"owner_id\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/lists/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_id_update(client):
    """Test case for list_id_update

    Update List.
    """
    body = {"private":True,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='PUT',
        path='/2/lists/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_remove_member(client):
    """Test case for list_remove_member

    Remove a List member
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/lists/{id}/members/{user_id}'.format(id='id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_follow(client):
    """Test case for list_user_follow

    Follow a List
    """
    body = {"list_id":"1146654567674912769"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/followed_lists'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_owned_lists(client):
    """Test case for list_user_owned_lists

    Get a User's Owned Lists.
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('list.fields', ['[\"created_at\",\"description\",\"follower_count\",\"id\",\"member_count\",\"name\",\"owner_id\",\"private\"]']),
                    ('expansions', ['[\"owner_id\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/owned_lists'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_pin(client):
    """Test case for list_user_pin

    Pin a List
    """
    body = {"list_id":"1146654567674912769"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/pinned_lists'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_pinned_lists(client):
    """Test case for list_user_pinned_lists

    Get a User's Pinned Lists
    """
    params = [('list.fields', ['[\"created_at\",\"description\",\"follower_count\",\"id\",\"member_count\",\"name\",\"owner_id\",\"private\"]']),
                    ('expansions', ['[\"owner_id\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/pinned_lists'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_unfollow(client):
    """Test case for list_user_unfollow

    Unfollow a List
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{id}/followed_lists/{list_id}'.format(id='id_example', list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_unpin(client):
    """Test case for list_user_unpin

    Unpin a List
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{id}/pinned_lists/{list_id}'.format(id='id_example', list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_followed_lists(client):
    """Test case for user_followed_lists

    Get User's Followed Lists
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('list.fields', ['[\"created_at\",\"description\",\"follower_count\",\"id\",\"member_count\",\"name\",\"owner_id\",\"private\"]']),
                    ('expansions', ['[\"owner_id\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/followed_lists'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

