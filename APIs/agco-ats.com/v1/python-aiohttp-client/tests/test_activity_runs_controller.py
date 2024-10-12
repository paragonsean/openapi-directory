# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_activity_run import APIPagedResponseBuildSystemSharedDTOActivityRun
from openapi_server.models.build_system_shared_dto_activity_run import BuildSystemSharedDTOActivityRun
from openapi_server.models.build_system_shared_dto_activity_run_status import BuildSystemSharedDTOActivityRunStatus


pytestmark = pytest.mark.asyncio

async def test_activity_runs_get_activity_run(client):
    """Test case for activity_runs_get_activity_run

    Get an ActivityRun by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/activityRuns/{activity_run_id}'.format(activity_run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_runs_get_activity_run_status(client):
    """Test case for activity_runs_get_activity_run_status

    Get the ActivityRunStatus of an ActivityRun
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/activityRuns/{activity_run_id}/status'.format(activity_run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_runs_get_activity_runs(client):
    """Test case for activity_runs_get_activity_runs

    Get ActivityRuns
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/activityRuns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activity_runs_put_activity_run(client):
    """Test case for activity_runs_put_activity_run

    Update an ActivityRun
    """
    body = openapi_server.BuildSystemSharedDTOActivityRun()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/activityRuns/{activity_run_id}'.format(activity_run_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activity_runs_put_activity_run_status(client):
    """Test case for activity_runs_put_activity_run_status

    Update the ActivityRunStatus of an ActivityRun
    """
    body = openapi_server.BuildSystemSharedDTOActivityRunStatus()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/activityRuns/{activity_run_id}/status'.format(activity_run_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

