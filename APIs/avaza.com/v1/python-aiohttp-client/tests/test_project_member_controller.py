# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_project_member import NewProjectMember
from openapi_server.models.project_member_details import ProjectMemberDetails
from openapi_server.models.project_member_list import ProjectMemberList
from openapi_server.models.update_project_member import UpdateProjectMember


pytestmark = pytest.mark.asyncio

async def test_project_member_get(client):
    """Test case for project_member_get

    Gets list of Project Members
    """
    params = [('ProjectID', 56),
                    ('UserID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ProjectMember',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_project_member_post(client):
    """Test case for project_member_post

    Assign a user as a Member of a Project
    """
    model = {"isTimesheetApprovalRequired":True,"canUpdateTasks":True,"canDeleteTasks":True,"canCommentOnTasks":True,"ProjectIDFK":1,"CostAmount":6.027456183070403,"canCreateTasks":True,"isTimesheetApprover":True,"RateAmount":5.962133916683182,"UserIDFK":5,"BudgetAmount":0.8008281904610115,"isTimesheetAllowed":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ProjectMember',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_project_member_put(client):
    """Test case for project_member_put

    Update a Member of a Project
    """
    model = {"isTimesheetApprovalRequired":True,"canUpdateTasks":True,"FieldsToUpdate":["FieldsToUpdate","FieldsToUpdate"],"ProjectIDFK":1,"isTimesheetApprover":True,"RateAmount":5.962133916683182,"BudgetAmount":0.8008281904610115,"canDeleteTasks":True,"canCommentOnTasks":True,"CostAmount":6.027456183070403,"canCreateTasks":True,"UserIDFK":5,"isTimesheetAllowed":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/ProjectMember',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

