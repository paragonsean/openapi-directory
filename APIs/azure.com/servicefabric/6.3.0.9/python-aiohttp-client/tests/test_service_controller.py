# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_health_policy import ApplicationHealthPolicy
from openapi_server.models.application_name_info import ApplicationNameInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.health_information import HealthInformation
from openapi_server.models.paged_service_info_list import PagedServiceInfoList
from openapi_server.models.resolved_service_partition import ResolvedServicePartition
from openapi_server.models.service_description import ServiceDescription
from openapi_server.models.service_from_template_description import ServiceFromTemplateDescription
from openapi_server.models.service_health import ServiceHealth
from openapi_server.models.service_info import ServiceInfo
from openapi_server.models.service_update_description import ServiceUpdateDescription


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_service(client):
    """Test case for create_service

    Creates the specified Service Fabric service.
    """
    service_description = openapi_server.ServiceDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/GetServices/$/Create'.format(application_id='application_id_example'),
        headers=headers,
        json=service_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_service_from_template(client):
    """Test case for create_service_from_template

    Creates a Service Fabric service from the service template.
    """
    service_from_template_description = openapi_server.ServiceFromTemplateDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/GetServices/$/CreateFromTemplate'.format(application_id='application_id_example'),
        headers=headers,
        json=service_from_template_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    Deletes an existing Service Fabric service.
    """
    params = [('api-version', 6.0),
                    ('ForceRemove', True),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/Delete'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_name_info(client):
    """Test case for get_application_name_info

    Gets the name of the Service Fabric application for a service.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_id}/$/GetApplicationName'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_description(client):
    """Test case for get_service_description

    Gets the description of an existing Service Fabric service.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_id}/$/GetDescription'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_health(client):
    """Test case for get_service_health

    Gets the health of the specified Service Fabric service.
    """
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('PartitionsHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_id}/$/GetHealth'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_service_health_using_policy(client):
    """Test case for get_service_health_using_policy

    Gets the health of the specified Service Fabric service, by using the specified health policy.
    """
    application_health_policy = openapi_server.ApplicationHealthPolicy()
    params = [('api-version', 6.0),
                    ('EventsHealthStateFilter', 0),
                    ('PartitionsHealthStateFilter', 0),
                    ('ExcludeHealthStatistics', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/GetHealth'.format(service_id='service_id_example'),
        headers=headers,
        json=application_health_policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_info(client):
    """Test case for get_service_info

    Gets the information about the specific service belonging to the Service Fabric application.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}/$/GetServices/{service_id}'.format(application_id='application_id_example', service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_info_list(client):
    """Test case for get_service_info_list

    Gets the information about all services belonging to the application specified by the application ID.
    """
    params = [('ServiceTypeName', 'service_type_name_example'),
                    ('api-version', 6.0),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}/$/GetServices'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_report_service_health(client):
    """Test case for report_service_health

    Sends a health report on the Service Fabric service.
    """
    health_information = openapi_server.HealthInformation()
    params = [('api-version', 6.0),
                    ('Immediate', False),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/ReportHealth'.format(service_id='service_id_example'),
        headers=headers,
        json=health_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resolve_service(client):
    """Test case for resolve_service

    Resolve a Service Fabric partition.
    """
    params = [('api-version', 6.0),
                    ('PartitionKeyType', 56),
                    ('PartitionKeyValue', 'partition_key_value_example'),
                    ('PreviousRspVersion', 'previous_rsp_version_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_id}/$/ResolvePartition'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_service(client):
    """Test case for update_service

    Updates a Service Fabric service using the specified update description.
    """
    service_update_description = openapi_server.ServiceUpdateDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/Update'.format(service_id='service_id_example'),
        headers=headers,
        json=service_update_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

