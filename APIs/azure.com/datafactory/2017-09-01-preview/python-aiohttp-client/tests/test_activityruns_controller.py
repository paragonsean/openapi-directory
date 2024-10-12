# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_runs_list_response import ActivityRunsListResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_activity_runs_list_by_pipeline_run(client):
    """Test case for activity_runs_list_by_pipeline_run

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('status', 'status_example'),
                    ('activityName', 'activity_name_example'),
                    ('linkedServiceName', 'linked_service_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelineruns/{run_id}/activityruns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', run_id='run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

