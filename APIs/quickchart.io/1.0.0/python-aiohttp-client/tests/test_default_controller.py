# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chart_post_request import ChartPostRequest
from openapi_server.models.qr_post_request import QrPostRequest


pytestmark = pytest.mark.asyncio

async def test_chart_get(client):
    """Test case for chart_get

    Generate a chart (GET)
    """
    params = [('chart', 'chart_example'),
                    ('width', 56),
                    ('height', 56),
                    ('format', 'format_example'),
                    ('backgroundColor', 'background_color_example')]
    headers = { 
        'Accept': 'image/webp',
    }
    response = await client.request(
        method='GET',
        path='/chart',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_post(client):
    """Test case for chart_post

    Generate a chart (POST)
    """
    body = openapi_server.ChartPostRequest()
    headers = { 
        'Accept': 'image/webp',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/chart',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qr_get(client):
    """Test case for qr_get

    Generate a QR code (GET)
    """
    params = [('text', 'text_example'),
                    ('width', 56),
                    ('height', 56),
                    ('format', 'format_example'),
                    ('margin', 56)]
    headers = { 
        'Accept': 'image/svg+xml',
    }
    response = await client.request(
        method='GET',
        path='/qr',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_qr_post(client):
    """Test case for qr_post

    Generate a QR code (POST)
    """
    body = openapi_server.QrPostRequest()
    headers = { 
        'Accept': 'image/svg+xml',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/qr',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

