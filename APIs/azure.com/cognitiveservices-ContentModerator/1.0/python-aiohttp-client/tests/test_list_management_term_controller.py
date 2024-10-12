# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.terms import Terms


pytestmark = pytest.mark.asyncio

async def test_list_management_term_add_term(client):
    """Test case for list_management_term_add_term

    
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/lists/v1.0/termlists/{list_id}/terms/{term}'.format(list_id='list_id_example', term='term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_term_delete_all_terms(client):
    """Test case for list_management_term_delete_all_terms

    
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/contentmoderator/lists/v1.0/termlists/{list_id}/terms'.format(list_id='list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_term_delete_term(client):
    """Test case for list_management_term_delete_term

    
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/contentmoderator/lists/v1.0/termlists/{list_id}/terms/{term}'.format(list_id='list_id_example', term='term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_term_get_all_terms(client):
    """Test case for list_management_term_get_all_terms

    
    """
    params = [('language', 'language_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentmoderator/lists/v1.0/termlists/{list_id}/terms'.format(list_id='list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

