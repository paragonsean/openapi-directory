# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.container import Container
from openapi_server.models.container_version import ContainerVersion
from openapi_server.models.create_container_version_request_version_options import CreateContainerVersionRequestVersionOptions
from openapi_server.models.create_container_version_response import CreateContainerVersionResponse
from openapi_server.models.environment import Environment
from openapi_server.models.folder import Folder
from openapi_server.models.folder_entities import FolderEntities
from openapi_server.models.list_account_users_response import ListAccountUsersResponse
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server.models.list_container_versions_response import ListContainerVersionsResponse
from openapi_server.models.list_containers_response import ListContainersResponse
from openapi_server.models.list_environments_response import ListEnvironmentsResponse
from openapi_server.models.list_folders_response import ListFoldersResponse
from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.list_triggers_response import ListTriggersResponse
from openapi_server.models.list_variables_response import ListVariablesResponse
from openapi_server.models.publish_container_version_response import PublishContainerVersionResponse
from openapi_server.models.tag import Tag
from openapi_server.models.trigger import Trigger
from openapi_server.models.user_access import UserAccess
from openapi_server.models.variable import Variable


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_create(client):
    """Test case for tagmanager_accounts_containers_create

    
    """
    body = {"accountId":"accountId","usageContext":["web","web"],"notes":"notes","timeZoneId":"timeZoneId","domainName":["domainName","domainName"],"enabledBuiltInVariable":["pageUrl","pageUrl"],"fingerprint":"fingerprint","name":"name","timeZoneCountryId":"timeZoneCountryId","containerId":"containerId","publicId":"publicId"}
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
        path='/tagmanager/v1/accounts/{account_id}/containers'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_delete(client):
    """Test case for tagmanager_accounts_containers_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_environments_create(client):
    """Test case for tagmanager_accounts_containers_environments_create

    
    """
    body = {"accountId":"accountId","enableDebug":True,"environmentId":"environmentId","authorizationCode":"authorizationCode","fingerprint":"fingerprint","name":"name","description":"description","containerVersionId":"containerVersionId","containerId":"containerId","type":"user","authorizationTimestampMs":"authorizationTimestampMs","url":"url"}
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/environments'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_environments_delete(client):
    """Test case for tagmanager_accounts_containers_environments_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/environments/{environment_id}'.format(account_id='account_id_example', container_id='container_id_example', environment_id='environment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_environments_get(client):
    """Test case for tagmanager_accounts_containers_environments_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/environments/{environment_id}'.format(account_id='account_id_example', container_id='container_id_example', environment_id='environment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_environments_list(client):
    """Test case for tagmanager_accounts_containers_environments_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/environments'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_environments_update(client):
    """Test case for tagmanager_accounts_containers_environments_update

    
    """
    body = {"accountId":"accountId","enableDebug":True,"environmentId":"environmentId","authorizationCode":"authorizationCode","fingerprint":"fingerprint","name":"name","description":"description","containerVersionId":"containerVersionId","containerId":"containerId","type":"user","authorizationTimestampMs":"authorizationTimestampMs","url":"url"}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/environments/{environment_id}'.format(account_id='account_id_example', container_id='container_id_example', environment_id='environment_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_folders_create(client):
    """Test case for tagmanager_accounts_containers_folders_create

    
    """
    body = {"accountId":"accountId","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId"}
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/folders'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_folders_delete(client):
    """Test case for tagmanager_accounts_containers_folders_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/folders/{folder_id}'.format(account_id='account_id_example', container_id='container_id_example', folder_id='folder_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_folders_entities_list(client):
    """Test case for tagmanager_accounts_containers_folders_entities_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/folders/{folder_id}/entities'.format(account_id='account_id_example', container_id='container_id_example', folder_id='folder_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_folders_get(client):
    """Test case for tagmanager_accounts_containers_folders_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/folders/{folder_id}'.format(account_id='account_id_example', container_id='container_id_example', folder_id='folder_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_folders_list(client):
    """Test case for tagmanager_accounts_containers_folders_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/folders'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_folders_update(client):
    """Test case for tagmanager_accounts_containers_folders_update

    
    """
    body = {"accountId":"accountId","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId"}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/folders/{folder_id}'.format(account_id='account_id_example', container_id='container_id_example', folder_id='folder_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_get(client):
    """Test case for tagmanager_accounts_containers_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_list(client):
    """Test case for tagmanager_accounts_containers_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_move_folders_update(client):
    """Test case for tagmanager_accounts_containers_move_folders_update

    
    """
    body = {"accountId":"accountId","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId"}
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
                    ('tagId', ['tag_id_example']),
                    ('triggerId', ['trigger_id_example']),
                    ('variableId', ['variable_id_example'])]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/move_folders/{folder_id}'.format(account_id='account_id_example', container_id='container_id_example', folder_id='folder_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_reauthorize_environments_update(client):
    """Test case for tagmanager_accounts_containers_reauthorize_environments_update

    
    """
    body = {"accountId":"accountId","enableDebug":True,"environmentId":"environmentId","authorizationCode":"authorizationCode","fingerprint":"fingerprint","name":"name","description":"description","containerVersionId":"containerVersionId","containerId":"containerId","type":"user","authorizationTimestampMs":"authorizationTimestampMs","url":"url"}
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/reauthorize_environments/{environment_id}'.format(account_id='account_id_example', container_id='container_id_example', environment_id='environment_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_tags_create(client):
    """Test case for tagmanager_accounts_containers_tags_create

    
    """
    body = {"paused":True,"notes":"notes","firingRuleId":["firingRuleId","firingRuleId"],"tagFiringOption":"unlimited","liveOnly":True,"parentFolderId":"parentFolderId","tagId":"tagId","priority":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"type","setupTag":[{"stopOnSetupFailure":True,"tagName":"tagName"},{"stopOnSetupFailure":True,"tagName":"tagName"}],"blockingTriggerId":["blockingTriggerId","blockingTriggerId"],"accountId":"accountId","blockingRuleId":["blockingRuleId","blockingRuleId"],"teardownTag":[{"stopTeardownOnFailure":True,"tagName":"tagName"},{"stopTeardownOnFailure":True,"tagName":"tagName"}],"firingTriggerId":["firingTriggerId","firingTriggerId"],"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","containerId":"containerId"}
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/tags'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_tags_delete(client):
    """Test case for tagmanager_accounts_containers_tags_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/tags/{tag_id}'.format(account_id='account_id_example', container_id='container_id_example', tag_id='tag_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_tags_get(client):
    """Test case for tagmanager_accounts_containers_tags_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/tags/{tag_id}'.format(account_id='account_id_example', container_id='container_id_example', tag_id='tag_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_tags_list(client):
    """Test case for tagmanager_accounts_containers_tags_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/tags'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_tags_update(client):
    """Test case for tagmanager_accounts_containers_tags_update

    
    """
    body = {"paused":True,"notes":"notes","firingRuleId":["firingRuleId","firingRuleId"],"tagFiringOption":"unlimited","liveOnly":True,"parentFolderId":"parentFolderId","tagId":"tagId","priority":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"type","setupTag":[{"stopOnSetupFailure":True,"tagName":"tagName"},{"stopOnSetupFailure":True,"tagName":"tagName"}],"blockingTriggerId":["blockingTriggerId","blockingTriggerId"],"accountId":"accountId","blockingRuleId":["blockingRuleId","blockingRuleId"],"teardownTag":[{"stopTeardownOnFailure":True,"tagName":"tagName"},{"stopTeardownOnFailure":True,"tagName":"tagName"}],"firingTriggerId":["firingTriggerId","firingTriggerId"],"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","containerId":"containerId"}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/tags/{tag_id}'.format(account_id='account_id_example', container_id='container_id_example', tag_id='tag_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_triggers_create(client):
    """Test case for tagmanager_accounts_containers_triggers_create

    
    """
    body = {"maxTimerLengthSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visibilitySelector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTags":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parentFolderId":"parentFolderId","checkValidation":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visiblePercentageMax":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"pageview","visiblePercentageMin":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","limit":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"eventName":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"totalTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"verticalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"selector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"containerId":"containerId","customEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"uniqueTriggerId":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTagsTimeout":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"autoEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"triggerId":"triggerId","filter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"accountId":"accountId","horizontalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"name":"name","interval":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"continuousTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"intervalSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}}
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/triggers'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_triggers_delete(client):
    """Test case for tagmanager_accounts_containers_triggers_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/triggers/{trigger_id}'.format(account_id='account_id_example', container_id='container_id_example', trigger_id='trigger_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_triggers_get(client):
    """Test case for tagmanager_accounts_containers_triggers_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/triggers/{trigger_id}'.format(account_id='account_id_example', container_id='container_id_example', trigger_id='trigger_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_triggers_list(client):
    """Test case for tagmanager_accounts_containers_triggers_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/triggers'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_triggers_update(client):
    """Test case for tagmanager_accounts_containers_triggers_update

    
    """
    body = {"maxTimerLengthSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visibilitySelector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTags":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parentFolderId":"parentFolderId","checkValidation":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visiblePercentageMax":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"pageview","visiblePercentageMin":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","limit":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"eventName":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"totalTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"verticalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"selector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"containerId":"containerId","customEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"uniqueTriggerId":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTagsTimeout":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"autoEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"triggerId":"triggerId","filter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"accountId":"accountId","horizontalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"name":"name","interval":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"continuousTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"intervalSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/triggers/{trigger_id}'.format(account_id='account_id_example', container_id='container_id_example', trigger_id='trigger_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_update(client):
    """Test case for tagmanager_accounts_containers_update

    
    """
    body = {"accountId":"accountId","usageContext":["web","web"],"notes":"notes","timeZoneId":"timeZoneId","domainName":["domainName","domainName"],"enabledBuiltInVariable":["pageUrl","pageUrl"],"fingerprint":"fingerprint","name":"name","timeZoneCountryId":"timeZoneCountryId","containerId":"containerId","publicId":"publicId"}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_variables_create(client):
    """Test case for tagmanager_accounts_containers_variables_create

    
    """
    body = {"notes":"notes","parentFolderId":"parentFolderId","enablingTriggerId":["enablingTriggerId","enablingTriggerId"],"type":"type","variableId":"variableId","accountId":"accountId","parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","disablingTriggerId":["disablingTriggerId","disablingTriggerId"],"containerId":"containerId"}
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/variables'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_variables_delete(client):
    """Test case for tagmanager_accounts_containers_variables_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/variables/{variable_id}'.format(account_id='account_id_example', container_id='container_id_example', variable_id='variable_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_variables_get(client):
    """Test case for tagmanager_accounts_containers_variables_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/variables/{variable_id}'.format(account_id='account_id_example', container_id='container_id_example', variable_id='variable_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_variables_list(client):
    """Test case for tagmanager_accounts_containers_variables_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/variables'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_variables_update(client):
    """Test case for tagmanager_accounts_containers_variables_update

    
    """
    body = {"notes":"notes","parentFolderId":"parentFolderId","enablingTriggerId":["enablingTriggerId","enablingTriggerId"],"type":"type","variableId":"variableId","accountId":"accountId","parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","disablingTriggerId":["disablingTriggerId","disablingTriggerId"],"containerId":"containerId"}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/variables/{variable_id}'.format(account_id='account_id_example', container_id='container_id_example', variable_id='variable_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_create(client):
    """Test case for tagmanager_accounts_containers_versions_create

    
    """
    body = {"notes":"notes","name":"name","quickPreview":True}
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_delete(client):
    """Test case for tagmanager_accounts_containers_versions_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions/{container_version_id}'.format(account_id='account_id_example', container_id='container_id_example', container_version_id='container_version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_get(client):
    """Test case for tagmanager_accounts_containers_versions_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions/{container_version_id}'.format(account_id='account_id_example', container_id='container_id_example', container_version_id='container_version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_list(client):
    """Test case for tagmanager_accounts_containers_versions_list

    
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
                    ('headers', True),
                    ('includeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions'.format(account_id='account_id_example', container_id='container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_publish(client):
    """Test case for tagmanager_accounts_containers_versions_publish

    
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions/{container_version_id}/publish'.format(account_id='account_id_example', container_id='container_id_example', container_version_id='container_version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_restore(client):
    """Test case for tagmanager_accounts_containers_versions_restore

    
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
        method='POST',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions/{container_version_id}/restore'.format(account_id='account_id_example', container_id='container_id_example', container_version_id='container_version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_undelete(client):
    """Test case for tagmanager_accounts_containers_versions_undelete

    
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
        method='POST',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions/{container_version_id}/undelete'.format(account_id='account_id_example', container_id='container_id_example', container_version_id='container_version_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_update(client):
    """Test case for tagmanager_accounts_containers_versions_update

    
    """
    body = {"container":{"accountId":"accountId","usageContext":["web","web"],"notes":"notes","timeZoneId":"timeZoneId","domainName":["domainName","domainName"],"enabledBuiltInVariable":["pageUrl","pageUrl"],"fingerprint":"fingerprint","name":"name","timeZoneCountryId":"timeZoneCountryId","containerId":"containerId","publicId":"publicId"},"macro":[{"notes":"notes","parentFolderId":"parentFolderId","type":"type","accountId":"accountId","macroId":"macroId","parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","disablingRuleId":["disablingRuleId","disablingRuleId"],"scheduleEndMs":"scheduleEndMs","containerId":"containerId","enablingRuleId":["enablingRuleId","enablingRuleId"]},{"notes":"notes","parentFolderId":"parentFolderId","type":"type","accountId":"accountId","macroId":"macroId","parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","disablingRuleId":["disablingRuleId","disablingRuleId"],"scheduleEndMs":"scheduleEndMs","containerId":"containerId","enablingRuleId":["enablingRuleId","enablingRuleId"]}],"notes":"notes","rule":[{"accountId":"accountId","condition":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"notes":"notes","fingerprint":"fingerprint","name":"name","containerId":"containerId","ruleId":"ruleId"},{"accountId":"accountId","condition":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"notes":"notes","fingerprint":"fingerprint","name":"name","containerId":"containerId","ruleId":"ruleId"}],"trigger":[{"maxTimerLengthSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visibilitySelector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTags":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parentFolderId":"parentFolderId","checkValidation":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visiblePercentageMax":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"pageview","visiblePercentageMin":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","limit":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"eventName":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"totalTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"verticalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"selector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"containerId":"containerId","customEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"uniqueTriggerId":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTagsTimeout":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"autoEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"triggerId":"triggerId","filter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"accountId":"accountId","horizontalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"name":"name","interval":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"continuousTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"intervalSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}},{"maxTimerLengthSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visibilitySelector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTags":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parentFolderId":"parentFolderId","checkValidation":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"visiblePercentageMax":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"pageview","visiblePercentageMin":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","limit":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"eventName":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"totalTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"verticalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"selector":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"containerId":"containerId","customEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"uniqueTriggerId":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"waitForTagsTimeout":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"autoEventFilter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"triggerId":"triggerId","filter":[{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"},{"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"type":"equals"}],"accountId":"accountId","horizontalScrollPercentageList":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"name":"name","interval":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"continuousTimeMinMilliseconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"intervalSeconds":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}}],"accountId":"accountId","deleted":True,"folder":[{"accountId":"accountId","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId"},{"accountId":"accountId","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId"}],"fingerprint":"fingerprint","name":"name","variable":[{"notes":"notes","parentFolderId":"parentFolderId","enablingTriggerId":["enablingTriggerId","enablingTriggerId"],"type":"type","variableId":"variableId","accountId":"accountId","parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","disablingTriggerId":["disablingTriggerId","disablingTriggerId"],"containerId":"containerId"},{"notes":"notes","parentFolderId":"parentFolderId","enablingTriggerId":["enablingTriggerId","enablingTriggerId"],"type":"type","variableId":"variableId","accountId":"accountId","parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","disablingTriggerId":["disablingTriggerId","disablingTriggerId"],"containerId":"containerId"}],"containerVersionId":"containerVersionId","tag":[{"paused":True,"notes":"notes","firingRuleId":["firingRuleId","firingRuleId"],"tagFiringOption":"unlimited","liveOnly":True,"parentFolderId":"parentFolderId","tagId":"tagId","priority":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"type","setupTag":[{"stopOnSetupFailure":True,"tagName":"tagName"},{"stopOnSetupFailure":True,"tagName":"tagName"}],"blockingTriggerId":["blockingTriggerId","blockingTriggerId"],"accountId":"accountId","blockingRuleId":["blockingRuleId","blockingRuleId"],"teardownTag":[{"stopTeardownOnFailure":True,"tagName":"tagName"},{"stopTeardownOnFailure":True,"tagName":"tagName"}],"firingTriggerId":["firingTriggerId","firingTriggerId"],"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","containerId":"containerId"},{"paused":True,"notes":"notes","firingRuleId":["firingRuleId","firingRuleId"],"tagFiringOption":"unlimited","liveOnly":True,"parentFolderId":"parentFolderId","tagId":"tagId","priority":{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},"type":"type","setupTag":[{"stopOnSetupFailure":True,"tagName":"tagName"},{"stopOnSetupFailure":True,"tagName":"tagName"}],"blockingTriggerId":["blockingTriggerId","blockingTriggerId"],"accountId":"accountId","blockingRuleId":["blockingRuleId","blockingRuleId"],"teardownTag":[{"stopTeardownOnFailure":True,"tagName":"tagName"},{"stopTeardownOnFailure":True,"tagName":"tagName"}],"firingTriggerId":["firingTriggerId","firingTriggerId"],"parameter":[{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"template","map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","containerId":"containerId"}],"containerId":"containerId"}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}/containers/{container_id}/versions/{container_version_id}'.format(account_id='account_id_example', container_id='container_id_example', container_version_id='container_version_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_get(client):
    """Test case for tagmanager_accounts_get

    
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
        path='/tagmanager/v1/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_list(client):
    """Test case for tagmanager_accounts_list

    
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
        path='/tagmanager/v1/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_permissions_create(client):
    """Test case for tagmanager_accounts_permissions_create

    
    """
    body = {"accountId":"accountId","permissionId":"permissionId","emailAddress":"emailAddress","accountAccess":{"permission":["read","read"]},"containerAccess":[{"permission":["read","read"],"containerId":"containerId"},{"permission":["read","read"],"containerId":"containerId"}]}
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
        path='/tagmanager/v1/accounts/{account_id}/permissions'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_permissions_delete(client):
    """Test case for tagmanager_accounts_permissions_delete

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v1/accounts/{account_id}/permissions/{permission_id}'.format(account_id='account_id_example', permission_id='permission_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_permissions_get(client):
    """Test case for tagmanager_accounts_permissions_get

    
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
        path='/tagmanager/v1/accounts/{account_id}/permissions/{permission_id}'.format(account_id='account_id_example', permission_id='permission_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_permissions_list(client):
    """Test case for tagmanager_accounts_permissions_list

    
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
        path='/tagmanager/v1/accounts/{account_id}/permissions'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_permissions_update(client):
    """Test case for tagmanager_accounts_permissions_update

    
    """
    body = {"accountId":"accountId","permissionId":"permissionId","emailAddress":"emailAddress","accountAccess":{"permission":["read","read"]},"containerAccess":[{"permission":["read","read"],"containerId":"containerId"},{"permission":["read","read"],"containerId":"containerId"}]}
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
        path='/tagmanager/v1/accounts/{account_id}/permissions/{permission_id}'.format(account_id='account_id_example', permission_id='permission_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_update(client):
    """Test case for tagmanager_accounts_update

    
    """
    body = {"accountId":"accountId","shareData":True,"fingerprint":"fingerprint","name":"name"}
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
                    ('fingerprint', 'fingerprint_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tagmanager/v1/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

