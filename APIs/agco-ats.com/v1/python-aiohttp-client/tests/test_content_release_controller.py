# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_content_release_version import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion
from openapi_server.models.content_submission_shared_business_entities_content_release_version import ContentSubmissionSharedBusinessEntitiesContentReleaseVersion


pytestmark = pytest.mark.asyncio

async def test_api_v2_content_releases_content_release_id_get(client):
    """Test case for api_v2_content_releases_content_release_id_get

    Get a Content Release Version by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentReleases/{content_release_id}'.format(content_release_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_release_delete_content_release_versionn(client):
    """Test case for content_release_delete_content_release_versionn

    Delete a ContentReleaseVersion
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/ContentReleases/{content_release_id}'.format(content_release_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_release_get_content_release_version(client):
    """Test case for content_release_get_content_release_version

    Get ContentReleaseVersion
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('deleted', True),
                    ('releaseID', 56),
                    ('userId', 56),
                    ('contentDefinitionID', 56),
                    ('version', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentReleases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_release_post_content_release(client):
    """Test case for content_release_post_content_release

    Create a ContentReleaseVersion
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentReleaseVersion()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentReleases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_release_put_content_definition(client):
    """Test case for content_release_put_content_definition

    Update a ContentReleaseVersion
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentReleaseVersion()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentReleases/{content_release_id}'.format(content_release_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

