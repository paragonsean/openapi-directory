# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_env_vars_request_inner import CreateEnvVarsRequestInner
from openapi_server.models.env_var import EnvVar
from openapi_server.models.error import Error
from openapi_server.models.set_env_var_value_request import SetEnvVarValueRequest


pytestmark = pytest.mark.asyncio

async def test_create_env_vars(client):
    """Test case for create_env_vars

    
    """
    env_vars = [openapi_server.CreateEnvVarsRequestInner()]
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts/{account_id}/env'.format(account_id='account_id_example'),
        headers=headers,
        json=env_vars,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_env_var(client):
    """Test case for delete_env_var

    
    """
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/accounts/{account_id}/env/{key}'.format(account_id='account_id_example', key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_env_var_value(client):
    """Test case for delete_env_var_value

    
    """
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/accounts/{account_id}/env/{key}/value/{id}'.format(account_id='account_id_example', id='id_example', key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_env_var(client):
    """Test case for get_env_var

    
    """
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{account_id}/env/{key}'.format(account_id='account_id_example', key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_env_vars(client):
    """Test case for get_env_vars

    
    """
    params = [('context_name', 'context_name_example'),
                    ('scope', 'scope_example'),
                    ('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{account_id}/env'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_env_var_value(client):
    """Test case for set_env_var_value

    
    """
    env_var = openapi_server.SetEnvVarValueRequest()
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/accounts/{account_id}/env/{key}'.format(account_id='account_id_example', key='key_example'),
        headers=headers,
        json=env_var,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_env_var(client):
    """Test case for update_env_var

    
    """
    env_var = openapi_server.CreateEnvVarsRequestInner()
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/accounts/{account_id}/env/{key}'.format(account_id='account_id_example', key='key_example'),
        headers=headers,
        json=env_var,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

