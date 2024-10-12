# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.breadcrumbs_api_models_address_risk_exposure_response import BreadcrumbsAPIModelsAddressRiskExposureResponse
from openapi_server.models.breadcrumbs_api_models_transaction_risk_response import BreadcrumbsAPIModelsTransactionRiskResponse
from openapi_server.models.breadcrumbs_response_unauthorized_response import BreadcrumbsResponseUnauthorizedResponse
from openapi_server.models.breadcrumbs_response_unprocessable_response import BreadcrumbsResponseUnprocessableResponse


pytestmark = pytest.mark.asyncio

async def test_risk_address_get(client):
    """Test case for risk_address_get

    Will check the risk score for single address
    """
    params = [('chain', ETH),
                    ('address', 'address_example'),
                    ('include_exposure', False)]
    headers = { 
        'Accept': 'application/json',
        'X-API-KEY': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/risk/address',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_risk_transaction_get(client):
    """Test case for risk_transaction_get

    Will check the risk score for every addresses in a transaction
    """
    params = [('chain', ETH),
                    ('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'X-API-KEY': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/risk/transaction',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

