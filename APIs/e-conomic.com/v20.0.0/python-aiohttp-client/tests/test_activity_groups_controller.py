# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_group import ActivityGroup
from openapi_server.models.activity_group_cursor_results import ActivityGroupCursorResults
from openapi_server.models.created_result import CreatedResult
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_activity_group(client):
    """Test case for create_activity_group

    Create a single Activity Group
    """
    body = {"Description":"An awesome activity group","Id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v20.0.0/activitygroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_activity_group_by_id(client):
    """Test case for get_activity_group_by_id

    Retrieve single Activity Group
    """
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/activitygroups/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_activity_groups(client):
    """Test case for get_all_activity_groups

    Retrieve all Activity Groups
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
        path='/api/v20.0.0/activitygroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_of_activity_groups(client):
    """Test case for get_number_of_activity_groups

    Retrieve the number of Activity Groups
    """
    params = [('Filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/activitygroups/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page_of_activity_groups(client):
    """Test case for get_page_of_activity_groups

    Retrieve a page of Activity Groups
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
        path='/api/v20.0.0/activitygroups/paged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

