# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server.models.regression_api_body import RegressionApiBody


pytestmark = pytest.mark.asyncio

async def test_regression_api_post(client):
    """Test case for regression_api_post

    Returns regression analysis.
    """
    body = openapi_server.RegressionApiBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/regression/api',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

