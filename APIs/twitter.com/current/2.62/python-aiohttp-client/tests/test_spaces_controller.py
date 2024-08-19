# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get2_spaces_by_creator_ids_response import Get2SpacesByCreatorIdsResponse
from openapi_server.models.get2_spaces_id_buyers_response import Get2SpacesIdBuyersResponse
from openapi_server.models.get2_spaces_id_response import Get2SpacesIdResponse
from openapi_server.models.get2_spaces_id_tweets_response import Get2SpacesIdTweetsResponse
from openapi_server.models.get2_spaces_response import Get2SpacesResponse
from openapi_server.models.get2_spaces_search_response import Get2SpacesSearchResponse
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_find_space_by_id(client):
    """Test case for find_space_by_id

    Space lookup by Space ID
    """
    params = [('space.fields', ['[\"created_at\",\"creator_id\",\"ended_at\",\"host_ids\",\"id\",\"invited_user_ids\",\"is_ticketed\",\"lang\",\"participant_count\",\"scheduled_start\",\"speaker_ids\",\"started_at\",\"state\",\"subscriber_count\",\"title\",\"topic_ids\",\"updated_at\"]']),
                    ('expansions', ['[\"creator_id\",\"host_ids\",\"invited_user_ids\",\"speaker_ids\",\"topic_ids\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('topic.fields', ['[\"description\",\"id\",\"name\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/spaces/{id}'.format(id='1YqKDqWqdPLsV'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_spaces_by_creator_ids(client):
    """Test case for find_spaces_by_creator_ids

    Space lookup by their creators
    """
    params = [('user_ids', ['user_ids_example']),
                    ('space.fields', ['[\"created_at\",\"creator_id\",\"ended_at\",\"host_ids\",\"id\",\"invited_user_ids\",\"is_ticketed\",\"lang\",\"participant_count\",\"scheduled_start\",\"speaker_ids\",\"started_at\",\"state\",\"subscriber_count\",\"title\",\"topic_ids\",\"updated_at\"]']),
                    ('expansions', ['[\"creator_id\",\"host_ids\",\"invited_user_ids\",\"speaker_ids\",\"topic_ids\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('topic.fields', ['[\"description\",\"id\",\"name\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/spaces/by/creator_ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_spaces_by_ids(client):
    """Test case for find_spaces_by_ids

    Space lookup up Space IDs
    """
    params = [('ids', ['ids_example']),
                    ('space.fields', ['[\"created_at\",\"creator_id\",\"ended_at\",\"host_ids\",\"id\",\"invited_user_ids\",\"is_ticketed\",\"lang\",\"participant_count\",\"scheduled_start\",\"speaker_ids\",\"started_at\",\"state\",\"subscriber_count\",\"title\",\"topic_ids\",\"updated_at\"]']),
                    ('expansions', ['[\"creator_id\",\"host_ids\",\"invited_user_ids\",\"speaker_ids\",\"topic_ids\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('topic.fields', ['[\"description\",\"id\",\"name\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/spaces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_spaces(client):
    """Test case for search_spaces

    Search for Spaces
    """
    params = [('query', 'crypto'),
                    ('state', all),
                    ('max_results', 100),
                    ('space.fields', ['[\"created_at\",\"creator_id\",\"ended_at\",\"host_ids\",\"id\",\"invited_user_ids\",\"is_ticketed\",\"lang\",\"participant_count\",\"scheduled_start\",\"speaker_ids\",\"started_at\",\"state\",\"subscriber_count\",\"title\",\"topic_ids\",\"updated_at\"]']),
                    ('expansions', ['[\"creator_id\",\"host_ids\",\"invited_user_ids\",\"speaker_ids\",\"topic_ids\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('topic.fields', ['[\"description\",\"id\",\"name\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/spaces/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_space_buyers(client):
    """Test case for space_buyers

    Retrieve the list of Users who purchased a ticket to the given space
    """
    params = [('pagination_token', 'pagination_token_example'),
                    ('max_results', 100),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('expansions', ['[\"pinned_tweet_id\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/spaces/{id}/buyers'.format(id='1YqKDqWqdPLsV'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_space_tweets(client):
    """Test case for space_tweets

    Retrieve Tweets from a Space.
    """
    params = [('max_results', 100),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]']),
                    ('expansions', ['[\"attachments.media_keys\",\"attachments.poll_ids\",\"author_id\",\"edit_history_tweet_ids\",\"entities.mentions.username\",\"geo.place_id\",\"in_reply_to_user_id\",\"referenced_tweets.id\",\"referenced_tweets.id.author_id\"]']),
                    ('media.fields', ['[\"alt_text\",\"duration_ms\",\"height\",\"media_key\",\"non_public_metrics\",\"organic_metrics\",\"preview_image_url\",\"promoted_metrics\",\"public_metrics\",\"type\",\"url\",\"variants\",\"width\"]']),
                    ('poll.fields', ['[\"duration_minutes\",\"end_datetime\",\"id\",\"options\",\"voting_status\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('place.fields', ['[\"contained_within\",\"country\",\"country_code\",\"full_name\",\"geo\",\"id\",\"name\",\"place_type\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/spaces/{id}/tweets'.format(id='1YqKDqWqdPLsV'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

