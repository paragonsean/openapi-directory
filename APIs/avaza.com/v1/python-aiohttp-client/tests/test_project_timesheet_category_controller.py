# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assign_project_timesheet_category import AssignProjectTimesheetCategory
from openapi_server.models.project_timesheet_category_details import ProjectTimesheetCategoryDetails
from openapi_server.models.project_timesheet_category_list import ProjectTimesheetCategoryList


pytestmark = pytest.mark.asyncio

async def test_project_timesheet_category_get(client):
    """Test case for project_timesheet_category_get

    Gets list of Project Timesheet Categories
    """
    params = [('ProjectID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ProjectTimesheetCategory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_project_timesheet_category_post(client):
    """Test case for project_timesheet_category_post

    Assign a TimeSheetCategory to a Project.
    """
    model = {"BudgetHours":0.8008281904610115,"ProjectIDFK":1,"CostAmount":6.027456183070403,"RateAmount":5.962133916683182,"TimesheetCategoryIDFK":5,"isBillable":True,"isPayable":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ProjectTimesheetCategory',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

