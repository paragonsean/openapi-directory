# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.endpoint_policy import EndpointPolicy
from openapi_server.models.gateway import Gateway
from openapi_server.models.grpc_route import GrpcRoute
from openapi_server.models.http_route import HttpRoute
from openapi_server.models.lb_route_extension import LbRouteExtension
from openapi_server.models.lb_traffic_extension import LbTrafficExtension
from openapi_server.models.list_endpoint_policies_response import ListEndpointPoliciesResponse
from openapi_server.models.list_gateways_response import ListGatewaysResponse
from openapi_server.models.list_grpc_routes_response import ListGrpcRoutesResponse
from openapi_server.models.list_http_routes_response import ListHttpRoutesResponse
from openapi_server.models.list_lb_route_extensions_response import ListLbRouteExtensionsResponse
from openapi_server.models.list_lb_traffic_extensions_response import ListLbTrafficExtensionsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_meshes_response import ListMeshesResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_service_bindings_response import ListServiceBindingsResponse
from openapi_server.models.list_service_lb_policies_response import ListServiceLbPoliciesResponse
from openapi_server.models.list_tcp_routes_response import ListTcpRoutesResponse
from openapi_server.models.list_tls_routes_response import ListTlsRoutesResponse
from openapi_server.models.mesh import Mesh
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.service_binding import ServiceBinding
from openapi_server.models.service_lb_policy import ServiceLbPolicy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.tcp_route import TcpRoute
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.tls_route import TlsRoute


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_endpoint_policies_create(client):
    """Test case for networkservices_projects_locations_endpoint_policies_create

    
    """
    body = {"createTime":"createTime","serverTlsPolicy":"serverTlsPolicy","trafficPortSelector":{"ports":["ports","ports"]},"name":"name","description":"description","endpointMatcher":{"metadataLabelMatcher":{"metadataLabels":[{"labelValue":"labelValue","labelName":"labelName"},{"labelValue":"labelValue","labelName":"labelName"}],"metadataLabelMatchCriteria":"METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED"}},"updateTime":"updateTime","type":"ENDPOINT_POLICY_TYPE_UNSPECIFIED","authorizationPolicy":"authorizationPolicy","clientTlsPolicy":"clientTlsPolicy","labels":{"key":"labels"}}
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
                    ('endpointPolicyId', 'endpoint_policy_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/endpointPolicies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_endpoint_policies_list(client):
    """Test case for networkservices_projects_locations_endpoint_policies_list

    
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
        path='/v1/{parent}/endpointPolicies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_gateways_create(client):
    """Test case for networkservices_projects_locations_gateways_create

    
    """
    body = {"envoyHeaders":"ENVOY_HEADERS_UNSPECIFIED","addresses":["addresses","addresses"],"gatewaySecurityPolicy":"gatewaySecurityPolicy","serverTlsPolicy":"serverTlsPolicy","description":"description","updateTime":"updateTime","ports":[0,0],"type":"TYPE_UNSPECIFIED","labels":{"key":"labels"},"network":"network","selfLink":"selfLink","ipVersion":"IP_VERSION_UNSPECIFIED","certificateUrls":["certificateUrls","certificateUrls"],"createTime":"createTime","scope":"scope","subnetwork":"subnetwork","name":"name"}
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
                    ('gatewayId', 'gateway_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/gateways'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_gateways_list(client):
    """Test case for networkservices_projects_locations_gateways_list

    
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
        path='/v1/{parent}/gateways'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_grpc_routes_create(client):
    """Test case for networkservices_projects_locations_grpc_routes_create

    
    """
    body = {"gateways":["gateways","gateways"],"createTime":"createTime","name":"name","description":"description","hostnames":["hostnames","hostnames"],"rules":[{"action":{"retryPolicy":{"numRetries":5,"retryConditions":["retryConditions","retryConditions"]},"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout","statefulSessionAffinity":{"cookieTtl":"cookieTtl"},"faultInjectionPolicy":{"delay":{"fixedDelay":"fixedDelay","percentage":5},"abort":{"httpStatus":6,"percentage":1}},"timeout":"timeout"},"matches":[{"headers":[{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"},{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"}],"method":{"grpcMethod":"grpcMethod","caseSensitive":True,"type":"TYPE_UNSPECIFIED","grpcService":"grpcService"}},{"headers":[{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"},{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"}],"method":{"grpcMethod":"grpcMethod","caseSensitive":True,"type":"TYPE_UNSPECIFIED","grpcService":"grpcService"}}]},{"action":{"retryPolicy":{"numRetries":5,"retryConditions":["retryConditions","retryConditions"]},"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout","statefulSessionAffinity":{"cookieTtl":"cookieTtl"},"faultInjectionPolicy":{"delay":{"fixedDelay":"fixedDelay","percentage":5},"abort":{"httpStatus":6,"percentage":1}},"timeout":"timeout"},"matches":[{"headers":[{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"},{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"}],"method":{"grpcMethod":"grpcMethod","caseSensitive":True,"type":"TYPE_UNSPECIFIED","grpcService":"grpcService"}},{"headers":[{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"},{"type":"TYPE_UNSPECIFIED","value":"value","key":"key"}],"method":{"grpcMethod":"grpcMethod","caseSensitive":True,"type":"TYPE_UNSPECIFIED","grpcService":"grpcService"}}]}],"updateTime":"updateTime","meshes":["meshes","meshes"],"labels":{"key":"labels"},"selfLink":"selfLink"}
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
                    ('grpcRouteId', 'grpc_route_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/grpcRoutes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_grpc_routes_list(client):
    """Test case for networkservices_projects_locations_grpc_routes_list

    
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
        path='/v1/{parent}/grpcRoutes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_http_routes_create(client):
    """Test case for networkservices_projects_locations_http_routes_create

    
    """
    body = {"gateways":["gateways","gateways"],"createTime":"createTime","name":"name","description":"description","hostnames":["hostnames","hostnames"],"rules":[{"action":{"redirect":{"portRedirect":2,"httpsRedirect":True,"hostRedirect":"hostRedirect","pathRedirect":"pathRedirect","prefixRewrite":"prefixRewrite","responseCode":"RESPONSE_CODE_UNSPECIFIED","stripQuery":True},"retryPolicy":{"numRetries":9,"perTryTimeout":"perTryTimeout","retryConditions":["retryConditions","retryConditions"]},"corsPolicy":{"allowMethods":["allowMethods","allowMethods"],"allowHeaders":["allowHeaders","allowHeaders"],"exposeHeaders":["exposeHeaders","exposeHeaders"],"maxAge":"maxAge","allowOriginRegexes":["allowOriginRegexes","allowOriginRegexes"],"disabled":True,"allowCredentials":True,"allowOrigins":["allowOrigins","allowOrigins"]},"destinations":[{"requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"weight":0,"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"serviceName":"serviceName"},{"requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"weight":0,"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"serviceName":"serviceName"}],"requestMirrorPolicy":{"mirrorPercent":7.0614014,"destination":{"requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"weight":0,"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"serviceName":"serviceName"}},"statefulSessionAffinity":{"cookieTtl":"cookieTtl"},"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"timeout":"timeout","requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"idleTimeout":"idleTimeout","directResponse":{"stringBody":"stringBody","bytesBody":"bytesBody","status":6},"faultInjectionPolicy":{"delay":{"fixedDelay":"fixedDelay","percentage":5},"abort":{"httpStatus":1,"percentage":5}},"urlRewrite":{"hostRewrite":"hostRewrite","pathPrefixRewrite":"pathPrefixRewrite"}},"matches":[{"headers":[{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True},{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True}],"queryParameters":[{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"},{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"}],"ignoreCase":True,"fullPathMatch":"fullPathMatch","prefixMatch":"prefixMatch","regexMatch":"regexMatch"},{"headers":[{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True},{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True}],"queryParameters":[{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"},{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"}],"ignoreCase":True,"fullPathMatch":"fullPathMatch","prefixMatch":"prefixMatch","regexMatch":"regexMatch"}]},{"action":{"redirect":{"portRedirect":2,"httpsRedirect":True,"hostRedirect":"hostRedirect","pathRedirect":"pathRedirect","prefixRewrite":"prefixRewrite","responseCode":"RESPONSE_CODE_UNSPECIFIED","stripQuery":True},"retryPolicy":{"numRetries":9,"perTryTimeout":"perTryTimeout","retryConditions":["retryConditions","retryConditions"]},"corsPolicy":{"allowMethods":["allowMethods","allowMethods"],"allowHeaders":["allowHeaders","allowHeaders"],"exposeHeaders":["exposeHeaders","exposeHeaders"],"maxAge":"maxAge","allowOriginRegexes":["allowOriginRegexes","allowOriginRegexes"],"disabled":True,"allowCredentials":True,"allowOrigins":["allowOrigins","allowOrigins"]},"destinations":[{"requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"weight":0,"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"serviceName":"serviceName"},{"requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"weight":0,"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"serviceName":"serviceName"}],"requestMirrorPolicy":{"mirrorPercent":7.0614014,"destination":{"requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"weight":0,"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"serviceName":"serviceName"}},"statefulSessionAffinity":{"cookieTtl":"cookieTtl"},"responseHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"timeout":"timeout","requestHeaderModifier":{"add":{"key":"add"},"set":{"key":"set"},"remove":["remove","remove"]},"idleTimeout":"idleTimeout","directResponse":{"stringBody":"stringBody","bytesBody":"bytesBody","status":6},"faultInjectionPolicy":{"delay":{"fixedDelay":"fixedDelay","percentage":5},"abort":{"httpStatus":1,"percentage":5}},"urlRewrite":{"hostRewrite":"hostRewrite","pathPrefixRewrite":"pathPrefixRewrite"}},"matches":[{"headers":[{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True},{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True}],"queryParameters":[{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"},{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"}],"ignoreCase":True,"fullPathMatch":"fullPathMatch","prefixMatch":"prefixMatch","regexMatch":"regexMatch"},{"headers":[{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True},{"rangeMatch":{"start":2,"end":3},"presentMatch":True,"exactMatch":"exactMatch","suffixMatch":"suffixMatch","header":"header","prefixMatch":"prefixMatch","regexMatch":"regexMatch","invertMatch":True}],"queryParameters":[{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"},{"presentMatch":True,"exactMatch":"exactMatch","queryParameter":"queryParameter","regexMatch":"regexMatch"}],"ignoreCase":True,"fullPathMatch":"fullPathMatch","prefixMatch":"prefixMatch","regexMatch":"regexMatch"}]}],"updateTime":"updateTime","meshes":["meshes","meshes"],"labels":{"key":"labels"},"selfLink":"selfLink"}
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
                    ('httpRouteId', 'http_route_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/httpRoutes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_http_routes_list(client):
    """Test case for networkservices_projects_locations_http_routes_list

    
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
        path='/v1/{parent}/httpRoutes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_lb_route_extensions_create(client):
    """Test case for networkservices_projects_locations_lb_route_extensions_create

    
    """
    body = {"createTime":"createTime","name":"name","description":"description","loadBalancingScheme":"LOAD_BALANCING_SCHEME_UNSPECIFIED","updateTime":"updateTime","forwardingRules":["forwardingRules","forwardingRules"],"extensionChains":[{"extensions":[{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"},{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"}],"matchCondition":{"celExpression":"celExpression"},"name":"name"},{"extensions":[{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"},{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"}],"matchCondition":{"celExpression":"celExpression"},"name":"name"}],"labels":{"key":"labels"}}
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
                    ('lbRouteExtensionId', 'lb_route_extension_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/lbRouteExtensions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_lb_route_extensions_list(client):
    """Test case for networkservices_projects_locations_lb_route_extensions_list

    
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
        path='/v1/{parent}/lbRouteExtensions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_lb_traffic_extensions_create(client):
    """Test case for networkservices_projects_locations_lb_traffic_extensions_create

    
    """
    body = {"createTime":"createTime","name":"name","description":"description","loadBalancingScheme":"LOAD_BALANCING_SCHEME_UNSPECIFIED","updateTime":"updateTime","forwardingRules":["forwardingRules","forwardingRules"],"extensionChains":[{"extensions":[{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"},{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"}],"matchCondition":{"celExpression":"celExpression"},"name":"name"},{"extensions":[{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"},{"failOpen":True,"service":"service","authority":"authority","name":"name","forwardHeaders":["forwardHeaders","forwardHeaders"],"supportedEvents":["EVENT_TYPE_UNSPECIFIED","EVENT_TYPE_UNSPECIFIED"],"timeout":"timeout"}],"matchCondition":{"celExpression":"celExpression"},"name":"name"}],"labels":{"key":"labels"}}
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
                    ('lbTrafficExtensionId', 'lb_traffic_extension_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/lbTrafficExtensions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_lb_traffic_extensions_list(client):
    """Test case for networkservices_projects_locations_lb_traffic_extensions_list

    
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
        path='/v1/{parent}/lbTrafficExtensions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_list(client):
    """Test case for networkservices_projects_locations_list

    
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


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_meshes_create(client):
    """Test case for networkservices_projects_locations_meshes_create

    
    """
    body = {"envoyHeaders":"ENVOY_HEADERS_UNSPECIFIED","createTime":"createTime","name":"name","description":"description","updateTime":"updateTime","interceptionPort":0,"labels":{"key":"labels"},"selfLink":"selfLink"}
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
                    ('meshId', 'mesh_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/meshes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_meshes_list(client):
    """Test case for networkservices_projects_locations_meshes_list

    
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
        path='/v1/{parent}/meshes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_operations_cancel(client):
    """Test case for networkservices_projects_locations_operations_cancel

    
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

async def test_networkservices_projects_locations_operations_list(client):
    """Test case for networkservices_projects_locations_operations_list

    
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

async def test_networkservices_projects_locations_service_bindings_create(client):
    """Test case for networkservices_projects_locations_service_bindings_create

    
    """
    body = {"createTime":"createTime","service":"service","name":"name","description":"description","updateTime":"updateTime","serviceId":"serviceId","labels":{"key":"labels"}}
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
                    ('serviceBindingId', 'service_binding_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/serviceBindings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_service_bindings_list(client):
    """Test case for networkservices_projects_locations_service_bindings_list

    
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
        path='/v1/{parent}/serviceBindings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_service_lb_policies_create(client):
    """Test case for networkservices_projects_locations_service_lb_policies_create

    
    """
    body = {"loadBalancingAlgorithm":"LOAD_BALANCING_ALGORITHM_UNSPECIFIED","autoCapacityDrain":{"enable":True},"failoverConfig":{"failoverHealthThreshold":0},"createTime":"createTime","name":"name","description":"description","updateTime":"updateTime","labels":{"key":"labels"}}
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
                    ('serviceLbPolicyId', 'service_lb_policy_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/serviceLbPolicies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_service_lb_policies_get_iam_policy(client):
    """Test case for networkservices_projects_locations_service_lb_policies_get_iam_policy

    
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

async def test_networkservices_projects_locations_service_lb_policies_list(client):
    """Test case for networkservices_projects_locations_service_lb_policies_list

    
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
        path='/v1/{parent}/serviceLbPolicies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_service_lb_policies_set_iam_policy(client):
    """Test case for networkservices_projects_locations_service_lb_policies_set_iam_policy

    
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

async def test_networkservices_projects_locations_service_lb_policies_test_iam_permissions(client):
    """Test case for networkservices_projects_locations_service_lb_policies_test_iam_permissions

    
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

async def test_networkservices_projects_locations_tcp_routes_create(client):
    """Test case for networkservices_projects_locations_tcp_routes_create

    
    """
    body = {"gateways":["gateways","gateways"],"createTime":"createTime","name":"name","description":"description","rules":[{"action":{"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout","originalDestination":True},"matches":[{"address":"address","port":"port"},{"address":"address","port":"port"}]},{"action":{"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout","originalDestination":True},"matches":[{"address":"address","port":"port"},{"address":"address","port":"port"}]}],"updateTime":"updateTime","meshes":["meshes","meshes"],"labels":{"key":"labels"},"selfLink":"selfLink"}
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
                    ('tcpRouteId', 'tcp_route_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/tcpRoutes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_tcp_routes_list(client):
    """Test case for networkservices_projects_locations_tcp_routes_list

    
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
        path='/v1/{parent}/tcpRoutes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_tls_routes_create(client):
    """Test case for networkservices_projects_locations_tls_routes_create

    
    """
    body = {"gateways":["gateways","gateways"],"createTime":"createTime","name":"name","description":"description","rules":[{"action":{"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout"},"matches":[{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]},{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]}]},{"action":{"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout"},"matches":[{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]},{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]}]}],"updateTime":"updateTime","meshes":["meshes","meshes"],"labels":{"key":"labels"},"selfLink":"selfLink"}
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
                    ('tlsRouteId', 'tls_route_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/tlsRoutes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_tls_routes_delete(client):
    """Test case for networkservices_projects_locations_tls_routes_delete

    
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
                    ('requestId', 'request_id_example')]
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

async def test_networkservices_projects_locations_tls_routes_get(client):
    """Test case for networkservices_projects_locations_tls_routes_get

    
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

async def test_networkservices_projects_locations_tls_routes_list(client):
    """Test case for networkservices_projects_locations_tls_routes_list

    
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
        path='/v1/{parent}/tlsRoutes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_networkservices_projects_locations_tls_routes_patch(client):
    """Test case for networkservices_projects_locations_tls_routes_patch

    
    """
    body = {"gateways":["gateways","gateways"],"createTime":"createTime","name":"name","description":"description","rules":[{"action":{"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout"},"matches":[{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]},{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]}]},{"action":{"destinations":[{"weight":0,"serviceName":"serviceName"},{"weight":0,"serviceName":"serviceName"}],"idleTimeout":"idleTimeout"},"matches":[{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]},{"alpn":["alpn","alpn"],"sniHost":["sniHost","sniHost"]}]}],"updateTime":"updateTime","meshes":["meshes","meshes"],"labels":{"key":"labels"},"selfLink":"selfLink"}
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

