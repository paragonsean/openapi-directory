# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_permission_grants import BulkPermissionGrants
from openapi_server.models.bulk_permissions_request_bean import BulkPermissionsRequestBean
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.permissions import Permissions
from openapi_server.models.permissions_keys_bean import PermissionsKeysBean
from openapi_server.models.permitted_projects import PermittedProjects


pytestmark = pytest.mark.asyncio

async def test_get_all_permissions(client):
    """Test case for get_all_permissions

    Get all permissions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/permissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bulk_permissions(client):
    """Test case for get_bulk_permissions

    Get bulk permissions
    """
    body = {"accountId":"accountId","globalPermissions":["globalPermissions","globalPermissions"],"projectPermissions":[{"projects":[6,6],"permissions":["permissions","permissions"],"issues":[0,0]},{"projects":[6,6],"permissions":["permissions","permissions"],"issues":[0,0]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/permissions/check',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_my_permissions(client):
    """Test case for get_my_permissions

    Get my permissions
    """
    params = [('projectKey', 'project_key_example'),
                    ('projectId', 'project_id_example'),
                    ('issueKey', 'issue_key_example'),
                    ('issueId', 'issue_id_example'),
                    ('permissions', 'BROWSE_PROJECTS,EDIT_ISSUES'),
                    ('projectUuid', 'project_uuid_example'),
                    ('projectConfigurationUuid', 'project_configuration_uuid_example'),
                    ('commentId', 'comment_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/mypermissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permitted_projects(client):
    """Test case for get_permitted_projects

    Get permitted projects
    """
    body = {"permissions":["permissions","permissions"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/permissions/project',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

