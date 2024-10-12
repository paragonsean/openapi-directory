# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vmware_hierarchy_info import VmwareHierarchyInfo
from openapi_server.models.vmware_hierarchy_info_list_response import VmwareHierarchyInfoListResponse


pytestmark = pytest.mark.asyncio

async def test_get_vmware_hierarchy_export(client):
    """Test case for get_vmware_hierarchy_export

    Get Available VMware Hierarchy Objects for Export Operations
    """
    params = [('root_id', 'root_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/hierarchy/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_hierarchy_object(client):
    """Test case for get_vmware_hierarchy_object

    Get VMware Hierarchy Object Information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/hierarchy/{id}/export'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

