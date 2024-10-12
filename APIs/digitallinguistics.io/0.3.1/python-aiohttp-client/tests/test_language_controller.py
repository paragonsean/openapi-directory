# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_add_language(client):
    """Test case for add_language

    Add a new Language
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0/languages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_lexeme_by_language(client):
    """Test case for add_lexeme_by_language

    Add a new Lexeme to a Language
    """
    headers = { 
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0/languages/{language_id}/lexemes'.format(language_id='language_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_language(client):
    """Test case for delete_language

    Delete a Language by ID
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0/languages/{language_id}'.format(language_id='language_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_lexeme_by_language(client):
    """Test case for delete_lexeme_by_language

    Delete a Lexeme by ID
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0/languages/{language_id}/lexemes/{lexeme_id}'.format(language_id='language_id_example', lexeme_id='lexeme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_language(client):
    """Test case for get_language

    Retrieve a Language by ID
    """
    params = [('deleted', False)]
    headers = { 
        'if_none_match': 'if_none_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0/languages/{language_id}'.format(language_id='language_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_languages(client):
    """Test case for get_languages

    Get all Languages
    """
    params = [('deleted', False),
                    ('public', 'false')]
    headers = { 
        'continuation': 'continuation_example',
        'if_modified_since': 'if_modified_since_example',
        'max_item_count': 'max_item_count_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0/languages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lexeme_by_language(client):
    """Test case for get_lexeme_by_language

    Get a Lexeme by ID
    """
    params = [('deleted', False)]
    headers = { 
        'if_none_match': 'if_none_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0/languages/{language_id}/lexemes/{lexeme_id}'.format(language_id='language_id_example', lexeme_id='lexeme_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lexemes_by_language(client):
    """Test case for get_lexemes_by_language

    Get all Lexemes for a Language
    """
    params = [('deleted', False),
                    ('public', 'false')]
    headers = { 
        'continuation': 'continuation_example',
        'if_modified_since': 'if_modified_since_example',
        'max_item_count': 'max_item_count_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0/languages/{language_id}/lexemes'.format(language_id='language_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_language(client):
    """Test case for update_language

    Perform a partial update on a Language
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0/languages/{language_id}'.format(language_id='language_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_language(client):
    """Test case for upsert_language

    Upsert (create or replace) a Language
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0/languages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_lexeme_by_language(client):
    """Test case for upsert_lexeme_by_language

    Upsert (add or replace) a Lexeme
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0/languages/{language_id}/lexemes'.format(language_id='language_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

