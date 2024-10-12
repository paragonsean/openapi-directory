# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_company_management_v1_assign_companies_post_request import SharedCatalogCompanyManagementV1AssignCompaniesPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_shared_catalog_company_management_v1_assign_companies_post(client):
    """Test case for shared_catalog_company_management_v1_assign_companies_post

    sharedCatalog/{sharedCatalogId}/assignCompanies
    """
    body = openapi_server.SharedCatalogCompanyManagementV1AssignCompaniesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/sharedCatalog/{shared_catalog_id}/assignCompanies'.format(shared_catalog_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

