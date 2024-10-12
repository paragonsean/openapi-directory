# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_customer_service_metric_response import GetCustomerServiceMetricResponse


pytestmark = pytest.mark.asyncio

async def test_get_customer_service_metric(client):
    """Test case for get_customer_service_metric

    
    """
    params = [('evaluation_marketplace_id', 'evaluation_marketplace_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/analytics/v1/customer_service_metric/{customer_service_metric_type}/{evaluation_type}'.format(customer_service_metric_type='customer_service_metric_type_example', evaluation_type='evaluation_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

