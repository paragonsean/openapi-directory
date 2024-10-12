# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.registry_configuration import RegistryConfiguration
from openapi_server.models.registry_configuration_request import RegistryConfigurationRequest


pytestmark = pytest.mark.asyncio

async def test_create_registry(client):
    """Test case for create_registry

    Add a new registry
    """
    body = {"registry":"registry","registry_type":"registry_type","registry_user":"registry_user","registry_name":"registry_name","registry_pass":"registry_pass","registry_verify":True}
    params = [('validate', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='POST',
        path='/registries',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_registry(client):
    """Test case for delete_registry

    Delete a registry configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/registries/{registry}'.format(registry='registry_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registry(client):
    """Test case for get_registry

    Get a specific registry configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/registries/{registry}'.format(registry='registry_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_registries(client):
    """Test case for list_registries

    List configured registries
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/registries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_registry(client):
    """Test case for update_registry

    Update/replace a registry configuration
    """
    body = {"registry":"registry","registry_type":"registry_type","registry_user":"registry_user","registry_name":"registry_name","registry_pass":"registry_pass","registry_verify":True}
    params = [('validate', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='PUT',
        path='/registries/{registry}'.format(registry='registry_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

