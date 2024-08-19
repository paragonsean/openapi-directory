# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_or_delete_rules_request import AddOrDeleteRulesRequest
from openapi_server.models.add_or_delete_rules_response import AddOrDeleteRulesResponse
from openapi_server.models.error import Error
from openapi_server.models.filtered_streaming_tweet_response import FilteredStreamingTweetResponse
from openapi_server.models.get2_lists_id_tweets_response import Get2ListsIdTweetsResponse
from openapi_server.models.get2_spaces_id_buyers_response import Get2SpacesIdBuyersResponse
from openapi_server.models.get2_spaces_id_tweets_response import Get2SpacesIdTweetsResponse
from openapi_server.models.get2_tweets_counts_all_response import Get2TweetsCountsAllResponse
from openapi_server.models.get2_tweets_counts_recent_response import Get2TweetsCountsRecentResponse
from openapi_server.models.get2_tweets_id_quote_tweets_response import Get2TweetsIdQuoteTweetsResponse
from openapi_server.models.get2_tweets_id_response import Get2TweetsIdResponse
from openapi_server.models.get2_tweets_response import Get2TweetsResponse
from openapi_server.models.get2_tweets_sample10_stream_response import Get2TweetsSample10StreamResponse
from openapi_server.models.get2_tweets_search_all_response import Get2TweetsSearchAllResponse
from openapi_server.models.get2_tweets_search_recent_response import Get2TweetsSearchRecentResponse
from openapi_server.models.get2_users_id_liked_tweets_response import Get2UsersIdLikedTweetsResponse
from openapi_server.models.get2_users_id_mentions_response import Get2UsersIdMentionsResponse
from openapi_server.models.get2_users_id_timelines_reverse_chronological_response import Get2UsersIdTimelinesReverseChronologicalResponse
from openapi_server.models.get2_users_id_tweets_response import Get2UsersIdTweetsResponse
from openapi_server.models.problem import Problem
from openapi_server.models.rules_lookup_response import RulesLookupResponse
from openapi_server.models.streaming_tweet_response import StreamingTweetResponse
from openapi_server.models.tweet_create_request import TweetCreateRequest
from openapi_server.models.tweet_create_response import TweetCreateResponse
from openapi_server.models.tweet_delete_response import TweetDeleteResponse
from openapi_server.models.tweet_hide_request import TweetHideRequest
from openapi_server.models.tweet_hide_response import TweetHideResponse
from openapi_server.models.users_likes_create_request import UsersLikesCreateRequest
from openapi_server.models.users_likes_create_response import UsersLikesCreateResponse
from openapi_server.models.users_likes_delete_response import UsersLikesDeleteResponse
from openapi_server.models.users_retweets_create_request import UsersRetweetsCreateRequest
from openapi_server.models.users_retweets_create_response import UsersRetweetsCreateResponse
from openapi_server.models.users_retweets_delete_response import UsersRetweetsDeleteResponse


pytestmark = pytest.mark.asyncio

async def test_add_or_delete_rules(client):
    """Test case for add_or_delete_rules

    Add/Delete rules
    """
    body = {"add":[{"tag":"Non-retweeted coffee Tweets","value":"coffee -is:retweet"},{"tag":"Non-retweeted coffee Tweets","value":"coffee -is:retweet"}]}
    params = [('dry_run', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/2/tweets/search/stream/rules',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_tweet(client):
    """Test case for create_tweet

    Creation of a Tweet
    """
    body = {"geo":{"place_id":"place_id"},"nullcast":False,"for_super_followers_only":False,"quote_tweet_id":"1346889436626259968","direct_message_deep_link":"direct_message_deep_link","card_uri":"card_uri","media":{"media_ids":["1146654567674912769","1146654567674912769","1146654567674912769","1146654567674912769"],"tagged_user_ids":["2244994945","2244994945","2244994945","2244994945","2244994945"]},"poll":{"duration_minutes":811,"options":["options","options","options","options"],"reply_settings":"following"},"text":"Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i","reply":{"exclude_reply_user_ids":["2244994945","2244994945"],"in_reply_to_tweet_id":"1346889436626259968"},"reply_settings":"following"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/tweets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tweet_by_id(client):
    """Test case for delete_tweet_by_id

    Tweet delete by Tweet ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/tweets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_tweet_by_id(client):
    """Test case for find_tweet_by_id

    Tweet lookup by Tweet ID
    """
    params = [('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]']),
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
        path='/2/tweets/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_tweets_by_id(client):
    """Test case for find_tweets_by_id

    Tweet lookup by Tweet IDs
    """
    params = [('ids', ['ids_example']),
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
        path='/2/tweets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_tweets_that_quote_a_tweet(client):
    """Test case for find_tweets_that_quote_a_tweet

    Retrieve Tweets that quote a Tweet.
    """
    params = [('max_results', 10),
                    ('pagination_token', 'pagination_token_example'),
                    ('exclude', ['[\"replies\",\"retweets\"]']),
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
        path='/2/tweets/{id}/quote_tweets'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rules(client):
    """Test case for get_rules

    Rules lookup
    """
    params = [('ids', ['ids_example']),
                    ('max_results', 1000),
                    ('pagination_token', 'pagination_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/tweets/search/stream/rules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tweets_firehose_stream(client):
    """Test case for get_tweets_firehose_stream

    Firehose stream
    """
    params = [('backfill_minutes', 56),
                    ('partition', 56),
                    ('start_time', '2021-02-14T18:40:40.000Z'),
                    ('end_time', '2021-02-14T18:40:40.000Z'),
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
        path='/2/tweets/firehose/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tweets_sample10_stream(client):
    """Test case for get_tweets_sample10_stream

    Sample 10% stream
    """
    params = [('backfill_minutes', 56),
                    ('partition', 56),
                    ('start_time', '2021-02-14T18:40:40.000Z'),
                    ('end_time', '2021-02-14T18:40:40.000Z'),
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
        path='/2/tweets/sample10/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hide_reply_by_id(client):
    """Test case for hide_reply_by_id

    Hide replies
    """
    body = {"hidden":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='PUT',
        path='/2/tweets/{tweet_id}/hidden'.format(tweet_id='tweet_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lists_id_tweets(client):
    """Test case for lists_id_tweets

    List Tweets timeline by List ID.
    """
    params = [('max_results', 100),
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
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/lists/{id}/tweets'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sample_stream(client):
    """Test case for sample_stream

    Sample stream
    """
    params = [('backfill_minutes', 56),
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
        path='/2/tweets/sample/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_stream(client):
    """Test case for search_stream

    Filtered stream
    """
    params = [('backfill_minutes', 56),
                    ('start_time', '2021-02-01T18:40:40.000Z'),
                    ('end_time', '2021-02-14T18:40:40.000Z'),
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
        path='/2/tweets/search/stream',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_space_buyers_0(client):
    """Test case for space_buyers_0

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

async def test_space_tweets_0(client):
    """Test case for space_tweets_0

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


pytestmark = pytest.mark.asyncio

async def test_tweet_counts_full_archive_search(client):
    """Test case for tweet_counts_full_archive_search

    Full archive search counts
    """
    params = [('query', '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'),
                    ('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('since_id', 'since_id_example'),
                    ('until_id', 'until_id_example'),
                    ('next_token', 'next_token_example'),
                    ('pagination_token', 'pagination_token_example'),
                    ('granularity', hour),
                    ('search_count.fields', ['[\"end\",\"start\",\"tweet_count\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/tweets/counts/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tweet_counts_recent_search(client):
    """Test case for tweet_counts_recent_search

    Recent search counts
    """
    params = [('query', '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'),
                    ('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('since_id', 'since_id_example'),
                    ('until_id', 'until_id_example'),
                    ('next_token', 'next_token_example'),
                    ('pagination_token', 'pagination_token_example'),
                    ('granularity', hour),
                    ('search_count.fields', ['[\"end\",\"start\",\"tweet_count\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/2/tweets/counts/recent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tweets_fullarchive_search(client):
    """Test case for tweets_fullarchive_search

    Full-archive search
    """
    params = [('query', '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'),
                    ('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('since_id', 'since_id_example'),
                    ('until_id', 'until_id_example'),
                    ('max_results', 10),
                    ('next_token', 'next_token_example'),
                    ('pagination_token', 'pagination_token_example'),
                    ('sort_order', 'sort_order_example'),
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
        path='/2/tweets/search/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tweets_recent_search(client):
    """Test case for tweets_recent_search

    Recent search
    """
    params = [('query', '(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet'),
                    ('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('since_id', 'since_id_example'),
                    ('until_id', 'until_id_example'),
                    ('max_results', 10),
                    ('next_token', 'next_token_example'),
                    ('pagination_token', 'pagination_token_example'),
                    ('sort_order', 'sort_order_example'),
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
        path='/2/tweets/search/recent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_like(client):
    """Test case for users_id_like

    Causes the User (in the path) to like the specified Tweet
    """
    body = {"tweet_id":"1346889436626259968"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/likes'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_liked_tweets(client):
    """Test case for users_id_liked_tweets

    Returns Tweet objects liked by the provided User ID
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
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/users/{id}/liked_tweets'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_mentions(client):
    """Test case for users_id_mentions

    User mention timeline by User ID
    """
    params = [('since_id', 'since_id_example'),
                    ('until_id', '1346889436626259968'),
                    ('max_results', 56),
                    ('pagination_token', 'pagination_token_example'),
                    ('start_time', '2021-02-01T18:40:40.000Z'),
                    ('end_time', '2021-02-14T18:40:40.000Z'),
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
        path='/2/users/{id}/mentions'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_retweets(client):
    """Test case for users_id_retweets

    Causes the User (in the path) to retweet the specified Tweet.
    """
    body = {"tweet_id":"1346889436626259968"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/users/{id}/retweets'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_timeline(client):
    """Test case for users_id_timeline

    User home timeline by User ID
    """
    params = [('since_id', '791775337160081409'),
                    ('until_id', '1346889436626259968'),
                    ('max_results', 56),
                    ('pagination_token', 'pagination_token_example'),
                    ('exclude', ['[\"replies\",\"retweets\"]']),
                    ('start_time', '2021-02-01T18:40:40.000Z'),
                    ('end_time', '2021-02-14T18:40:40.000Z'),
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
        path='/2/users/{id}/timelines/reverse_chronological'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_tweets(client):
    """Test case for users_id_tweets

    User Tweets timeline by User ID
    """
    params = [('since_id', '791775337160081409'),
                    ('until_id', '1346889436626259968'),
                    ('max_results', 56),
                    ('pagination_token', 'pagination_token_example'),
                    ('exclude', ['[\"replies\",\"retweets\"]']),
                    ('start_time', '2021-02-01T18:40:40.000Z'),
                    ('end_time', '2021-02-14T18:40:40.000Z'),
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
        path='/2/users/{id}/tweets'.format(id='2244994945'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_unlike(client):
    """Test case for users_id_unlike

    Causes the User (in the path) to unlike the specified Tweet
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{id}/likes/{tweet_id}'.format(id='id_example', tweet_id='tweet_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_unretweets(client):
    """Test case for users_id_unretweets

    Causes the User (in the path) to unretweet the specified Tweet
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='DELETE',
        path='/2/users/{id}/retweets/{source_tweet_id}'.format(id='id_example', source_tweet_id='source_tweet_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

