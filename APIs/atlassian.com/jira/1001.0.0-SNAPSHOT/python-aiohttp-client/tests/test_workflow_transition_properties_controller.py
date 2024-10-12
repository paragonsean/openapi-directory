# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workflow_transition_property import WorkflowTransitionProperty


pytestmark = pytest.mark.asyncio

async def test_create_workflow_transition_property(client):
    """Test case for create_workflow_transition_property

    Create workflow transition property
    """
    body = {"id":"id","value":"value","key":"key"}
    params = [('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', live)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/workflow/transitions/{transition_id}/properties'.format(transition_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workflow_transition_property(client):
    """Test case for delete_workflow_transition_property

    Delete workflow transition property
    """
    params = [('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', 'workflow_mode_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/workflow/transitions/{transition_id}/properties'.format(transition_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflow_transition_properties(client):
    """Test case for get_workflow_transition_properties

    Get workflow transition properties
    """
    params = [('includeReservedKeys', False),
                    ('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', live)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflow/transitions/{transition_id}/properties'.format(transition_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workflow_transition_property(client):
    """Test case for update_workflow_transition_property

    Update workflow transition property
    """
    body = {"id":"id","value":"value","key":"key"}
    params = [('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', 'workflow_mode_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflow/transitions/{transition_id}/properties'.format(transition_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

