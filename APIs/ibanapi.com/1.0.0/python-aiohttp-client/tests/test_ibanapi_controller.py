# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_response import BalanceResponse
from openapi_server.models.iban_result import IBANResult
from openapi_server.models.iban_result_basic import IBANResultBasic
from openapi_server.models.model400 import Model400
from openapi_server.models.model401 import Model401
from openapi_server.models.model403 import Model403
from openapi_server.models.model422 import Model422


pytestmark = pytest.mark.asyncio

async def test_get_balance(client):
    """Test case for get_balance

    Get Account Balance
    """
    headers = { 
        'Accept': 'application/json',
        'api_key_security': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/balance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_iban(client):
    """Test case for validate_iban

    Validate IBAN
    """
    params = [('iban', 'iban_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key_security': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/validate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_iban_basic(client):
    """Test case for validate_iban_basic

    Validate IBAN Basic
    """
    params = [('iban', 'iban_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key_security': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/validate-basic',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

