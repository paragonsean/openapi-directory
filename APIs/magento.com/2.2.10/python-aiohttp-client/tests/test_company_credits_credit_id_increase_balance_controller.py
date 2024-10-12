# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_credit_credit_balance_management_v1_decrease_post_request import CompanyCreditCreditBalanceManagementV1DecreasePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_credit_credit_balance_management_v1_increase_post(client):
    """Test case for company_credit_credit_balance_management_v1_increase_post

    companyCredits/{creditId}/increaseBalance
    """
    body = openapi_server.CompanyCreditCreditBalanceManagementV1DecreasePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/companyCredits/{credit_id}/increaseBalance'.format(credit_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

