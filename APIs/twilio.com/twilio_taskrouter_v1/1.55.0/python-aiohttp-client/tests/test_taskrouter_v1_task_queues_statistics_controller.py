# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_task_queues_statistics_response import ListTaskQueuesStatisticsResponse


pytestmark = pytest.mark.asyncio

async def test_list_task_queues_statistics(client):
    """Test case for list_task_queues_statistics

    
    """
    params = [('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('Minutes', 56),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('TaskChannel', 'task_channel_example'),
                    ('SplitByWaitTime', 'split_by_wait_time_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/TaskQueues/Statistics'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

