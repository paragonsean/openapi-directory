# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.run_filter_parameters import RunFilterParameters
from openapi_server.models.trigger_runs_query_response import TriggerRunsQueryResponse


pytestmark = pytest.mark.asyncio

async def test_trigger_runs_query_by_factory(client):
    """Test case for trigger_runs_query_by_factory

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/queryTriggerRuns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=filter_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trigger_runs_rerun(client):
    """Test case for trigger_runs_rerun

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/triggerRuns/{run_id}/rerun'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example', run_id='run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

