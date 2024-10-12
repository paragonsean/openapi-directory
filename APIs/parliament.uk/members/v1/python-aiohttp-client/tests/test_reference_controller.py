# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.answering_body import AnsweringBody
from openapi_server.models.generic_reference_data import GenericReferenceData
from openapi_server.models.government_department import GovernmentDepartment


pytestmark = pytest.mark.asyncio

async def test_api_reference_answering_bodies_get(client):
    """Test case for api_reference_answering_bodies_get

    Returns a list of answering bodies.
    """
    params = [('id', 56),
                    ('nameContains', 'name_contains_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Reference/AnsweringBodies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_reference_departments_get(client):
    """Test case for api_reference_departments_get

    Returns a list of departments.
    """
    params = [('id', 56),
                    ('nameContains', 'name_contains_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Reference/Departments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_reference_departments_id_logo_get(client):
    """Test case for api_reference_departments_id_logo_get

    Returns department logo.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/Reference/Departments/{id}/Logo'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_reference_policy_interests_get(client):
    """Test case for api_reference_policy_interests_get

    Returns a list of policy interest.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Reference/PolicyInterests',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

