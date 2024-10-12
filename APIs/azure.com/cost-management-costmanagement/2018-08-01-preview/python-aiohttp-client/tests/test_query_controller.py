# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.query_result import QueryResult
from openapi_server.models.report_definition import ReportDefinition


pytestmark = pytest.mark.asyncio

async def test_query_billing_account(client):
    """Test case for query_billing_account

    
    """
    parameters = {"timeframe":"WeekToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"name":"name","type":"Tag"},{"name":"name","type":"Tag"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/Query'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_resource_group(client):
    """Test case for query_resource_group

    
    """
    parameters = {"timeframe":"WeekToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"name":"name","type":"Tag"},{"name":"name","type":"Tag"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.CostManagement/Query'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_subscription(client):
    """Test case for query_subscription

    
    """
    parameters = {"timeframe":"WeekToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"name":"name","type":"Tag"},{"name":"name","type":"Tag"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/Query'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

