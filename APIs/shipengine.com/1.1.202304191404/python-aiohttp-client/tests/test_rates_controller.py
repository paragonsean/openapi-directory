# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_rate import BulkRate
from openapi_server.models.calculate_rates_request_body import CalculateRatesRequestBody
from openapi_server.models.calculate_rates_response_body import CalculateRatesResponseBody
from openapi_server.models.compare_bulk_rates_request_body import CompareBulkRatesRequestBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.estimate_rates_request_body import EstimateRatesRequestBody
from openapi_server.models.get_rate_by_id_response_body import GetRateByIdResponseBody
from openapi_server.models.rate_estimate import RateEstimate


pytestmark = pytest.mark.asyncio

async def test_calculate_rates(client):
    """Test case for calculate_rates

    Get Shipping Rates
    """
    body = openapi_server.CalculateRatesRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/rates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_compare_bulk_rates(client):
    """Test case for compare_bulk_rates

    Get Bulk Rates
    """
    body = openapi_server.CompareBulkRatesRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/rates/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_estimate_rates(client):
    """Test case for estimate_rates

    Estimate Rates
    """
    body = openapi_server.EstimateRatesRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/rates/estimate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rate_by_id(client):
    """Test case for get_rate_by_id

    Get Rate By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/rates/{rate_id}'.format(rate_id='rate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

