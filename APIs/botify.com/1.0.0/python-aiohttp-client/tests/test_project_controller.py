# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_payload import DefaultPayload
from openapi_server.models.get_project_analyses200_response import GetProjectAnalyses200Response
from openapi_server.models.get_saved_filters200_response import GetSavedFilters200Response
from openapi_server.models.project_saved_filter import ProjectSavedFilter
from openapi_server.models.url_rewriting_rules_serializer import URLRewritingRulesSerializer
from openapi_server.models.urls_aggs_query import UrlsAggsQuery


pytestmark = pytest.mark.asyncio

async def test_get_project_analyses(client):
    """Test case for get_project_analyses

    List all analyses for a project
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}'.format(username='username_example', project_slug='project_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_urls_aggs(client):
    """Test case for get_project_urls_aggs

    Project Query aggregator
    """
    body = {"filters":"{}","aggs":["{}","{}"]}
    params = [('area', current),
                    ('last_analysis_slug', 'last_analysis_slug_example'),
                    ('nb_analyses', 20)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{username}/{project_slug}/urls/aggs'.format(username='username_example', project_slug='project_slug_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_saved_filter(client):
    """Test case for get_saved_filter

    Retrieves a specific saved filter's name, ID and filter value
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{username}/{project_slug}/filters/{identifier}'.format(username='username_example', project_slug='project_slug_example', identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_saved_filters(client):
    """Test case for get_saved_filters

    List all the project's saved filters (each filter's name, ID and filter value)
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/projects/{username}/{project_slug}/filters'.format(username='username_example', project_slug='project_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_url_rewriting_rules(client):
    """Test case for test_url_rewriting_rules

    Match and replace parts of a URL based on rules passed in POST data
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/projects/{username}/{project_slug}/features/url_rewriting/rules_validator'.format(username='username_example', project_slug='project_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

