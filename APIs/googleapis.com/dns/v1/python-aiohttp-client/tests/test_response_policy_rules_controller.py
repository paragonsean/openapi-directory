# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.response_policy_rule import ResponsePolicyRule
from openapi_server.models.response_policy_rules_list_response import ResponsePolicyRulesListResponse
from openapi_server.models.response_policy_rules_patch_response import ResponsePolicyRulesPatchResponse
from openapi_server.models.response_policy_rules_update_response import ResponsePolicyRulesUpdateResponse


pytestmark = pytest.mark.asyncio

async def test_dns_response_policy_rules_create(client):
    """Test case for dns_response_policy_rules_create

    
    """
    body = {"kind":"dns#responsePolicyRule","localData":{"localDatas":[{"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1},{"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1}]},"dnsName":"dnsName","ruleName":"ruleName","behavior":"behaviorUnspecified"}
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
        path='/dns/v1/projects/{project}/responsePolicies/{response_policy}/rules'.format(project='project_example', response_policy='response_policy_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policy_rules_delete(client):
    """Test case for dns_response_policy_rules_delete

    
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
        path='/dns/v1/projects/{project}/responsePolicies/{response_policy}/rules/{response_policy_rule}'.format(project='project_example', response_policy='response_policy_example', response_policy_rule='response_policy_rule_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policy_rules_get(client):
    """Test case for dns_response_policy_rules_get

    
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
        path='/dns/v1/projects/{project}/responsePolicies/{response_policy}/rules/{response_policy_rule}'.format(project='project_example', response_policy='response_policy_example', response_policy_rule='response_policy_rule_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policy_rules_list(client):
    """Test case for dns_response_policy_rules_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dns/v1/projects/{project}/responsePolicies/{response_policy}/rules'.format(project='project_example', response_policy='response_policy_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policy_rules_patch(client):
    """Test case for dns_response_policy_rules_patch

    
    """
    body = {"kind":"dns#responsePolicyRule","localData":{"localDatas":[{"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1},{"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1}]},"dnsName":"dnsName","ruleName":"ruleName","behavior":"behaviorUnspecified"}
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
        path='/dns/v1/projects/{project}/responsePolicies/{response_policy}/rules/{response_policy_rule}'.format(project='project_example', response_policy='response_policy_example', response_policy_rule='response_policy_rule_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policy_rules_update(client):
    """Test case for dns_response_policy_rules_update

    
    """
    body = {"kind":"dns#responsePolicyRule","localData":{"localDatas":[{"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1},{"rrdatas":["rrdatas","rrdatas"],"kind":"dns#resourceRecordSet","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"name":"name","routingPolicy":{"geo":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"kind":"dns#rRSetRoutingPolicy","wrr":{"kind":"dns#rRSetRoutingPolicyWrrPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyWrrPolicyWrrPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"weight":6.027456183070403}]},"healthCheck":"healthCheck","primaryBackup":{"primaryTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyPrimaryBackupPolicy","backupGeoTargets":{"enableFencing":True,"kind":"dns#rRSetRoutingPolicyGeoPolicy","items":[{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"},{"rrdatas":["rrdatas","rrdatas"],"healthCheckedTargets":{"externalEndpoints":["externalEndpoints","externalEndpoints"],"internalLoadBalancers":[{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"},{"loadBalancerType":"none","port":"port","kind":"dns#rRSetRoutingPolicyLoadBalancerTarget","ipAddress":"ipAddress","project":"project","ipProtocol":"undefined","region":"region","networkUrl":"networkUrl"}]},"kind":"dns#rRSetRoutingPolicyGeoPolicyGeoPolicyItem","signatureRrdatas":["signatureRrdatas","signatureRrdatas"],"location":"location"}]},"trickleTraffic":0.8008281904610115}},"type":"type","ttl":1}]},"dnsName":"dnsName","ruleName":"ruleName","behavior":"behaviorUnspecified"}
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
        method='PUT',
        path='/dns/v1/projects/{project}/responsePolicies/{response_policy}/rules/{response_policy_rule}'.format(project='project_example', response_policy='response_policy_example', response_policy_rule='response_policy_rule_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

