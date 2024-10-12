# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alias_model import AliasModel
from openapi_server.models.create_alias_model import CreateAliasModel
from openapi_server.models.create_alias_response_model import CreateAliasResponseModel
from openapi_server.models.get_aliases_model import GetAliasesModel


pytestmark = pytest.mark.asyncio

async def test_create_alias(client):
    """Test case for create_alias

    Create alias
    """
    body = {"snippets":[{"id":"id","parameters":{"key":"parameters"}},{"id":"id","parameters":{"key":"parameters"}}],"destinations":[{"country":"country","os":"os","url":"url"},{"country":"country","os":"os","url":"url"}],"metatags":[{"name":"name","content":"content"},{"name":"name","content":"content"}]}
    params = [('domainName', 'short.fyi'),
                    ('aliasName', '@rnd')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/aliases',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_alias(client):
    """Test case for delete_alias

    Delete alias
    """
    params = [('domainName', 'short.fyi'),
                    ('aliasName', 'aBcDe012')]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/aliases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_alias(client):
    """Test case for get_alias

    Get alias
    """
    params = [('domainName', 'short.fyi'),
                    ('aliasName', 'aBcDe012')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/aliases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_aliases(client):
    """Test case for get_aliases

    Get aliases by domain
    """
    params = [('domainName', 'short.fyi'),
                    ('continueFrom', '1588788835614657618'),
                    ('limit', 1000)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/aliases/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_alias(client):
    """Test case for update_alias

    Update alias
    """
    body = {"snippets":[{"id":"id","parameters":{"key":"parameters"}},{"id":"id","parameters":{"key":"parameters"}}],"destinations":[{"country":"country","os":"os","url":"url"},{"country":"country","os":"os","url":"url"}],"metatags":[{"name":"name","content":"content"},{"name":"name","content":"content"}]}
    params = [('domainName', 'short.fyi'),
                    ('aliasName', 'aBcDe012')]
    headers = { 
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/aliases',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

