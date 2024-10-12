# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_orgpolicy_v2_list_constraints_response import GoogleCloudOrgpolicyV2ListConstraintsResponse
from openapi_server.models.google_cloud_orgpolicy_v2_list_policies_response import GoogleCloudOrgpolicyV2ListPoliciesResponse
from openapi_server.models.google_cloud_orgpolicy_v2_policy import GoogleCloudOrgpolicyV2Policy


pytestmark = pytest.mark.asyncio

async def test_orgpolicy_projects_constraints_list(client):
    """Test case for orgpolicy_projects_constraints_list

    
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
        path='/v2/{parent}/constraints'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgpolicy_projects_policies_create(client):
    """Test case for orgpolicy_projects_policies_create

    
    """
    body = {"dryRunSpec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"},"name":"name","alternate":{"launch":"launch","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}},"etag":"etag","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}}
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
        path='/v2/{parent}/policies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgpolicy_projects_policies_delete(client):
    """Test case for orgpolicy_projects_policies_delete

    
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
                    ('etag', 'etag_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgpolicy_projects_policies_get(client):
    """Test case for orgpolicy_projects_policies_get

    
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgpolicy_projects_policies_get_effective_policy(client):
    """Test case for orgpolicy_projects_policies_get_effective_policy

    
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
        path='/v2/{nameget_effective_polic}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgpolicy_projects_policies_list(client):
    """Test case for orgpolicy_projects_policies_list

    
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
        path='/v2/{parent}/policies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgpolicy_projects_policies_patch(client):
    """Test case for orgpolicy_projects_policies_patch

    
    """
    body = {"dryRunSpec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"},"name":"name","alternate":{"launch":"launch","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}},"etag":"etag","spec":{"inheritFromParent":True,"reset":True,"etag":"etag","rules":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"values":{"allowedValues":["allowedValues","allowedValues"],"deniedValues":["deniedValues","deniedValues"]},"allowAll":True,"enforce":True,"denyAll":True}],"updateTime":"updateTime"}}
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
        path='/v2/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

