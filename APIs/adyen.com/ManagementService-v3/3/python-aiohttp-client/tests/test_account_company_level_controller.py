# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company import Company
from openapi_server.models.list_company_response import ListCompanyResponse
from openapi_server.models.list_merchant_response import ListMerchantResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_get_companies(client):
    """Test case for get_companies

    Get a list of company accounts
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id(client):
    """Test case for get_companies_company_id

    Get a company account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_merchants(client):
    """Test case for get_companies_company_id_merchants

    Get a list of merchant accounts
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/merchants'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

