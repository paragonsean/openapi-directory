# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.block_user_mutation_response import BlockUserMutationResponse
from openapi_server.models.block_user_request import BlockUserRequest
from openapi_server.models.error import Error
from openapi_server.models.get2_lists_id_followers_response import Get2ListsIdFollowersResponse
from openapi_server.models.get2_lists_id_members_response import Get2ListsIdMembersResponse
from openapi_server.models.get2_tweets_id_liking_users_response import Get2TweetsIdLikingUsersResponse
from openapi_server.models.get2_tweets_id_retweeted_by_response import Get2TweetsIdRetweetedByResponse
from openapi_server.models.get2_users_by_response import Get2UsersByResponse
from openapi_server.models.get2_users_by_username_username_response import Get2UsersByUsernameUsernameResponse
from openapi_server.models.get2_users_id_blocking_response import Get2UsersIdBlockingResponse
from openapi_server.models.get2_users_id_followers_response import Get2UsersIdFollowersResponse
from openapi_server.models.get2_users_id_following_response import Get2UsersIdFollowingResponse
from openapi_server.models.get2_users_id_muting_response import Get2UsersIdMutingResponse
from openapi_server.models.get2_users_id_response import Get2UsersIdResponse
from openapi_server.models.get2_users_me_response import Get2UsersMeResponse
from openapi_server.models.get2_users_response import Get2UsersResponse
from openapi_server.models.mute_user_mutation_response import MuteUserMutationResponse
from openapi_server.models.mute_user_request import MuteUserRequest
from openapi_server.models.problem import Problem
from openapi_server.models.users_following_create_request import UsersFollowingCreateRequest
from openapi_server.models.users_following_create_response import UsersFollowingCreateResponse
from openapi_server.models.users_following_delete_response import UsersFollowingDeleteResponse


pytestmark = pytest.mark.asyncio

async def test_find_my_user(client):
    """Test case for find_my_user

    User lookup me
    """
    params = [('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/me',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_user_by_id(client):
    """Test case for find_user_by_id

    User lookup by ID
    """
    params = [('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_user_by_username(client):
    """Test case for find_user_by_username

    User lookup by username
    """
    params = [('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/by/username/{username}'.format(username='TwitterDev'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_by_id(client):
    """Test case for find_users_by_id

    User lookup by IDs
    """
    params = [('ids', ['2244994945,6253282,12']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_by_username(client):
    """Test case for find_users_by_username

    User lookup by usernames
    """
    params = [('usernames', ['TwitterDev,TwitterAPI']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/by',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_get_followers(client):
    """Test case for list_get_followers

    Returns User objects that follow a List by the provided List ID
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/lists/{id}/followers'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_get_members(client):
    """Test case for list_get_members

    Returns User objects that are members of a List by the provided List ID.
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/lists/{id}/members'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tweets_id_liking_users(client):
    """Test case for tweets_id_liking_users

    Returns User objects that have liked the provided Tweet ID
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/tweets/{id}/liking_users'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tweets_id_retweeting_users(client):
    """Test case for tweets_id_retweeting_users

    Returns User objects that have retweeted the provided Tweet ID
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/tweets/{id}/retweeted_by'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_block(client):
    """Test case for users_id_block

    Block User by User ID
    """
    body = {"target_user_id":"2244994945"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/blocking'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_blocking(client):
    """Test case for users_id_blocking

    Returns User objects that are blocked by provided User ID
    """
    params = [('max_results', 56),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/blocking'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_follow(client):
    """Test case for users_id_follow

    Follow User
    """
    body = {"target_user_id":"2244994945"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/following'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_followers(client):
    """Test case for users_id_followers

    Followers by User ID
    """
    params = [('max_results', 56),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/followers'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_following(client):
    """Test case for users_id_following

    Following by User ID
    """
    params = [('max_results', 56),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/following'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_mute(client):
    """Test case for users_id_mute

    Mute User by User ID.
    """
    body = {"target_user_id":"2244994945"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/muting'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_muting(client):
    """Test case for users_id_muting

    Returns User objects that are muted by the provided User ID
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/muting'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_unblock(client):
    """Test case for users_id_unblock

    Unblock User by User ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{source_user_id}/blocking/{target_user_id}'.format(source_user_id='source_user_id_example', target_user_id='target_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_unfollow(client):
    """Test case for users_id_unfollow

    Unfollow User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{source_user_id}/following/{target_user_id}'.format(source_user_id='source_user_id_example', target_user_id='target_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_unmute(client):
    """Test case for users_id_unmute

    Unmute User by User ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{source_user_id}/muting/{target_user_id}'.format(source_user_id='source_user_id_example', target_user_id='target_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

