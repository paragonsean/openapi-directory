# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_role_assignment_list_result import AppRoleAssignmentListResult
from openapi_server.models.graph_error import GraphError


pytestmark = pytest.mark.asyncio

async def test_service_principals_list_app_role_assigned_to(client):
    """Test case for service_principals_list_app_role_assigned_to

    Principals (users, groups, and service principals) that are assigned to this service principal.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{tenant_id}/servicePrincipals/{object_id}/appRoleAssignedTo'.format(object_id='object_id_example', tenant_id='tenant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

