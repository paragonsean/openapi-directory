# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connectors import Connectors
from openapi_server.models.credentials import Credentials
from openapi_server.models.data_freshness_details import DataFreshnessDetails
from openapi_server.models.export_statuses import ExportStatuses
from openapi_server.models.global_configurations import GlobalConfigurations
from openapi_server.models.service_configuration import ServiceConfiguration
from openapi_server.models.service_member import ServiceMember
from openapi_server.models.service_members import ServiceMembers


pytestmark = pytest.mark.asyncio

async def test_service_members_add(client):
    """Test case for service_members_add

    
    """
    service_member = {"recommendedQfes":"{}","lastServerReportedMonitoringLevelChange":"2000-01-23T04:56:07.000+00:00","serverReportedMonitoringLevel":"Partial","role":"role","machineName":"machineName","serviceMemberId":"serviceMemberId","lastUpdated":"2000-01-23T04:56:07.000+00:00","osVersion":"osVersion","lastReboot":"2000-01-23T04:56:07.000+00:00","disabled":True,"serviceId":"serviceId","additionalInformation":"additionalInformation","disabledReason":1,"monitoringConfigurationsComputed":"{}","lastDisabled":"2000-01-23T04:56:07.000+00:00","resolvedAlerts":5,"osName":"osName","createdDate":"2000-01-23T04:56:07.000+00:00","machineId":"machineId","installedQfes":"{}","monitoringConfigurationsCustomized":"{}","tenantId":"tenantId","activeAlerts":6,"properties":"{}","dimensions":"{}","status":"status"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers'.format(service_name='service_name_example'),
        headers=headers,
        json=service_member,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_delete(client):
    """Test case for service_members_delete

    
    """
    params = [('confirm', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_delete_data(client):
    """Test case for service_members_delete_data

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/data'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_get(client):
    """Test case for service_members_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_get_service_configuration(client):
    """Test case for service_members_get_service_configuration

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/serviceconfiguration'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_list(client):
    """Test case for service_members_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('dimensionType', 'dimension_type_example'),
                    ('dimensionSignature', 'dimension_signature_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_list_connectors(client):
    """Test case for service_members_list_connectors

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/service/{service_name}/servicemembers/{service_member_id}/connectors'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_list_credentials(client):
    """Test case for service_members_list_credentials

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/credentials'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_list_data_freshness(client):
    """Test case for service_members_list_data_freshness

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/datafreshness'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_list_export_status(client):
    """Test case for service_members_list_export_status

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/exportstatus'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_members_list_global_configuration(client):
    """Test case for service_members_list_global_configuration

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/servicemembers/{service_member_id}/globalconfiguration'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

