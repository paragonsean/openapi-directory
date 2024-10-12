# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.events_results import EventsResults
from openapi_server.models.metrics_result import MetricsResult
from openapi_server.models.query_body import QueryBody
from openapi_server.models.query_results import QueryResults


pytestmark = pytest.mark.asyncio

async def test_events_get(client):
    """Test case for events_get

    Get an event
    """
    params = [('timespan', 'timespan_example'),
                    ('apiVersion', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Insights/components/{application_name}/events/{event_type}/{event_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example', event_type='event_type_example', event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_get_by_type(client):
    """Test case for events_get_by_type

    Execute OData query
    """
    params = [('timespan', 'timespan_example'),
                    ('$filter', 'filter_example'),
                    ('$search', 'search_example'),
                    ('$orderby', 'orderby_example'),
                    ('$select', 'select_example'),
                    ('$skip', 56),
                    ('$top', 56),
                    ('$format', 'format_example'),
                    ('$count', True),
                    ('$apply', 'apply_example'),
                    ('apiVersion', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Insights/components/{application_name}/events/{event_type}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example', event_type='event_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_get_odata_metadata(client):
    """Test case for events_get_odata_metadata

    Get OData metadata
    """
    params = [('apiVersion', 'api_version_example')]
    headers = { 
        'Accept': 'application/xml;charset=utf-8',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Insights/components/{application_name}/events/$metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_get(client):
    """Test case for metrics_get

    Retrieve metric data
    """
    params = [('timespan', 'timespan_example'),
                    ('interval', 'interval_example'),
                    ('aggregation', ['aggregation_example']),
                    ('segment', ['segment_example']),
                    ('top', 56),
                    ('orderby', 'orderby_example'),
                    ('filter', 'filter_example'),
                    ('apiVersion', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Insights/components/{application_name}/metrics/{metric_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example', metric_id='metric_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_get_metadata(client):
    """Test case for metrics_get_metadata

    Retrieve metric metadata
    """
    params = [('apiVersion', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Insights/components/{application_name}/metrics/metadata'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_execute(client):
    """Test case for query_execute

    Execute an Analytics query
    """
    body = openapi_server.QueryBody()
    params = [('apiVersion', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Insights/components/{application_name}/query'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_get(client):
    """Test case for query_get

    Execute an Analytics query
    """
    params = [('query', 'query_example'),
                    ('timespan', 'timespan_example'),
                    ('apiVersion', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Insights/components/{application_name}/query'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

