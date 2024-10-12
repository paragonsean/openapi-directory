# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.form_field_set_entity import FormFieldSetEntity
from openapi_server.models.patch_form_field_sets import PatchFormFieldSets
from openapi_server.models.post_form_field_sets import PostFormFieldSets


pytestmark = pytest.mark.asyncio

async def test_delete_form_field_sets_id(client):
    """Test case for delete_form_field_sets_id

    Delete Form Field Set
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/form_field_sets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_form_field_sets(client):
    """Test case for get_form_field_sets

    List Form Field Sets
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/form_field_sets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_form_field_sets_id(client):
    """Test case for get_form_field_sets_id

    Show Form Field Set
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/form_field_sets/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_patch_form_field_sets_id(client):
    """Test case for patch_form_field_sets_id

    Update Form Field Set
    """
    body = openapi_server.PatchFormFieldSets()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/form_field_sets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_form_field_sets(client):
    """Test case for post_form_field_sets

    Create Form Field Set
    """
    body = openapi_server.PostFormFieldSets()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/form_field_sets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

