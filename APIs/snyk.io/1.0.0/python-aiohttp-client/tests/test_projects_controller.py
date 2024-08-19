# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_a_tag_to_a_project200_response import AddATagToAProject200Response
from openapi_server.models.add_a_tag_to_a_project_request import AddATagToAProjectRequest
from openapi_server.models.add_ignore_request import AddIgnoreRequest
from openapi_server.models.applying_attributes200_response import ApplyingAttributes200Response
from openapi_server.models.applying_attributes_request import ApplyingAttributesRequest
from openapi_server.models.create_jira_issue200_response import CreateJiraIssue200Response
from openapi_server.models.create_jira_issue_request import CreateJiraIssueRequest
from openapi_server.models.get_project_dependency_graph200_response import GetProjectDependencyGraph200Response
from openapi_server.models.list_all_aggregated_issues200_response import ListAllAggregatedIssues200Response
from openapi_server.models.list_all_aggregated_issues_request import ListAllAggregatedIssuesRequest
from openapi_server.models.list_all_project_snapshot_issue_paths200_response import ListAllProjectSnapshotIssuePaths200Response
from openapi_server.models.list_all_project_snapshots200_response import ListAllProjectSnapshots200Response
from openapi_server.models.list_all_project_snapshots_request import ListAllProjectSnapshotsRequest
from openapi_server.models.list_all_projects200_response import ListAllProjects200Response
from openapi_server.models.list_all_projects_request import ListAllProjectsRequest
from openapi_server.models.list_project_settings200_response import ListProjectSettings200Response
from openapi_server.models.move_project_to_a_different_organization_request import MoveProjectToADifferentOrganizationRequest
from openapi_server.models.retrieve_a_single_project200_response import RetrieveASingleProject200Response
from openapi_server.models.update_a_project_request import UpdateAProjectRequest
from openapi_server.models.update_project_settings_request import UpdateProjectSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_activate(client):
    """Test case for activate

    Activate
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/activate'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_a_tag_to_a_project(client):
    """Test case for add_a_tag_to_a_project

    Add a tag to a project
    """
    body = openapi_server.AddATagToAProjectRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/tags'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_ignore(client):
    """Test case for add_ignore

    Add ignore
    """
    body = openapi_server.AddIgnoreRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/ignore/{issue_id}'.format(org_id='org_id_example', project_id='project_id_example', issue_id='issue_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applying_attributes(client):
    """Test case for applying_attributes

    Applying attributes
    """
    body = openapi_server.ApplyingAttributesRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/attributes'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_jira_issue(client):
    """Test case for create_jira_issue

    Create jira issue
    """
    body = openapi_server.CreateJiraIssueRequest()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/issue/{issue_id}/jira-issue'.format(issue_id='npm:qs:20140806-1', org_id='org_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate(client):
    """Test case for deactivate

    Deactivate
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/deactivate'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_a_project(client):
    """Test case for delete_a_project

    Delete a project
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}/project/{project_id}'.format(org_id='org_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ignores(client):
    """Test case for delete_ignores

    Delete ignores
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}/project/{project_id}/ignore/{issue_id}'.format(org_id='org_id_example', project_id='project_id_example', issue_id='issue_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_settings(client):
    """Test case for delete_project_settings

    Delete project settings
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/org/{org_id}/project/{project_id}/settings'.format(org_id='org_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_dependency_graph(client):
    """Test case for get_project_dependency_graph

    Get Project dependency graph
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}/dep-graph'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_aggregated_issues(client):
    """Test case for list_all_aggregated_issues

    List all Aggregated issues
    """
    body = openapi_server.ListAllAggregatedIssuesRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/aggregated-issues'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_ignores(client):
    """Test case for list_all_ignores

    List all ignores
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}/ignores'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_jira_issues(client):
    """Test case for list_all_jira_issues

    List all jira issues
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}/jira-issues'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_project_issue_paths(client):
    """Test case for list_all_project_issue_paths

    List all project issue paths
    """
    params = [('snapshotId', 'latest'),
                    ('perPage', 100),
                    ('page', 1)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}/issue/{issue_id}/paths'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545', issue_id='SNYK-JS-LODASH-590103'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_project_snapshot_aggregated_issues(client):
    """Test case for list_all_project_snapshot_aggregated_issues

    List all project snapshot aggregated issues
    """
    body = openapi_server.ListAllAggregatedIssuesRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/history/{snapshot_id}/aggregated-issues'.format(org_id='2d5c4d0c-c6d6-4658-a703-c2721c135b26', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545', snapshot_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454553'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_project_snapshot_issue_paths(client):
    """Test case for list_all_project_snapshot_issue_paths

    List all project snapshot issue paths
    """
    params = [('perPage', 100),
                    ('page', 1)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}/history/{snapshot_id}/issue/{issue_id}/paths'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545', snapshot_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454553', issue_id='SNYK-JS-LODASH-590103'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_project_snapshots(client):
    """Test case for list_all_project_snapshots

    List all project snapshots
    """
    body = openapi_server.ListAllProjectSnapshotsRequest()
    params = [('perPage', 10),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/history'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_projects(client):
    """Test case for list_all_projects

    List all projects
    """
    body = openapi_server.ListAllProjectsRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/projects'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_project_settings(client):
    """Test case for list_project_settings

    List project settings
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}/settings'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_project_to_a_different_organization(client):
    """Test case for move_project_to_a_different_organization

    Move project to a different organization
    """
    body = openapi_server.MoveProjectToADifferentOrganizationRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/project/{project_id}/move'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_a_tag_from_a_project(client):
    """Test case for remove_a_tag_from_a_project

    Remove a tag from a project
    """
    body = openapi_server.AddATagToAProjectRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/org/{org_id}/project/{project_id}/tags/remove'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='6d5813be-7e6d-4ab8-80c2-1e3e2a454545'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_ignores(client):
    """Test case for replace_ignores

    Replace ignores
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/project/{project_id}/ignore/{issue_id}'.format(org_id='org_id_example', project_id='project_id_example', issue_id='issue_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_single_project(client):
    """Test case for retrieve_a_single_project

    Retrieve a single project
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_ignore(client):
    """Test case for retrieve_ignore

    Retrieve ignore
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/org/{org_id}/project/{project_id}/ignore/{issue_id}'.format(org_id='4a18d42f-0706-4ad0-b127-24078731fbed', project_id='463c1ee5-31bc-428c-b451-b79a3270db08', issue_id='npm:qs:20140806-1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_project(client):
    """Test case for update_a_project

    Update a project
    """
    body = openapi_server.UpdateAProjectRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/project/{project_id}'.format(org_id='org_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_settings(client):
    """Test case for update_project_settings

    Update project settings
    """
    body = openapi_server.UpdateProjectSettingsRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/org/{org_id}/project/{project_id}/settings'.format(org_id='org_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

