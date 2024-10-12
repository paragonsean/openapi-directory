# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_workflow import DefaultWorkflow
from openapi_server.models.issue_type_workflow_mapping import IssueTypeWorkflowMapping
from openapi_server.models.issue_types_workflow_mapping import IssueTypesWorkflowMapping
from openapi_server.models.page_bean_workflow_scheme import PageBeanWorkflowScheme
from openapi_server.models.workflow_scheme import WorkflowScheme


pytestmark = pytest.mark.asyncio

async def test_create_workflow_scheme(client):
    """Test case for create_workflow_scheme

    Create workflow scheme
    """
    body = {"originalDefaultWorkflow":"originalDefaultWorkflow","description":"description","issueTypes":{"key":{"avatarId":0,"hierarchyLevel":6,"scope":"","name":"name","description":"description","self":"self","entityId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","iconUrl":"iconUrl","id":"id","subtask":True}},"originalIssueTypeMappings":{"key":"originalIssueTypeMappings"},"defaultWorkflow":"defaultWorkflow","updateDraftIfNeeded":True,"draft":True,"name":"name","self":"https://openapi-generator.tech","lastModifiedUser":"","id":5,"lastModified":"lastModified","issueTypeMappings":{"key":"issueTypeMappings"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/workflowscheme',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_default_workflow(client):
    """Test case for delete_default_workflow

    Delete default workflow
    """
    params = [('updateDraftIfNeeded', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/workflowscheme/{id}/default'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workflow_mapping(client):
    """Test case for delete_workflow_mapping

    Delete issue types for workflow in workflow scheme
    """
    params = [('workflowName', 'workflow_name_example'),
                    ('updateDraftIfNeeded', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/workflowscheme/{id}/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workflow_scheme(client):
    """Test case for delete_workflow_scheme

    Delete workflow scheme
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/workflowscheme/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workflow_scheme_issue_type(client):
    """Test case for delete_workflow_scheme_issue_type

    Delete workflow for issue type in workflow scheme
    """
    params = [('updateDraftIfNeeded', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/workflowscheme/{id}/issuetype/{issue_type}'.format(id=56, issue_type='issue_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_workflow_schemes(client):
    """Test case for get_all_workflow_schemes

    Get all workflow schemes
    """
    params = [('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflowscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_workflow(client):
    """Test case for get_default_workflow

    Get default workflow
    """
    params = [('returnDraftIfExists', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflowscheme/{id}/default'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflow(client):
    """Test case for get_workflow

    Get issue types for workflows in workflow scheme
    """
    params = [('workflowName', 'workflow_name_example'),
                    ('returnDraftIfExists', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflowscheme/{id}/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflow_scheme(client):
    """Test case for get_workflow_scheme

    Get workflow scheme
    """
    params = [('returnDraftIfExists', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflowscheme/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflow_scheme_issue_type(client):
    """Test case for get_workflow_scheme_issue_type

    Get workflow for issue type in workflow scheme
    """
    params = [('returnDraftIfExists', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/workflowscheme/{id}/issuetype/{issue_type}'.format(id=56, issue_type='issue_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_workflow_scheme_issue_type(client):
    """Test case for set_workflow_scheme_issue_type

    Set workflow for issue type in workflow scheme
    """
    body = {"issueType":"issueType","updateDraftIfNeeded":True,"workflow":"workflow"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflowscheme/{id}/issuetype/{issue_type}'.format(id=56, issue_type='issue_type_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_default_workflow(client):
    """Test case for update_default_workflow

    Update default workflow
    """
    body = {"updateDraftIfNeeded":True,"workflow":"workflow"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflowscheme/{id}/default'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workflow_mapping(client):
    """Test case for update_workflow_mapping

    Set issue types for workflow in workflow scheme
    """
    body = {"updateDraftIfNeeded":True,"workflow":"workflow","defaultMapping":True,"issueTypes":["issueTypes","issueTypes"]}
    params = [('workflowName', 'workflow_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflowscheme/{id}/workflow'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workflow_scheme(client):
    """Test case for update_workflow_scheme

    Update workflow scheme
    """
    body = {"originalDefaultWorkflow":"originalDefaultWorkflow","description":"description","issueTypes":{"key":{"avatarId":0,"hierarchyLevel":6,"scope":"","name":"name","description":"description","self":"self","entityId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","iconUrl":"iconUrl","id":"id","subtask":True}},"originalIssueTypeMappings":{"key":"originalIssueTypeMappings"},"defaultWorkflow":"defaultWorkflow","updateDraftIfNeeded":True,"draft":True,"name":"name","self":"https://openapi-generator.tech","lastModifiedUser":"","id":5,"lastModified":"lastModified","issueTypeMappings":{"key":"issueTypeMappings"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/workflowscheme/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

