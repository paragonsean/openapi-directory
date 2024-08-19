# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_service_point_by_id_response_body import GetServicePointByIdResponseBody
from openapi_server.models.get_service_points_request import GetServicePointsRequest
from openapi_server.models.list_service_points_response_body import ListServicePointsResponseBody


pytestmark = pytest.mark.asyncio

async def test_service_points_get_by_id(client):
    """Test case for service_points_get_by_id

    Get Service Point By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/service_points/{carrier_code}/{country_code}/{service_point_id}'.format(carrier_code='stamps_com', country_code='CA', service_point_id='614940'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_points_list(client):
    """Test case for service_points_list

    List Service Points
    """
    body = openapi_server.GetServicePointsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/service_points/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

