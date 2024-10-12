# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_acl_v1_assign_roles_put_request import CompanyAclV1AssignRolesPutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_acl_v1_assign_roles_put(client):
    """Test case for company_acl_v1_assign_roles_put

    company/assignRoles
    """
    body = openapi_server.CompanyAclV1AssignRolesPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/company/assignRoles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

