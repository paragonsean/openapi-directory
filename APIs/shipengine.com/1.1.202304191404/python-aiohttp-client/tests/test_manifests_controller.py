# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_manifest_request_body import CreateManifestRequestBody
from openapi_server.models.create_manifest_response_body import CreateManifestResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_manifest_by_id_response_body import GetManifestByIdResponseBody
from openapi_server.models.list_manifests_response_body import ListManifestsResponseBody


pytestmark = pytest.mark.asyncio

async def test_create_manifest(client):
    """Test case for create_manifest

    Create Manifest
    """
    body = openapi_server.CreateManifestRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/manifests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_manifest_by_id(client):
    """Test case for get_manifest_by_id

    Get Manifest By Id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/manifests/{manifest_id}'.format(manifest_id='manifest_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_manifest_request_by_id(client):
    """Test case for get_manifest_request_by_id

    Get Manifest Request By Id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/manifests/requests/{manifest_request_id}'.format(manifest_request_id='manifest_request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_manifests(client):
    """Test case for list_manifests

    List Manifests
    """
    params = [('warehouse_id', 'warehouse_id_example'),
                    ('ship_date_start', '2018-09-23T15:00:00.000Z'),
                    ('ship_date_end', '2018-09-23T15:00:00.000Z'),
                    ('created_at_start', '2019-03-12T19:24:13.657Z'),
                    ('created_at_end', '2019-03-12T19:24:13.657Z'),
                    ('carrier_id', 'carrier_id_example'),
                    ('page', 1),
                    ('page_size', 25),
                    ('label_ids', ['label_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/manifests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

