# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.area_request import AreaRequest
from openapi_server.models.path_request import PathRequest
from openapi_server.models.points_request import PointsRequest


pytestmark = pytest.mark.asyncio

async def test_area(client):
    """Test case for area

    Create a point-to-multipoint heatmap
    """
    body = openapi_server.AreaRequest()
    headers = { 
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/area',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_path(client):
    """Test case for path

    Point-to-point path profile analysis (Tx to Rx)
    """
    body = openapi_server.PathRequest()
    headers = { 
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/path',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_points(client):
    """Test case for points

    Point-to-multipoint path profile analysis (Many Tx, one Rx)
    """
    body = openapi_server.PointsRequest()
    headers = { 
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/points',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

