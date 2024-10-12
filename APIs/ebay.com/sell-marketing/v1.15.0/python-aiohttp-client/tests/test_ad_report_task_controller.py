# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_report_task import CreateReportTask
from openapi_server.models.report_task import ReportTask
from openapi_server.models.report_task_paged_collection import ReportTaskPagedCollection


pytestmark = pytest.mark.asyncio

async def test_create_report_task(client):
    """Test case for create_report_task

    
    """
    body = {"marketplaceId":"marketplaceId","reportType":"reportType","metricKeys":["metricKeys","metricKeys"],"listingIds":["listingIds","listingIds"],"inventoryReferences":[{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType"},{"inventoryReferenceId":"inventoryReferenceId","inventoryReferenceType":"inventoryReferenceType"}],"dateTo":"dateTo","fundingModels":["fundingModels","fundingModels"],"reportFormat":"reportFormat","campaignIds":["campaignIds","campaignIds"],"dateFrom":"dateFrom","additionalRecords":["additionalRecords","additionalRecords"],"dimensions":[{"dimensionKey":"dimensionKey","annotationKeys":["annotationKeys","annotationKeys"]},{"dimensionKey":"dimensionKey","annotationKeys":["annotationKeys","annotationKeys"]}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/marketing/v1/ad_report_task',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_report_task(client):
    """Test case for delete_report_task

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/marketing/v1/ad_report_task/{report_task_id}'.format(report_task_id='report_task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_task(client):
    """Test case for get_report_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_report_task/{report_task_id}'.format(report_task_id='report_task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_tasks(client):
    """Test case for get_report_tasks

    
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('report_task_statuses', 'report_task_statuses_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/ad_report_task',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

