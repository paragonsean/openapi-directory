# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.view import View
from openapi_server.models.view_list_result import ViewListResult


pytestmark = pytest.mark.asyncio

async def test_views_create_or_update(client):
    """Test case for views_create_or_update

    
    """
    parameters = {"properties":{"modifiedOn":"2000-01-23T04:56:07.000+00:00","metric":"ActualCost","displayName":"displayName","query":{"timeframe":"WeekToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","sorting":[{"name":"name","direction":"Ascending"},{"name":"name","direction":"Ascending"}],"aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"name":"name","type":"Tag"},{"name":"name","type":"Tag"}]}},"scope":"scope","pivots":[{"name":"name","type":"Dimension"},{"name":"name","type":"Dimension"}],"chart":"Area","createdOn":"2000-01-23T04:56:07.000+00:00","kpis":[{"id":"id","type":"Forecast","enabled":True},{"id":"id","type":"Forecast","enabled":True}],"accumulated":"true"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.CostManagement/views/{view_name}'.format(view_name='view_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_create_or_update_by_scope(client):
    """Test case for views_create_or_update_by_scope

    
    """
    parameters = {"properties":{"modifiedOn":"2000-01-23T04:56:07.000+00:00","metric":"ActualCost","displayName":"displayName","query":{"timeframe":"WeekToDate","timePeriod":{"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"},"type":"Usage","dataset":{"filter":{"or":[null,null],"and":[null,null],"tag":{"values":["values","values"],"name":"name","operator":"In"},"dimension":{"values":["values","values"],"name":"name","operator":"In"}},"configuration":{"columns":["columns","columns"]},"granularity":"Daily","sorting":[{"name":"name","direction":"Ascending"},{"name":"name","direction":"Ascending"}],"aggregation":{"key":{"function":"Sum","name":"name"}},"grouping":[{"name":"name","type":"Tag"},{"name":"name","type":"Tag"}]}},"scope":"scope","pivots":[{"name":"name","type":"Dimension"},{"name":"name","type":"Dimension"}],"chart":"Area","createdOn":"2000-01-23T04:56:07.000+00:00","kpis":[{"id":"id","type":"Forecast","enabled":True},{"id":"id","type":"Forecast","enabled":True}],"accumulated":"true"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.CostManagement/views/{view_name}'.format(scope='scope_example', view_name='view_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_delete(client):
    """Test case for views_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.CostManagement/views/{view_name}'.format(view_name='view_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_delete_by_scope(client):
    """Test case for views_delete_by_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.CostManagement/views/{view_name}'.format(scope='scope_example', view_name='view_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_get(client):
    """Test case for views_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/views/{view_name}'.format(view_name='view_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_get_by_scope(client):
    """Test case for views_get_by_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CostManagement/views/{view_name}'.format(scope='scope_example', view_name='view_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_list(client):
    """Test case for views_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.CostManagement/views',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_list_by_scope(client):
    """Test case for views_list_by_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.CostManagement/views'.format(scope='scope_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

