# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.adds_configuration import AddsConfiguration
from openapi_server.models.adds_service_members import AddsServiceMembers
from openapi_server.models.alerts import Alerts
from openapi_server.models.credentials import Credentials
from openapi_server.models.dimensions import Dimensions
from openapi_server.models.forest_summary import ForestSummary
from openapi_server.models.metric_metadata import MetricMetadata
from openapi_server.models.metric_metadata_list import MetricMetadataList
from openapi_server.models.metric_sets import MetricSets
from openapi_server.models.metrics import Metrics
from openapi_server.models.replication_details_list import ReplicationDetailsList
from openapi_server.models.replication_status import ReplicationStatus
from openapi_server.models.replication_summary_list import ReplicationSummaryList
from openapi_server.models.service_member import ServiceMember
from openapi_server.models.service_members import ServiceMembers
from openapi_server.models.service_properties import ServiceProperties
from openapi_server.models.services import Services
from openapi_server.models.user_preference import UserPreference


pytestmark = pytest.mark.asyncio

async def test_ad_domain_service_members_list(client):
    """Test case for ad_domain_service_members_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('isGroupbySite', True),
                    ('query', 'query_example'),
                    ('nextPartitionKey', 'next_partition_key_example'),
                    ('nextRowKey', 'next_row_key_example'),
                    ('takeCount', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/addomainservicemembers'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_service_get_metrics(client):
    """Test case for adds_service_get_metrics

    
    """
    params = [('groupKey', 'group_key_example'),
                    ('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/metrics/{metric_name}/groups/{group_name}'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_service_members_delete(client):
    """Test case for adds_service_members_delete

    
    """
    params = [('confirm', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/servicemembers/{service_member_id}'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_service_members_get(client):
    """Test case for adds_service_members_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/servicemembers/{service_member_id}'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_service_members_list(client):
    """Test case for adds_service_members_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/addsservicemembers'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_service_members_list_credentials(client):
    """Test case for adds_service_members_list_credentials

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/servicemembers/{service_member_id}/credentials'.format(service_name='service_name_example', service_member_id='service_member_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_add(client):
    """Test case for adds_services_add

    
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
        path='/providers/Microsoft.ADHybridHealthService/addsservices',
        headers=headers,
        json=service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_get_forest_summary(client):
    """Test case for adds_services_get_forest_summary

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/forestsummary'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_get_metric_metadata(client):
    """Test case for adds_services_get_metric_metadata

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/metricmetadata/{metric_name}'.format(service_name='service_name_example', metric_name='metric_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_get_metric_metadata_for_group(client):
    """Test case for adds_services_get_metric_metadata_for_group

    
    """
    params = [('groupKey', 'group_key_example'),
                    ('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/metricmetadata/{metric_name}/groups/{group_name}'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list(client):
    """Test case for adds_services_list

    
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
        path='/providers/Microsoft.ADHybridHealthService/addsservices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list_metric_metadata(client):
    """Test case for adds_services_list_metric_metadata

    
    """
    params = [('$filter', 'filter_example'),
                    ('perfCounter', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/metricmetadata'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list_metrics_average(client):
    """Test case for adds_services_list_metrics_average

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/metrics/{metric_name}/groups/{group_name}/average'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list_metrics_sum(client):
    """Test case for adds_services_list_metrics_sum

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/metrics/{metric_name}/groups/{group_name}/sum'.format(service_name='service_name_example', metric_name='metric_name_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list_replication_details(client):
    """Test case for adds_services_list_replication_details

    
    """
    params = [('$filter', 'filter_example'),
                    ('withDetails', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/replicationdetails'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list_replication_summary(client):
    """Test case for adds_services_list_replication_summary

    
    """
    params = [('$filter', 'filter_example'),
                    ('isGroupbySite', True),
                    ('query', 'query_example'),
                    ('nextPartitionKey', 'next_partition_key_example'),
                    ('nextRowKey', 'next_row_key_example'),
                    ('takeCount', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/replicationsummary'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_list_server_alerts(client):
    """Test case for adds_services_list_server_alerts

    
    """
    params = [('$filter', 'filter_example'),
                    ('state', 'state_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/servicemembers/{service_member_id}/alerts'.format(service_member_id='service_member_id_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_replication_status_get(client):
    """Test case for adds_services_replication_status_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/replicationstatus'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_service_members_add(client):
    """Test case for adds_services_service_members_add

    
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
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/servicemembers'.format(service_name='service_name_example'),
        headers=headers,
        json=service_member,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_service_members_list(client):
    """Test case for adds_services_service_members_list

    
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
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/servicemembers'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_user_preference_add(client):
    """Test case for adds_services_user_preference_add

    
    """
    setting = {"metricNames":["metricNames","metricNames"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/features/{feature_name}/userpreference'.format(service_name='service_name_example', feature_name='feature_name_example'),
        headers=headers,
        json=setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_user_preference_delete(client):
    """Test case for adds_services_user_preference_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/features/{feature_name}/userpreference'.format(service_name='service_name_example', feature_name='feature_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adds_services_user_preference_get(client):
    """Test case for adds_services_user_preference_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/features/{feature_name}/userpreference'.format(service_name='service_name_example', feature_name='feature_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_adds_alerts(client):
    """Test case for alerts_list_adds_alerts

    
    """
    params = [('$filter', 'filter_example'),
                    ('state', 'state_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/alerts'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_list_adds_configurations(client):
    """Test case for configuration_list_adds_configurations

    
    """
    params = [('grouping', 'grouping_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/configuration'.format(service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dimensions_list_adds_dimensions(client):
    """Test case for dimensions_list_adds_dimensions

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/addsservices/{service_name}/dimensions/{dimension}'.format(service_name='service_name_example', dimension='dimension_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

