# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_id_response import BundleIdResponse
from openapi_server.models.certificates_response import CertificatesResponse
from openapi_server.models.devices_response import DevicesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.profile_create_request import ProfileCreateRequest
from openapi_server.models.profile_response import ProfileResponse
from openapi_server.models.profiles_response import ProfilesResponse


pytestmark = pytest.mark.asyncio

async def test_profiles_bundle_id_get_to_one_related(client):
    """Test case for profiles_bundle_id_get_to_one_related

    
    """
    params = [('fields[bundleIds]', ['fields_bundle_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/profiles/{id}/bundleId'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_certificates_get_to_many_related(client):
    """Test case for profiles_certificates_get_to_many_related

    
    """
    params = [('fields[certificates]', ['fields_certificates_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/profiles/{id}/certificates'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_create_instance(client):
    """Test case for profiles_create_instance

    
    """
    body = {"data":{"relationships":{"certificates":{"data":[{"id":"id","type":"certificates"},{"id":"id","type":"certificates"}]},"devices":{"data":[{"id":"id","type":"devices"},{"id":"id","type":"devices"}]},"bundleId":{"data":{"id":"id","type":"bundleIds"}}},"attributes":{"profileType":"IOS_APP_DEVELOPMENT","name":"name"},"type":"profiles"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/profiles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_delete_instance(client):
    """Test case for profiles_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/profiles/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_devices_get_to_many_related(client):
    """Test case for profiles_devices_get_to_many_related

    
    """
    params = [('fields[devices]', ['fields_devices_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/profiles/{id}/devices'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_get_collection(client):
    """Test case for profiles_get_collection

    
    """
    params = [('filter[name]', ['filter_name_example']),
                    ('filter[profileState]', ['filter_profile_state_example']),
                    ('filter[profileType]', ['filter_profile_type_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('sort', ['sort_example']),
                    ('fields[profiles]', ['fields_profiles_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[certificates]', ['fields_certificates_example']),
                    ('fields[devices]', ['fields_devices_example']),
                    ('fields[bundleIds]', ['fields_bundle_ids_example']),
                    ('limit[certificates]', 56),
                    ('limit[devices]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_profiles_get_instance(client):
    """Test case for profiles_get_instance

    
    """
    params = [('fields[profiles]', ['fields_profiles_example']),
                    ('include', ['include_example']),
                    ('fields[certificates]', ['fields_certificates_example']),
                    ('fields[devices]', ['fields_devices_example']),
                    ('fields[bundleIds]', ['fields_bundle_ids_example']),
                    ('limit[certificates]', 56),
                    ('limit[devices]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

