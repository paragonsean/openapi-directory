# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_checkout_post201_response import ClockingRecordsCheckoutPost201Response
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_get200_response import ClockingRecordsClockingRecordIdGet200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_get200_response import ClockingRecordsGet200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.clocking_records_post_request import ClockingRecordsPostRequest
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation


pytestmark = pytest.mark.asyncio

async def test_clocking_records_checkout_post(client):
    """Test case for clocking_records_checkout_post

    Checkout active clocking record for authenticated user
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/clocking_records/checkout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clocking_records_clocking_record_id_delete(client):
    """Test case for clocking_records_clocking_record_id_delete

    Delete a clocking record
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/clocking_records/{clocking_record_id}'.format(clocking_record_id='clocking_record_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clocking_records_clocking_record_id_get(client):
    """Test case for clocking_records_clocking_record_id_get

    Details of 1 clocking_record
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/clocking_records/{clocking_record_id}'.format(clocking_record_id='clocking_record_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clocking_records_clocking_record_id_put(client):
    """Test case for clocking_records_clocking_record_id_put

    Edit a clocking record
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/clocking_records/{clocking_record_id}'.format(clocking_record_id='clocking_record_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clocking_records_get(client):
    """Test case for clocking_records_get

    Get a list of clocking records
    """
    params = [('active', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/clocking_records',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clocking_records_post(client):
    """Test case for clocking_records_post

    Create clocking record for authenticated user
    """
    body = openapi_server.ClockingRecordsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/clocking_records',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

