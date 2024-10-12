# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server.models.page_of_variant_sets import PageOfVariantSets
from openapi_server.models.variant_set import VariantSet


pytestmark = pytest.mark.asyncio

async def test_delete_variant_set_item(client):
    """Test case for delete_variant_set_item

    Deletes variant set
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/variation/set/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_analyze(client):
    """Test case for get_variant_analyze

    Returns list of matches
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/variation/set/analyze/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_set_item(client):
    """Test case for get_variant_set_item

    Returns a variant set
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/variation/set/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_sets_archive_collection(client):
    """Test case for get_variant_sets_archive_collection

    Returns list of variant sets from a specified time period
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/variation/set/archive/{year}/{month}/{day}'.format(year=56, month=56, day=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variant_sets_collection(client):
    """Test case for get_variant_sets_collection

    Returns list of variant sets
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/variation/set/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_variant_sets_collection(client):
    """Test case for post_variant_sets_collection

    Creates a new variant set
    """
    body = openapi_server.VariantSet()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/variation/set/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_variant_set_item(client):
    """Test case for put_variant_set_item

    Updates a variant set
    """
    body = openapi_server.VariantSet()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/variation/set/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

