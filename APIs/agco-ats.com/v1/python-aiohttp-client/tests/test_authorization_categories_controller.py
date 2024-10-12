# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_category import APIIPagedResponseAuthorizationCodesSharedModelsCategory
from openapi_server.models.apii_paged_response_authorization_codes_shared_models_category_user_report import APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_category import AuthorizationCodesSharedModelsCategory


pytestmark = pytest.mark.asyncio

async def test_authorization_categories_add_user(client):
    """Test case for authorization_categories_add_user

    Add a category that a user can see.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/AuthorizationCategories/{id}/Users/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_categories_delete(client):
    """Test case for authorization_categories_delete

    Remove an authorization category.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/AuthorizationCategories/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_categories_get(client):
    """Test case for authorization_categories_get

    Get authorization categories.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('userID', 56),
                    ('definitionID', 'definition_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_categories_get_users(client):
    """Test case for authorization_categories_get_users

    Returns a report of access that users have to Authorization Categories.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('userIDs', 'user_ids_example'),
                    ('categoryIDs', 'category_ids_example'),
                    ('includeCategories', True),
                    ('includeUsers', True),
                    ('userSearch', 'user_search_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCategories/Users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authorization_categories_post(client):
    """Test case for authorization_categories_post

    Add an authorization category.
    """
    body = openapi_server.AuthorizationCodesSharedModelsCategory()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/AuthorizationCategories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authorization_categories_put(client):
    """Test case for authorization_categories_put

    Update an authorization category.
    """
    body = openapi_server.AuthorizationCodesSharedModelsCategory()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/AuthorizationCategories/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_categories_remove_user(client):
    """Test case for authorization_categories_remove_user

    Deletes a category a user could see.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/AuthorizationCategories/{id}/Users/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

