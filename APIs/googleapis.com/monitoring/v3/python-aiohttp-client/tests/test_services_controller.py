# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_service_level_objectives_response import ListServiceLevelObjectivesResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.service import Service
from openapi_server.models.service_level_objective import ServiceLevelObjective


pytestmark = pytest.mark.asyncio

async def test_monitoring_services_create(client):
    """Test case for monitoring_services_create

    
    """
    body = {"gkeNamespace":{"clusterName":"clusterName","location":"location","projectId":"projectId","namespaceName":"namespaceName"},"displayName":"displayName","custom":"{}","cloudRun":{"location":"location","serviceName":"serviceName"},"userLabels":{"key":"userLabels"},"appEngine":{"moduleId":"moduleId"},"clusterIstio":{"clusterName":"clusterName","location":"location","serviceNamespace":"serviceNamespace","serviceName":"serviceName"},"gkeService":{"clusterName":"clusterName","location":"location","serviceName":"serviceName","projectId":"projectId","namespaceName":"namespaceName"},"basicService":{"serviceLabels":{"key":"serviceLabels"},"serviceType":"serviceType"},"istioCanonicalService":{"meshUid":"meshUid","canonicalServiceNamespace":"canonicalServiceNamespace","canonicalService":"canonicalService"},"gkeWorkload":{"clusterName":"clusterName","location":"location","topLevelControllerName":"topLevelControllerName","topLevelControllerType":"topLevelControllerType","projectId":"projectId","namespaceName":"namespaceName"},"name":"name","meshIstio":{"meshUid":"meshUid","serviceNamespace":"serviceNamespace","serviceName":"serviceName"},"telemetry":{"resourceName":"resourceName"},"cloudEndpoints":{"service":"service"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('serviceId', 'service_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{parent}/services'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_services_list(client):
    """Test case for monitoring_services_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{parent}/services'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_services_service_level_objectives_create(client):
    """Test case for monitoring_services_service_level_objectives_create

    
    """
    body = {"goal":0.8008281904610115,"rollingPeriod":"rollingPeriod","displayName":"displayName","serviceLevelIndicator":{"basicSli":{"method":["method","method"],"latency":{"threshold":"threshold"},"location":["location","location"],"availability":"{}","version":["version","version"]},"windowsBased":{"metricMeanInRange":{"timeSeries":"timeSeries","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodBadMetricFilter":"goodBadMetricFilter","windowPeriod":"windowPeriod","metricSumInRange":{"timeSeries":"timeSeries","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodTotalRatioThreshold":{"performance":{"distributionCut":{"distributionFilter":"distributionFilter","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodTotalRatio":{"badServiceFilter":"badServiceFilter","totalServiceFilter":"totalServiceFilter","goodServiceFilter":"goodServiceFilter"}},"threshold":5.962133916683182,"basicSliPerformance":{"method":["method","method"],"latency":{"threshold":"threshold"},"location":["location","location"],"availability":"{}","version":["version","version"]}}},"requestBased":{"distributionCut":{"distributionFilter":"distributionFilter","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodTotalRatio":{"badServiceFilter":"badServiceFilter","totalServiceFilter":"totalServiceFilter","goodServiceFilter":"goodServiceFilter"}}},"name":"name","userLabels":{"key":"userLabels"},"calendarPeriod":"CALENDAR_PERIOD_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('serviceLevelObjectiveId', 'service_level_objective_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{parent}/serviceLevelObjectives'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_services_service_level_objectives_delete(client):
    """Test case for monitoring_services_service_level_objectives_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('force', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_services_service_level_objectives_get(client):
    """Test case for monitoring_services_service_level_objectives_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_services_service_level_objectives_list(client):
    """Test case for monitoring_services_service_level_objectives_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{parent}/serviceLevelObjectives'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_services_service_level_objectives_patch(client):
    """Test case for monitoring_services_service_level_objectives_patch

    
    """
    body = {"goal":0.8008281904610115,"rollingPeriod":"rollingPeriod","displayName":"displayName","serviceLevelIndicator":{"basicSli":{"method":["method","method"],"latency":{"threshold":"threshold"},"location":["location","location"],"availability":"{}","version":["version","version"]},"windowsBased":{"metricMeanInRange":{"timeSeries":"timeSeries","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodBadMetricFilter":"goodBadMetricFilter","windowPeriod":"windowPeriod","metricSumInRange":{"timeSeries":"timeSeries","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodTotalRatioThreshold":{"performance":{"distributionCut":{"distributionFilter":"distributionFilter","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodTotalRatio":{"badServiceFilter":"badServiceFilter","totalServiceFilter":"totalServiceFilter","goodServiceFilter":"goodServiceFilter"}},"threshold":5.962133916683182,"basicSliPerformance":{"method":["method","method"],"latency":{"threshold":"threshold"},"location":["location","location"],"availability":"{}","version":["version","version"]}}},"requestBased":{"distributionCut":{"distributionFilter":"distributionFilter","range":{"min":1.4658129805029452,"max":6.027456183070403}},"goodTotalRatio":{"badServiceFilter":"badServiceFilter","totalServiceFilter":"totalServiceFilter","goodServiceFilter":"goodServiceFilter"}}},"name":"name","userLabels":{"key":"userLabels"},"calendarPeriod":"CALENDAR_PERIOD_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

