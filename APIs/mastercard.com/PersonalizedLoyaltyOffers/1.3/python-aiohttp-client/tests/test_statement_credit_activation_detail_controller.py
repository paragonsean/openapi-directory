# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.statement_credit_activation_response import StatementCreditActivationResponse


pytestmark = pytest.mark.asyncio

async def test_statementcreditactivationdetail_get(client):
    """Test case for statementcreditactivationdetail_get

    Returns Information About Redeemable Postpaid Credit Offer
    """
    params = [('FId', '999999'),
                    ('UserToken', 'user_token_example'),
                    ('ActivationId', 'TRU_1000136')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plo/v1/statementcreditactivationdetail',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

