# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tokens_webhooks import TokensWebhooks


pytestmark = pytest.mark.asyncio

async def test_add_tokens_webhooks_by_token(client):
    """Test case for add_tokens_webhooks_by_token

    addTokensWebhooksByToken()
    """
    body = openapi_server.TokensWebhooks()
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/tokens/{token}/webhooks'.format(token='token_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tokens_by_token(client):
    """Test case for delete_tokens_by_token

    deleteTokensByToken()
    """
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/tokens/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tokens_webhooks_by_token_by_id_webhook(client):
    """Test case for delete_tokens_webhooks_by_token_by_id_webhook

    deleteTokensWebhooksByTokenByIdWebhook()
    """
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/tokens/{token}/webhooks/{id_webhook}'.format(token='token_example', id_webhook='id_webhook_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tokens_by_token(client):
    """Test case for get_tokens_by_token

    getTokensByToken()
    """
    params = [('fields', 'all'),
                    ('webhooks', 'webhooks_example'),
                    ('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/tokens/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tokens_by_token_by_field(client):
    """Test case for get_tokens_by_token_by_field

    getTokensByTokenByField()
    """
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/tokens/{token}/{_field}'.format(token='token_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tokens_member_by_token(client):
    """Test case for get_tokens_member_by_token

    getTokensMemberByToken()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/tokens/{token}/member'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tokens_member_by_token_by_field(client):
    """Test case for get_tokens_member_by_token_by_field

    getTokensMemberByTokenByField()
    """
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/tokens/{token}/member/{_field}'.format(token='token_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tokens_webhooks_by_token(client):
    """Test case for get_tokens_webhooks_by_token

    getTokensWebhooksByToken()
    """
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/tokens/{token}/webhooks'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tokens_webhooks_by_token_by_id_webhook(client):
    """Test case for get_tokens_webhooks_by_token_by_id_webhook

    getTokensWebhooksByTokenByIdWebhook()
    """
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/tokens/{token}/webhooks/{id_webhook}'.format(token='token_example', id_webhook='id_webhook_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_tokens_webhooks_by_token(client):
    """Test case for update_tokens_webhooks_by_token

    updateTokensWebhooksByToken()
    """
    body = openapi_server.TokensWebhooks()
    params = [('key', 'key_example'),
                    ('token2', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/tokens/{token}/webhooks'.format(token='token_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

