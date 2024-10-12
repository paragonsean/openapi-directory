# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_annotation_result import EntityAnnotationResult


pytestmark = pytest.mark.asyncio

async def test_get_annotate(client):
    """Test case for get_annotate

    Annotate a given text using SciGraph annotator
    """
    params = [('content', 'content_example'),
                    ('include_category', ['include_category_example']),
                    ('exclude_category', ['exclude_category_example']),
                    ('min_length', '4'),
                    ('longest_only', False),
                    ('include_abbreviation', False),
                    ('include_acronym', False),
                    ('include_numbers', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/nlp/annotate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_annotate_entities(client):
    """Test case for get_annotate_entities

    Annotate a given content using SciGraph annotator and get all entities from content
    """
    params = [('content', 'content_example'),
                    ('include_category', ['include_category_example']),
                    ('exclude_category', ['exclude_category_example']),
                    ('min_length', '4'),
                    ('longest_only', False),
                    ('include_abbreviation', False),
                    ('include_acronym', False),
                    ('include_numbers', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/nlp/annotate/entities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_annotate(client):
    """Test case for post_annotate

    Annotate a given text using SciGraph annotator
    """
    params = [('content', 'content_example'),
                    ('include_category', ['include_category_example']),
                    ('exclude_category', ['exclude_category_example']),
                    ('min_length', '4'),
                    ('longest_only', False),
                    ('include_abbreviation', False),
                    ('include_acronym', False),
                    ('include_numbers', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/nlp/annotate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_annotate_entities(client):
    """Test case for post_annotate_entities

    Annotate a given content using SciGraph annotator and get all entities from content
    """
    params = [('content', 'content_example'),
                    ('include_category', ['include_category_example']),
                    ('exclude_category', ['exclude_category_example']),
                    ('min_length', '4'),
                    ('longest_only', False),
                    ('include_abbreviation', False),
                    ('include_acronym', False),
                    ('include_numbers', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/nlp/annotate/entities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

