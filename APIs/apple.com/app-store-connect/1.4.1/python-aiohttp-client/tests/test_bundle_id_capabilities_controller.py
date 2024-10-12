# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_id_capability_create_request import BundleIdCapabilityCreateRequest
from openapi_server.models.bundle_id_capability_response import BundleIdCapabilityResponse
from openapi_server.models.bundle_id_capability_update_request import BundleIdCapabilityUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_bundle_id_capabilities_create_instance(client):
    """Test case for bundle_id_capabilities_create_instance

    
    """
    body = {"data":{"relationships":{"bundleId":{"data":{"id":"id","type":"bundleIds"}}},"attributes":{"settings":[{"minInstances":0,"visible":True,"allowedInstances":"ENTRY","enabledByDefault":True,"name":"name","options":[{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"},{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"}],"description":"description","key":"ICLOUD_VERSION"},{"minInstances":0,"visible":True,"allowedInstances":"ENTRY","enabledByDefault":True,"name":"name","options":[{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"},{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"}],"description":"description","key":"ICLOUD_VERSION"}],"capabilityType":"ICLOUD"},"type":"bundleIdCapabilities"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/bundleIdCapabilities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_id_capabilities_delete_instance(client):
    """Test case for bundle_id_capabilities_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/bundleIdCapabilities/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_id_capabilities_update_instance(client):
    """Test case for bundle_id_capabilities_update_instance

    
    """
    body = {"data":{"attributes":{"settings":[{"minInstances":0,"visible":True,"allowedInstances":"ENTRY","enabledByDefault":True,"name":"name","options":[{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"},{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"}],"description":"description","key":"ICLOUD_VERSION"},{"minInstances":0,"visible":True,"allowedInstances":"ENTRY","enabledByDefault":True,"name":"name","options":[{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"},{"supportsWildcard":True,"enabledByDefault":True,"name":"name","description":"description","enabled":True,"key":"XCODE_5"}],"description":"description","key":"ICLOUD_VERSION"}],"capabilityType":"ICLOUD"},"id":"id","type":"bundleIdCapabilities"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/bundleIdCapabilities/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

