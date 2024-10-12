# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_funds_to_insurance_request_body import AddFundsToInsuranceRequestBody
from openapi_server.models.add_funds_to_insurance_response_body import AddFundsToInsuranceResponseBody
from openapi_server.models.connect_insurer_request_body import ConnectInsurerRequestBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_insurance_balance_response_body import GetInsuranceBalanceResponseBody


pytestmark = pytest.mark.asyncio

async def test_add_funds_to_insurance(client):
    """Test case for add_funds_to_insurance

    Add Funds To Insurance
    """
    body = openapi_server.AddFundsToInsuranceRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/insurance/shipsurance/add_funds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connect_insurer(client):
    """Test case for connect_insurer

    Connect a Shipsurance Account
    """
    body = openapi_server.ConnectInsurerRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/connections/insurance/shipsurance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disconnect_insurer(client):
    """Test case for disconnect_insurer

    Disconnect a Shipsurance Account
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/connections/insurance/shipsurance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_insurance_balance(client):
    """Test case for get_insurance_balance

    Get Insurance Funds Balance
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/insurance/shipsurance/balance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

