# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.principal_summary_v1_list_response import PrincipalSummaryV1ListResponse
from openapi_server.models.principal_with_role_info import PrincipalWithRoleInfo
from openapi_server.models.role_assignment_request import RoleAssignmentRequest
from openapi_server.models.role_info import RoleInfo


pytestmark = pytest.mark.asyncio

async def test_assign_roles_to_principals(client):
    """Test case for assign_roles_to_principals

    Assign roles to principals
    """
    body = {"roles":["roles","roles"],"principals":["principals","principals"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/principal/role',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_roles_for_principals(client):
    """Test case for get_roles_for_principals

    Get roles assigned to principals
    """
    params = [('principals', ['principals_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/principal/role',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_roles_from_principals(client):
    """Test case for revoke_roles_from_principals

    Revoke roles from principals
    """
    body = {"roles":["roles","roles"],"principals":["principals","principals"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/principal/role/bulk_revoke',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_principals_v1(client):
    """Test case for search_principals_v1

    Search for principals
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('auth_domain_id', 'auth_domain_id_example'),
                    ('organization_id', 'organization_id_example'),
                    ('is_assigned_roles_or_is_local', True),
                    ('role_id', 'role_id_example'),
                    ('name', 'name_example'),
                    ('principal_type', 'principal_type_example'),
                    ('is_totp_enabled', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/principal',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

