# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_data_role_interface import CompanyDataRoleInterface
from openapi_server.models.company_role_repository_v1_save_post_request import CompanyRoleRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_role_repository_v1_save_put(client):
    """Test case for company_role_repository_v1_save_put

    company/role/{id}
    """
    body = openapi_server.CompanyRoleRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/company/role/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

