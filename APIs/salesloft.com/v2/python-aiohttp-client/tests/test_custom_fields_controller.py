# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field import CustomField


pytestmark = pytest.mark.asyncio

async def test_v2_custom_fields_id_json_delete(client):
    """Test case for v2_custom_fields_id_json_delete

    Delete a custom field
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/custom_fields/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_custom_fields_id_json_get(client):
    """Test case for v2_custom_fields_id_json_get

    Fetch a custom field
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/custom_fields/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_custom_fields_id_json_put(client):
    """Test case for v2_custom_fields_id_json_put

    Update a custom field
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'field_type': 'field_type_example',
        'name': 'name_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/custom_fields/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_custom_fields_json_get(client):
    """Test case for v2_custom_fields_json_get

    List custom fields
    """
    params = [('ids', [56]),
                    ('field_type', 'field_type_example'),
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
        path='/v2/custom_fields.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_custom_fields_json_post(client):
    """Test case for v2_custom_fields_json_post

    Create a custom field
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'field_type': 'field_type_example',
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/custom_fields.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

