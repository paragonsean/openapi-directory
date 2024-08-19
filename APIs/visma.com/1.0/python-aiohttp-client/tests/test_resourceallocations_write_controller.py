# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.resource_allocation_input_model import ResourceAllocationInputModel
from openapi_server.models.resource_allocation_output_model import ResourceAllocationOutputModel
from openapi_server.models.role_allocation_input_model import RoleAllocationInputModel
from openapi_server.models.role_allocation_output_model import RoleAllocationOutputModel


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_patch_resource_allocation(client):
    """Test case for resource_allocations_patch_resource_allocation

    Update (Patch) a resource allocation or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/resourceallocations/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_allocations_post_resource_allocation(client):
    """Test case for resource_allocations_post_resource_allocation

    Insert a resource allocation
    """
    body = {"allocationPercentage":6,"phase":{"guid":"guid"},"endDate":"2000-01-23","allocationHours":0.8008281904610115,"project":{"guid":"guid"},"user":{"guid":"guid"},"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/resourceallocations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_allocations_patch_role_allocation(client):
    """Test case for role_allocations_patch_role_allocation

    Update (Patch) a role allocation.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/roleallocations/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_allocations_post_role_allocation(client):
    """Test case for role_allocations_post_role_allocation

    Insert a role allocation.
    """
    body = {"phase":{"guid":"guid"},"role":{"guid":"guid"},"endDate":"2000-01-23","allocationHours":0.8008281904610115,"project":{"guid":"guid"},"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/roleallocations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

