# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.page_bean_workflow_transition_rules import PageBeanWorkflowTransitionRules
from openapi_server.models.workflow_transition_rules_update import WorkflowTransitionRulesUpdate
from openapi_server.models.workflow_transition_rules_update_errors import WorkflowTransitionRulesUpdateErrors
from openapi_server.models.workflows_with_transition_rules_details import WorkflowsWithTransitionRulesDetails


pytestmark = pytest.mark.asyncio

async def test_delete_workflow_transition_rule_configurations(client):
    """Test case for delete_workflow_transition_rule_configurations

    Delete workflow transition rule configurations
    """
    body = {"workflows":[{"workflowRuleIds":["workflowRuleIds","workflowRuleIds"],"workflowId":{"draft":True,"name":"name"}},{"workflowRuleIds":["workflowRuleIds","workflowRuleIds"],"workflowId":{"draft":True,"name":"name"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflow/rule/config/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflow_transition_rule_configurations(client):
    """Test case for get_workflow_transition_rule_configurations

    Get workflow transition rule configurations
    """
    params = [('startAt', 0),
                    ('maxResults', 10),
                    ('types', ['types_example']),
                    ('keys', ['keys_example']),
                    ('workflowNames', ['workflow_names_example']),
                    ('withTags', ['with_tags_example']),
                    ('draft', True),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflow/rule/config',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workflow_transition_rule_configurations(client):
    """Test case for update_workflow_transition_rule_configurations

    Update workflow transition rule configurations
    """
    body = {"workflows":[{"postFunctions":[{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""},{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""}],"validators":[{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""},{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""}],"conditions":[{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""},{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""}],"workflowId":{"draft":True,"name":"name"}},{"postFunctions":[{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""},{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""}],"validators":[{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""},{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""}],"conditions":[{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""},{"configuration":{"disabled":False,"tag":"tag","value":"value"},"id":"id","key":"key","transition":""}],"workflowId":{"draft":True,"name":"name"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflow/rule/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

