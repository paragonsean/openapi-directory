# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_search_results import ArtifactSearchResults
from openapi_server.models.error import Error
from openapi_server.models.sort_by import SortBy
from openapi_server.models.sort_order import SortOrder


pytestmark = pytest.mark.asyncio

async def test_search_artifacts(client):
    """Test case for search_artifacts

    Search for artifacts
    """
    params = [('name', 'name_example'),
                    ('offset', 0),
                    ('limit', 20),
                    ('order', openapi_server.SortOrder()),
                    ('orderby', openapi_server.SortBy()),
                    ('labels', ['labels_example']),
                    ('properties', ['properties_example']),
                    ('description', 'description_example'),
                    ('group', 'group_example'),
                    ('globalId', 56),
                    ('contentId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/artifacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_search_artifacts_by_content(client):
    """Test case for search_artifacts_by_content

    Search for artifacts by content
    """
    body = '/path/to/file'
    params = [('canonical', True),
                    ('artifactType', 'artifact_type_example'),
                    ('offset', 0),
                    ('limit', 20),
                    ('order', 'order_example'),
                    ('orderby', 'orderby_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/search/artifacts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

