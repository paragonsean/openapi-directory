# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.organization_response import OrganizationResponse
from openapi_server.models.organizations_response import OrganizationsResponse


pytestmark = pytest.mark.asyncio

async def test_organizations_get(client):
    """Test case for organizations_get

    List of organizations
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[search]', 'filter_search_example'),
                    ('filter[name]', 'filter_name_example'),
                    ('filter[code]', 'filter_code_example'),
                    ('filter[status]', ['filter_status_example']),
                    ('filter[industries]', 'filter_industries_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_id_get(client):
    """Test case for organizations_id_get

    Organization by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/organizations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

