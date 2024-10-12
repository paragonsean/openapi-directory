# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_preview_set_app_previews_linkages_request import AppPreviewSetAppPreviewsLinkagesRequest
from openapi_server.models.app_preview_set_app_previews_linkages_response import AppPreviewSetAppPreviewsLinkagesResponse
from openapi_server.models.app_preview_set_create_request import AppPreviewSetCreateRequest
from openapi_server.models.app_preview_set_response import AppPreviewSetResponse
from openapi_server.models.app_previews_response import AppPreviewsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_preview_sets_app_previews_get_to_many_related(client):
    """Test case for app_preview_sets_app_previews_get_to_many_related

    
    """
    params = [('fields[appPreviews]', ['fields_app_previews_example']),
                    ('fields[appPreviewSets]', ['fields_app_preview_sets_example']),
                    ('limit', 56),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPreviewSets/{id}/appPreviews'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_preview_sets_app_previews_get_to_many_relationship(client):
    """Test case for app_preview_sets_app_previews_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPreviewSets/{id}/relationships/appPreviews'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_preview_sets_app_previews_replace_to_many_relationship(client):
    """Test case for app_preview_sets_app_previews_replace_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"appPreviews"},{"id":"id","type":"appPreviews"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/appPreviewSets/{id}/relationships/appPreviews'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_preview_sets_create_instance(client):
    """Test case for app_preview_sets_create_instance

    
    """
    body = {"data":{"relationships":{"appStoreVersionLocalization":{"data":{"id":"id","type":"appStoreVersionLocalizations"}}},"attributes":{"previewType":"IPHONE_65"},"type":"appPreviewSets"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/appPreviewSets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_preview_sets_delete_instance(client):
    """Test case for app_preview_sets_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/appPreviewSets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_preview_sets_get_instance(client):
    """Test case for app_preview_sets_get_instance

    
    """
    params = [('fields[appPreviewSets]', ['fields_app_preview_sets_example']),
                    ('include', ['include_example']),
                    ('fields[appPreviews]', ['fields_app_previews_example']),
                    ('limit[appPreviews]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPreviewSets/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

