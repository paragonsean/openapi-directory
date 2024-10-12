# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_domain import CustomDomain
from openapi_server.models.list_custom_domains_response import ListCustomDomainsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_sites_response import ListSitesResponse
from openapi_server.models.operation import Operation
from openapi_server.models.site import Site
from openapi_server.models.undelete_custom_domain_request import UndeleteCustomDomainRequest


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_projects_sites_create(client):
    """Test case for firebasehosting_projects_sites_create

    
    """
    body = {"appId":"appId","name":"name","type":"TYPE_UNSPECIFIED","defaultUrl":"defaultUrl","labels":{"key":"labels"}}
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
                    ('siteId', 'site_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/sites'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_projects_sites_custom_domains_create(client):
    """Test case for firebasehosting_projects_sites_custom_domains_create

    
    """
    body = {"ownershipState":"OWNERSHIP_STATE_UNSPECIFIED","annotations":{"key":"annotations"},"reconciling":True,"cert":{"expireTime":"expireTime","createTime":"createTime","state":"CERT_STATE_UNSPECIFIED","type":"TYPE_UNSPECIFIED","issues":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"verification":{"dns":{"discovered":[{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}],"checkTime":"checkTime","desired":[{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}]},"http":{"path":"path","discovered":"discovered","lastCheckTime":"lastCheckTime","desired":"desired","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}}},"updateTime":"updateTime","redirectTarget":"redirectTarget","issues":[{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}],"labels":{"key":"labels"},"requiredDnsUpdates":{"discovered":[{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}],"checkTime":"checkTime","desired":[{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}},{"records":[{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"},{"domainName":"domainName","rdata":"rdata","type":"TYPE_UNSPECIFIED","requiredAction":"NONE"}],"domainName":"domainName","checkError":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"}}]},"expireTime":"expireTime","createTime":"createTime","deleteTime":"deleteTime","name":"name","etag":"etag","certPreference":"TYPE_UNSPECIFIED","hostState":"HOST_STATE_UNSPECIFIED"}
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
                    ('customDomainId', 'custom_domain_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/customDomains'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_projects_sites_custom_domains_list(client):
    """Test case for firebasehosting_projects_sites_custom_domains_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/customDomains'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_projects_sites_custom_domains_operations_list(client):
    """Test case for firebasehosting_projects_sites_custom_domains_operations_list

    
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
        path='/v1beta1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_projects_sites_custom_domains_undelete(client):
    """Test case for firebasehosting_projects_sites_custom_domains_undelete

    
    """
    body = {"validateOnly":True,"etag":"etag"}
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
        path='/v1beta1/{nameundelet}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_projects_sites_list(client):
    """Test case for firebasehosting_projects_sites_list

    
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
        path='/v1beta1/{parent}/sites'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

