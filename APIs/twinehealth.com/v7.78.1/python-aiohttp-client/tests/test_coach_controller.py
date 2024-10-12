# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_coach_response import FetchCoachResponse
from openapi_server.models.fetch_coaches_response import FetchCoachesResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_coach(client):
    """Test case for fetch_coach

    Get a coach
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/coach/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_coaches(client):
    """Test case for fetch_coaches

    List coaches
    """
    params = [('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/coach',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

