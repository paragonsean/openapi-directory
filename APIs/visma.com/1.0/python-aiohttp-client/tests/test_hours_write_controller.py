# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.time_entry_model import TimeEntryModel
from openapi_server.models.work_hour_input_model import WorkHourInputModel
from openapi_server.models.work_hour_output_model import WorkHourOutputModel


pytestmark = pytest.mark.asyncio

async def test_time_entries_patch_time_entry(client):
    """Test case for time_entries_patch_time_entry

    Update (Patch) a time entry or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/timeentries/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entries_post_time_entry(client):
    """Test case for time_entries_post_time_entry

    Insert a time entry.
    """
    body = {"phase":{"name":"name","guid":"guid"},"lastUpdatedBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"quantity":6.027456183070403,"createdDateTime":"2000-01-23T04:56:07.000+00:00","description":"description","project":{"number":0,"name":"name","guid":"guid"},"timeEntryType":{"name":"name","guid":"guid"},"createdBy":{"firstName":"firstName","lastName":"lastName","code":"code","name":"name","guid":"guid"},"guid":"guid","startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","lastUpdatedDateTime":"2000-01-23T04:56:07.000+00:00","user":{"name":"name","guid":"guid"},"customer":{"name":"name","guid":"guid"},"eventDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/timeentries',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_patch_work_hour(client):
    """Test case for work_hours_patch_work_hour

    Update (Patch) a work hour or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/workhours/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_post_work_hour(client):
    """Test case for work_hours_post_work_hour

    Insert a work hour
    """
    body = {"phase":{"guid":"guid"},"unitPrice":{"amount":5.962133916683182,"currencyCode":"currencyCode"},"quantity":1.4658129805029452,"description":"description","invoiceRowDescription":"invoiceRowDescription","isBillable":True,"plannedInvoiceQuantity":6.027456183070403,"invoiceQuantity":0.8008281904610115,"workType":{"guid":"guid"},"overtime":{"guid":"guid"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","invoice":{"guid":"guid"},"invoiceRowComment":"invoiceRowComment","isApproved":True,"user":{"guid":"guid"},"eventDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/workhours',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

