# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_company_repository_v1_save_post_request import CompanyCompanyRepositoryV1SavePostRequest
from openapi_server.models.company_data_company_interface import CompanyDataCompanyInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_company_repository_v1_delete_by_id_delete(client):
    """Test case for company_company_repository_v1_delete_by_id_delete

    company/{companyId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/company/{company_id}'.format(company_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_company_repository_v1_get_get(client):
    """Test case for company_company_repository_v1_get_get

    company/{companyId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/company/{company_id}'.format(company_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_company_repository_v1_save_put(client):
    """Test case for company_company_repository_v1_save_put

    company/{companyId}
    """
    body = openapi_server.CompanyCompanyRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/company/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

