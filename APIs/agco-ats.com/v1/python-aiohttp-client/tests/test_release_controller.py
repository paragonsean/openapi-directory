# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_release import APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease
from openapi_server.models.content_submission_shared_business_entities_release import ContentSubmissionSharedBusinessEntitiesRelease


pytestmark = pytest.mark.asyncio

async def test_release_delete_release_bundle(client):
    """Test case for release_delete_release_bundle

    Deletes the association between a release and a bundle.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Releases/{release_id}/Bundle/{bundle_id}'.format(release_id=56, bundle_id='bundle_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_release_get_releases(client):
    """Test case for release_get_releases

    Get Release
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('visible', True),
                    ('bundleID', 'bundle_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Releases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_release_post_release(client):
    """Test case for release_post_release

    Create a Release
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesRelease()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Releases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_release_post_release_bundle(client):
    """Test case for release_post_release_bundle

    Associates the release with a bundle.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Releases/{release_id}/Bundle/{bundle_id}'.format(release_id=56, bundle_id='bundle_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_release_put_content_definition(client):
    """Test case for release_put_content_definition

    Update a Release
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesRelease()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Releases/{release_id}'.format(release_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

