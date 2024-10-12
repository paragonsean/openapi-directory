# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_callback_url_parameters import GetCallbackUrlParameters
from openapi_server.models.json_schema import JsonSchema
from openapi_server.models.set_trigger_state_action_definition import SetTriggerStateActionDefinition
from openapi_server.models.workflow_trigger import WorkflowTrigger
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl
from openapi_server.models.workflow_trigger_list_result import WorkflowTriggerListResult


pytestmark = pytest.mark.asyncio

async def test_workflow_triggers_get(client):
    """Test case for workflow_triggers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_triggers_get_schema_json(client):
    """Test case for workflow_triggers_get_schema_json

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/schemas/json'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_triggers_list(client):
    """Test case for workflow_triggers_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_triggers_list_callback_url(client):
    """Test case for workflow_triggers_list_callback_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/listCallbackUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_triggers_reset(client):
    """Test case for workflow_triggers_reset

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/reset'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_triggers_run(client):
    """Test case for workflow_triggers_run

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/run'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_triggers_set_state(client):
    """Test case for workflow_triggers_set_state

    
    """
    set_state = {"source":{"name":"name","type":"type","properties":{"recurrence":{"schedule":{"hours":[5,5],"monthlyOccurrences":[{"occurrence":7,"day":"Sunday"},{"occurrence":7,"day":"Sunday"}],"weekDays":["Sunday","Sunday"],"minutes":[5,5],"monthDays":[2,2]},"timeZone":"timeZone","interval":1,"startTime":"startTime","endTime":"endTime","frequency":"NotSpecified"},"workflow":{"name":"name","id":"id","type":"type"},"nextExecutionTime":"2000-01-23T04:56:07.000+00:00","createdTime":"2000-01-23T04:56:07.000+00:00","changedTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"NotSpecified","state":"NotSpecified","lastExecutionTime":"2000-01-23T04:56:07.000+00:00","status":"NotSpecified"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/setState'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        json=set_state,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_versions_list_callback_url(client):
    """Test case for workflow_versions_list_callback_url

    
    """
    parameters = {"notAfter":"2000-01-23T04:56:07.000+00:00","keyType":"NotSpecified"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/versions/{version_id}/triggers/{trigger_name}/listCallbackUrl'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', version_id='version_id_example', trigger_name='trigger_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

