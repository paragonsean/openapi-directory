# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_companies_company_detail import CredasApiModelsCompaniesCompanyDetail
from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_company(client):
    """Test case for get_company

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/companies/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_company(client):
    """Test case for search_company

    Searches for a company based on its Company Number and returns its details.
    """
    params = [('companyNumber', 'company_number_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/companies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

