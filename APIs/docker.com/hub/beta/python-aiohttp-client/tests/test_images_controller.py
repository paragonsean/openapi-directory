# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_namespace_repository_images_response import GetNamespaceRepositoryImagesResponse
from openapi_server.models.get_namespace_repository_images_summary_response import GetNamespaceRepositoryImagesSummaryResponse
from openapi_server.models.get_namespace_repository_images_tags_response import GetNamespaceRepositoryImagesTagsResponse
from openapi_server.models.post_namespaces_delete_images_request import PostNamespacesDeleteImagesRequest
from openapi_server.models.post_namespaces_delete_images_response_error import PostNamespacesDeleteImagesResponseError
from openapi_server.models.post_namespaces_delete_images_response_success import PostNamespacesDeleteImagesResponseSuccess


pytestmark = pytest.mark.asyncio

async def test_get_namespaces_repositories_images(client):
    """Test case for get_namespaces_repositories_images

    Get details of repository's images
    """
    params = [('status', 'status_example'),
                    ('currently_tagged', True),
                    ('ordering', 'ordering_example'),
                    ('active_from', 'active_from_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/namespaces/{namespace}/repositories/{repository}/images'.format(namespace='namespace_example', repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespaces_repositories_images_summary(client):
    """Test case for get_namespaces_repositories_images_summary

    Get summary of repository's images
    """
    params = [('active_from', 'active_from_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/namespaces/{namespace}/repositories/{repository}/images-summary'.format(namespace='namespace_example', repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespaces_repositories_images_tags(client):
    """Test case for get_namespaces_repositories_images_tags

    Get image's tags
    """
    params = [('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/namespaces/{namespace}/repositories/{repository}/images/{digest}/tags'.format(namespace='namespace_example', repository='repository_example', digest='digest_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_namespaces_delete_images(client):
    """Test case for post_namespaces_delete_images

    Delete images
    """
    body = {"ignore_warnings":[{"digest":"sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr","warning":"current_tag","repository":"myrepo","tags":["latest","latest"]},{"digest":"sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr","warning":"current_tag","repository":"myrepo","tags":["latest","latest"]}],"manifests":[{"digest":"sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr","repository":"myrepo"},{"digest":"sha256:1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqr","repository":"myrepo"}],"dry_run":False,"active_from":"2020-12-01T12:00:00Z"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/namespaces/{namespace}/delete-images'.format(namespace='namespace_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

