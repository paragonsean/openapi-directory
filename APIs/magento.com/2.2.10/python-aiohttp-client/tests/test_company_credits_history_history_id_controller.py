# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_credit_credit_history_management_v1_update_put_request import CompanyCreditCreditHistoryManagementV1UpdatePutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_credit_credit_history_management_v1_update_put(client):
    """Test case for company_credit_credit_history_management_v1_update_put

    companyCredits/history/{historyId}
    """
    body = openapi_server.CompanyCreditCreditHistoryManagementV1UpdatePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/companyCredits/history/{history_id}'.format(history_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

