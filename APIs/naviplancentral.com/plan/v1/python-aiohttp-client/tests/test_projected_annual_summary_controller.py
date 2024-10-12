# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.projected_annual_summaries_model import ProjectedAnnualSummariesModel
from openapi_server.models.projected_annual_summary_model import ProjectedAnnualSummaryModel


pytestmark = pytest.mark.asyncio

async def test_projected_annual_summary_get_by_id_planid(client):
    """Test case for projected_annual_summary_get_by_id_planid

    Retrieve projected annual summary by id
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedAnnualSummary/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_annual_summary_get_by_planid(client):
    """Test case for projected_annual_summary_get_by_planid

    Retrieve projected annual summaries
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/ProjectedAnnualSummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

