# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_and_identity import ActivityAndIdentity
from openapi_server.models.custom_or_post_activity import CustomOrPostActivity


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_activities_get(client):
    """Test case for workspace_slug_activities_get

    List activities for a workspace
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
                    ('page', 'page_example'),
                    ('direction', 'direction_example'),
                    ('items', 'items_example'),
                    ('sort', 'sort_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/activities'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_activities_id_get(client):
    """Test case for workspace_slug_activities_id_get

    Get an activity in the workspace
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/activities/{id}'.format(workspace_slug='workspace_slug_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_activities_post(client):
    """Test case for workspace_slug_activities_post

    Create a Custom or a Content activity for a new or existing member
    """
    body = openapi_server.ActivityAndIdentity()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{workspace_slug}/activities'.format(workspace_slug='workspace_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_activities_get(client):
    """Test case for workspace_slug_members_member_slug_activities_get

    List activities for a member
    """
    params = [('page', 'page_example'),
                    ('direction', 'direction_example'),
                    ('items', 'items_example'),
                    ('sort', 'sort_example'),
                    ('activity_type', 'activity_type_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/members/{member_slug}/activities'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_activities_id_delete(client):
    """Test case for workspace_slug_members_member_slug_activities_id_delete

    Delete a post activity
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/{workspace_slug}/members/{member_slug}/activities/{id}'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_activities_id_put(client):
    """Test case for workspace_slug_members_member_slug_activities_id_put

    Update a custom activity for a member
    """
    body = openapi_server.Activity()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/{workspace_slug}/members/{member_slug}/activities/{id}'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_members_member_slug_activities_post(client):
    """Test case for workspace_slug_members_member_slug_activities_post

    Create a Custom or a Content activity for a member
    """
    body = openapi_server.CustomOrPostActivity()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/{workspace_slug}/members/{member_slug}/activities'.format(workspace_slug='workspace_slug_example', member_slug='member_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_slug_organizations_organization_id_activities_get(client):
    """Test case for workspace_slug_organizations_organization_id_activities_get

    List member activities in an organization
    """
    params = [('page', 'page_example'),
                    ('direction', 'direction_example'),
                    ('items', 'items_example'),
                    ('sort', 'sort_example'),
                    ('activity_type', 'activity_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{workspace_slug}/organizations/{organization_id}/activities'.format(workspace_slug='workspace_slug_example', organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

