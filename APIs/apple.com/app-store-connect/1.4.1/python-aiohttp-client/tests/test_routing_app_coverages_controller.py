# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.routing_app_coverage_create_request import RoutingAppCoverageCreateRequest
from openapi_server.models.routing_app_coverage_response import RoutingAppCoverageResponse
from openapi_server.models.routing_app_coverage_update_request import RoutingAppCoverageUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_routing_app_coverages_create_instance(client):
    """Test case for routing_app_coverages_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersion":{"data":{"id":"id","type":"appStoreVersions"}}},"attributes":{"fileName":"fileName","fileSize":0},"type":"routingAppCoverages"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/routingAppCoverages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routing_app_coverages_delete_instance(client):
    """Test case for routing_app_coverages_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/routingAppCoverages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routing_app_coverages_get_instance(client):
    """Test case for routing_app_coverages_get_instance

    
    """
    params = [('fields[routingAppCoverages]', ['fields_routing_app_coverages_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/routingAppCoverages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routing_app_coverages_update_instance(client):
    """Test case for routing_app_coverages_update_instance

    
    """
    body = {"data":{"attributes":{"uploaded":True,"sourceFileChecksum":"sourceFileChecksum"},"id":"id","type":"routingAppCoverages"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/routingAppCoverages/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

