# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.organization import Organization


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_organizations_get(client):
    """Test case for workspace_slug_organizations_get

    List organizations in a workspace
    """
    params = [('query', 'query_example'),
                    ('page', 'page_example'),
                    ('direction', 'direction_example'),
                    ('items', 'items_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/organizations'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_organizations_organization_id_get(client):
    """Test case for workspace_slug_organizations_organization_id_get

    Get an organization
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/organizations/{organization_id}'.format(workspace_slug='workspace_slug_example', organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_organizations_organization_id_put(client):
    """Test case for workspace_slug_organizations_organization_id_put

    Update an organization
    """
    body = openapi_server.Organization()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/{workspace_slug}/organizations/{organization_id}'.format(workspace_slug='workspace_slug_example', organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

