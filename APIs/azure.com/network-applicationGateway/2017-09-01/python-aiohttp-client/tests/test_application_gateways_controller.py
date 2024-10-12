# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_gateway import ApplicationGateway
from openapi_server.models.application_gateway_available_ssl_predefined_policies import ApplicationGatewayAvailableSslPredefinedPolicies
from openapi_server.models.application_gateway_available_waf_rule_sets_result import ApplicationGatewayAvailableWafRuleSetsResult
from openapi_server.models.application_gateway_backend_health import ApplicationGatewayBackendHealth
from openapi_server.models.application_gateway_list_result import ApplicationGatewayListResult
from openapi_server.models.application_gateways_update_tags_request import ApplicationGatewaysUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_application_gateways_backend_health(client):
    """Test case for application_gateways_backend_health

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}/backendhealth'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_create_or_update(client):
    """Test case for application_gateways_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"sslCertificates":[{"name":"name","etag":"etag","type":"type","properties":{"password":"password","data":"data","provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","type":"type","properties":{"password":"password","data":"data","provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"resourceGuid":"resourceGuid","sslPolicy":{"policyName":"AppGwSslPolicy20150501","cipherSuites":["TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384","TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"],"policyType":"Predefined","disabledSslProtocols":["TLSv1_0","TLSv1_0"]},"backendHttpSettingsCollection":[{"name":"name","etag":"etag","type":"type","properties":{"affinityCookieName":"affinityCookieName","hostName":"hostName","probeEnabled":True,"cookieBasedAffinity":"Enabled","provisioningState":"provisioningState","pickHostNameFromBackendAddress":True,"probe":"{}","authenticationCertificates":["{}","{}"],"path":"path","protocol":"Http","port":6,"connectionDraining":{"drainTimeoutInSec":289,"enabled":True},"requestTimeout":1}},{"name":"name","etag":"etag","type":"type","properties":{"affinityCookieName":"affinityCookieName","hostName":"hostName","probeEnabled":True,"cookieBasedAffinity":"Enabled","provisioningState":"provisioningState","pickHostNameFromBackendAddress":True,"probe":"{}","authenticationCertificates":["{}","{}"],"path":"path","protocol":"Http","port":6,"connectionDraining":{"drainTimeoutInSec":289,"enabled":True},"requestTimeout":1}}],"redirectConfigurations":[{"name":"name","etag":"etag","type":"type","properties":{"targetListener":"{}","pathRules":["{}","{}"],"urlPathMaps":["{}","{}"],"includePath":True,"redirectType":"Permanent","targetUrl":"targetUrl","requestRoutingRules":["{}","{}"],"includeQueryString":True}},{"name":"name","etag":"etag","type":"type","properties":{"targetListener":"{}","pathRules":["{}","{}"],"urlPathMaps":["{}","{}"],"includePath":True,"redirectType":"Permanent","targetUrl":"targetUrl","requestRoutingRules":["{}","{}"],"includeQueryString":True}}],"urlPathMaps":[{"name":"name","etag":"etag","type":"type","properties":{"defaultBackendHttpSettings":"{}","defaultRedirectConfiguration":"{}","pathRules":[{"name":"name","etag":"etag","type":"type","properties":{"redirectConfiguration":"{}","paths":["paths","paths"],"backendAddressPool":"{}","provisioningState":"provisioningState","backendHttpSettings":"{}"}},{"name":"name","etag":"etag","type":"type","properties":{"redirectConfiguration":"{}","paths":["paths","paths"],"backendAddressPool":"{}","provisioningState":"provisioningState","backendHttpSettings":"{}"}}],"defaultBackendAddressPool":"{}","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","type":"type","properties":{"defaultBackendHttpSettings":"{}","defaultRedirectConfiguration":"{}","pathRules":[{"name":"name","etag":"etag","type":"type","properties":{"redirectConfiguration":"{}","paths":["paths","paths"],"backendAddressPool":"{}","provisioningState":"provisioningState","backendHttpSettings":"{}"}},{"name":"name","etag":"etag","type":"type","properties":{"redirectConfiguration":"{}","paths":["paths","paths"],"backendAddressPool":"{}","provisioningState":"provisioningState","backendHttpSettings":"{}"}}],"defaultBackendAddressPool":"{}","provisioningState":"provisioningState"}}],"provisioningState":"provisioningState","frontendPorts":[{"name":"name","etag":"etag","type":"type","properties":{"port":5,"provisioningState":"provisioningState"}},{"name":"name","etag":"etag","type":"type","properties":{"port":5,"provisioningState":"provisioningState"}}],"requestRoutingRules":[{"name":"name","etag":"etag","type":"type","properties":{"redirectConfiguration":"{}","httpListener":"{}","ruleType":"Basic","backendAddressPool":"{}","provisioningState":"provisioningState","urlPathMap":"{}","backendHttpSettings":"{}"}},{"name":"name","etag":"etag","type":"type","properties":{"redirectConfiguration":"{}","httpListener":"{}","ruleType":"Basic","backendAddressPool":"{}","provisioningState":"provisioningState","urlPathMap":"{}","backendHttpSettings":"{}"}}],"webApplicationFirewallConfiguration":{"firewallMode":"Detection","ruleSetVersion":"ruleSetVersion","ruleSetType":"ruleSetType","disabledRuleGroups":[{"ruleGroupName":"ruleGroupName","rules":[2,2]},{"ruleGroupName":"ruleGroupName","rules":[2,2]}],"enabled":True},"authenticationCertificates":[{"name":"name","etag":"etag","type":"type","properties":{"data":"data","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","type":"type","properties":{"data":"data","provisioningState":"provisioningState"}}],"gatewayIPConfigurations":[{"name":"name","etag":"etag","type":"type","properties":{"subnet":"{}","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","type":"type","properties":{"subnet":"{}","provisioningState":"provisioningState"}}],"probes":[{"name":"name","etag":"etag","type":"type","properties":{"path":"path","protocol":"Http","host":"host","match":{"statusCodes":["statusCodes","statusCodes"],"body":"body"},"unhealthyThreshold":9,"interval":5,"minServers":2,"pickHostNameFromBackendHttpSettings":True,"provisioningState":"provisioningState","timeout":7}},{"name":"name","etag":"etag","type":"type","properties":{"path":"path","protocol":"Http","host":"host","match":{"statusCodes":["statusCodes","statusCodes"],"body":"body"},"unhealthyThreshold":9,"interval":5,"minServers":2,"pickHostNameFromBackendHttpSettings":True,"provisioningState":"provisioningState","timeout":7}}],"frontendIPConfigurations":[{"name":"name","etag":"etag","type":"type","properties":{"subnet":"{}","privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":"{}"}},{"name":"name","etag":"etag","type":"type","properties":{"subnet":"{}","privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":"{}"}}],"operationalState":"Stopped","backendAddressPools":[{"name":"name","etag":"etag","type":"type","properties":{"backendIPConfigurations":["{}","{}"],"provisioningState":"provisioningState","backendAddresses":[{"fqdn":"fqdn","ipAddress":"ipAddress"},{"fqdn":"fqdn","ipAddress":"ipAddress"}]}},{"name":"name","etag":"etag","type":"type","properties":{"backendIPConfigurations":["{}","{}"],"provisioningState":"provisioningState","backendAddresses":[{"fqdn":"fqdn","ipAddress":"ipAddress"},{"fqdn":"fqdn","ipAddress":"ipAddress"}]}}],"sku":{"tier":"Standard","name":"Standard_Small","capacity":3},"httpListeners":[{"name":"name","etag":"etag","type":"type","properties":{"hostName":"hostName","protocol":"Http","sslCertificate":"{}","frontendIPConfiguration":"{}","frontendPort":"{}","provisioningState":"provisioningState","requireServerNameIndication":True}},{"name":"name","etag":"etag","type":"type","properties":{"hostName":"hostName","protocol":"Http","sslCertificate":"{}","frontendIPConfiguration":"{}","frontendPort":"{}","provisioningState":"provisioningState","requireServerNameIndication":True}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_delete(client):
    """Test case for application_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_get(client):
    """Test case for application_gateways_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_get_ssl_predefined_policy(client):
    """Test case for application_gateways_get_ssl_predefined_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default/predefinedPolicies/{predefined_policy_name}'.format(subscription_id='subscription_id_example', predefined_policy_name='predefined_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_list(client):
    """Test case for application_gateways_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_list_all(client):
    """Test case for application_gateways_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/applicationGateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_list_available_ssl_options(client):
    """Test case for application_gateways_list_available_ssl_options

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_list_available_ssl_predefined_policies(client):
    """Test case for application_gateways_list_available_ssl_predefined_policies

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default/predefinedPolicies'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_list_available_waf_rule_sets(client):
    """Test case for application_gateways_list_available_waf_rule_sets

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/applicationGatewayAvailableWafRuleSets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_start(client):
    """Test case for application_gateways_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}/start'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_stop(client):
    """Test case for application_gateways_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}/stop'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_gateways_update_tags(client):
    """Test case for application_gateways_update_tags

    
    """
    parameters = openapi_server.ApplicationGatewaysUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/applicationGateways/{application_gateway_name}'.format(resource_group_name='resource_group_name_example', application_gateway_name='application_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

