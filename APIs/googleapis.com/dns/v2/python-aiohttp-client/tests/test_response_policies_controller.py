# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.response_policies_list_response import ResponsePoliciesListResponse
from openapi_server.models.response_policies_patch_response import ResponsePoliciesPatchResponse
from openapi_server.models.response_policies_update_response import ResponsePoliciesUpdateResponse
from openapi_server.models.response_policy import ResponsePolicy


pytestmark = pytest.mark.asyncio

async def test_dns_response_policies_create(client):
    """Test case for dns_response_policies_create

    
    """
    body = {"kind":"dns#responsePolicy","responsePolicyName":"responsePolicyName","description":"description","id":"id","networks":[{"kind":"dns#responsePolicyNetwork","networkUrl":"networkUrl"},{"kind":"dns#responsePolicyNetwork","networkUrl":"networkUrl"}],"gkeClusters":[{"gkeClusterName":"gkeClusterName","kind":"dns#responsePolicyGKECluster"},{"gkeClusterName":"gkeClusterName","kind":"dns#responsePolicyGKECluster"}],"labels":{"key":"labels"}}
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
        path='/dns/v2/projects/{project}/locations/{location}/responsePolicies'.format(project='project_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policies_delete(client):
    """Test case for dns_response_policies_delete

    
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
        path='/dns/v2/projects/{project}/locations/{location}/responsePolicies/{response_policy}'.format(project='project_example', location='location_example', response_policy='response_policy_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policies_get(client):
    """Test case for dns_response_policies_get

    
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
        path='/dns/v2/projects/{project}/locations/{location}/responsePolicies/{response_policy}'.format(project='project_example', location='location_example', response_policy='response_policy_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policies_list(client):
    """Test case for dns_response_policies_list

    
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
        path='/dns/v2/projects/{project}/locations/{location}/responsePolicies'.format(project='project_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policies_patch(client):
    """Test case for dns_response_policies_patch

    
    """
    body = {"kind":"dns#responsePolicy","responsePolicyName":"responsePolicyName","description":"description","id":"id","networks":[{"kind":"dns#responsePolicyNetwork","networkUrl":"networkUrl"},{"kind":"dns#responsePolicyNetwork","networkUrl":"networkUrl"}],"gkeClusters":[{"gkeClusterName":"gkeClusterName","kind":"dns#responsePolicyGKECluster"},{"gkeClusterName":"gkeClusterName","kind":"dns#responsePolicyGKECluster"}],"labels":{"key":"labels"}}
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
        path='/dns/v2/projects/{project}/locations/{location}/responsePolicies/{response_policy}'.format(project='project_example', location='location_example', response_policy='response_policy_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_response_policies_update(client):
    """Test case for dns_response_policies_update

    
    """
    body = {"kind":"dns#responsePolicy","responsePolicyName":"responsePolicyName","description":"description","id":"id","networks":[{"kind":"dns#responsePolicyNetwork","networkUrl":"networkUrl"},{"kind":"dns#responsePolicyNetwork","networkUrl":"networkUrl"}],"gkeClusters":[{"gkeClusterName":"gkeClusterName","kind":"dns#responsePolicyGKECluster"},{"gkeClusterName":"gkeClusterName","kind":"dns#responsePolicyGKECluster"}],"labels":{"key":"labels"}}
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
        path='/dns/v2/projects/{project}/locations/{location}/responsePolicies/{response_policy}'.format(project='project_example', location='location_example', response_policy='response_policy_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

