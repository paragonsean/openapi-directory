# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.members_interests_members_service_search_result import MembersInterestsMembersServiceSearchResult
from openapi_server.models.members_staff_members_service_search_result import MembersStaffMembersServiceSearchResult


pytestmark = pytest.mark.asyncio

async def test_api_lords_interests_register_get(client):
    """Test case for api_lords_interests_register_get

    Returns a list of registered interests
    """
    params = [('searchTerm', 'search_term_example'),
                    ('page', 56),
                    ('includeDeleted', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/LordsInterests/Register',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_lords_interests_staff_get(client):
    """Test case for api_lords_interests_staff_get

    Returns a list of staff
    """
    params = [('searchTerm', 'search_term_example'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/LordsInterests/Staff',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

