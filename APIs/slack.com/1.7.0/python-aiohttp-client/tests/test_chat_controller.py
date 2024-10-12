# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_delete_error_schema import ChatDeleteErrorSchema
from openapi_server.models.chat_delete_scheduled_message_error_schema import ChatDeleteScheduledMessageErrorSchema
from openapi_server.models.chat_delete_scheduled_message_schema import ChatDeleteScheduledMessageSchema
from openapi_server.models.chat_delete_success_schema import ChatDeleteSuccessSchema
from openapi_server.models.chat_get_permalink_error_schema import ChatGetPermalinkErrorSchema
from openapi_server.models.chat_get_permalink_success_schema import ChatGetPermalinkSuccessSchema
from openapi_server.models.chat_me_message_error_schema import ChatMeMessageErrorSchema
from openapi_server.models.chat_me_message_schema import ChatMeMessageSchema
from openapi_server.models.chat_post_ephemeral_error_schema import ChatPostEphemeralErrorSchema
from openapi_server.models.chat_post_ephemeral_success_schema import ChatPostEphemeralSuccessSchema
from openapi_server.models.chat_post_message_error_schema import ChatPostMessageErrorSchema
from openapi_server.models.chat_post_message_success_schema import ChatPostMessageSuccessSchema
from openapi_server.models.chat_schedule_message_error_schema import ChatScheduleMessageErrorSchema
from openapi_server.models.chat_schedule_message_success_schema import ChatScheduleMessageSuccessSchema
from openapi_server.models.chat_scheduled_messages_list_error_schema import ChatScheduledMessagesListErrorSchema
from openapi_server.models.chat_scheduled_messages_list_schema import ChatScheduledMessagesListSchema
from openapi_server.models.chat_unfurl_error_schema import ChatUnfurlErrorSchema
from openapi_server.models.chat_unfurl_success_schema import ChatUnfurlSuccessSchema
from openapi_server.models.chat_update_error_schema import ChatUpdateErrorSchema
from openapi_server.models.chat_update_success_schema import ChatUpdateSuccessSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_delete(client):
    """Test case for chat_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'as_user': True,
        'channel': 'channel_example',
        'ts': 3.4
        }
    response = await client.request(
        method='POST',
        path='/api/chat.delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_delete_scheduled_message(client):
    """Test case for chat_delete_scheduled_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'as_user': True,
        'channel': 'channel_example',
        'scheduled_message_id': 'scheduled_message_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/chat.deleteScheduledMessage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chat_get_permalink(client):
    """Test case for chat_get_permalink

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example'),
                    ('message_ts', 'message_ts_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/chat.getPermalink',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_me_message(client):
    """Test case for chat_me_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/api/chat.meMessage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_post_ephemeral(client):
    """Test case for chat_post_ephemeral

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'as_user': True,
        'attachments': 'attachments_example',
        'blocks': 'blocks_example',
        'channel': 'channel_example',
        'icon_emoji': 'icon_emoji_example',
        'icon_url': 'icon_url_example',
        'link_names': True,
        'parse': 'parse_example',
        'text': 'text_example',
        'thread_ts': 'thread_ts_example',
        'user': 'user_example',
        'username': 'username_example'
        }
    response = await client.request(
        method='POST',
        path='/api/chat.postEphemeral',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_post_message(client):
    """Test case for chat_post_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'as_user': 'as_user_example',
        'attachments': 'attachments_example',
        'blocks': 'blocks_example',
        'channel': 'channel_example',
        'icon_emoji': 'icon_emoji_example',
        'icon_url': 'icon_url_example',
        'link_names': True,
        'mrkdwn': True,
        'parse': 'parse_example',
        'reply_broadcast': True,
        'text': 'text_example',
        'thread_ts': 'thread_ts_example',
        'unfurl_links': True,
        'unfurl_media': True,
        'username': 'username_example'
        }
    response = await client.request(
        method='POST',
        path='/api/chat.postMessage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_schedule_message(client):
    """Test case for chat_schedule_message

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'as_user': True,
        'attachments': 'attachments_example',
        'blocks': 'blocks_example',
        'channel': 'channel_example',
        'link_names': True,
        'parse': 'parse_example',
        'post_at': 'post_at_example',
        'reply_broadcast': True,
        'text': 'text_example',
        'thread_ts': 3.4,
        'unfurl_links': True,
        'unfurl_media': True
        }
    response = await client.request(
        method='POST',
        path='/api/chat.scheduleMessage',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chat_scheduled_messages_list_0(client):
    """Test case for chat_scheduled_messages_list_0

    
    """
    params = [('channel', 'channel_example'),
                    ('latest', 3.4),
                    ('oldest', 3.4),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/chat.scheduledMessages.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_unfurl(client):
    """Test case for chat_unfurl

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'ts': 'ts_example',
        'unfurls': 'unfurls_example',
        'user_auth_message': 'user_auth_message_example',
        'user_auth_required': True,
        'user_auth_url': 'user_auth_url_example'
        }
    response = await client.request(
        method='POST',
        path='/api/chat.unfurl',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_chat_update(client):
    """Test case for chat_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'as_user': 'as_user_example',
        'attachments': 'attachments_example',
        'blocks': 'blocks_example',
        'channel': 'channel_example',
        'link_names': 'link_names_example',
        'parse': 'parse_example',
        'text': 'text_example',
        'ts': 'ts_example'
        }
    response = await client.request(
        method='POST',
        path='/api/chat.update',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

