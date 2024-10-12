# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentication_options import AuthenticationOptions
from openapi_server.models.authentication_token import AuthenticationToken
from openapi_server.models.credential import Credential
from openapi_server.models.customer_jwt import CustomerJWT
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.reset_password_token import ResetPasswordToken


pytestmark = pytest.mark.asyncio

async def test_delete_authentication_token(client):
    """Test case for delete_authentication_token

    Logout a customer
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/authentication-tokens/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_credential(client):
    """Test case for delete_credential

    Delete a credential
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/credentials/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_password_token(client):
    """Test case for delete_password_token

    Delete a Reset Password Token
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/password-tokens/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_authentication_option(client):
    """Test case for get_authentication_option

    Read current authentication options
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/authentication-options',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_authentication_token_collection(client):
    """Test case for get_authentication_token_collection

    Retrieve a list of auth tokens
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/authentication-tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_authentication_token_verification(client):
    """Test case for get_authentication_token_verification

    Verify
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/authentication-tokens/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_credential(client):
    """Test case for get_credential

    Retrieve a credential
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/credentials/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_credential_collection(client):
    """Test case for get_credential_collection

    Retrieve a list of credentials
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/credentials',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_password_token(client):
    """Test case for get_password_token

    Retrieve a Reset Password Token
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/password-tokens/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_password_token_collection(client):
    """Test case for get_password_token_collection

    Retrieve a list of tokens
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/password-tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_authentication_token(client):
    """Test case for post_authentication_token

    Login
    """
    body = {"mode":"password","otpRequired":True,"credentialId":"","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/authentication-tokens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_authentication_token_exchange(client):
    """Test case for post_authentication_token_exchange

    Exchange
    """
    body = {"updatedTime":"","_links":[{"rel":"customer"},{"rel":"customer"}],"customerId":"","createdTime":"2000-01-23T04:56:07.000+00:00","acl":[{"permissions":"","scope":""},{"permissions":"","scope":""}],"id":"","invalidate":True,"type":"customer","customClaims":{"documents":["identity-proof","address-proof"],"redirectUrl":"https://mywebsite.com"},"expiredTime":"2000-01-23T04:56:07.000+00:00","oneTimePassword":"123456","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
        'PublishableApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/authentication-tokens/{token}/exchange'.format(token='token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_credential(client):
    """Test case for post_credential

    Create a credential
    """
    body = {"password":"password","_links":[{"rel":"self"},{"rel":"self"}],"customerId":"customerId","id":"","expiredTime":"2000-01-23T04:56:07.000+00:00","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/credentials',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_password_token(client):
    """Test case for post_password_token

    Create a Reset Password Token
    """
    body = {"_links":[{"rel":"self"},{"rel":"self"}],"credentialId":"credentialId","expiredTime":"2000-01-23T04:56:07.000+00:00","token":"token","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/password-tokens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_authentication_option(client):
    """Test case for put_authentication_option

    Change authentication options
    """
    body = {"authTokenTtl":0,"resetTokenTtl":1,"otpRequired":True,"passwordPattern":"passwordPattern","credentialTtl":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/authentication-options',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_credential(client):
    """Test case for put_credential

    Create or update a credential with predefined ID
    """
    body = {"password":"password","_links":[{"rel":"self"},{"rel":"self"}],"customerId":"customerId","id":"","expiredTime":"2000-01-23T04:56:07.000+00:00","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/credentials/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

