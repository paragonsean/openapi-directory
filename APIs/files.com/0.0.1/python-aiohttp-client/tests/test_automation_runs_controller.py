# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.automation_run_entity import AutomationRunEntity


pytestmark = pytest.mark.asyncio

async def test_get_automation_runs(client):
    """Test case for get_automation_runs

    List Automation Runs
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('automation_id', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/automation_runs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_automation_runs_id(client):
    """Test case for get_automation_runs_id

    Show Automation Run
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/automation_runs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

