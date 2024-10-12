# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_credit_data_credit_limit_interface import CompanyCreditDataCreditLimitInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_credit_credit_limit_repository_v1_get_get(client):
    """Test case for company_credit_credit_limit_repository_v1_get_get

    companyCredits/{creditId}
    """
    params = [('reload', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/companyCredits/{credit_id}'.format(credit_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

