# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filter import Filter
from openapi_server.models.source_tag_filter import SourceTagFilter
from openapi_server.models.tag_path_tag import TagPathTag


pytestmark = pytest.mark.asyncio

async def test_filtering_associations_get(client):
    """Test case for filtering_associations_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/filtering/associations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filtering_associations_id_delete(client):
    """Test case for filtering_associations_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/filtering/associations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_filtering_associations_post(client):
    """Test case for filtering_associations_post

    
    """
    sourcetagfilter = openapi_server.SourceTagFilter()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/filtering/associations',
        headers=headers,
        json=sourcetagfilter,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filtering_filters_get(client):
    """Test case for filtering_filters_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/filtering/filters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filtering_filters_id_delete(client):
    """Test case for filtering_filters_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/filtering/filters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filtering_filters_id_tagpaths_get(client):
    """Test case for filtering_filters_id_tagpaths_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/filtering/filters/{id}/tagpaths'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_filtering_filters_id_tagpaths_post(client):
    """Test case for filtering_filters_id_tagpaths_post

    
    """
    tagpath = openapi_server.TagPathTag()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/filtering/filters/{id}/tagpaths'.format(id=56),
        headers=headers,
        json=tagpath,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filtering_filters_id_tagpaths_tagpathid_delete(client):
    """Test case for filtering_filters_id_tagpaths_tagpathid_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/filtering/filters/{id}/tagpaths/{tagpathid}'.format(id=56, tagpathid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_filtering_filters_post(client):
    """Test case for filtering_filters_post

    
    """
    tag_filter = openapi_server.Filter()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/filtering/filters',
        headers=headers,
        json=tag_filter,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

