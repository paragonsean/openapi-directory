# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_dm_conversation_request import CreateDmConversationRequest
from openapi_server.models.create_dm_event_response import CreateDmEventResponse
from openapi_server.models.create_message_request import CreateMessageRequest
from openapi_server.models.error import Error
from openapi_server.models.get2_dm_conversations_id_dm_events_response import Get2DmConversationsIdDmEventsResponse
from openapi_server.models.get2_dm_conversations_with_participant_id_dm_events_response import Get2DmConversationsWithParticipantIdDmEventsResponse
from openapi_server.models.get2_dm_events_response import Get2DmEventsResponse
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_dm_conversation_by_id_event_id_create(client):
    """Test case for dm_conversation_by_id_event_id_create

    Send a new message to a DM Conversation
    """
    body = {"attachments":[{"media_id":"1146654567674912769"},{"media_id":"1146654567674912769"}],"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/dm_conversations/{dm_conversation_id}/messages'.format(dm_conversation_id='dm_conversation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dm_conversation_id_create(client):
    """Test case for dm_conversation_id_create

    Create a new DM Conversation
    """
    body = {"conversation_type":"Group","participant_ids":["2244994945","2244994945","2244994945","2244994945","2244994945"],"message":{"attachments":[{"media_id":"1146654567674912769"},{"media_id":"1146654567674912769"}],"text":"text"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/dm_conversations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dm_conversation_with_user_event_id_create(client):
    """Test case for dm_conversation_with_user_event_id_create

    Send a new message to a user
    """
    body = {"attachments":[{"media_id":"1146654567674912769"},{"media_id":"1146654567674912769"}],"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='POST',
        path='/2/dm_conversations/with/{participant_id}/messages'.format(participant_id='participant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dm_conversations_id_dm_events(client):
    """Test case for get_dm_conversations_id_dm_events

    Get DM Events for a DM Conversation
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('event_types', ["MessageCreate","ParticipantsLeave","ParticipantsJoin"]),
                    ('dm_event.fields', ['[\"attachments\",\"created_at\",\"dm_conversation_id\",\"event_type\",\"id\",\"participant_ids\",\"referenced_tweets\",\"sender_id\",\"text\"]']),
                    ('expansions', ['[\"attachments.media_keys\",\"participant_ids\",\"referenced_tweets.id\",\"sender_id\"]']),
                    ('media.fields', ['[\"alt_text\",\"duration_ms\",\"height\",\"media_key\",\"non_public_metrics\",\"organic_metrics\",\"preview_image_url\",\"promoted_metrics\",\"public_metrics\",\"type\",\"url\",\"variants\",\"width\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/dm_conversations/{id}/dm_events'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dm_conversations_with_participant_id_dm_events(client):
    """Test case for get_dm_conversations_with_participant_id_dm_events

    Get DM Events for a DM Conversation
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('event_types', ["MessageCreate","ParticipantsLeave","ParticipantsJoin"]),
                    ('dm_event.fields', ['[\"attachments\",\"created_at\",\"dm_conversation_id\",\"event_type\",\"id\",\"participant_ids\",\"referenced_tweets\",\"sender_id\",\"text\"]']),
                    ('expansions', ['[\"attachments.media_keys\",\"participant_ids\",\"referenced_tweets.id\",\"sender_id\"]']),
                    ('media.fields', ['[\"alt_text\",\"duration_ms\",\"height\",\"media_key\",\"non_public_metrics\",\"organic_metrics\",\"preview_image_url\",\"promoted_metrics\",\"public_metrics\",\"type\",\"url\",\"variants\",\"width\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/dm_conversations/with/{participant_id}/dm_events'.format(participant_id='participant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dm_events(client):
    """Test case for get_dm_events

    Get recent DM Events
    """
    params = [('max_results', 100),
                    ('pagination_token', 'pagination_token_example'),
                    ('event_types', ["MessageCreate","ParticipantsLeave","ParticipantsJoin"]),
                    ('dm_event.fields', ['[\"attachments\",\"created_at\",\"dm_conversation_id\",\"event_type\",\"id\",\"participant_ids\",\"referenced_tweets\",\"sender_id\",\"text\"]']),
                    ('expansions', ['[\"attachments.media_keys\",\"participant_ids\",\"referenced_tweets.id\",\"sender_id\"]']),
                    ('media.fields', ['[\"alt_text\",\"duration_ms\",\"height\",\"media_key\",\"non_public_metrics\",\"organic_metrics\",\"preview_image_url\",\"promoted_metrics\",\"public_metrics\",\"type\",\"url\",\"variants\",\"width\"]']),
                    ('user.fields', ['[\"created_at\",\"description\",\"entities\",\"id\",\"location\",\"name\",\"pinned_tweet_id\",\"profile_image_url\",\"protected\",\"public_metrics\",\"url\",\"username\",\"verified\",\"verified_type\",\"withheld\"]']),
                    ('tweet.fields', ['[\"attachments\",\"author_id\",\"context_annotations\",\"conversation_id\",\"created_at\",\"edit_controls\",\"edit_history_tweet_ids\",\"entities\",\"geo\",\"id\",\"in_reply_to_user_id\",\"lang\",\"non_public_metrics\",\"organic_metrics\",\"possibly_sensitive\",\"promoted_metrics\",\"public_metrics\",\"referenced_tweets\",\"reply_settings\",\"source\",\"text\",\"withheld\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        
    }
    response = await client.request(
        method='GET',
        path='/2/dm_events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

