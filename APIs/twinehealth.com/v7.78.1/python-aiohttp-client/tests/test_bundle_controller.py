# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_bundle_request import CreateBundleRequest
from openapi_server.models.create_bundle_response import CreateBundleResponse
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_bundle_response import FetchBundleResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.update_bundle_request import UpdateBundleRequest
from openapi_server.models.update_bundle_response import UpdateBundleResponse


pytestmark = pytest.mark.asyncio

async def test_create_bundle(client):
    """Test case for create_bundle

    Create bundle
    """
    body = openapi_server.CreateBundleRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/bundle',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_bundle(client):
    """Test case for fetch_bundle

    Get a bundle
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/bundle/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_bundle(client):
    """Test case for update_bundle

    Update a bundle
    """
    body = openapi_server.UpdateBundleRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='PATCH',
        path='/pub/bundle/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

