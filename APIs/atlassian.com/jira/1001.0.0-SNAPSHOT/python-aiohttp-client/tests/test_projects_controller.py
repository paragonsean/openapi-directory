# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_project_details import CreateProjectDetails
from openapi_server.models.issue_type_with_status import IssueTypeWithStatus
from openapi_server.models.notification_scheme import NotificationScheme
from openapi_server.models.page_bean_project import PageBeanProject
from openapi_server.models.project import Project
from openapi_server.models.project_identifiers import ProjectIdentifiers
from openapi_server.models.project_issue_type_hierarchy import ProjectIssueTypeHierarchy
from openapi_server.models.task_progress_bean_object import TaskProgressBeanObject
from openapi_server.models.update_project_details import UpdateProjectDetails


pytestmark = pytest.mark.asyncio

async def test_archive_project(client):
    """Test case for archive_project

    Archive project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/project/{project_id_or_key}/archive'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_project(client):
    """Test case for create_project

    Create project
    """
    body = {"notificationScheme":7,"description":"description","leadAccountId":"leadAccountId","lead":"lead","url":"url","workflowScheme":3,"issueTypeScheme":5,"avatarId":0,"issueSecurityScheme":5,"projectTemplateKey":"com.pyxis.greenhopper.jira:gh-simplified-agility-kanban","name":"name","issueTypeScreenScheme":2,"permissionScheme":9,"assigneeType":"PROJECT_LEAD","fieldConfigurationScheme":1,"projectTypeKey":"software","categoryId":6,"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/project',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    Delete project
    """
    params = [('enableUndo', False)]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/project/{project_id_or_key}'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_asynchronously(client):
    """Test case for delete_project_asynchronously

    Delete project asynchronously
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/project/{project_id_or_key}/delete'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_projects(client):
    """Test case for get_all_projects

    Get all projects
    """
    params = [('expand', 'expand_example'),
                    ('recent', 56),
                    ('properties', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_statuses(client):
    """Test case for get_all_statuses

    Get all statuses for project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}/statuses'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hierarchy(client):
    """Test case for get_hierarchy

    Get project issue type hierarchy
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id}/hierarchy'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_scheme_for_project(client):
    """Test case for get_notification_scheme_for_project

    Get project notification scheme
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_key_or_id}/notificationscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project(client):
    """Test case for get_project

    Get project
    """
    params = [('expand', 'expand_example'),
                    ('properties', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/{project_id_or_key}'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent(client):
    """Test case for get_recent

    Get recent projects
    """
    params = [('expand', 'expand_example'),
                    ('properties', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/recent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore(client):
    """Test case for restore

    Restore deleted or archived project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/project/{project_id_or_key}/restore'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_projects(client):
    """Test case for search_projects

    Get projects paginated
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('orderBy', key),
                    ('id', [56]),
                    ('keys', ['keys_example']),
                    ('query', 'query_example'),
                    ('typeKey', 'type_key_example'),
                    ('categoryId', 56),
                    ('action', view),
                    ('expand', 'expand_example'),
                    ('status', ['status_example']),
                    ('properties', None),
                    ('propertyQuery', 'property_query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/project/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project(client):
    """Test case for update_project

    Update project
    """
    body = {"avatarId":0,"issueSecurityScheme":1,"notificationScheme":5,"name":"name","description":"description","permissionScheme":5,"assigneeType":"PROJECT_LEAD","leadAccountId":"leadAccountId","categoryId":6,"key":"key","lead":"lead","url":"url"}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_id_or_key}'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_type(client):
    """Test case for update_project_type

    Update project type
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/project/{project_id_or_key}/type/{new_project_type_key}'.format(project_id_or_key='project_id_or_key_example', new_project_type_key='new_project_type_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

