# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_policy import AlertPolicy
from openapi_server.models.create_collectd_time_series_request import CreateCollectdTimeSeriesRequest
from openapi_server.models.create_collectd_time_series_response import CreateCollectdTimeSeriesResponse
from openapi_server.models.create_time_series_request import CreateTimeSeriesRequest
from openapi_server.models.get_notification_channel_verification_code_request import GetNotificationChannelVerificationCodeRequest
from openapi_server.models.get_notification_channel_verification_code_response import GetNotificationChannelVerificationCodeResponse
from openapi_server.models.group import Group
from openapi_server.models.list_alert_policies_response import ListAlertPoliciesResponse
from openapi_server.models.list_group_members_response import ListGroupMembersResponse
from openapi_server.models.list_groups_response import ListGroupsResponse
from openapi_server.models.list_metric_descriptors_response import ListMetricDescriptorsResponse
from openapi_server.models.list_monitored_resource_descriptors_response import ListMonitoredResourceDescriptorsResponse
from openapi_server.models.list_notification_channel_descriptors_response import ListNotificationChannelDescriptorsResponse
from openapi_server.models.list_notification_channels_response import ListNotificationChannelsResponse
from openapi_server.models.list_snoozes_response import ListSnoozesResponse
from openapi_server.models.list_time_series_response import ListTimeSeriesResponse
from openapi_server.models.list_uptime_check_configs_response import ListUptimeCheckConfigsResponse
from openapi_server.models.metric_descriptor import MetricDescriptor
from openapi_server.models.notification_channel import NotificationChannel
from openapi_server.models.query_time_series_request import QueryTimeSeriesRequest
from openapi_server.models.query_time_series_response import QueryTimeSeriesResponse
from openapi_server.models.snooze import Snooze
from openapi_server.models.uptime_check_config import UptimeCheckConfig
from openapi_server.models.verify_notification_channel_request import VerifyNotificationChannelRequest


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_alert_policies_create(client):
    """Test case for monitoring_projects_alert_policies_create

    
    """
    body = {"severity":"SEVERITY_UNSPECIFIED","displayName":"displayName","documentation":{"subject":"subject","mimeType":"mimeType","content":"content"},"userLabels":{"key":"userLabels"},"combiner":"COMBINE_UNSPECIFIED","enabled":True,"mutationRecord":{"mutatedBy":"mutatedBy","mutateTime":"mutateTime"},"name":"name","notificationChannels":["notificationChannels","notificationChannels"],"validity":{"code":5,"details":[{"key":""},{"key":""}],"message":"message"},"conditions":[{"conditionThreshold":{"duration":"duration","filter":"filter","comparison":"COMPARISON_UNSPECIFIED","forecastOptions":{"forecastHorizon":"forecastHorizon"},"denominatorAggregations":[{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]},{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]}],"thresholdValue":1.4658129805029452,"trigger":{"count":0,"percent":6.027456183070403},"aggregations":[{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]},{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]}],"evaluationMissingData":"EVALUATION_MISSING_DATA_UNSPECIFIED","denominatorFilter":"denominatorFilter"},"conditionAbsent":{"duration":"duration","filter":"filter","trigger":{"count":0,"percent":6.027456183070403},"aggregations":[{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]},{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]}]},"displayName":"displayName","name":"name","conditionPrometheusQueryLanguage":{"duration":"duration","query":"query","evaluationInterval":"evaluationInterval","ruleGroup":"ruleGroup","alertRule":"alertRule","labels":{"key":"labels"}},"conditionMatchedLog":{"filter":"filter","labelExtractors":{"key":"labelExtractors"}},"conditionMonitoringQueryLanguage":{"duration":"duration","query":"query","trigger":{"count":0,"percent":6.027456183070403},"evaluationMissingData":"EVALUATION_MISSING_DATA_UNSPECIFIED"}},{"conditionThreshold":{"duration":"duration","filter":"filter","comparison":"COMPARISON_UNSPECIFIED","forecastOptions":{"forecastHorizon":"forecastHorizon"},"denominatorAggregations":[{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]},{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]}],"thresholdValue":1.4658129805029452,"trigger":{"count":0,"percent":6.027456183070403},"aggregations":[{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]},{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]}],"evaluationMissingData":"EVALUATION_MISSING_DATA_UNSPECIFIED","denominatorFilter":"denominatorFilter"},"conditionAbsent":{"duration":"duration","filter":"filter","trigger":{"count":0,"percent":6.027456183070403},"aggregations":[{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]},{"perSeriesAligner":"ALIGN_NONE","alignmentPeriod":"alignmentPeriod","crossSeriesReducer":"REDUCE_NONE","groupByFields":["groupByFields","groupByFields"]}]},"displayName":"displayName","name":"name","conditionPrometheusQueryLanguage":{"duration":"duration","query":"query","evaluationInterval":"evaluationInterval","ruleGroup":"ruleGroup","alertRule":"alertRule","labels":{"key":"labels"}},"conditionMatchedLog":{"filter":"filter","labelExtractors":{"key":"labelExtractors"}},"conditionMonitoringQueryLanguage":{"duration":"duration","query":"query","trigger":{"count":0,"percent":6.027456183070403},"evaluationMissingData":"EVALUATION_MISSING_DATA_UNSPECIFIED"}}],"alertStrategy":{"notificationRateLimit":{"period":"period"},"notificationChannelStrategy":[{"notificationChannelNames":["notificationChannelNames","notificationChannelNames"],"renotifyInterval":"renotifyInterval"},{"notificationChannelNames":["notificationChannelNames","notificationChannelNames"],"renotifyInterval":"renotifyInterval"}],"autoClose":"autoClose"},"creationRecord":{"mutatedBy":"mutatedBy","mutateTime":"mutateTime"}}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/alertPolicies'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_alert_policies_list(client):
    """Test case for monitoring_projects_alert_policies_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{name}/alertPolicies'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_collectd_time_series_create(client):
    """Test case for monitoring_projects_collectd_time_series_create

    
    """
    body = {"resource":{"type":"type","labels":{"key":"labels"}},"collectdPayloads":[{"metadata":{"key":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}},"pluginInstance":"pluginInstance","plugin":"plugin","typeInstance":"typeInstance","values":[{"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}},"dataSourceName":"dataSourceName","dataSourceType":"UNSPECIFIED_DATA_SOURCE_TYPE"},{"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}},"dataSourceName":"dataSourceName","dataSourceType":"UNSPECIFIED_DATA_SOURCE_TYPE"}],"startTime":"startTime","endTime":"endTime","type":"type"},{"metadata":{"key":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}},"pluginInstance":"pluginInstance","plugin":"plugin","typeInstance":"typeInstance","values":[{"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}},"dataSourceName":"dataSourceName","dataSourceType":"UNSPECIFIED_DATA_SOURCE_TYPE"},{"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}},"dataSourceName":"dataSourceName","dataSourceType":"UNSPECIFIED_DATA_SOURCE_TYPE"}],"startTime":"startTime","endTime":"endTime","type":"type"}],"collectdVersion":"collectdVersion"}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/collectdTimeSeries'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_groups_create(client):
    """Test case for monitoring_projects_groups_create

    
    """
    body = {"filter":"filter","parentName":"parentName","displayName":"displayName","name":"name","isCluster":True}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/groups'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_groups_list(client):
    """Test case for monitoring_projects_groups_list

    
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
                    ('ancestorsOfGroup', 'ancestors_of_group_example'),
                    ('childrenOfGroup', 'children_of_group_example'),
                    ('descendantsOfGroup', 'descendants_of_group_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{name}/groups'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_groups_members_list(client):
    """Test case for monitoring_projects_groups_members_list

    
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
                    ('interval.endTime', 'interval_end_time_example'),
                    ('interval.startTime', 'interval_start_time_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{name}/members'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_groups_update(client):
    """Test case for monitoring_projects_groups_update

    
    """
    body = {"filter":"filter","parentName":"parentName","displayName":"displayName","name":"name","isCluster":True}
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
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_metric_descriptors_create(client):
    """Test case for monitoring_projects_metric_descriptors_create

    
    """
    body = {"monitoredResourceTypes":["monitoredResourceTypes","monitoredResourceTypes"],"metadata":{"ingestDelay":"ingestDelay","launchStage":"LAUNCH_STAGE_UNSPECIFIED","samplePeriod":"samplePeriod"},"unit":"unit","metricKind":"METRIC_KIND_UNSPECIFIED","displayName":"displayName","valueType":"VALUE_TYPE_UNSPECIFIED","name":"name","description":"description","launchStage":"LAUNCH_STAGE_UNSPECIFIED","type":"type","labels":[{"valueType":"STRING","description":"description","key":"key"},{"valueType":"STRING","description":"description","key":"key"}]}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/metricDescriptors'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_metric_descriptors_list(client):
    """Test case for monitoring_projects_metric_descriptors_list

    
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
        path='/v3/{name}/metricDescriptors'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_monitored_resource_descriptors_list(client):
    """Test case for monitoring_projects_monitored_resource_descriptors_list

    
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
        path='/v3/{name}/monitoredResourceDescriptors'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_notification_channel_descriptors_list(client):
    """Test case for monitoring_projects_notification_channel_descriptors_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{name}/notificationChannelDescriptors'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_notification_channels_create(client):
    """Test case for monitoring_projects_notification_channels_create

    
    """
    body = {"verificationStatus":"VERIFICATION_STATUS_UNSPECIFIED","displayName":"displayName","name":"name","description":"description","userLabels":{"key":"userLabels"},"mutationRecords":[{"mutatedBy":"mutatedBy","mutateTime":"mutateTime"},{"mutatedBy":"mutatedBy","mutateTime":"mutateTime"}],"type":"type","enabled":True,"creationRecord":{"mutatedBy":"mutatedBy","mutateTime":"mutateTime"},"labels":{"key":"labels"}}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/notificationChannels'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_notification_channels_get_verification_code(client):
    """Test case for monitoring_projects_notification_channels_get_verification_code

    
    """
    body = {"expireTime":"expireTime"}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{nameget_verification_cod}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_notification_channels_list(client):
    """Test case for monitoring_projects_notification_channels_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{name}/notificationChannels'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_notification_channels_send_verification_code(client):
    """Test case for monitoring_projects_notification_channels_send_verification_code

    
    """
    body = None
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{namesend_verification_cod}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_notification_channels_verify(client):
    """Test case for monitoring_projects_notification_channels_verify

    
    """
    body = {"code":"code"}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{nameverif}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_snoozes_create(client):
    """Test case for monitoring_projects_snoozes_create

    
    """
    body = {"criteria":{"policies":["policies","policies"]},"displayName":"displayName","name":"name","interval":{"startTime":"startTime","endTime":"endTime"}}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{parent}/snoozes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_snoozes_list(client):
    """Test case for monitoring_projects_snoozes_list

    
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
        path='/v3/{parent}/snoozes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_time_series_create(client):
    """Test case for monitoring_projects_time_series_create

    
    """
    body = {"timeSeries":[{"metadata":{"systemLabels":{"key":""},"userLabels":{"key":"userLabels"}},"unit":"unit","metricKind":"METRIC_KIND_UNSPECIFIED","metric":{"type":"type","labels":{"key":"labels"}},"resource":{"type":"type","labels":{"key":"labels"}},"valueType":"VALUE_TYPE_UNSPECIFIED","points":[{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}},{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}}]},{"metadata":{"systemLabels":{"key":""},"userLabels":{"key":"userLabels"}},"unit":"unit","metricKind":"METRIC_KIND_UNSPECIFIED","metric":{"type":"type","labels":{"key":"labels"}},"resource":{"type":"type","labels":{"key":"labels"}},"valueType":"VALUE_TYPE_UNSPECIFIED","points":[{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}},{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}}]}]}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/timeSeries'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_time_series_create_service(client):
    """Test case for monitoring_projects_time_series_create_service

    
    """
    body = {"timeSeries":[{"metadata":{"systemLabels":{"key":""},"userLabels":{"key":"userLabels"}},"unit":"unit","metricKind":"METRIC_KIND_UNSPECIFIED","metric":{"type":"type","labels":{"key":"labels"}},"resource":{"type":"type","labels":{"key":"labels"}},"valueType":"VALUE_TYPE_UNSPECIFIED","points":[{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}},{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}}]},{"metadata":{"systemLabels":{"key":""},"userLabels":{"key":"userLabels"}},"unit":"unit","metricKind":"METRIC_KIND_UNSPECIFIED","metric":{"type":"type","labels":{"key":"labels"}},"resource":{"type":"type","labels":{"key":"labels"}},"valueType":"VALUE_TYPE_UNSPECIFIED","points":[{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}},{"interval":{"startTime":"startTime","endTime":"endTime"},"value":{"int64Value":"int64Value","stringValue":"stringValue","boolValue":True,"doubleValue":1.2315135367772556,"distributionValue":{"exemplars":[{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"},{"attachments":[{"key":""},{"key":""}],"value":9.301444243932576,"timestamp":"timestamp"}],"mean":3.616076749251911,"bucketCounts":["bucketCounts","bucketCounts"],"bucketOptions":{"explicitBuckets":{"bounds":[0.8008281904610115,0.8008281904610115]},"linearBuckets":{"offset":2.3021358869347655,"width":7.061401241503109,"numFiniteBuckets":5},"exponentialBuckets":{"growthFactor":6.027456183070403,"scale":5.962133916683182,"numFiniteBuckets":1}},"count":"count","range":{"min":4.145608029883936,"max":2.027123023002322},"sumOfSquaredDeviation":7.386281948385884}}}]}]}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/timeSeries:createService'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_time_series_list(client):
    """Test case for monitoring_projects_time_series_list

    
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
                    ('aggregation.alignmentPeriod', 'aggregation_alignment_period_example'),
                    ('aggregation.crossSeriesReducer', 'aggregation_cross_series_reducer_example'),
                    ('aggregation.groupByFields', ['aggregation_group_by_fields_example']),
                    ('aggregation.perSeriesAligner', 'aggregation_per_series_aligner_example'),
                    ('filter', 'filter_example'),
                    ('interval.endTime', 'interval_end_time_example'),
                    ('interval.startTime', 'interval_start_time_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('secondaryAggregation.alignmentPeriod', 'secondary_aggregation_alignment_period_example'),
                    ('secondaryAggregation.crossSeriesReducer', 'secondary_aggregation_cross_series_reducer_example'),
                    ('secondaryAggregation.groupByFields', ['secondary_aggregation_group_by_fields_example']),
                    ('secondaryAggregation.perSeriesAligner', 'secondary_aggregation_per_series_aligner_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/{name}/timeSeries'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_time_series_query(client):
    """Test case for monitoring_projects_time_series_query

    
    """
    body = {"query":"query","pageSize":0,"pageToken":"pageToken"}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{name}/timeSeries:query'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_uptime_check_configs_create(client):
    """Test case for monitoring_projects_uptime_check_configs_create

    
    """
    body = {"resourceGroup":{"groupId":"groupId","resourceType":"RESOURCE_TYPE_UNSPECIFIED"},"period":"period","displayName":"displayName","httpCheck":{"headers":{"key":"headers"},"acceptedResponseStatusCodes":[{"statusClass":"STATUS_CLASS_UNSPECIFIED","statusValue":6},{"statusClass":"STATUS_CLASS_UNSPECIFIED","statusValue":6}],"requestMethod":"METHOD_UNSPECIFIED","validateSsl":True,"body":"body","pingConfig":{"pingsCount":1},"authInfo":{"password":"password","username":"username"},"useSsl":True,"path":"path","customContentType":"customContentType","maskHeaders":True,"port":5,"contentType":"TYPE_UNSPECIFIED"},"userLabels":{"key":"userLabels"},"monitoredResource":{"type":"type","labels":{"key":"labels"}},"internalCheckers":[{"displayName":"displayName","gcpZone":"gcpZone","peerProjectId":"peerProjectId","name":"name","state":"UNSPECIFIED","network":"network"},{"displayName":"displayName","gcpZone":"gcpZone","peerProjectId":"peerProjectId","name":"name","state":"UNSPECIFIED","network":"network"}],"timeout":"timeout","isInternal":True,"checkerType":"CHECKER_TYPE_UNSPECIFIED","contentMatchers":[{"jsonPathMatcher":{"jsonPath":"jsonPath","jsonMatcher":"JSON_PATH_MATCHER_OPTION_UNSPECIFIED"},"matcher":"CONTENT_MATCHER_OPTION_UNSPECIFIED","content":"content"},{"jsonPathMatcher":{"jsonPath":"jsonPath","jsonMatcher":"JSON_PATH_MATCHER_OPTION_UNSPECIFIED"},"matcher":"CONTENT_MATCHER_OPTION_UNSPECIFIED","content":"content"}],"selectedRegions":["REGION_UNSPECIFIED","REGION_UNSPECIFIED"],"syntheticMonitor":{"cloudFunctionV2":{"cloudRunRevision":{"type":"type","labels":{"key":"labels"}},"name":"name"}},"tcpCheck":{"port":5,"pingConfig":{"pingsCount":1}},"name":"name"}
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/{parent}/uptimeCheckConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_monitoring_projects_uptime_check_configs_list(client):
    """Test case for monitoring_projects_uptime_check_configs_list

    
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
        path='/v3/{parent}/uptimeCheckConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

