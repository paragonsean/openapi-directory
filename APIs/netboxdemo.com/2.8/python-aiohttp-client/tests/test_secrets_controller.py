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

async def test_secrets_generate_rsa_key_pair_list(client):
    """Test case for secrets_generate_rsa_key_pair_list

    This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.
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
    body = {"secret_count":1,"name":"name","description":"description","id":6,"slug":"slug"}
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
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('q', 'q_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
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
    body = {"secret_count":1,"name":"name","description":"description","id":6,"slug":"slug"}
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
    body = {"secret_count":1,"name":"name","description":"description","id":6,"slug":"slug"}
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
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('tag__n', 'tag__n_example'),
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

