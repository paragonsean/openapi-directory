# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.management_group_list_result import ManagementGroupListResult
from openapi_server.models.management_group_with_hierarchy import ManagementGroupWithHierarchy


pytestmark = pytest.mark.asyncio

async def test_management_groups_get(client):
    """Test case for management_groups_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example'),
                    ('$recurse', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_groups_list(client):
    """Test case for management_groups_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

