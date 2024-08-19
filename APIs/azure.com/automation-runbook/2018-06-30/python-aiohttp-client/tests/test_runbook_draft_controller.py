# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.runbook_draft import RunbookDraft
from openapi_server.models.runbook_draft_undo_edit_result import RunbookDraftUndoEditResult
from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_runbook_draft_get(client):
    """Test case for runbook_draft_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runbook_draft_get_content(client):
    """Test case for runbook_draft_get_content

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'text/powershell',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/content'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/powershell not supported by Connexion")
async def test_runbook_draft_replace_content(client):
    """Test case for runbook_draft_replace_content

    
    """
    runbook_content = None
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/powershell',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/content'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        json=runbook_content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runbook_draft_undo_edit(client):
    """Test case for runbook_draft_undo_edit

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/undoEdit'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

