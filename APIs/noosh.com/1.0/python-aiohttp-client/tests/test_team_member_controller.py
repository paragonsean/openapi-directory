# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact_user_vo import ContactUserVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.team_member_base_inf_vo import TeamMemberBaseInfVO
from openapi_server.models.team_member_list_vo import TeamMemberListVO
from openapi_server.models.team_member_po import TeamMemberPO
from openapi_server.models.v1x1_invited_team_member_results_vo import V1x1InvitedTeamMemberResultsVO


pytestmark = pytest.mark.asyncio

async def test_delete_team_member_of_project(client):
    """Test case for delete_team_member_of_project

    Delete a team member for the specific project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers/{teammember_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', teammember_id='teammember_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_member_list_of_client_project(client):
    """Test case for get_team_member_list_of_client_project

    List team member of client project side.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/teamMembersOfClientProject'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_member_list_of_project(client):
    """Test case for get_team_member_list_of_project

    List team member of project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_team_member_of_project(client):
    """Test case for post_team_member_of_project

    Invite a team member or all the members of team template for the specific project.
    """
    body = {"role_id":1,"user_id":1,"team_template_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/1.1/workgroups/{workgroup_id}/projects/{project_id}/teammembers'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_workgroups_workgroup_id_projects_project_id_teammembers_post(client):
    """Test case for v1_workgroups_workgroup_id_projects_project_id_teammembers_post

    Deprecated, please use 1.1 Version
    """
    body = {"role_id":1,"user_id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

