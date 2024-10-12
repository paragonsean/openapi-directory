# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.paginated_tags import PaginatedTags
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_v2_namespaces_namespace_repositories_repository_tags_get(client):
    """Test case for v2_namespaces_namespace_repositories_repository_tags_get

    List repository tags
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/namespaces/{namespace}/repositories/{repository}/tags'.format(namespace='namespace_example', repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_namespaces_namespace_repositories_repository_tags_head(client):
    """Test case for v2_namespaces_namespace_repositories_repository_tags_head

    Check repository tags
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/v2/namespaces/{namespace}/repositories/{repository}/tags'.format(namespace='namespace_example', repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_namespaces_namespace_repositories_repository_tags_tag_get(client):
    """Test case for v2_namespaces_namespace_repositories_repository_tags_tag_get

    Read repository tag
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/namespaces/{namespace}/repositories/{repository}/tags/{tag}'.format(namespace='namespace_example', repository='repository_example', tag='tag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_namespaces_namespace_repositories_repository_tags_tag_head(client):
    """Test case for v2_namespaces_namespace_repositories_repository_tags_tag_head

    Check repository tag
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/v2/namespaces/{namespace}/repositories/{repository}/tags/{tag}'.format(namespace='namespace_example', repository='repository_example', tag='tag_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

