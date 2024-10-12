# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.incoming_webhook import IncomingWebhook


pytestmark = pytest.mark.asyncio

async def test_create_incoming_webhook(client):
    """Test case for create_incoming_webhook

    Create a new webhook for existing conversation.
    """
    params = [('name', 'name_example'),
                    ('userId', 'user_id_example'),
                    ('description', 'description_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest/v2/webhooks/incoming/create/{conversation_id}'.format(conversation_id='conversation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_incoming_webhook(client):
    """Test case for delete_incoming_webhook

    Delete an existing webhook
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/webhooks/incoming/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_incoming_webhook_by_user(client):
    """Test case for get_incoming_webhook_by_user

    Get all webhooks of a special user.
    """
    params = [('pagesize', 25),
                    ('searchpointer', 'searchpointer_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/webhooks/incoming/user/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_post_webhook_as_slack_message(client):
    """Test case for post_webhook_as_slack_message

    Post text item for conversation via webhook.
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'file_url': 'file_url_example',
        'filename': 'filename_example',
        'markdown': True,
        'subject': 'subject_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/webhooks/incoming/{webhook_id}'.format(webhook_id='webhook_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

