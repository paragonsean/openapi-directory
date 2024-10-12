# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_health_profile_response import FetchHealthProfileResponse
from openapi_server.models.fetch_health_profiles_response import FetchHealthProfilesResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_health_profile(client):
    """Test case for fetch_health_profile

    Get a health profile
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_profile/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_health_profiles(client):
    """Test case for fetch_health_profiles

    List health profiles
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example'),
                    ('page[number]', 1),
                    ('page[size]', 10),
                    ('page[limit]', 50),
                    ('page[cursor]', 'page_cursor_example'),
                    ('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/health_profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

