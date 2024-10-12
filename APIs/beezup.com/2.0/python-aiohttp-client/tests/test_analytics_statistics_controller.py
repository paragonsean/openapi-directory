# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.report_by_category_request import ReportByCategoryRequest
from openapi_server.models.report_by_category_response import ReportByCategoryResponse
from openapi_server.models.report_by_channel_request import ReportByChannelRequest
from openapi_server.models.report_by_channel_response import ReportByChannelResponse
from openapi_server.models.report_by_day_request import ReportByDayRequest
from openapi_server.models.report_by_day_response import ReportByDayResponse
from openapi_server.models.report_by_product_request import ReportByProductRequest
from openapi_server.models.report_by_product_response import ReportByProductResponse


pytestmark = pytest.mark.asyncio

async def test_get_store_report_by_category(client):
    """Test case for get_store_report_by_category

    Get the report by category
    """
    body = openapi_server.ReportByCategoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/reports/bycategory'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store_report_by_channel(client):
    """Test case for get_store_report_by_channel

    Get the report by channel
    """
    body = openapi_server.ReportByChannelRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/reports/bychannel'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store_report_by_day(client):
    """Test case for get_store_report_by_day

    Get the report by day for a StoreId
    """
    body = openapi_server.ReportByDayRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/reports/byday'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store_report_by_day_per_store(client):
    """Test case for get_store_report_by_day_per_store

    Get the report by day for a StoreId
    """
    body = openapi_server.ReportByDayRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/reports/byday',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store_report_by_product(client):
    """Test case for get_store_report_by_product

    Get the report by product
    """
    body = openapi_server.ReportByProductRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/analytics/{store_id}/reports/byproduct'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

