# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_chrome_policy_versions_v1_batch_delete_group_policies_request import GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_batch_inherit_org_unit_policies_request import GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_batch_modify_group_policies_request import GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_batch_modify_org_unit_policies_request import GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequest
from openapi_server.models.google_chrome_policy_versions_v1_define_certificate_request import GoogleChromePolicyVersionsV1DefineCertificateRequest
from openapi_server.models.google_chrome_policy_versions_v1_define_certificate_response import GoogleChromePolicyVersionsV1DefineCertificateResponse
from openapi_server.models.google_chrome_policy_versions_v1_define_network_request import GoogleChromePolicyVersionsV1DefineNetworkRequest
from openapi_server.models.google_chrome_policy_versions_v1_define_network_response import GoogleChromePolicyVersionsV1DefineNetworkResponse
from openapi_server.models.google_chrome_policy_versions_v1_list_group_priority_ordering_request import GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequest
from openapi_server.models.google_chrome_policy_versions_v1_list_group_priority_ordering_response import GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponse
from openapi_server.models.google_chrome_policy_versions_v1_list_policy_schemas_response import GoogleChromePolicyVersionsV1ListPolicySchemasResponse
from openapi_server.models.google_chrome_policy_versions_v1_policy_schema import GoogleChromePolicyVersionsV1PolicySchema
from openapi_server.models.google_chrome_policy_versions_v1_remove_certificate_request import GoogleChromePolicyVersionsV1RemoveCertificateRequest
from openapi_server.models.google_chrome_policy_versions_v1_remove_network_request import GoogleChromePolicyVersionsV1RemoveNetworkRequest
from openapi_server.models.google_chrome_policy_versions_v1_resolve_request import GoogleChromePolicyVersionsV1ResolveRequest
from openapi_server.models.google_chrome_policy_versions_v1_resolve_response import GoogleChromePolicyVersionsV1ResolveResponse
from openapi_server.models.google_chrome_policy_versions_v1_update_group_priority_ordering_request import GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequest


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_groups_batch_delete(client):
    """Test case for chromepolicy_customers_policies_groups_batch_delete

    
    """
    body = {"requests":[{"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"policySchema":"policySchema"},{"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"policySchema":"policySchema"}]}
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
        path='/v1/{customer}/policies/groups:batchDelete'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_groups_batch_modify(client):
    """Test case for chromepolicy_customers_policies_groups_batch_modify

    
    """
    body = {"requests":[{"policyValue":{"policySchema":"policySchema","value":{"key":""}},"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"updateMask":"updateMask"},{"policyValue":{"policySchema":"policySchema","value":{"key":""}},"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"updateMask":"updateMask"}]}
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
        path='/v1/{customer}/policies/groups:batchModify'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_groups_list_group_priority_ordering(client):
    """Test case for chromepolicy_customers_policies_groups_list_group_priority_ordering

    
    """
    body = {"policyNamespace":"policyNamespace","policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"policySchema":"policySchema"}
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
        path='/v1/{customer}/policies/groups:listGroupPriorityOrdering'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_groups_update_group_priority_ordering(client):
    """Test case for chromepolicy_customers_policies_groups_update_group_priority_ordering

    
    """
    body = {"policyNamespace":"policyNamespace","policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"groupIds":["groupIds","groupIds"],"policySchema":"policySchema"}
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
        path='/v1/{customer}/policies/groups:updateGroupPriorityOrdering'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_networks_define_certificate(client):
    """Test case for chromepolicy_customers_policies_networks_define_certificate

    
    """
    body = {"settings":[{"policySchema":"policySchema","value":{"key":""}},{"policySchema":"policySchema","value":{"key":""}}],"ceritificateName":"ceritificateName","certificate":"certificate","targetResource":"targetResource"}
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
        path='/v1/{customer}/policies/networks:defineCertificate'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_networks_define_network(client):
    """Test case for chromepolicy_customers_policies_networks_define_network

    
    """
    body = {"settings":[{"policySchema":"policySchema","value":{"key":""}},{"policySchema":"policySchema","value":{"key":""}}],"name":"name","targetResource":"targetResource"}
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
        path='/v1/{customer}/policies/networks:defineNetwork'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_networks_remove_certificate(client):
    """Test case for chromepolicy_customers_policies_networks_remove_certificate

    
    """
    body = {"targetResource":"targetResource","networkId":"networkId"}
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
        path='/v1/{customer}/policies/networks:removeCertificate'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_networks_remove_network(client):
    """Test case for chromepolicy_customers_policies_networks_remove_network

    
    """
    body = {"targetResource":"targetResource","networkId":"networkId"}
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
        path='/v1/{customer}/policies/networks:removeNetwork'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_orgunits_batch_inherit(client):
    """Test case for chromepolicy_customers_policies_orgunits_batch_inherit

    
    """
    body = {"requests":[{"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"policySchema":"policySchema"},{"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"policySchema":"policySchema"}]}
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
        path='/v1/{customer}/policies/orgunits:batchInherit'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_orgunits_batch_modify(client):
    """Test case for chromepolicy_customers_policies_orgunits_batch_modify

    
    """
    body = {"requests":[{"policyValue":{"policySchema":"policySchema","value":{"key":""}},"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"updateMask":"updateMask"},{"policyValue":{"policySchema":"policySchema","value":{"key":""}},"policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"updateMask":"updateMask"}]}
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
        path='/v1/{customer}/policies/orgunits:batchModify'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policies_resolve(client):
    """Test case for chromepolicy_customers_policies_resolve

    
    """
    body = {"policySchemaFilter":"policySchemaFilter","policyTargetKey":{"targetResource":"targetResource","additionalTargetKeys":{"key":"additionalTargetKeys"}},"pageSize":0,"pageToken":"pageToken"}
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
        path='/v1/{customer}/policies:resolve'.format(customer='customer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chromepolicy_customers_policy_schemas_get(client):
    """Test case for chromepolicy_customers_policy_schemas_get

    
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

async def test_chromepolicy_customers_policy_schemas_list(client):
    """Test case for chromepolicy_customers_policy_schemas_list

    
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
        path='/v1/{parent}/policySchemas'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

