# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact_search_results import ArtifactSearchResults
from openapi_server.models.error import Error
from openapi_server.models.version_search_results import VersionSearchResults


pytestmark = pytest.mark.asyncio

async def test_search_artifacts(client):
    """Test case for search_artifacts

    Search for artifacts
    """
    params = [('search', 'search_example'),
                    ('offset', 0),
                    ('limit', 20),
                    ('over', 'over_example'),
                    ('order', 'order_example')]
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

async def test_search_versions(client):
    """Test case for search_versions

    Search artifact versions
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/search/artifacts/{artifact_id}/versions'.format(artifact_id='artifact_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

