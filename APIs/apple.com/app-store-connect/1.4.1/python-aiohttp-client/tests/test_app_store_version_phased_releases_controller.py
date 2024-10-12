# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_store_version_phased_release_create_request import AppStoreVersionPhasedReleaseCreateRequest
from openapi_server.models.app_store_version_phased_release_response import AppStoreVersionPhasedReleaseResponse
from openapi_server.models.app_store_version_phased_release_update_request import AppStoreVersionPhasedReleaseUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_store_version_phased_releases_create_instance(client):
    """Test case for app_store_version_phased_releases_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersion":{"data":{"id":"id","type":"appStoreVersions"}}},"attributes":{"phasedReleaseState":"INACTIVE"},"type":"appStoreVersionPhasedReleases"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appStoreVersionPhasedReleases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_phased_releases_delete_instance(client):
    """Test case for app_store_version_phased_releases_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appStoreVersionPhasedReleases/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_store_version_phased_releases_update_instance(client):
    """Test case for app_store_version_phased_releases_update_instance

    
    """
    body = {"data":{"attributes":{"phasedReleaseState":"INACTIVE"},"id":"id","type":"appStoreVersionPhasedReleases"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appStoreVersionPhasedReleases/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

