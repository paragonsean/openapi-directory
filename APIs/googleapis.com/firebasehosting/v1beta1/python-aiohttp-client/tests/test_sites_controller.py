# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.clone_version_request import CloneVersionRequest
from openapi_server.models.domain import Domain
from openapi_server.models.list_channels_response import ListChannelsResponse
from openapi_server.models.list_domains_response import ListDomainsResponse
from openapi_server.models.list_releases_response import ListReleasesResponse
from openapi_server.models.list_version_files_response import ListVersionFilesResponse
from openapi_server.models.list_versions_response import ListVersionsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.populate_version_files_request import PopulateVersionFilesRequest
from openapi_server.models.populate_version_files_response import PopulateVersionFilesResponse
from openapi_server.models.release import Release
from openapi_server.models.version import Version


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_channels_create(client):
    """Test case for firebasehosting_sites_channels_create

    
    """
    body = {"expireTime":"expireTime","createTime":"createTime","release":{"releaseTime":"releaseTime","name":"name","releaseUser":{"imageUrl":"imageUrl","email":"email"},"message":"message","type":"TYPE_UNSPECIFIED","version":{"createTime":"createTime","deleteTime":"deleteTime","deleteUser":{"imageUrl":"imageUrl","email":"email"},"name":"name","createUser":{"imageUrl":"imageUrl","email":"email"},"finalizeUser":{"imageUrl":"imageUrl","email":"email"},"config":{"headers":[{"headers":{"key":"headers"},"regex":"regex","glob":"glob"},{"headers":{"key":"headers"},"regex":"regex","glob":"glob"}],"rewrites":[{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}},{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}}],"redirects":[{"regex":"regex","glob":"glob","location":"location","statusCode":0},{"regex":"regex","glob":"glob","location":"location","statusCode":0}],"appAssociation":"AUTO","cleanUrls":True,"trailingSlashBehavior":"TRAILING_SLASH_BEHAVIOR_UNSPECIFIED","i18n":{"root":"root"}},"fileCount":"fileCount","finalizeTime":"finalizeTime","versionBytes":"versionBytes","labels":{"key":"labels"},"status":"VERSION_STATUS_UNSPECIFIED"}},"name":"name","retainedReleaseCount":0,"updateTime":"updateTime","ttl":"ttl","url":"url","labels":{"key":"labels"}}
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
                    ('channelId', 'channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/channels'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_channels_list(client):
    """Test case for firebasehosting_sites_channels_list

    
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
        path='/v1beta1/{parent}/channels'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_domains_create(client):
    """Test case for firebasehosting_sites_domains_create

    
    """
    body = {"site":"site","domainName":"domainName","provisioning":{"dnsStatus":"DNS_STATUS_UNSPECIFIED","certChallengeDns":{"domainName":"domainName","token":"token"},"expectedIps":["expectedIps","expectedIps"],"certChallengeHttp":{"path":"path","token":"token"},"certStatus":"CERT_STATUS_UNSPECIFIED","discoveredIps":["discoveredIps","discoveredIps"],"dnsFetchTime":"dnsFetchTime","certChallengeDiscoveredTxt":["certChallengeDiscoveredTxt","certChallengeDiscoveredTxt"]},"updateTime":"updateTime","domainRedirect":{"domainName":"domainName","type":"REDIRECT_TYPE_UNSPECIFIED"},"status":"DOMAIN_STATUS_UNSPECIFIED"}
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
        path='/v1beta1/{parent}/domains'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_domains_list(client):
    """Test case for firebasehosting_sites_domains_list

    
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
        path='/v1beta1/{parent}/domains'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_domains_update(client):
    """Test case for firebasehosting_sites_domains_update

    
    """
    body = {"site":"site","domainName":"domainName","provisioning":{"dnsStatus":"DNS_STATUS_UNSPECIFIED","certChallengeDns":{"domainName":"domainName","token":"token"},"expectedIps":["expectedIps","expectedIps"],"certChallengeHttp":{"path":"path","token":"token"},"certStatus":"CERT_STATUS_UNSPECIFIED","discoveredIps":["discoveredIps","discoveredIps"],"dnsFetchTime":"dnsFetchTime","certChallengeDiscoveredTxt":["certChallengeDiscoveredTxt","certChallengeDiscoveredTxt"]},"updateTime":"updateTime","domainRedirect":{"domainName":"domainName","type":"REDIRECT_TYPE_UNSPECIFIED"},"status":"DOMAIN_STATUS_UNSPECIFIED"}
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
        method='PUT',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_releases_create(client):
    """Test case for firebasehosting_sites_releases_create

    
    """
    body = {"releaseTime":"releaseTime","name":"name","releaseUser":{"imageUrl":"imageUrl","email":"email"},"message":"message","type":"TYPE_UNSPECIFIED","version":{"createTime":"createTime","deleteTime":"deleteTime","deleteUser":{"imageUrl":"imageUrl","email":"email"},"name":"name","createUser":{"imageUrl":"imageUrl","email":"email"},"finalizeUser":{"imageUrl":"imageUrl","email":"email"},"config":{"headers":[{"headers":{"key":"headers"},"regex":"regex","glob":"glob"},{"headers":{"key":"headers"},"regex":"regex","glob":"glob"}],"rewrites":[{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}},{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}}],"redirects":[{"regex":"regex","glob":"glob","location":"location","statusCode":0},{"regex":"regex","glob":"glob","location":"location","statusCode":0}],"appAssociation":"AUTO","cleanUrls":True,"trailingSlashBehavior":"TRAILING_SLASH_BEHAVIOR_UNSPECIFIED","i18n":{"root":"root"}},"fileCount":"fileCount","finalizeTime":"finalizeTime","versionBytes":"versionBytes","labels":{"key":"labels"},"status":"VERSION_STATUS_UNSPECIFIED"}}
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
                    ('versionName', 'version_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/releases'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_releases_list(client):
    """Test case for firebasehosting_sites_releases_list

    
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
        path='/v1beta1/{parent}/releases'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_clone(client):
    """Test case for firebasehosting_sites_versions_clone

    
    """
    body = {"include":{"regexes":["regexes","regexes"]},"sourceVersion":"sourceVersion","exclude":{"regexes":["regexes","regexes"]},"finalize":True}
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
        path='/v1beta1/{parent}/versions:clone'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_create(client):
    """Test case for firebasehosting_sites_versions_create

    
    """
    body = {"createTime":"createTime","deleteTime":"deleteTime","deleteUser":{"imageUrl":"imageUrl","email":"email"},"name":"name","createUser":{"imageUrl":"imageUrl","email":"email"},"finalizeUser":{"imageUrl":"imageUrl","email":"email"},"config":{"headers":[{"headers":{"key":"headers"},"regex":"regex","glob":"glob"},{"headers":{"key":"headers"},"regex":"regex","glob":"glob"}],"rewrites":[{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}},{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}}],"redirects":[{"regex":"regex","glob":"glob","location":"location","statusCode":0},{"regex":"regex","glob":"glob","location":"location","statusCode":0}],"appAssociation":"AUTO","cleanUrls":True,"trailingSlashBehavior":"TRAILING_SLASH_BEHAVIOR_UNSPECIFIED","i18n":{"root":"root"}},"fileCount":"fileCount","finalizeTime":"finalizeTime","versionBytes":"versionBytes","labels":{"key":"labels"},"status":"VERSION_STATUS_UNSPECIFIED"}
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
                    ('sizeBytes', 'size_bytes_example'),
                    ('versionId', 'version_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/versions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_delete(client):
    """Test case for firebasehosting_sites_versions_delete

    
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
                    ('allowMissing', True),
                    ('etag', 'etag_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_files_list(client):
    """Test case for firebasehosting_sites_versions_files_list

    
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
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/files'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_get(client):
    """Test case for firebasehosting_sites_versions_get

    
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
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_list(client):
    """Test case for firebasehosting_sites_versions_list

    
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
        path='/v1beta1/{parent}/versions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_patch(client):
    """Test case for firebasehosting_sites_versions_patch

    
    """
    body = {"createTime":"createTime","deleteTime":"deleteTime","deleteUser":{"imageUrl":"imageUrl","email":"email"},"name":"name","createUser":{"imageUrl":"imageUrl","email":"email"},"finalizeUser":{"imageUrl":"imageUrl","email":"email"},"config":{"headers":[{"headers":{"key":"headers"},"regex":"regex","glob":"glob"},{"headers":{"key":"headers"},"regex":"regex","glob":"glob"}],"rewrites":[{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}},{"functionRegion":"functionRegion","path":"path","dynamicLinks":True,"regex":"regex","function":"function","glob":"glob","run":{"tag":"tag","region":"region","serviceId":"serviceId"}}],"redirects":[{"regex":"regex","glob":"glob","location":"location","statusCode":0},{"regex":"regex","glob":"glob","location":"location","statusCode":0}],"appAssociation":"AUTO","cleanUrls":True,"trailingSlashBehavior":"TRAILING_SLASH_BEHAVIOR_UNSPECIFIED","i18n":{"root":"root"}},"fileCount":"fileCount","finalizeTime":"finalizeTime","versionBytes":"versionBytes","labels":{"key":"labels"},"status":"VERSION_STATUS_UNSPECIFIED"}
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
                    ('updateMask', 'update_mask_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firebasehosting_sites_versions_populate_files(client):
    """Test case for firebasehosting_sites_versions_populate_files

    
    """
    body = {"files":{"key":"files"}}
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
        path='/v1beta1/{parentpopulate_file}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

