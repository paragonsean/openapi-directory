# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.query_forecast_request import QueryForecastRequest
from openapi_server.models.query_forecast_response import QueryForecastResponse
from openapi_server.models.query_what_if_forecast_request import QueryWhatIfForecastRequest
from openapi_server.models.query_what_if_forecast_response import QueryWhatIfForecastResponse


pytestmark = pytest.mark.asyncio

async def test_query_forecast(client):
    """Test case for query_forecast

    
    """
    body = {"StartDate":"","Filters":"","NextToken":"","ForecastArn":"","EndDate":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AmazonForecastRuntime.QueryForecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_what_if_forecast(client):
    """Test case for query_what_if_forecast

    
    """
    body = {"StartDate":"","Filters":"","NextToken":"","EndDate":"","WhatIfForecastArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AmazonForecastRuntime.QueryWhatIfForecast',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

