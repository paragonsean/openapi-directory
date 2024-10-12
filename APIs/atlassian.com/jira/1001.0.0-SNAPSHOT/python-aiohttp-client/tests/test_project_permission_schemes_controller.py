# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.id_bean import IdBean
from openapi_server.models.permission_scheme import PermissionScheme
from openapi_server.models.project_issue_security_levels import ProjectIssueSecurityLevels
from openapi_server.models.security_scheme import SecurityScheme


pytestmark = pytest.mark.asyncio

async def test_assign_permission_scheme(client):
    """Test case for assign_permission_scheme

    Assign permission scheme
    """
    body = {"id":0}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_key_or_id}/permissionscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_assigned_permission_scheme(client):
    """Test case for get_assigned_permission_scheme

    Get assigned permission scheme
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_key_or_id}/permissionscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_issue_security_scheme(client):
    """Test case for get_project_issue_security_scheme

    Get project issue security scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_key_or_id}/issuesecuritylevelscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_security_levels_for_project(client):
    """Test case for get_security_levels_for_project

    Get project issue security levels
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_key_or_id}/securitylevel'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

