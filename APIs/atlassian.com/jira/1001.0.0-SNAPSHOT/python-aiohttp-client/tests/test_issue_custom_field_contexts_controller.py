# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_custom_field_context import CreateCustomFieldContext
from openapi_server.models.custom_field_context_default_value_update import CustomFieldContextDefaultValueUpdate
from openapi_server.models.custom_field_context_update_details import CustomFieldContextUpdateDetails
from openapi_server.models.issue_type_ids import IssueTypeIds
from openapi_server.models.page_bean_context_for_project_and_issue_type import PageBeanContextForProjectAndIssueType
from openapi_server.models.page_bean_custom_field_context import PageBeanCustomFieldContext
from openapi_server.models.page_bean_custom_field_context_default_value import PageBeanCustomFieldContextDefaultValue
from openapi_server.models.page_bean_custom_field_context_project_mapping import PageBeanCustomFieldContextProjectMapping
from openapi_server.models.page_bean_issue_type_to_context_mapping import PageBeanIssueTypeToContextMapping
from openapi_server.models.project_ids import ProjectIds
from openapi_server.models.project_issue_type_mappings import ProjectIssueTypeMappings


pytestmark = pytest.mark.asyncio

async def test_add_issue_types_to_context(client):
    """Test case for add_issue_types_to_context

    Add issue types to context
    """
    body = {"issueTypeIds":["issueTypeIds","issueTypeIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_id}/context/{context_id}/issuetype'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assign_projects_to_custom_field_context(client):
    """Test case for assign_projects_to_custom_field_context

    Assign custom field context to projects
    """
    body = {"projectIds":["projectIds","projectIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_id}/context/{context_id}/project'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_custom_field_context(client):
    """Test case for create_custom_field_context

    Create custom field context
    """
    body = {"issueTypeIds":["issueTypeIds","issueTypeIds"],"name":"name","description":"description","id":"id","projectIds":["projectIds","projectIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{field_id}/context'.format(field_id='field_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_field_context(client):
    """Test case for delete_custom_field_context

    Delete custom field context
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/field/{field_id}/context/{context_id}'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contexts_for_field(client):
    """Test case for get_contexts_for_field

    Get custom field contexts
    """
    params = [('isAnyIssueType', True),
                    ('isGlobalContext', True),
                    ('contextId', [56]),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_id}/context'.format(field_id='field_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_field_contexts_for_projects_and_issue_types(client):
    """Test case for get_custom_field_contexts_for_projects_and_issue_types

    Get custom field contexts for projects and issue types
    """
    body = {"mappings":[{"issueTypeId":"issueTypeId","projectId":"projectId"},{"issueTypeId":"issueTypeId","projectId":"projectId"}]}
    params = [('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{field_id}/context/mapping'.format(field_id='field_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_values(client):
    """Test case for get_default_values

    Get custom field contexts default values
    """
    params = [('contextId', [56]),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_id}/context/defaultValue'.format(field_id='field_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_type_mappings_for_contexts(client):
    """Test case for get_issue_type_mappings_for_contexts

    Get issue types for custom field context
    """
    params = [('contextId', [56]),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_id}/context/issuetypemapping'.format(field_id='field_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_context_mapping(client):
    """Test case for get_project_context_mapping

    Get project mappings for custom field context
    """
    params = [('contextId', [56]),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/field/{field_id}/context/projectmapping'.format(field_id='field_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_custom_field_context_from_projects(client):
    """Test case for remove_custom_field_context_from_projects

    Remove custom field context from projects
    """
    body = {"projectIds":["projectIds","projectIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{field_id}/context/{context_id}/project/remove'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_issue_types_from_context(client):
    """Test case for remove_issue_types_from_context

    Remove issue types from context
    """
    body = {"issueTypeIds":["issueTypeIds","issueTypeIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/field/{field_id}/context/{context_id}/issuetype/remove'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_default_values(client):
    """Test case for set_default_values

    Set custom field contexts default values
    """
    body = {"defaultValues":[{"contextId":"contextId","optionId":"optionId","type":"type","cascadingOptionId":"cascadingOptionId"},{"contextId":"contextId","optionId":"optionId","type":"type","cascadingOptionId":"cascadingOptionId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_id}/context/defaultValue'.format(field_id='field_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field_context(client):
    """Test case for update_custom_field_context

    Update custom field context
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/field/{field_id}/context/{context_id}'.format(field_id='field_id_example', context_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

