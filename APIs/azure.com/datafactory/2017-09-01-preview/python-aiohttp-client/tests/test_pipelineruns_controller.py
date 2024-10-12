# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.pipeline_run import PipelineRun
from openapi_server.models.pipeline_run_filter_parameters import PipelineRunFilterParameters
from openapi_server.models.pipeline_run_query_response import PipelineRunQueryResponse


pytestmark = pytest.mark.asyncio

async def test_factories_cancel_pipeline_run(client):
    """Test case for factories_cancel_pipeline_run

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/cancelpipelinerun/{run_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', run_id='run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipeline_runs_get(client):
    """Test case for pipeline_runs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelineruns/{run_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', run_id='run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipeline_runs_query_by_factory(client):
    """Test case for pipeline_runs_query_by_factory

    
    """
    filter_parameters = {"orderBy":[{"orderBy":"RunStart","order":"ASC"},{"orderBy":"RunStart","order":"ASC"}],"filters":[{"values":["values","values"],"operand":"PipelineName","operator":"Equals"},{"values":["values","values"],"operand":"PipelineName","operator":"Equals"}],"lastUpdatedAfter":"2000-01-23T04:56:07.000+00:00","lastUpdatedBefore":"2000-01-23T04:56:07.000+00:00","continuationToken":"continuationToken"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelineruns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=filter_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

