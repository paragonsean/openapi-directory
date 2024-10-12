# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_credit_credit_limit_repository_v1_save_put_request import CompanyCreditCreditLimitRepositoryV1SavePutRequest
from openapi_server.models.company_credit_data_credit_limit_interface import CompanyCreditDataCreditLimitInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_credit_credit_limit_repository_v1_save_put(client):
    """Test case for company_credit_credit_limit_repository_v1_save_put

    companyCredits/{id}
    """
    body = openapi_server.CompanyCreditCreditLimitRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/companyCredits/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

