# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_authorization_code_definition import APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_authorization_code_definition import AuthorizationCodesSharedModelsAuthorizationCodeDefinition


pytestmark = pytest.mark.asyncio

async def test_api_v2_authorization_code_definitions_id_get(client):
    """Test case for api_v2_authorization_code_definitions_id_get

    Get an authorization code definition by its ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCodeDefinitions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_code_definitions_add_category_to_definition(client):
    """Test case for authorization_code_definitions_add_category_to_definition

    Add a category to an authorizationCodeDefintion.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/AuthorizationCodeDefinitions/{id}/Categories/{category_id}'.format(id='id_example', category_id='category_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_code_definitions_delete_authorization_code_definition(client):
    """Test case for authorization_code_definitions_delete_authorization_code_definition

    Disable an authorization code definition
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/AuthorizationCodeDefinitions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_code_definitions_get_authorization_code_definition(client):
    """Test case for authorization_code_definitions_get_authorization_code_definition

    Get authorization code definitions.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('createdByUserID', 56),
                    ('deletedByUserID', 56),
                    ('includeDeleted', True),
                    ('categoryID', 'category_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCodeDefinitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authorization_code_definitions_post_authorization_code_definition(client):
    """Test case for authorization_code_definitions_post_authorization_code_definition

    Add an authorization code definition.
    """
    body = openapi_server.AuthorizationCodesSharedModelsAuthorizationCodeDefinition()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/AuthorizationCodeDefinitions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authorization_code_definitions_put_authorization_code_definition(client):
    """Test case for authorization_code_definitions_put_authorization_code_definition

    Update an authorization code definition
    """
    body = openapi_server.AuthorizationCodesSharedModelsAuthorizationCodeDefinition()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/AuthorizationCodeDefinitions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_code_definitions_remove_category_from_definition(client):
    """Test case for authorization_code_definitions_remove_category_from_definition

    Deletes the category from the authorization code definition.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/AuthorizationCodeDefinitions/{id}/Categories/{category_id}'.format(id='id_example', category_id='category_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

