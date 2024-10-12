# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_resource_description import ApplicationResourceDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_service_resource_description_list import PagedServiceResourceDescriptionList
from openapi_server.models.paged_service_resource_replica_description_list import PagedServiceResourceReplicaDescriptionList
from openapi_server.models.service_resource_description import ServiceResourceDescription
from openapi_server.models.service_resource_replica_description import ServiceResourceReplicaDescription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_application_resource(client):
    """Test case for create_application_resource

    Creates or updates an application resource.
    """
    application_resource_description = openapi_server.ApplicationResourceDescription()
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Resources/Applications/{application_resource_name}'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        json=application_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_application_resource(client):
    """Test case for delete_application_resource

    Deletes the specified application.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Resources/Applications/{application_resource_name}'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_resource(client):
    """Test case for get_application_resource

    Gets the application with the given name.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replica(client):
    """Test case for get_replica

    Gets a specific replica of a given service in an application resource.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services/{service_resource_name}/Replicas/{replica_name}'.format(application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example', replica_name='replica_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replicas(client):
    """Test case for get_replicas

    Gets replicas of a given service in an application resource.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services/{service_resource_name}/replicas'.format(application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service(client):
    """Test case for get_service

    Gets the description of the specified service in an application resource.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services/{service_resource_name}'.format(application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services(client):
    """Test case for get_services

    Gets all the services in the application resource.
    """
    params = [('api-version', 6.3-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

