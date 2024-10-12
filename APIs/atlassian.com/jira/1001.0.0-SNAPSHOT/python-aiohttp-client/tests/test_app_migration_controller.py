# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connect_custom_field_values import ConnectCustomFieldValues
from openapi_server.models.entity_property_details import EntityPropertyDetails
from openapi_server.models.workflow_rules_search import WorkflowRulesSearch
from openapi_server.models.workflow_rules_search_details import WorkflowRulesSearchDetails


pytestmark = pytest.mark.asyncio

async def test_app_issue_field_value_update_resource_update_issue_fields_put(client):
    """Test case for app_issue_field_value_update_resource_update_issue_fields_put

    Bulk update custom field value
    """
    body = {"updateValueList":[{"number":1.4658129805029452,"issueID":6,"string":"string","_type":"StringIssueField","optionID":"optionID","text":"text","richText":"richText","fieldID":0},{"number":1.4658129805029452,"issueID":6,"string":"string","_type":"StringIssueField","optionID":"optionID","text":"text","richText":"richText","fieldID":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'atlassian_transfer_id': 'atlassian_transfer_id_example',
    }
    response = await client.request(
        method='PUT',
        path='/rest/atlassian-connect/1/migration/field',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migration_resource_update_entity_properties_value_put(client):
    """Test case for migration_resource_update_entity_properties_value_put

    Bulk update entity properties
    """
    body = {"entityId":123,"value":"newValue","key":"mykey"}
    headers = { 
        'Content-Type': 'application/json',
        'atlassian_transfer_id': 'atlassian_transfer_id_example',
    }
    response = await client.request(
        method='PUT',
        path='/rest/atlassian-connect/1/migration/properties/{entity_type}'.format(entity_type='entity_type_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migration_resource_workflow_rule_search_post(client):
    """Test case for migration_resource_workflow_rule_search_post

    Get workflow transition rule configurations
    """
    body = {"expand":"transition","ruleIds":["55d44f1d-c859-42e5-9c27-2c5ec3f340b1","55d44f1d-c859-42e5-9c27-2c5ec3f340b1","55d44f1d-c859-42e5-9c27-2c5ec3f340b1","55d44f1d-c859-42e5-9c27-2c5ec3f340b1","55d44f1d-c859-42e5-9c27-2c5ec3f340b1"],"workflowEntityId":"a498d711-685d-428d-8c3e-bc03bb450ea7"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'atlassian_transfer_id': 'atlassian_transfer_id_example',
    }
    response = await client.request(
        method='POST',
        path='/rest/atlassian-connect/1/migration/workflow/rule/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

