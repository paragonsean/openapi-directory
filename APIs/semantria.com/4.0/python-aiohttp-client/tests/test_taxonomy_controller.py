# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.taxonomy_node_response_version import TaxonomyNodeResponseVersion


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_taxonomy(client):
    """Test case for add_taxonomy

    Add taxonomy nodes
    """
    taxonomy = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/taxonomy.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=taxonomy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_taxonomy(client):
    """Test case for delete_taxonomy

    Remove taxonomy nodes
    """
    taxonomy_node_ids = ['taxonomy_node_ids_example']
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/taxonomy.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=taxonomy_node_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_taxonomy(client):
    """Test case for get_taxonomy

    Retrieve taxonomy
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/taxonomy.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_taxonomy(client):
    """Test case for update_taxonomy

    Update taxonomy nodes
    """
    taxonomy = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/taxonomy.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=taxonomy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

