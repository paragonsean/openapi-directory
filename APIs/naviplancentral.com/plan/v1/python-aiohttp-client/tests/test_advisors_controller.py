# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advisor_model import AdvisorModel
from openapi_server.models.advisors_model import AdvisorsModel


pytestmark = pytest.mark.asyncio

async def test_advisors_get(client):
    """Test case for advisors_get

    Retrieve Advisors
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Advisors',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_advisors_get_by_householdid_clientid(client):
    """Test case for advisors_get_by_householdid_clientid

    Retrieve Advisors for a Client
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Advisors/{household_id}/{client_id}'.format(household_id=56, client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_advisors_get_by_id(client):
    """Test case for advisors_get_by_id

    Retrieve an Advisor
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/Advisors/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

