# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_workflows_step_completed(client):
    """Test case for workflows_step_completed

    
    """
    params = [('workflow_step_execute_id', 'workflow_step_execute_id_example'),
                    ('outputs', 'outputs_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/workflows.stepCompleted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_step_failed(client):
    """Test case for workflows_step_failed

    
    """
    params = [('workflow_step_execute_id', 'workflow_step_execute_id_example'),
                    ('error', 'error_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/workflows.stepFailed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflows_update_step(client):
    """Test case for workflows_update_step

    
    """
    params = [('workflow_step_edit_id', 'workflow_step_edit_id_example'),
                    ('inputs', 'inputs_example'),
                    ('outputs', 'outputs_example'),
                    ('step_name', 'step_name_example'),
                    ('step_image_url', 'step_image_url_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/workflows.updateStep',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

