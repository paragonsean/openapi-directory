# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_type_manifest import ApplicationTypeManifest
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_application_type_info_list import PagedApplicationTypeInfoList
from openapi_server.models.provision_application_type_description_base import ProvisionApplicationTypeDescriptionBase
from openapi_server.models.unprovision_application_type_description_info import UnprovisionApplicationTypeDescriptionInfo


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

    Provisions or registers a Service Fabric application type with the cluster using the .sfpkg package in the external store or using the application package in the image store.
    """
    provision_application_type_description_base_required_body_param = openapi_server.ProvisionApplicationTypeDescriptionBase()
    params = [('api-version', 6.1),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ApplicationTypes/$/Provision',
        headers=headers,
        json=provision_application_type_description_base_required_body_param,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_unprovision_application_type(client):
    """Test case for unprovision_application_type

    Removes or unregisters a Service Fabric application type from the cluster.
    """
    unprovision_application_type_description_info = openapi_server.UnprovisionApplicationTypeDescriptionInfo()
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
        json=unprovision_application_type_description_info,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

