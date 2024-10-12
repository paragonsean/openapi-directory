# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_add_lexeme(client):
    """Test case for add_lexeme

    Add a new Lexeme
    """
    params = [('languageID', 'language_id_example')]
    headers = { 
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0/lexemes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_lexeme_by_language_0(client):
    """Test case for add_lexeme_by_language_0

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

async def test_delete_lexeme(client):
    """Test case for delete_lexeme

    Delete a Lexeme by ID
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0/lexemes/{lexeme_id}'.format(lexeme_id='lexeme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_lexeme_by_language_0(client):
    """Test case for delete_lexeme_by_language_0

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

async def test_get_lexeme(client):
    """Test case for get_lexeme

    Get a Lexeme by ID
    """
    params = [('deleted', False)]
    headers = { 
        'if_none_match': 'if_none_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0/lexemes/{lexeme_id}'.format(lexeme_id='lexeme_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lexeme_by_language_0(client):
    """Test case for get_lexeme_by_language_0

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

async def test_get_lexemes(client):
    """Test case for get_lexemes

    Get all Lexemes
    """
    params = [('deleted', False),
                    ('languageID', 'language_id_example'),
                    ('public', 'false')]
    headers = { 
        'continuation': 'continuation_example',
        'if_modified_since': 'if_modified_since_example',
        'max_item_count': 'max_item_count_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0/lexemes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lexemes_by_language_0(client):
    """Test case for get_lexemes_by_language_0

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

async def test_update_lexeme(client):
    """Test case for update_lexeme

    Perform a partial update on a Lexeme
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0/lexemes/{lexeme_id}'.format(lexeme_id='lexeme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_lexeme_by_language(client):
    """Test case for update_lexeme_by_language

    Perform a partial update on a Lexeme
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0/languages/{language_id}/lexemes/{lexeme_id}'.format(language_id='language_id_example', lexeme_id='lexeme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_lexeme(client):
    """Test case for upsert_lexeme

    Upsert (add or replace) a Lexeme
    """
    params = [('languageID', 'language_id_example')]
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0/lexemes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_lexeme_by_language_0(client):
    """Test case for upsert_lexeme_by_language_0

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

