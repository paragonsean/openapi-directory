# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connectivity_test import ConnectivityTest
from openapi_server.models.list_connectivity_tests_response import ListConnectivityTestsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_connectivity_tests_create(client):
    """Test case for networkmanagement_projects_locations_global_connectivity_tests_create

    
    """
    body = {"probingDetails":{"result":"PROBING_RESULT_UNSPECIFIED","destinationEgressLocation":{"metropolitanArea":"metropolitanArea"},"endpointInfo":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"successfulProbeCount":2,"abortCause":"PROBING_ABORT_CAUSE_UNSPECIFIED","probingLatency":{"latencyPercentiles":[{"latencyMicros":"latencyMicros","percent":5},{"latencyMicros":"latencyMicros","percent":5}]},"verifyTime":"verifyTime","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"sentProbeCount":5},"relatedProjects":["relatedProjects","relatedProjects"],"protocol":"protocol","createTime":"createTime","displayName":"displayName","destination":{"loadBalancerId":"loadBalancerId","cloudRunRevision":{"uri":"uri"},"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","instance":"instance","cloudSqlInstance":"cloudSqlInstance","forwardingRule":"forwardingRule","ipAddress":"ipAddress","forwardingRuleTarget":"FORWARDING_RULE_TARGET_UNSPECIFIED","gkeMasterCluster":"gkeMasterCluster","network":"network","cloudFunction":{"uri":"uri"},"appEngineVersion":{"uri":"uri"},"port":0,"networkType":"NETWORK_TYPE_UNSPECIFIED","projectId":"projectId"},"name":"name","description":"description","reachabilityDetails":{"result":"RESULT_UNSPECIFIED","traces":[{"endpointInfo":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"steps":[{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"},{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"}],"forwardTraceId":7},{"endpointInfo":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"steps":[{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"},{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"}],"forwardTraceId":7}],"verifyTime":"verifyTime","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},"updateTime":"updateTime","source":{"loadBalancerId":"loadBalancerId","cloudRunRevision":{"uri":"uri"},"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","instance":"instance","cloudSqlInstance":"cloudSqlInstance","forwardingRule":"forwardingRule","ipAddress":"ipAddress","forwardingRuleTarget":"FORWARDING_RULE_TARGET_UNSPECIFIED","gkeMasterCluster":"gkeMasterCluster","network":"network","cloudFunction":{"uri":"uri"},"appEngineVersion":{"uri":"uri"},"port":0,"networkType":"NETWORK_TYPE_UNSPECIFIED","projectId":"projectId"},"labels":{"key":"labels"}}
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
                    ('testId', 'test_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/connectivityTests'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_connectivity_tests_get_iam_policy(client):
    """Test case for networkmanagement_projects_locations_global_connectivity_tests_get_iam_policy

    
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
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_connectivity_tests_list(client):
    """Test case for networkmanagement_projects_locations_global_connectivity_tests_list

    
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
        path='/v1/{parent}/connectivityTests'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_connectivity_tests_patch(client):
    """Test case for networkmanagement_projects_locations_global_connectivity_tests_patch

    
    """
    body = {"probingDetails":{"result":"PROBING_RESULT_UNSPECIFIED","destinationEgressLocation":{"metropolitanArea":"metropolitanArea"},"endpointInfo":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"successfulProbeCount":2,"abortCause":"PROBING_ABORT_CAUSE_UNSPECIFIED","probingLatency":{"latencyPercentiles":[{"latencyMicros":"latencyMicros","percent":5},{"latencyMicros":"latencyMicros","percent":5}]},"verifyTime":"verifyTime","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"sentProbeCount":5},"relatedProjects":["relatedProjects","relatedProjects"],"protocol":"protocol","createTime":"createTime","displayName":"displayName","destination":{"loadBalancerId":"loadBalancerId","cloudRunRevision":{"uri":"uri"},"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","instance":"instance","cloudSqlInstance":"cloudSqlInstance","forwardingRule":"forwardingRule","ipAddress":"ipAddress","forwardingRuleTarget":"FORWARDING_RULE_TARGET_UNSPECIFIED","gkeMasterCluster":"gkeMasterCluster","network":"network","cloudFunction":{"uri":"uri"},"appEngineVersion":{"uri":"uri"},"port":0,"networkType":"NETWORK_TYPE_UNSPECIFIED","projectId":"projectId"},"name":"name","description":"description","reachabilityDetails":{"result":"RESULT_UNSPECIFIED","traces":[{"endpointInfo":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"steps":[{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"},{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"}],"forwardTraceId":7},{"endpointInfo":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"steps":[{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"},{"causesDrop":True,"drop":{"destinationIp":"destinationIp","sourceIp":"sourceIp","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri","region":"region"},"instance":{"networkUri":"networkUri","networkTags":["networkTags","networkTags"],"displayName":"displayName","serviceAccount":"serviceAccount","interface":"interface","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"cloudSqlInstance":{"networkUri":"networkUri","displayName":"displayName","region":"region","externalIp":"externalIp","internalIp":"internalIp","uri":"uri"},"forwardingRule":{"networkUri":"networkUri","displayName":"displayName","matchedPortRange":"matchedPortRange","matchedProtocol":"matchedProtocol","vip":"vip","uri":"uri","target":"target"},"deliver":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"description":"description","vpnTunnel":{"networkUri":"networkUri","remoteGatewayIp":"remoteGatewayIp","sourceGateway":"sourceGateway","routingType":"ROUTING_TYPE_UNSPECIFIED","displayName":"displayName","sourceGatewayIp":"sourceGatewayIp","region":"region","remoteGateway":"remoteGateway","uri":"uri"},"vpnGateway":{"networkUri":"networkUri","vpnTunnelUri":"vpnTunnelUri","displayName":"displayName","ipAddress":"ipAddress","region":"region","uri":"uri"},"network":{"matchedIpRange":"matchedIpRange","displayName":"displayName","uri":"uri"},"cloudFunction":{"versionId":"versionId","displayName":"displayName","location":"location","uri":"uri"},"storageBucket":{"bucket":"bucket"},"endpoint":{"destinationIp":"destinationIp","destinationPort":6,"protocol":"protocol","sourcePort":1,"sourceIp":"sourceIp","sourceNetworkUri":"sourceNetworkUri","sourceAgentUri":"sourceAgentUri","destinationNetworkUri":"destinationNetworkUri"},"appEngineVersion":{"environment":"environment","displayName":"displayName","runtime":"runtime","uri":"uri"},"loadBalancer":{"healthCheckUri":"healthCheckUri","loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","backendType":"BACKEND_TYPE_UNSPECIFIED","backendUri":"backendUri","backends":[{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"},{"healthCheckFirewallState":"HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED","healthCheckAllowingFirewallRules":["healthCheckAllowingFirewallRules","healthCheckAllowingFirewallRules"],"displayName":"displayName","healthCheckBlockingFirewallRules":["healthCheckBlockingFirewallRules","healthCheckBlockingFirewallRules"],"uri":"uri"}]},"googleService":{"sourceIp":"sourceIp","googleServiceType":"GOOGLE_SERVICE_TYPE_UNSPECIFIED"},"state":"STATE_UNSPECIFIED","nat":{"networkUri":"networkUri","routerUri":"routerUri","natGatewayName":"natGatewayName","newDestinationPort":3,"oldSourcePort":7,"type":"TYPE_UNSPECIFIED","newDestinationIp":"newDestinationIp","oldDestinationPort":4,"protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newSourceIp":"newSourceIp","newSourcePort":2},"cloudRunRevision":{"serviceUri":"serviceUri","displayName":"displayName","location":"location","uri":"uri"},"forward":{"ipAddress":"ipAddress","resourceUri":"resourceUri","target":"TARGET_UNSPECIFIED"},"vpcConnector":{"displayName":"displayName","location":"location","uri":"uri"},"proxyConnection":{"networkUri":"networkUri","protocol":"protocol","oldSourceIp":"oldSourceIp","oldDestinationIp":"oldDestinationIp","newDestinationPort":1,"oldSourcePort":6,"subnetUri":"subnetUri","newSourceIp":"newSourceIp","newDestinationIp":"newDestinationIp","newSourcePort":1,"oldDestinationPort":1},"gkeMaster":{"clusterUri":"clusterUri","clusterNetworkUri":"clusterNetworkUri","externalIp":"externalIp","internalIp":"internalIp"},"route":{"networkUri":"networkUri","nextHop":"nextHop","srcPortRanges":["srcPortRanges","srcPortRanges"],"nccHubUri":"nccHubUri","displayName":"displayName","nextHopType":"NEXT_HOP_TYPE_UNSPECIFIED","instanceTags":["instanceTags","instanceTags"],"destPortRanges":["destPortRanges","destPortRanges"],"priority":7,"uri":"uri","srcIpRange":"srcIpRange","nccSpokeUri":"nccSpokeUri","destIpRange":"destIpRange","protocols":["protocols","protocols"],"routeScope":"ROUTE_SCOPE_UNSPECIFIED","routeType":"ROUTE_TYPE_UNSPECIFIED"},"abort":{"projectsMissingPermission":["projectsMissingPermission","projectsMissingPermission"],"ipAddress":"ipAddress","cause":"CAUSE_UNSPECIFIED","resourceUri":"resourceUri"},"firewall":{"networkUri":"networkUri","targetServiceAccounts":["targetServiceAccounts","targetServiceAccounts"],"firewallRuleType":"FIREWALL_RULE_TYPE_UNSPECIFIED","displayName":"displayName","action":"action","targetTags":["targetTags","targetTags"],"priority":9,"uri":"uri","direction":"direction","policy":"policy"},"loadBalancerBackendInfo":{"healthCheckFirewallsConfigState":"HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED","healthCheckUri":"healthCheckUri","pscGoogleApiTarget":"pscGoogleApiTarget","backendServiceUri":"backendServiceUri","instanceUri":"instanceUri","name":"name","pscServiceAttachmentUri":"pscServiceAttachmentUri","instanceGroupUri":"instanceGroupUri","networkEndpointGroupUri":"networkEndpointGroupUri","backendBucketUri":"backendBucketUri"},"projectId":"projectId"}],"forwardTraceId":7}],"verifyTime":"verifyTime","error":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},"updateTime":"updateTime","source":{"loadBalancerId":"loadBalancerId","cloudRunRevision":{"uri":"uri"},"loadBalancerType":"LOAD_BALANCER_TYPE_UNSPECIFIED","instance":"instance","cloudSqlInstance":"cloudSqlInstance","forwardingRule":"forwardingRule","ipAddress":"ipAddress","forwardingRuleTarget":"FORWARDING_RULE_TARGET_UNSPECIFIED","gkeMasterCluster":"gkeMasterCluster","network":"network","cloudFunction":{"uri":"uri"},"appEngineVersion":{"uri":"uri"},"port":0,"networkType":"NETWORK_TYPE_UNSPECIFIED","projectId":"projectId"},"labels":{"key":"labels"}}
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_connectivity_tests_rerun(client):
    """Test case for networkmanagement_projects_locations_global_connectivity_tests_rerun

    
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
        path='/v1/{namereru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_connectivity_tests_set_iam_policy(client):
    """Test case for networkmanagement_projects_locations_global_connectivity_tests_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_connectivity_tests_test_iam_permissions(client):
    """Test case for networkmanagement_projects_locations_global_connectivity_tests_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_operations_cancel(client):
    """Test case for networkmanagement_projects_locations_global_operations_cancel

    
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
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_operations_delete(client):
    """Test case for networkmanagement_projects_locations_global_operations_delete

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_operations_get(client):
    """Test case for networkmanagement_projects_locations_global_operations_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_global_operations_list(client):
    """Test case for networkmanagement_projects_locations_global_operations_list

    
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
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkmanagement_projects_locations_list(client):
    """Test case for networkmanagement_projects_locations_list

    
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
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

