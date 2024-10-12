# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_counts import ErrorCounts
from openapi_server.models.export_statuses import ExportStatuses
from openapi_server.models.item import Item
from openapi_server.models.items import Items
from openapi_server.models.merged_export_errors import MergedExportErrors
from openapi_server.models.result import Result
from openapi_server.models.service_properties import ServiceProperties
from openapi_server.models.services import Services


pytestmark = pytest.mark.asyncio

async def test_adds_services_delete(client):
    """Test case for adds_services_delete

    
    """
    params = [('confirm', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_get(client):
    """Test case for adds_services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list_premium_services(client):
    """Test case for adds_services_list_premium_services

    
    """
    params = [('$filter', 'filter_example'),
                    ('serviceType', 'service_type_example'),
                    ('skipCount', 56),
                    ('takeCount', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/premiumCheck',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_update(client):
    """Test case for adds_services_update

    
    """
    service = {"additionalInformation":"additionalInformation","monitoringConfigurationsComputed":"{}","signature":"signature","displayName":"displayName","customNotificationEmails":["customNotificationEmails","customNotificationEmails"],"lastDisabled":"2000-01-23T04:56:07.000+00:00","health":"health","resolvedAlerts":1,"notificationEmailEnabledForGlobalAdmins":True,"serviceName":"serviceName","type":"type","lastUpdated":"2000-01-23T04:56:07.000+00:00","notificationEmailsEnabledForGlobalAdmins":True,"createdDate":"2000-01-23T04:56:07.000+00:00","notificationEmailEnabled":True,"originalDisabledState":True,"simpleProperties":"{}","monitoringConfigurationsCustomized":"{}","tenantId":"tenantId","disabled":True,"activeAlerts":6,"id":"id","notificationEmails":["notificationEmails","notificationEmails"],"serviceId":"serviceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        json=service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_add(client):
    """Test case for services_add

    
    """
    service = {"additionalInformation":"additionalInformation","monitoringConfigurationsComputed":"{}","signature":"signature","displayName":"displayName","customNotificationEmails":["customNotificationEmails","customNotificationEmails"],"lastDisabled":"2000-01-23T04:56:07.000+00:00","health":"health","resolvedAlerts":1,"notificationEmailEnabledForGlobalAdmins":True,"serviceName":"serviceName","type":"type","lastUpdated":"2000-01-23T04:56:07.000+00:00","notificationEmailsEnabledForGlobalAdmins":True,"createdDate":"2000-01-23T04:56:07.000+00:00","notificationEmailEnabled":True,"originalDisabledState":True,"simpleProperties":"{}","monitoringConfigurationsCustomized":"{}","tenantId":"tenantId","disabled":True,"activeAlerts":6,"id":"id","notificationEmails":["notificationEmails","notificationEmails"],"serviceId":"serviceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ADHybridHealthService/services',
        headers=headers,
        json=service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_delete(client):
    """Test case for services_delete

    
    """
    params = [('confirm', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get(client):
    """Test case for services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get_feature_availibility(client):
    """Test case for services_get_feature_availibility

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/checkServiceFeatureAvailibility/{feature_name}'.format(service_name='service_name_example', feature_name='feature_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get_tenant_whitelisting(client):
    """Test case for services_get_tenant_whitelisting

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/TenantWhitelisting/{feature_name}'.format(service_name='service_name_example', feature_name='feature_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list(client):
    """Test case for services_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('serviceType', 'service_type_example'),
                    ('skipCount', 56),
                    ('takeCount', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_export_errors(client):
    """Test case for services_list_export_errors

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/exporterrors/counts'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_export_errors_v2(client):
    """Test case for services_list_export_errors_v2

    
    """
    params = [('errorBucket', 'error_bucket_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/exporterrors/listV2'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_export_status(client):
    """Test case for services_list_export_status

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/exportstatus'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_monitoring_configurations(client):
    """Test case for services_list_monitoring_configurations

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/monitoringconfigurations'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_premium(client):
    """Test case for services_list_premium

    
    """
    params = [('$filter', 'filter_example'),
                    ('serviceType', 'service_type_example'),
                    ('skipCount', 56),
                    ('takeCount', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/services/premiumCheck',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_update(client):
    """Test case for services_update

    
    """
    service = {"additionalInformation":"additionalInformation","monitoringConfigurationsComputed":"{}","signature":"signature","displayName":"displayName","customNotificationEmails":["customNotificationEmails","customNotificationEmails"],"lastDisabled":"2000-01-23T04:56:07.000+00:00","health":"health","resolvedAlerts":1,"notificationEmailEnabledForGlobalAdmins":True,"serviceName":"serviceName","type":"type","lastUpdated":"2000-01-23T04:56:07.000+00:00","notificationEmailsEnabledForGlobalAdmins":True,"createdDate":"2000-01-23T04:56:07.000+00:00","notificationEmailEnabled":True,"originalDisabledState":True,"simpleProperties":"{}","monitoringConfigurationsCustomized":"{}","tenantId":"tenantId","disabled":True,"activeAlerts":6,"id":"id","notificationEmails":["notificationEmails","notificationEmails"],"serviceId":"serviceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}'.format(service_name='service_name_example'),
        headers=headers,
        json=service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_update_monitoring_configuration(client):
    """Test case for services_update_monitoring_configuration

    
    """
    configuration_setting = {"value":"value","key":"key"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.ADHybridHealthService/services/{service_name}/monitoringconfiguration'.format(service_name='service_name_example'),
        headers=headers,
        json=configuration_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

