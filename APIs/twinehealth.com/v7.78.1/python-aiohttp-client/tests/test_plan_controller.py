# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_patient_plan_summaries_response import FetchPatientPlanSummariesResponse
from openapi_server.models.fetch_patient_plan_summary_response import FetchPatientPlanSummaryResponse
from openapi_server.models.update_patient_plan_summary_request import UpdatePatientPlanSummaryRequest
from openapi_server.models.update_patient_plan_summary_response import UpdatePatientPlanSummaryResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_plan_summaries(client):
    """Test case for fetch_patient_plan_summaries

    List patient plan summaries
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient_plan_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_patient_plan_summary(client):
    """Test case for fetch_patient_plan_summary

    Get the plan summary for a patient
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/patient_plan_summary/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_patient_plan_summary(client):
    """Test case for update_patient_plan_summary

    Update a plan summary
    """
    body = openapi_server.UpdatePatientPlanSummaryRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='PATCH',
        path='/pub/patient_plan_summary/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

