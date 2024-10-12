# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_authorization_code import APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_authorization_code import AuthorizationCodesSharedModelsAuthorizationCode
from openapi_server.models.authorization_codes_shared_models_authorization_contact_information import AuthorizationCodesSharedModelsAuthorizationContactInformation
from openapi_server.models.authorization_codes_shared_models_code_validation_model import AuthorizationCodesSharedModelsCodeValidationModel


pytestmark = pytest.mark.asyncio

async def test_authorization_codes_delete_authorization_code(client):
    """Test case for authorization_codes_delete_authorization_code

    Hide an authorization code.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/AuthorizationCodes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_codes_get_authorization_code(client):
    """Test case for authorization_codes_get_authorization_code

    Get an authorization code by its ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCodes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_codes_get_authorization_codes(client):
    """Test case for authorization_codes_get_authorization_codes

    Get authorization codes.
    """
    params = [('code', 'code_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('definitionID', 'definition_id_example'),
                    ('createdByUserID', 56),
                    ('deletedByUserID', 56),
                    ('includeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_codes_get_contact_information(client):
    """Test case for authorization_codes_get_contact_information

    Get contact information for an authorization code.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCodes/{id}/ContactInformation'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authorization_codes_post_authorization_code(client):
    """Test case for authorization_codes_post_authorization_code

    Generates an authorization code using the provided definition and parameters.
    """
    body = openapi_server.AuthorizationCodesSharedModelsAuthorizationCode()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/AuthorizationCodes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authorization_codes_put_authorization_code(client):
    """Test case for authorization_codes_put_authorization_code

    Update an authorization code.
    """
    body = openapi_server.AuthorizationCodesSharedModelsAuthorizationCode()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/AuthorizationCodes/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorization_codes_validate_authorization_code(client):
    """Test case for authorization_codes_validate_authorization_code

    No Documentation Found.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationCodes/{id}/Validate'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

