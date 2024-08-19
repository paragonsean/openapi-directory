# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.age_usd_exchange_info import AgeUsdExchangeInfo
from openapi_server.models.age_usd_info import AgeUsdInfo
from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.token_price import TokenPrice


pytestmark = pytest.mark.asyncio

async def test_calc_sigma_rsv_exchange(client):
    """Test case for calc_sigma_rsv_exchange

    Calculates SigRSV exchange
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/sigrsv/exchange/{amount}/info'.format(amount=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calc_sigma_usd_exchange(client):
    """Test case for calc_sigma_usd_exchange

    Calculates SigUSD exchange
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/sigusd/exchange/{amount}/info'.format(amount=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_sigma_rsv_exchange(client):
    """Test case for do_sigma_rsv_exchange

    Builds ErgoPayRequest for SigRSV exchange
    """
    params = [('amount', 56),
                    ('address', 'address_example'),
                    ('checkRate', 0),
                    ('executionFee', 0)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/sigrsv/exchange/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_sigma_usd_exchange(client):
    """Test case for do_sigma_usd_exchange

    Builds ErgoPayRequest for SigUSD exchange
    """
    params = [('amount', 56),
                    ('address', 'address_example'),
                    ('checkRate', 0),
                    ('executionFee', 0)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/sigusd/exchange/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_age_usd_info(client):
    """Test case for get_age_usd_info

    Returns state of AgeUSD at this moment
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/ageusd/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sigma_rsv_price(client):
    """Test case for get_sigma_rsv_price

    Lists price and available volume for SigmaRSV
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/sigrsv/price',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sigma_usd_price(client):
    """Test case for get_sigma_usd_price

    Lists price and available volume for SigmaUSD
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/sigusd/price',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

