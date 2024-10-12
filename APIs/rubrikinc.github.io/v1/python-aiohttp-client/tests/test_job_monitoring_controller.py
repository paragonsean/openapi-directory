# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_monitoring_csv_download_response import JobMonitoringCsvDownloadResponse
from openapi_server.models.job_monitoring_response import JobMonitoringResponse
from openapi_server.models.job_monitoring_summary_by_state import JobMonitoringSummaryByState
from openapi_server.models.job_monitoring_summary_by_type import JobMonitoringSummaryByType
from openapi_server.models.monitoring_email_subscription_request import MonitoringEmailSubscriptionRequest
from openapi_server.models.monitoring_email_subscription_update import MonitoringEmailSubscriptionUpdate
from openapi_server.models.monitoring_subscription_summary import MonitoringSubscriptionSummary


pytestmark = pytest.mark.asyncio

async def test_create_monitoring_subscription(client):
    """Test case for create_monitoring_subscription

    Create an email subscription to the job monitoring page
    """
    body = {"jobStates":["Failure","Failure"],"attachments":["Csv","Csv"],"emailAddresses":["emailAddresses","emailAddresses"],"timeAttributes":{"dayOfMonth":6,"monthlyScheduleHour":5,"dailyScheduleHour":0,"daysOfWeek":[1,1],"weeklyScheduleHour":5}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/job_monitoring/subscription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_monitoring_subscription(client):
    """Test case for delete_monitoring_subscription

    Delete a monitoring page email subscription
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/job_monitoring/subscription/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_monitoring_info(client):
    """Test case for get_job_monitoring_info

    Get job monitoring information
    """
    params = [('limit', 56),
                    ('job_event_status', ['job_event_status_example']),
                    ('job_type', 'job_type_example'),
                    ('should_include_log_related_job', True),
                    ('is_first_full', True),
                    ('object_type', 'object_type_example'),
                    ('object_name', 'object_name_example'),
                    ('node_name', 'node_name_example'),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('is_on_demand', True),
                    ('last_update_time', '2013-10-20T19:20:30+01:00'),
                    ('after_id', 'after_id_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job_monitoring',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_job_monitoring_info_csv_download_link(client):
    """Test case for get_job_monitoring_info_csv_download_link

    Download job monitoring information as a CSV file
    """
    params = [('job_monitoring_state', 'job_monitoring_state_example'),
                    ('job_event_status', 'job_event_status_example'),
                    ('job_type', 'job_type_example'),
                    ('should_include_log_related_job', True),
                    ('object_type', 'object_type_example'),
                    ('object_name', 'object_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job_monitoring/csv_download_link',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_job_count_by_job_state(client):
    """Test case for get_monitoring_job_count_by_job_state

    Get job monitoring summary information separated by job state
    """
    params = [('job_types', ['job_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job_monitoring/summary_by_job_state',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_job_count_by_job_type(client):
    """Test case for get_monitoring_job_count_by_job_type

    Get job monitoring summary information separated by job type
    """
    params = [('job_monitoring_state', 'job_monitoring_state_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job_monitoring/summary_by_job_type',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_subscription(client):
    """Test case for get_monitoring_subscription

    Get a specific monitoring email subscription by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job_monitoring/subscription/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_subscriptions(client):
    """Test case for get_monitoring_subscriptions

    Returns all email subscriptions for the monitoring page
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/job_monitoring/subscription',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_monitoring_subscription(client):
    """Test case for update_monitoring_subscription

    Update a monitoring email subscription
    """
    body = {"jobStates":["Failure","Failure"],"attachments":["Csv","Csv"],"emailAddresses":["emailAddresses","emailAddresses"],"assumeOwnership":True,"id":"id","timeAttributes":{"dayOfMonth":6,"monthlyScheduleHour":5,"dailyScheduleHour":0,"daysOfWeek":[1,1],"weeklyScheduleHour":5}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/job_monitoring/subscription/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

