# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_vendor_request import AddVendorRequest
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_vendor200_response import GetVendor200Response
from openapi_server.models.get_vendors_list200_response import GetVendorsList200Response


pytestmark = pytest.mark.asyncio

async def test_add_vendor(client):
    """Test case for add_vendor

    Add a new vendor
    """
    body = openapi_server.AddVendorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vendors',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_vendor(client):
    """Test case for edit_vendor

    Edit a vendor
    """
    body = openapi_server.AddVendorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/vendors/{vendor_id}'.format(vendor_id='vendor_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vendor(client):
    """Test case for get_vendor

    Get a vendor
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendors/{vendor_id}'.format(vendor_id='vendor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vendors_list(client):
    """Test case for get_vendors_list

    Get a list of vendors
    """
    params = [('with_custom', True),
                    ('email', 'email_example'),
                    ('name', 'name_example'),
                    ('cvr', 'cvr_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vendors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendors_vendor_id_delete(client):
    """Test case for vendors_vendor_id_delete

    Delete a vendor
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vendors/{vendor_id}'.format(vendor_id='vendor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

