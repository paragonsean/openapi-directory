# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_browser_dlp_rule import GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_list_browser_dlp_rules_response import GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_list_partner_tenants_response import GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_list_proxy_configs_response import GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_partner_tenant import GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant
from openapi_server.models.google_cloud_beyondcorp_partnerservices_v1alpha_proxy_config import GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig
from openapi_server.models.google_cloud_beyondcorp_saasplatform_subscriptions_v1alpha_list_subscriptions_response import GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse
from openapi_server.models.google_cloud_beyondcorp_saasplatform_subscriptions_v1alpha_subscription import GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_create(client):
    """Test case for beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_create

    
    """
    body = {"ruleSetting":{"type":"type","value":{"key":""}},"name":"name","group":{"id":"id","email":"email"}}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/browserDlpRules'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_list(client):
    """Test case for beyondcorp_organizations_locations_global_partner_tenants_browser_dlp_rules_list

    
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
        path='/v1alpha/{parent}/browserDlpRules'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_global_partner_tenants_create(client):
    """Test case for beyondcorp_organizations_locations_global_partner_tenants_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","partnerMetadata":{"partnerTenantId":"partnerTenantId","internalTenantId":"internalTenantId"},"updateTime":"updateTime","group":{"id":"id","email":"email"}}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/partnerTenants'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_global_partner_tenants_list(client):
    """Test case for beyondcorp_organizations_locations_global_partner_tenants_list

    
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
        path='/v1alpha/{parent}/partnerTenants'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_create(client):
    """Test case for beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_create

    
    """
    body = {"encryptionInfo":{"encryptionSaEmail":"encryptionSaEmail","jwk":"jwk"},"transportInfo":{"sslDecryptCaCertPem":"sslDecryptCaCertPem","serverCaCertPem":"serverCaCertPem"},"routingInfo":{"pacUri":"pacUri"},"createTime":"createTime","displayName":"displayName","name":"name","proxyUri":"proxyUri","updateTime":"updateTime"}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/proxyConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_list(client):
    """Test case for beyondcorp_organizations_locations_global_partner_tenants_proxy_configs_list

    
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
        path='/v1alpha/{parent}/proxyConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_subscriptions_create(client):
    """Test case for beyondcorp_organizations_locations_subscriptions_create

    
    """
    body = {"createTime":"createTime","name":"name","startTime":"startTime","endTime":"endTime","state":"STATE_UNSPECIFIED","autoRenewEnabled":True,"sku":"SKU_UNSPECIFIED","type":"TYPE_UNSPECIFIED","seatCount":"seatCount"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/subscriptions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_beyondcorp_organizations_locations_subscriptions_list(client):
    """Test case for beyondcorp_organizations_locations_subscriptions_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{parent}/subscriptions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

