# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_acl_v1_get_users_by_role_id_get(client):
    """Test case for company_acl_v1_get_users_by_role_id_get

    company/role/{roleId}/users
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/company/role/{role_id}/users'.format(role_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

