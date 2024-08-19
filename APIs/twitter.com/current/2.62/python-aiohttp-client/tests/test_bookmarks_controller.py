# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bookmark_add_request import BookmarkAddRequest
from openapi_server.models.bookmark_mutation_response import BookmarkMutationResponse
from openapi_server.models.error import Error
from openapi_server.models.get2_users_id_bookmarks_response import Get2UsersIdBookmarksResponse
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_get_users_id_bookmarks(client):
    """Test case for get_users_id_bookmarks

    Bookmarks by User
    """
    params = [('max_results', 56),
                    ('pagination_token', 'pagination_token_example'),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]']),
                    ('expansions', ['[\"attachments.media_keys\",\"attachments.poll_ids\",\"author_id\",\"edit_history_tweet_ids\",\"entities.mentions.username\",\"geo.place_id\",\"in_reply_to_user_id\",\"referenced_tweets.id\",\"referenced_tweets.id.author_id\"]']),
                    ('media.fields', ['[\"alt_text\",\"duration_ms\",\"height\",\"media_key\",\"non_public_metrics\",\"organic_metrics\",\"preview_image_url\",\"promoted_metrics\",\"public_metrics\",\"type\",\"url\",\"variants\",\"width\"]']),
                    ('poll.fields', ['[\"duration_minutes\",\"end_datetime\",\"id\",\"options\",\"voting_status\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('place.fields', ['[\"contained_within\",\"country\",\"country_code\",\"full_name\",\"geo\",\"id\",\"name\",\"place_type\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/bookmarks'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users_id_bookmarks(client):
    """Test case for post_users_id_bookmarks

    Add Tweet to Bookmarks
    """
    body = {"tweet_id":"1346889436626259968"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/bookmarks'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_bookmarks_delete(client):
    """Test case for users_id_bookmarks_delete

    Remove a bookmarked Tweet
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{id}/bookmarks/{tweet_id}'.format(id='id_example', tweet_id='tweet_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

