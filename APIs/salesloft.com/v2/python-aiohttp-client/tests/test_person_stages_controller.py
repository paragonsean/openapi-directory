# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.person_stage import PersonStage


pytestmark = pytest.mark.asyncio

async def test_v2_person_stages_id_json_delete(client):
    """Test case for v2_person_stages_id_json_delete

    Delete an person stage
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/person_stages/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_person_stages_id_json_get(client):
    """Test case for v2_person_stages_id_json_get

    Fetch a person stage
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/person_stages/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_person_stages_id_json_put(client):
    """Test case for v2_person_stages_id_json_put

    Update a person stage
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'name': 'name_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/person_stages/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_person_stages_json_get(client):
    """Test case for v2_person_stages_json_get

    List person stages
    """
    params = [('ids', [56]),
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
        path='/v2/person_stages.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_person_stages_json_post(client):
    """Test case for v2_person_stages_json_post

    Create a person stage
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/person_stages.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

