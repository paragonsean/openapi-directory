# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.holding_companies_model import HoldingCompaniesModel
from openapi_server.models.holding_company_model import HoldingCompanyModel


pytestmark = pytest.mark.asyncio

async def test_holding_companies_get_by_id_planid(client):
    """Test case for holding_companies_get_by_id_planid

    Retrieve a holding company
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/HoldingCompanies/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_holding_companies_get_by_planid(client):
    """Test case for holding_companies_get_by_planid

    Retrieve holding companies
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/HoldingCompanies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

