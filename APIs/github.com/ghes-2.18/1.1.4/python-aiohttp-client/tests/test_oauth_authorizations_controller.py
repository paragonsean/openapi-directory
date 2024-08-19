# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_grant import ApplicationGrant
from openapi_server.models.authorization import Authorization
from openapi_server.models.authorization_with_user import AuthorizationWithUser
from openapi_server.models.basic_error import BasicError
from openapi_server.models.oauth_authorizations_create_authorization_request import OauthAuthorizationsCreateAuthorizationRequest
from openapi_server.models.oauth_authorizations_get_or_create_authorization_for_app_and_fingerprint_request import OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest
from openapi_server.models.oauth_authorizations_get_or_create_authorization_for_app_request import OauthAuthorizationsGetOrCreateAuthorizationForAppRequest
from openapi_server.models.oauth_authorizations_update_authorization_request import OauthAuthorizationsUpdateAuthorizationRequest
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_check_authorization(client):
    """Test case for oauth_authorizations_check_authorization

    Check an authorization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/applications/{client_id}/tokens/{access_token}'.format(client_id='client_id_example', access_token='access_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_create_authorization(client):
    """Test case for oauth_authorizations_create_authorization

    Create a new authorization
    """
    body = openapi_server.OauthAuthorizationsCreateAuthorizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/authorizations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_delete_authorization(client):
    """Test case for oauth_authorizations_delete_authorization

    Delete an authorization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/authorizations/{authorization_id}'.format(authorization_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_delete_grant(client):
    """Test case for oauth_authorizations_delete_grant

    Delete a grant
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/applications/grants/{grant_id}'.format(grant_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_get_authorization(client):
    """Test case for oauth_authorizations_get_authorization

    Get a single authorization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/authorizations/{authorization_id}'.format(authorization_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_get_grant(client):
    """Test case for oauth_authorizations_get_grant

    Get a single grant
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/applications/grants/{grant_id}'.format(grant_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_get_or_create_authorization_for_app(client):
    """Test case for oauth_authorizations_get_or_create_authorization_for_app

    Get-or-create an authorization for a specific app
    """
    body = openapi_server.OauthAuthorizationsGetOrCreateAuthorizationForAppRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/authorizations/clients/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_get_or_create_authorization_for_app_and_fingerprint(client):
    """Test case for oauth_authorizations_get_or_create_authorization_for_app_and_fingerprint

    Get-or-create an authorization for a specific app and fingerprint
    """
    body = openapi_server.OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/authorizations/clients/{client_id}/{fingerprint}'.format(client_id='client_id_example', fingerprint='fingerprint_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_list_authorizations(client):
    """Test case for oauth_authorizations_list_authorizations

    List your authorizations
    """
    params = [('per_page', 30),
                    ('page', 1),
                    ('client_id', 'client_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/authorizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_list_grants(client):
    """Test case for oauth_authorizations_list_grants

    List your grants
    """
    params = [('per_page', 30),
                    ('page', 1),
                    ('client_id', 'client_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/applications/grants',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_reset_authorization(client):
    """Test case for oauth_authorizations_reset_authorization

    Reset an authorization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/applications/{client_id}/tokens/{access_token}'.format(client_id='client_id_example', access_token='access_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_revoke_authorization_for_application(client):
    """Test case for oauth_authorizations_revoke_authorization_for_application

    Revoke an authorization for an application
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/applications/{client_id}/tokens/{access_token}'.format(client_id='client_id_example', access_token='access_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_revoke_grant_for_application(client):
    """Test case for oauth_authorizations_revoke_grant_for_application

    Revoke a grant for an application
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/applications/{client_id}/grants/{access_token}'.format(client_id='client_id_example', access_token='access_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_authorizations_update_authorization(client):
    """Test case for oauth_authorizations_update_authorization

    Update an existing authorization
    """
    body = openapi_server.OauthAuthorizationsUpdateAuthorizationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/authorizations/{authorization_id}'.format(authorization_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

