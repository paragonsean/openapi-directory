# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_record_set import ResourceRecordSet
from openapi_server.models.resource_record_sets_list_response import ResourceRecordSetsListResponse


pytestmark = pytest.mark.asyncio

async def test_dns_resource_record_sets_create(client):
    """Test case for dns_resource_record_sets_create

    
    """
    body = {"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1}
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
                    ('clientOperationId', 'client_operation_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/dns/v2/projects/{project}/locations/{location}/managedZones/{managed_zone}/rrsets'.format(project='project_example', location='location_example', managed_zone='managed_zone_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_resource_record_sets_delete(client):
    """Test case for dns_resource_record_sets_delete

    
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
                    ('clientOperationId', 'client_operation_id_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/dns/v2/projects/{project}/locations/{location}/managedZones/{managed_zone}/rrsets/{name}/{type}'.format(project='project_example', location='location_example', managed_zone='managed_zone_example', name='name_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_resource_record_sets_get(client):
    """Test case for dns_resource_record_sets_get

    
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
                    ('clientOperationId', 'client_operation_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dns/v2/projects/{project}/locations/{location}/managedZones/{managed_zone}/rrsets/{name}/{type}'.format(project='project_example', location='location_example', managed_zone='managed_zone_example', name='name_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_resource_record_sets_list(client):
    """Test case for dns_resource_record_sets_list

    
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
                    ('maxResults', 56),
                    ('name', 'name_example'),
                    ('pageToken', 'page_token_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dns/v2/projects/{project}/locations/{location}/managedZones/{managed_zone}/rrsets'.format(project='project_example', location='location_example', managed_zone='managed_zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_resource_record_sets_patch(client):
    """Test case for dns_resource_record_sets_patch

    
    """
    body = {"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"NONE","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"UNDEFINED","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1}
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
                    ('clientOperationId', 'client_operation_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/dns/v2/projects/{project}/locations/{location}/managedZones/{managed_zone}/rrsets/{name}/{type}'.format(project='project_example', location='location_example', managed_zone='managed_zone_example', name='name_example', type='type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

