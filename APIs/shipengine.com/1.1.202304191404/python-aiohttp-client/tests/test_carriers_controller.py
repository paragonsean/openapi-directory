# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_funds_to_carrier_request_body import AddFundsToCarrierRequestBody
from openapi_server.models.add_funds_to_carrier_response_body import AddFundsToCarrierResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_carrier_by_id_response_body import GetCarrierByIdResponseBody
from openapi_server.models.get_carrier_options_response_body import GetCarrierOptionsResponseBody
from openapi_server.models.get_carriers_response_body import GetCarriersResponseBody
from openapi_server.models.list_carrier_package_types_response_body import ListCarrierPackageTypesResponseBody
from openapi_server.models.list_carrier_services_response_body import ListCarrierServicesResponseBody


pytestmark = pytest.mark.asyncio

async def test_add_funds_to_carrier(client):
    """Test case for add_funds_to_carrier

    Add Funds To Carrier
    """
    body = openapi_server.AddFundsToCarrierRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/carriers/{carrier_id}/add_funds'.format(carrier_id='se-28529731'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_carrier_by_id(client):
    """Test case for get_carrier_by_id

    Get Carrier By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/carriers/{carrier_id}'.format(carrier_id='se-28529731'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_carrier_options(client):
    """Test case for get_carrier_options

    Get Carrier Options
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/carriers/{carrier_id}/options'.format(carrier_id='se-28529731'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_carrier_package_types(client):
    """Test case for list_carrier_package_types

    List Carrier Package Types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/carriers/{carrier_id}/packages'.format(carrier_id='se-28529731'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_carrier_services(client):
    """Test case for list_carrier_services

    List Carrier Services
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/carriers/{carrier_id}/services'.format(carrier_id='se-28529731'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_carriers(client):
    """Test case for list_carriers

    List Carriers
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/carriers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

