# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.pre_release_versions_response import PreReleaseVersionsResponse
from openapi_server.models.prerelease_version_response import PrereleaseVersionResponse


pytestmark = pytest.mark.asyncio

async def test_pre_release_versions_app_get_to_one_related(client):
    """Test case for pre_release_versions_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/preReleaseVersions/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pre_release_versions_builds_get_to_many_related(client):
    """Test case for pre_release_versions_builds_get_to_many_related

    
    """
    params = [('fields[builds]', ['fields_builds_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/preReleaseVersions/{id}/builds'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pre_release_versions_get_collection(client):
    """Test case for pre_release_versions_get_collection

    
    """
    params = [('filter[builds.expired]', ['filter_builds_expired_example']),
                    ('filter[builds.processingState]', ['filter_builds_processing_state_example']),
                    ('filter[platform]', ['filter_platform_example']),
                    ('filter[version]', ['filter_version_example']),
                    ('filter[app]', ['filter_app_example']),
                    ('filter[builds]', ['filter_builds_example']),
                    ('sort', ['sort_example']),
                    ('fields[preReleaseVersions]', ['fields_pre_release_versions_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[builds]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/preReleaseVersions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pre_release_versions_get_instance(client):
    """Test case for pre_release_versions_get_instance

    
    """
    params = [('fields[preReleaseVersions]', ['fields_pre_release_versions_example']),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[builds]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/preReleaseVersions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

