# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_service_metrics_task_request import CreateServiceMetricsTaskRequest
from openapi_server.models.customer_service_metric_task_collection import CustomerServiceMetricTaskCollection
from openapi_server.models.service_metrics_task import ServiceMetricsTask


pytestmark = pytest.mark.asyncio

async def test_create_customer_service_metric_task(client):
    """Test case for create_customer_service_metric_task

    
    """
    body = {"filterCriteria":{"shippingRegions":["shippingRegions","shippingRegions"],"customerServiceMetricType":"customerServiceMetricType","evaluationMarketplaceId":"evaluationMarketplaceId","listingCategories":["listingCategories","listingCategories"]},"schemaVersion":"schemaVersion","feedType":"feedType"}
    headers = { 
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/feed/v1/customer_service_metric_task',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_service_metric_task(client):
    """Test case for get_customer_service_metric_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/customer_service_metric_task/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_service_metric_tasks(client):
    """Test case for get_customer_service_metric_tasks

    
    """
    params = [('date_range', 'date_range_example'),
                    ('feed_type', 'feed_type_example'),
                    ('limit', 'limit_example'),
                    ('look_back_days', 'look_back_days_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/customer_service_metric_task',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

