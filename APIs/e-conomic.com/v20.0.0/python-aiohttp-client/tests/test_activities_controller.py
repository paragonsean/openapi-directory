# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_cursor_results import ActivityCursorResults
from openapi_server.models.created_result import CreatedResult
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_activity(client):
    """Test case for create_activity

    Create a single Activity
    """
    body = {"Description":"An awesome activity","Id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v20.0.0/activities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_activity_by_id(client):
    """Test case for get_activity_by_id

    Retrieve single Activity
    """
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/activities/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_activities(client):
    """Test case for get_all_activities

    Retrieve all Activities
    """
    params = [('Cursor', 'cursor_example'),
                    ('Filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_allowed_activities(client):
    """Test case for get_allowed_activities

    Retrieve allowed activities
    """
    params = [('employeeNumber', 56),
                    ('projectNumber', 56)]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/activities/allowed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_of_activities(client):
    """Test case for get_number_of_activities

    Retrieve the number of Activities
    """
    params = [('Filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/activities/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page_of_activities(client):
    """Test case for get_page_of_activities

    Retrieve a page of Activities
    """
    params = [('Filter', 'filter_example'),
                    ('Sort', 'sort_example'),
                    ('PageSize', 20),
                    ('SkipPages', 0)]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/activities/paged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_activity(client):
    """Test case for update_activity

    Update a single Activity
    """
    body = {"Description":"An awesome activity","Id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v20.0.0/activities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

