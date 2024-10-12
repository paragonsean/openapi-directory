# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cadence_membership import CadenceMembership


pytestmark = pytest.mark.asyncio

async def test_v2_cadence_memberships_id_json_delete(client):
    """Test case for v2_cadence_memberships_id_json_delete

    Delete a cadence membership
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/cadence_memberships/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_cadence_memberships_id_json_get(client):
    """Test case for v2_cadence_memberships_id_json_get

    Fetch a cadence membership
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/cadence_memberships/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_cadence_memberships_json_get(client):
    """Test case for v2_cadence_memberships_json_get

    List cadence memberships
    """
    params = [('ids', [56]),
                    ('person_id', 56),
                    ('cadence_id', 56),
                    ('updated_at', ['updated_at_example']),
                    ('currently_on_cadence', True),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/cadence_memberships.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_cadence_memberships_json_post(client):
    """Test case for v2_cadence_memberships_json_post

    Create a cadence membership
    """
    params = [('person_id', 56),
                    ('cadence_id', 56),
                    ('user_id', 56),
                    ('step_id', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/v2/cadence_memberships.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

