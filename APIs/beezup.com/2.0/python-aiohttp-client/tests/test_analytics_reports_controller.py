# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.report_filter import ReportFilter
from openapi_server.models.report_filter_list import ReportFilterList
from openapi_server.models.save_report_filter_request import SaveReportFilterRequest


pytestmark = pytest.mark.asyncio

async def test_delete_report_filter(client):
    """Test case for delete_report_filter

    Delete the report filter
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/analytics/{store_id}/reports/filters/{report_filter_id}'.format(store_id='store_id_example', report_filter_id='report_filter_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_filter(client):
    """Test case for get_report_filter

    Get the report filter description
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/reports/filters/{report_filter_id}'.format(store_id='store_id_example', report_filter_id='report_filter_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_filters(client):
    """Test case for get_report_filters

    Get report filter list for the given store
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/reports/filters'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_report_filter(client):
    """Test case for save_report_filter

    Save the report filter
    """
    body = openapi_server.SaveReportFilterRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/analytics/{store_id}/reports/filters/{report_filter_id}'.format(store_id='store_id_example', report_filter_id='report_filter_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

