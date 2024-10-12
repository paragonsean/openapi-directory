# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_change_password(client):
    """Test case for change_password

    Changes a user’s password.
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'text/plain',
        'x_request_id': 'test-id',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/authn/{account}/password'.format(account='account_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enable_authenticator(client):
    """Test case for enable_authenticator

    Enables or disables authenticator defined without service_id.
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
        'Authorization': 'BasicZm9vOmJhcg==',
        
        'conjurAuth': 'special-key',
    }
    data = {
        'enabled': True
        }
    response = await client.request(
        method='PATCH',
        path='/{authenticator}/{account}'.format(authenticator='authn-gcp', account='dev'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_enable_authenticator_instance(client):
    """Test case for enable_authenticator_instance

    Enables or disables authenticator service instances.
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{authenticator}/{service_id}/{account}'.format(authenticator=openapi_server.ERRORUNKNOWN(), service_id='prod%2fgke', account='dev'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_get_access_token(client):
    """Test case for get_access_token

    Gets a short-lived access token, which is required in the header of most subsequent API requests. 
    """
    body = None
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'text/plain',
        'x_request_id': 'test-id',
        'accept_encoding': application/json,
    }
    response = await client.request(
        method='POST',
        path='/authn/{account}/{login}/authenticate'.format(account='account_example', login='admin'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_get_access_token_via_aws(client):
    """Test case for get_access_token_via_aws

    Get a short-lived access token for applications running in AWS.
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'text/plain',
        'x_request_id': 'test-id',
        'accept_encoding': application/json,
    }
    response = await client.request(
        method='POST',
        path='/authn-iam/{service_id}/{account}/{login}/authenticate'.format(service_id='prod%2fgke', account='account_example', login=openapi_server.ERRORUNKNOWN()),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_access_token_via_azure(client):
    """Test case for get_access_token_via_azure

    Gets a short-lived access token for applications running in Azure.
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
        'accept_encoding': application/json,
    }
    data = {
        'jwt': 'jwt_example'
        }
    response = await client.request(
        method='POST',
        path='/authn-azure/{service_id}/{account}/{login}/authenticate'.format(service_id='prod%2fgke', account='account_example', login=openapi_server.ERRORUNKNOWN()),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_access_token_via_gcp(client):
    """Test case for get_access_token_via_gcp

    Gets a short-lived access token for applications running in Google Cloud Platform. 
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
        'accept_encoding': 'accept_encoding_example',
    }
    data = {
        'jwt': 'jwt_example'
        }
    response = await client.request(
        method='POST',
        path='/authn-gcp/{account}/authenticate'.format(account='dev'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_access_token_via_jwt(client):
    """Test case for get_access_token_via_jwt

    Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
    }
    data = {
        'jwt': 'jwt_example'
        }
    response = await client.request(
        method='POST',
        path='/authn-jwt/{service_id}/{account}/authenticate'.format(account='account_example', service_id='prod%2fgke'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_access_token_via_jwt_with_id(client):
    """Test case for get_access_token_via_jwt_with_id

    Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \"ID\" 
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
    }
    response = await client.request(
        method='POST',
        path='/authn-jwt/{service_id}/{account}/{id}/authenticate'.format(account='account_example', id='SomeUserID', service_id='prod%2fgke'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_access_token_via_kubernetes(client):
    """Test case for get_access_token_via_kubernetes

    Gets a short-lived access token for applications running in Kubernetes.
    """
    headers = { 
        'x_request_id': 'test-id',
        'accept_encoding': application/json,
        
    }
    response = await client.request(
        method='POST',
        path='/authn-k8s/{service_id}/{account}/{login}/authenticate'.format(service_id='prod%2fgke', account='account_example', login=openapi_server.ERRORUNKNOWN()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_get_access_token_via_ldap(client):
    """Test case for get_access_token_via_ldap

    Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 
    """
    body = None
    headers = { 
        'Content-Type': 'text/plain',
        'x_request_id': 'test-id',
        'accept_encoding': application/json,
    }
    response = await client.request(
        method='POST',
        path='/authn-ldap/{service_id}/{account}/{login}/authenticate'.format(service_id='prod%2fgke', account='account_example', login=openapi_server.ERRORUNKNOWN()),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_access_token_via_oidc(client):
    """Test case for get_access_token_via_oidc

    Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
    }
    data = {
        'id_token': 'id_token_example'
        }
    response = await client.request(
        method='POST',
        path='/authn-oidc/{service_id}/{account}/authenticate'.format(service_id='prod%2fgke', account='account_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_key(client):
    """Test case for get_api_key

    Gets the API key of a user given the username and password via HTTP Basic Authentication. 
    """
    headers = { 
        'Accept': 'text/plain',
        'x_request_id': 'test-id',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/authn/{account}/login'.format(account='account_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_key_via_ldap(client):
    """Test case for get_api_key_via_ldap

    Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 
    """
    headers = { 
        'x_request_id': 'test-id',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/authn-ldap/{service_id}/{account}/login'.format(service_id='prod%2fgke', account='account_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_k8s_inject_client_cert(client):
    """Test case for k8s_inject_client_cert

    For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application's Kubernetes pod. 
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'text/plain',
        'x_request_id': 'test-id',
        'host_id_prefix': 'host/conjur/authn-k8s/my-authenticator-id/apps',
        'Authorization': 'BasicZm9vOmJhcg==',
        
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/authn-k8s/{service_id}/inject_client_cert'.format(service_id='prod%2fgke'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rotate_api_key(client):
    """Test case for rotate_api_key

    Rotates a role's API key.
    """
    params = [('role', 'role_example')]
    headers = { 
        'x_request_id': 'test-id',
        'Authorization': 'BasicZm9vOmJhcg==',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/authn/{account}/api_key'.format(account='account_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

