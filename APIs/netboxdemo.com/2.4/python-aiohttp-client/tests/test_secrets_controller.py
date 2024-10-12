# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.secret import Secret
from openapi_server.models.secret_role import SecretRole
from openapi_server.models.secrets_secret_roles_list200_response import SecretsSecretRolesList200Response
from openapi_server.models.secrets_secrets_list200_response import SecretsSecretsList200Response
from openapi_server.models.writable_secret import WritableSecret


pytestmark = pytest.mark.asyncio

async def test_secrets_choices_list(client):
    """Test case for secrets_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/secrets/_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_choices_read(client):
    """Test case for secrets_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/secrets/_choices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_generate_rsa_key_pair_list(client):
    """Test case for secrets_generate_rsa_key_pair_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/secrets/generate-rsa-key-pair/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_get_session_key_create(client):
    """Test case for secrets_get_session_key_create

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/secrets/get-session-key/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_roles_create(client):
    """Test case for secrets_secret_roles_create

    
    """
    body = {"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/secrets/secret-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_roles_delete(client):
    """Test case for secrets_secret_roles_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/secrets/secret-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_roles_list(client):
    """Test case for secrets_secret_roles_list

    
    """
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/secrets/secret-roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_roles_partial_update(client):
    """Test case for secrets_secret_roles_partial_update

    
    """
    body = {"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/secrets/secret-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_roles_read(client):
    """Test case for secrets_secret_roles_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/secrets/secret-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secret_roles_update(client):
    """Test case for secrets_secret_roles_update

    
    """
    body = {"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/secrets/secret-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secrets_create(client):
    """Test case for secrets_secrets_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","name":"name","plaintext":"plaintext","id":6,"device":0,"hash":"hash","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/secrets/secrets/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secrets_delete(client):
    """Test case for secrets_secrets_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/secrets/secrets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secrets_list(client):
    """Test case for secrets_secrets_list

    
    """
    params = [('name', 'name_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/secrets/secrets/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secrets_partial_update(client):
    """Test case for secrets_secrets_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","name":"name","plaintext":"plaintext","id":6,"device":0,"hash":"hash","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/secrets/secrets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secrets_read(client):
    """Test case for secrets_secrets_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/secrets/secrets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_secrets_update(client):
    """Test case for secrets_secrets_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":1,"created":"2000-01-23","custom_fields":"{}","name":"name","plaintext":"plaintext","id":6,"device":0,"hash":"hash","tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/secrets/secrets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

