# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_companies_vendor_request import AddCompaniesVendorRequest
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_compaies_vendors_list200_response import GetCompaiesVendorsList200Response
from openapi_server.models.get_companies_vendor200_response import GetCompaniesVendor200Response
from openapi_server.models.get_companies_vendors_expense_statistics200_response import GetCompaniesVendorsExpenseStatistics200Response


pytestmark = pytest.mark.asyncio

async def test_add_companies_vendor(client):
    """Test case for add_companies_vendor

    Add a new companies vendor
    """
    body = openapi_server.AddCompaniesVendorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/companies_vendors',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_companies_vendors(client):
    """Test case for bulk_companies_vendors

    Bulk delete companies vendors
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/companies_vendors/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_vendors_companies_vendor_id_delete(client):
    """Test case for companies_vendors_companies_vendor_id_delete

    Delete a companies vendor
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/companies_vendors/{companies_vendor_id}'.format(companies_vendor_id='companies_vendor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_companies_vendor(client):
    """Test case for edit_companies_vendor

    Edit a companies vendor
    """
    body = openapi_server.AddCompaniesVendorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/companies_vendors/{companies_vendor_id}'.format(companies_vendor_id='companies_vendor_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compaies_vendors_list(client):
    """Test case for get_compaies_vendors_list

    Get a list of companies vendors
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies_vendors',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_vendor(client):
    """Test case for get_companies_vendor

    Get a companies vendor
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies_vendors/{companies_vendor_id}'.format(companies_vendor_id='companies_vendor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_vendors_expense_statistics(client):
    """Test case for get_companies_vendors_expense_statistics

    Get companies vendor expense statistics
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies_vendors/{companies_vendor_id}/expense_statistics'.format(companies_vendor_id='companies_vendor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

