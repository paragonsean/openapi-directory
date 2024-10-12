# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tag import Tag
from openapi_server.models.tag_set import TagSet
from openapi_server.models.tag_set_submission import TagSetSubmission
from openapi_server.models.tag_submission import TagSubmission


pytestmark = pytest.mark.asyncio

async def test_tags_get(client):
    """Test case for tags_get

    List tags
    """
    params = [('ownedBy', 'owned_by_example'),
                    ('tagSet', 'tag_set_example'),
                    ('urlWords', 'url_words_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_id_get(client):
    """Test case for tags_id_get

    Retrieve a single tag by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/tags/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_post(client):
    """Test case for tags_post

    Create a new tag
    """
    body = {"tagSet":{"name":"name","id":"id"},"colour":"colour","urlWords":"urlWords","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/tags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagsets_get(client):
    """Test case for tagsets_get

    List tag sets
    """
    params = [('ownedBy', 'owned_by_example'),
                    ('urlWords', 'url_words_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/tagsets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagsets_id_get(client):
    """Test case for tagsets_id_get

    Retrieve a single tag set by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/tagsets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagsets_post(client):
    """Test case for tagsets_post

    Create a new tag set
    """
    body = {"urlWords":"urlWords","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/1/tagsets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

