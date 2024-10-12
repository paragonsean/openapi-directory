# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_option_dto import CompanyOptionDto
from openapi_server.models.company_setup_config_view_model import CompanySetupConfigViewModel
from openapi_server.models.financial_year_dto import FinancialYearDto


pytestmark = pytest.mark.asyncio

async def test_company_setup_config_get(client):
    """Test case for company_setup_config_get

    Returns the company configuration settings.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companySetupConfig',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_setup_config_get_company_options(client):
    """Test case for company_setup_config_get_company_options

    Returns the company option setting.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companySetupConfig/getCompanyOptions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_setup_config_get_financial_year(client):
    """Test case for company_setup_config_get_financial_year

    Returns the financial year.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companySetupConfig/getFinancialYear',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

