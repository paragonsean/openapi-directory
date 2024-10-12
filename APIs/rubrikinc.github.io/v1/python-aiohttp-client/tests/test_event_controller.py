# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_log_summary_v1_list_response import ActivityLogSummaryV1ListResponse
from openapi_server.models.event_csv_download_response import EventCsvDownloadResponse
from openapi_server.models.events_and_series_summaries_v1 import EventsAndSeriesSummariesV1


pytestmark = pytest.mark.asyncio

async def test_get_events_csv_download_link(client):
    """Test case for get_events_csv_download_link

    Download summary of events as a CSV file
    """
    params = [('limit', 56),
                    ('event_series_status', 'event_series_status_example'),
                    ('event_status', 'event_status_example'),
                    ('event_type', 'event_type_example'),
                    ('event_severity', 'event_severity_example'),
                    ('object_ids', ['object_ids_example']),
                    ('object_type', 'object_type_example'),
                    ('object_name', 'object_name_example'),
                    ('after_id', 'after_id_example'),
                    ('before_date', '2013-10-20T19:20:30+01:00'),
                    ('after_date', '2013-10-20T19:20:30+01:00'),
                    ('order_by_time', 'order_by_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/event/csv_download_link',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_event_v1(client):
    """Test case for query_event_v1

    Get information for all events
    """
    params = [('limit', 56),
                    ('after_id', 'after_id_example'),
                    ('before_date', '2013-10-20T19:20:30+01:00'),
                    ('after_date', '2013-10-20T19:20:30+01:00'),
                    ('order_by_time', 'order_by_time_example'),
                    ('should_include_event_series', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/event',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_latest_events_v1(client):
    """Test case for query_latest_events_v1

    Get latest events with their associated event series information
    """
    params = [('limit', 56),
                    ('event_series_status', 'event_series_status_example'),
                    ('event_status', 'event_status_example'),
                    ('event_type', 'event_type_example'),
                    ('event_severity', 'event_severity_example'),
                    ('object_ids', ['object_ids_example']),
                    ('object_type', 'object_type_example'),
                    ('object_name', 'object_name_example'),
                    ('after_id', 'after_id_example'),
                    ('before_date', '2013-10-20T19:20:30+01:00'),
                    ('after_date', '2013-10-20T19:20:30+01:00'),
                    ('order_by_time', 'order_by_time_example'),
                    ('should_include_event_series', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/event/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

