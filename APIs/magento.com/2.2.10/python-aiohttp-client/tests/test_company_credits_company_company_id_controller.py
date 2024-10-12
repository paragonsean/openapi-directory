# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_credit_data_credit_limit_interface import CompanyCreditDataCreditLimitInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_credit_credit_limit_management_v1_get_credit_by_company_id_get(client):
    """Test case for company_credit_credit_limit_management_v1_get_credit_by_company_id_get

    companyCredits/company/{companyId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/companyCredits/company/{company_id}'.format(company_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

