# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_report409_response import CancelReport409Response
from openapi_server.models.create_async_report200_response import CreateAsyncReport200Response
from openapi_server.models.create_async_report400_response import CreateAsyncReport400Response
from openapi_server.models.create_async_report403_response import CreateAsyncReport403Response
from openapi_server.models.create_async_report422_response import CreateAsyncReport422Response
from openapi_server.models.create_async_report_request import CreateAsyncReportRequest
from openapi_server.models.download_report200_response import DownloadReport200Response
from openapi_server.models.get_records200_response import GetRecords200Response
from openapi_server.models.get_records403_response import GetRecords403Response
from openapi_server.models.get_records422_response import GetRecords422Response
from openapi_server.models.get_report200_response import GetReport200Response
from openapi_server.models.get_report404_response import GetReport404Response
from openapi_server.models.list_reports200_response import ListReports200Response
from openapi_server.models.list_reports400_response import ListReports400Response
from openapi_server.models.list_reports401_response import ListReports401Response


pytestmark = pytest.mark.asyncio

async def test_cancel_report(client):
    """Test case for cancel_report

    Cancel the execution of a report
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/reports/{report_id}'.format(report_id='aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_async_report(client):
    """Test case for create_async_report

    Create an asynchronous report
    """
    body = openapi_server.CreateAsyncReportRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/reports',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_report(client):
    """Test case for download_report

    Get report data
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v3/media/{file_id}'.format(file_id='aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_records(client):
    """Test case for get_records

    Load records synchronously
    """
    params = [('account_id', 'abcd1234'),
                    ('product', 'SMS'),
                    ('direction', 'inbound'),
                    ('id', 'aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
                    ('date_start', '2017-12-01T00:00:00+0000'),
                    ('date_end', '2018-01-01T00:00:00+0000'),
                    ('include_message', False),
                    ('show_concatenated', False),
                    ('status', none)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/reports/records',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report(client):
    """Test case for get_report

    Get status of report
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/reports/{report_id}'.format(report_id='aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_reports(client):
    """Test case for list_reports

    List reports
    """
    params = [('account_id', 'abcd1234'),
                    ('status', 'SUCCESS, FAILED'),
                    ('date_from', '2019-06-28T00:00:00-00:00'),
                    ('date_to', '2019-06-28T23:59:59-00:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/reports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

