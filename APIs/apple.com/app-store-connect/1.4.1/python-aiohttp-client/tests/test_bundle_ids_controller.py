# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.bundle_id_capabilities_response import BundleIdCapabilitiesResponse
from openapi_server.models.bundle_id_create_request import BundleIdCreateRequest
from openapi_server.models.bundle_id_response import BundleIdResponse
from openapi_server.models.bundle_id_update_request import BundleIdUpdateRequest
from openapi_server.models.bundle_ids_response import BundleIdsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.profiles_response import ProfilesResponse


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_app_get_to_one_related(client):
    """Test case for bundle_ids_app_get_to_one_related

    
    """
    params = [('fields[apps]', ['fields_apps_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/bundleIds/{id}/app'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_bundle_id_capabilities_get_to_many_related(client):
    """Test case for bundle_ids_bundle_id_capabilities_get_to_many_related

    
    """
    params = [('fields[bundleIdCapabilities]', ['fields_bundle_id_capabilities_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/bundleIds/{id}/bundleIdCapabilities'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_create_instance(client):
    """Test case for bundle_ids_create_instance

    
    """
    body = {"data":{"attributes":{"identifier":"identifier","seedId":"seedId","name":"name","platform":"IOS"},"type":"bundleIds"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/bundleIds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_delete_instance(client):
    """Test case for bundle_ids_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/bundleIds/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_get_collection(client):
    """Test case for bundle_ids_get_collection

    
    """
    params = [('filter[identifier]', ['filter_identifier_example']),
                    ('filter[name]', ['filter_name_example']),
                    ('filter[platform]', ['filter_platform_example']),
                    ('filter[seedId]', ['filter_seed_id_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[bundleIds]', ['fields_bundle_ids_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[bundleIdCapabilities]', ['fields_bundle_id_capabilities_example']),
                    ('fields[profiles]', ['fields_profiles_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[bundleIdCapabilities]', 56),
                    ('limit[profiles]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/bundleIds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_get_instance(client):
    """Test case for bundle_ids_get_instance

    
    """
    params = [('fields[bundleIds]', ['fields_bundle_ids_example']),
                    ('include', ['include_example']),
                    ('fields[bundleIdCapabilities]', ['fields_bundle_id_capabilities_example']),
                    ('fields[profiles]', ['fields_profiles_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[bundleIdCapabilities]', 56),
                    ('limit[profiles]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/bundleIds/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_profiles_get_to_many_related(client):
    """Test case for bundle_ids_profiles_get_to_many_related

    
    """
    params = [('fields[profiles]', ['fields_profiles_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/bundleIds/{id}/profiles'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bundle_ids_update_instance(client):
    """Test case for bundle_ids_update_instance

    
    """
    body = {"data":{"attributes":{"name":"name"},"id":"id","type":"bundleIds"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/bundleIds/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

