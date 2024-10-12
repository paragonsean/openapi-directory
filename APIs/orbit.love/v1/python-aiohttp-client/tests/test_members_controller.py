# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.identity import Identity
from openapi_server.models.member import Member
from openapi_server.models.member_and_identity import MemberAndIdentity


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_find_get(client):
    """Test case for workspace_slug_members_find_get

    Find a member by an identity
    """
    params = [('source', 'source_example'),
                    ('source_host', 'source_host_example'),
                    ('uid', 'uid_example'),
                    ('username', 'username_example'),
                    ('email', 'email_example'),
                    ('github', 'github_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/members/find'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_get(client):
    """Test case for workspace_slug_members_get

    List members in a workspace
    """
    params = [('affiliation', 'affiliation_example'),
                    ('member_tags', 'member_tags_example'),
                    ('orbit', 'orbit_example'),
                    ('activity_type', 'activity_type_example'),
                    ('identity', 'identity_example'),
                    ('company[]', 'company_example'),
                    ('title[]', 'title_example'),
                    ('regions[]', 'regions_example'),
                    ('countries[]', 'countries_example'),
                    ('cities[]', 'cities_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('relative', 'relative_example'),
                    ('query', 'query_example'),
                    ('page', 'page_example'),
                    ('direction', 'direction_example'),
                    ('items', 'items_example'),
                    ('activities_count_min', 'activities_count_min_example'),
                    ('activities_count_max', 'activities_count_max_example'),
                    ('sort', 'sort_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/members'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_delete(client):
    """Test case for workspace_slug_members_member_slug_delete

    Delete a member
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/{workspace_slug}/members/{member_slug}'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_get(client):
    """Test case for workspace_slug_members_member_slug_get

    Get a member
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/members/{member_slug}'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_identities_delete(client):
    """Test case for workspace_slug_members_member_slug_identities_delete

    Remove identity from a member
    """
    body = openapi_server.Identity()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/{workspace_slug}/members/{member_slug}/identities'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_identities_post(client):
    """Test case for workspace_slug_members_member_slug_identities_post

    Add identity to a member
    """
    body = openapi_server.Identity()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{workspace_slug}/members/{member_slug}/identities'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_put(client):
    """Test case for workspace_slug_members_member_slug_put

    Update a member
    """
    body = openapi_server.Member()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/{workspace_slug}/members/{member_slug}'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_post(client):
    """Test case for workspace_slug_members_post

    Create or update a member
    """
    body = openapi_server.MemberAndIdentity()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{workspace_slug}/members'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_organizations_organization_id_members_get(client):
    """Test case for workspace_slug_organizations_organization_id_members_get

    List members in an organization
    """
    params = [('page', 'page_example'),
                    ('items', 'items_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/organizations/{organization_id}/members'.format(workspace_slug='workspace_slug_example', organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

