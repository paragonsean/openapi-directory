# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.policies_list_response import PoliciesListResponse
from openapi_server.models.policies_patch_response import PoliciesPatchResponse
from openapi_server.models.policies_update_response import PoliciesUpdateResponse
from openapi_server.models.policy import Policy


pytestmark = pytest.mark.asyncio

async def test_dns_policies_create(client):
    """Test case for dns_policies_create

    
    """
    body = {"alternativeNameServerConfig":{"kind":"dns#policyAlternativeNameServerConfig","targetNameServers":[{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#policyAlternativeNameServerConfigTargetNameServer","ipv4Address":"ipv4Address"},{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#policyAlternativeNameServerConfigTargetNameServer","ipv4Address":"ipv4Address"}]},"kind":"dns#policy","enableInboundForwarding":True,"name":"name","description":"description","id":"id","enableLogging":True,"networks":[{"kind":"dns#policyNetwork","networkUrl":"networkUrl"},{"kind":"dns#policyNetwork","networkUrl":"networkUrl"}]}
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
        path='/dns/v1beta2/projects/{project}/policies'.format(project='project_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_policies_delete(client):
    """Test case for dns_policies_delete

    
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
        path='/dns/v1beta2/projects/{project}/policies/{policy}'.format(project='project_example', policy='policy_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_policies_get(client):
    """Test case for dns_policies_get

    
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
        path='/dns/v1beta2/projects/{project}/policies/{policy}'.format(project='project_example', policy='policy_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_policies_list(client):
    """Test case for dns_policies_list

    
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
        path='/dns/v1beta2/projects/{project}/policies'.format(project='project_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_policies_patch(client):
    """Test case for dns_policies_patch

    
    """
    body = {"alternativeNameServerConfig":{"kind":"dns#policyAlternativeNameServerConfig","targetNameServers":[{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#policyAlternativeNameServerConfigTargetNameServer","ipv4Address":"ipv4Address"},{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#policyAlternativeNameServerConfigTargetNameServer","ipv4Address":"ipv4Address"}]},"kind":"dns#policy","enableInboundForwarding":True,"name":"name","description":"description","id":"id","enableLogging":True,"networks":[{"kind":"dns#policyNetwork","networkUrl":"networkUrl"},{"kind":"dns#policyNetwork","networkUrl":"networkUrl"}]}
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
        path='/dns/v1beta2/projects/{project}/policies/{policy}'.format(project='project_example', policy='policy_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_policies_update(client):
    """Test case for dns_policies_update

    
    """
    body = {"alternativeNameServerConfig":{"kind":"dns#policyAlternativeNameServerConfig","targetNameServers":[{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#policyAlternativeNameServerConfigTargetNameServer","ipv4Address":"ipv4Address"},{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#policyAlternativeNameServerConfigTargetNameServer","ipv4Address":"ipv4Address"}]},"kind":"dns#policy","enableInboundForwarding":True,"name":"name","description":"description","id":"id","enableLogging":True,"networks":[{"kind":"dns#policyNetwork","networkUrl":"networkUrl"},{"kind":"dns#policyNetwork","networkUrl":"networkUrl"}]}
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
        path='/dns/v1beta2/projects/{project}/policies/{policy}'.format(project='project_example', policy='policy_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

