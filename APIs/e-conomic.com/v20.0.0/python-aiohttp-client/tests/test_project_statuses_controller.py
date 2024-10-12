# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.project_status import ProjectStatus
from openapi_server.models.project_status_cursor_results import ProjectStatusCursorResults


pytestmark = pytest.mark.asyncio

async def test_get_all_project_statuses(client):
    """Test case for get_all_project_statuses

    Retrieve all Project Statuses
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
        path='/api/v20.0.0/projectstatuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_of_project_statuses(client):
    """Test case for get_number_of_project_statuses

    Retrieve the number of Project Statuses
    """
    params = [('Filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/projectstatuses/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page_of_project_statuses(client):
    """Test case for get_page_of_project_statuses

    Retrieve a page of Project Statuses
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
        path='/api/v20.0.0/projectstatuses/paged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_status_by_id(client):
    """Test case for get_project_status_by_id

    Retrieve single Project Status
    """
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/projectstatuses/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

