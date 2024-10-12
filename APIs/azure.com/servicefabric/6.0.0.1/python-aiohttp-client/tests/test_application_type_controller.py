# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_type_image_store_path import ApplicationTypeImageStorePath
from openapi_server.models.application_type_image_store_version import ApplicationTypeImageStoreVersion
from openapi_server.models.application_type_manifest import ApplicationTypeManifest
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_application_type_info_list import PagedApplicationTypeInfoList


pytestmark = pytest.mark.asyncio

async def test_get_application_manifest(client):
    """Test case for get_application_manifest

    Gets the manifest describing an application type.
    """
    params = [('api-version', 6.0),
                    ('ApplicationTypeVersion', 'application_type_version_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}/$/GetApplicationManifest'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_type_info_list(client):
    """Test case for get_application_type_info_list

    Gets the list of application types in the Service Fabric cluster.
    """
    params = [('api-version', 6.0),
                    ('ApplicationTypeDefinitionKindFilter', 0),
                    ('ExcludeApplicationParameters', False),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_type_info_list_by_name(client):
    """Test case for get_application_type_info_list_by_name

    Gets the list of application types in the Service Fabric cluster matching exactly the specified name.
    """
    params = [('api-version', 6.0),
                    ('ApplicationTypeVersion', 'application_type_version_example'),
                    ('ExcludeApplicationParameters', False),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ApplicationTypes/{application_type_name}'.format(application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_provision_application_type(client):
    """Test case for provision_application_type

    Provisions or registers a Service Fabric application type with the cluster.
    """
    application_type_image_store_path = openapi_server.ApplicationTypeImageStorePath()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ApplicationTypes/$/Provision',
        headers=headers,
        json=application_type_image_store_path,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_unprovision_application_type(client):
    """Test case for unprovision_application_type

    Removes or unregisters a Service Fabric application type from the cluster.
    """
    application_type_image_store_version = openapi_server.ApplicationTypeImageStoreVersion()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ApplicationTypes/{application_type_name}/$/Unprovision'.format(application_type_name='application_type_name_example'),
        headers=headers,
        json=application_type_image_store_version,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

