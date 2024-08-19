# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_package_type_request_body import CreatePackageTypeRequestBody
from openapi_server.models.create_package_type_response_body import CreatePackageTypeResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_package_type_by_id_response_body import GetPackageTypeByIdResponseBody
from openapi_server.models.list_package_types_response_body import ListPackageTypesResponseBody
from openapi_server.models.update_package_type_request_body import UpdatePackageTypeRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_package_type(client):
    """Test case for create_package_type

    Create Custom Package Type
    """
    body = openapi_server.CreatePackageTypeRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/packages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_package_type(client):
    """Test case for delete_package_type

    Delete A Custom Package By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/packages/{package_id}'.format(package_id='package_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_package_type_by_id(client):
    """Test case for get_package_type_by_id

    Get Custom Package Type By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/packages/{package_id}'.format(package_id='package_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_package_types(client):
    """Test case for list_package_types

    List Custom Package Types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/packages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_package_type(client):
    """Test case for update_package_type

    Update Custom Package Type By ID
    """
    body = openapi_server.UpdatePackageTypeRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/packages/{package_id}'.format(package_id='package_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

