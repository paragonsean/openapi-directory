# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_data_role_interface import CompanyDataRoleInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_role_repository_v1_delete_delete(client):
    """Test case for company_role_repository_v1_delete_delete

    company/role/{roleId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/company/role/{role_id}'.format(role_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_role_repository_v1_get_get(client):
    """Test case for company_role_repository_v1_get_get

    company/role/{roleId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/company/role/{role_id}'.format(role_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

