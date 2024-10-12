# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.db_log_report_properties import DbLogReportProperties
from openapi_server.models.db_log_report_properties_update import DbLogReportPropertiesUpdate
from openapi_server.models.db_log_report_summary_list_response import DbLogReportSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_query_log_report(client):
    """Test case for query_log_report

    Get the database log backup delay information
    """
    params = [('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('name', 'name_example'),
                    ('database_type', 'database_type_example'),
                    ('location', 'location_example'),
                    ('log_backup_delay', 56),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/database/log_report',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_report_properties(client):
    """Test case for query_report_properties

    Get the database log backup report properties
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/database/log_report/defaults',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_report_properties(client):
    """Test case for update_report_properties

    Update the database log backup report properties
    """
    body = {"logDelayThresholdInMin":6,"enableDelayNotification":True,"logDelayNotificationFrequencyInMin":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/database/log_report/defaults',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

