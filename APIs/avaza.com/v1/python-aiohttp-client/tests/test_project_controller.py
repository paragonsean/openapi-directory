# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_project_model import NewProjectModel
from openapi_server.models.project_details import ProjectDetails
from openapi_server.models.project_dropdown_list import ProjectDropdownList
from openapi_server.models.project_list import ProjectList
from openapi_server.models.update_project_model import UpdateProjectModel


pytestmark = pytest.mark.asyncio

async def test_project_get(client):
    """Test case for project_get

    Gets list of Projects
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example'),
                    ('TimesheetUserID', 56),
                    ('includeArchived', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_get_by_id(client):
    """Test case for project_get_by_id

    Gets Project by Project ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Project/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_lookup(client):
    """Test case for project_lookup

    Gets minimal list of active Projects for the current user
    """
    params = [('pageSize', 56),
                    ('pageNumber', 56),
                    ('TimesheetUserID', 56),
                    ('CompanyIDFK', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Project/Lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_project_post(client):
    """Test case for project_post

    Create a Project
    """
    model = {"PopulateDefaultProjectMembers":True,"ProjectStatusCode":"ProjectStatusCode","isTaskRequiredOnTimesheet":True,"TimesheetApprovalRequiredbyDefault":True,"BudgetHours":6.027456183070403,"CompanyIDFK":1,"EndDate":"2000-01-23T04:56:07.000+00:00","BudgetAmount":0.8008281904610115,"CurrencyCode":"CurrencyCode","StartDate":"2000-01-23T04:56:07.000+00:00","CompanyName":"CompanyName","ProjectNotes":"ProjectNotes","ProjectCategoryIDFK":5,"ProjectTitle":"ProjectTitle","ProjectCode":"ProjectCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Project',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_project_put(client):
    """Test case for project_put

    Update an Project
    """
    model = {"ProjectStatusCode":"ProjectStatusCode","FieldsToUpdate":["FieldsToUpdate","FieldsToUpdate"],"isTaskRequiredOnTimesheet":True,"TimesheetApprovalRequiredbyDefault":True,"BudgetHours":6.027456183070403,"ProjectBillableTypeCode":"ProjectBillableTypeCode","ProjectID":5,"EndDate":"2000-01-23T04:56:07.000+00:00","BudgetAmount":0.8008281904610115,"StartDate":"2000-01-23T04:56:07.000+00:00","ProjectBudgetTypeCode":"ProjectBudgetTypeCode","ProjectNotes":"ProjectNotes","ProjectCategoryIDFK":1,"ProjectTitle":"ProjectTitle"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Project',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

