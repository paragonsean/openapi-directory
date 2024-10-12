# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.counter import Counter
from openapi_server.models.keycloak_config import KeycloakConfig
from openapi_server.models.secret import Secret


pytestmark = pytest.mark.asyncio

async def test_create_secret(client):
    """Test case for create_secret

    Create a new Secret
    """
    body = "{\n    \"id\": \"5be58fb51ed744d1b87481bd\",\n    \"name\": \"Gogs internal\",\n    \"description\": \"Gogs internal corporate repository\",\n    \"username\": \"team\",\n    \"password\": \"team\",\n    \"caCertPem\": \"-----BEGIN CERTIFICATE-----\\nMIIC6jCCAdKgAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBtvcGVu\\nc2hpZnQtc2lnbmVyQDE1MzE5MTA5MDIwHhcNMTgwNzE4MTA0ODIyWhcNMjMwNzE3\\nMTA0ODIzWjAmMSQwIgYDVQQDDBtvcGVuc2hpZnQtc2lnbmVyQDE1MzE5MTA5MDIw\\nggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCyaP1jlpnm8WpfCSnUa8Qt\\nhdUynOLLgElUtpWoW25wB9tO2ZmEj+fVsTyzEsW8+nfXXfRsBEzPm2ze9uEMTPTB\\nAY0k7DbLZfjmF1lCckUvvh1rR/8hoPuXETjXUuOdtm7gRHTOxLQyH2Qi/q0DYJAn\\nprKyRCLa35pRnykL6v4bHkqFnqDEho63i29XHhm2703moh4YCl1iYa2Rh6D44cjn\\n8lBCq6o7zoZSmc/aBamRkQrfZYcolR8OUtDS4oEB0zMftmea2ycashsLEMB+Cq4r\\n64NI2QM7qOxdTuXsDivHfLl7RTuWEOozGaJXoiPaGU/3d/KnY0gKJ2TC1KXt6Xjn\\nAgMBAAGjIzAhMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMBAf8EBTADAQH/MA0GCSqG\\nSIb3DQEBCwUAA4IBAQCeUmxfUzw0VAFG6HvVYIsfvumiIvsSWmclGIZqNJyfMHFD\\nMy6xzPRNNfWe5aumGTJsuIzuXfDRcdO7KmH1d2/5brkvWpxp6svVrYPvcoXjl4VN\\nQR2mv5Di4KHfiiwvP3eeewjUZj+uREGqX2fcbJPHTPy32Kpb0H8Uy09BklhjC7QP\\ngRAGexPhU1oBL/CoOwbHKcQ6dxs/y1SxzI8gXEtec4z62CroI13iT7U0UjSqFBE4\\nKfrJombfz0d68781Z40ll+8my251ZNfbLBhQ3UHW0JnkBEQkE1aBorUoj2iakYvx\\nA2qZh+8q2b8MwMb2YsQ0dlxKd6c4tN3lmMnO4bnd\\n-----END CERTIFICATE-----\"\n}"
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/secrets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_secret(client):
    """Test case for delete_secret

    Delete Secret
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/secrets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_features_configuration(client):
    """Test case for get_features_configuration

    Get features configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/features/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keycloak_config(client):
    """Test case for get_keycloak_config

    Get authentification configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/keycloak/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secret(client):
    """Test case for get_secret

    Get Secret
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/secrets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secrets(client):
    """Test case for get_secrets

    Get Secrets
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/secrets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secrets_counter(client):
    """Test case for get_secrets_counter

    Get the Secrets counter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/secrets/count',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_secret(client):
    """Test case for update_secret

    Update Secret
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/secrets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

