# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client import Client
from openapi_server.models.container import Container
from openapi_server.models.container_version import ContainerVersion
from openapi_server.models.container_version_header import ContainerVersionHeader
from openapi_server.models.create_built_in_variable_response import CreateBuiltInVariableResponse
from openapi_server.models.create_container_version_request_version_options import CreateContainerVersionRequestVersionOptions
from openapi_server.models.create_container_version_response import CreateContainerVersionResponse
from openapi_server.models.custom_template import CustomTemplate
from openapi_server.models.destination import Destination
from openapi_server.models.entity import Entity
from openapi_server.models.environment import Environment
from openapi_server.models.folder import Folder
from openapi_server.models.folder_entities import FolderEntities
from openapi_server.models.get_container_snippet_response import GetContainerSnippetResponse
from openapi_server.models.get_workspace_status_response import GetWorkspaceStatusResponse
from openapi_server.models.gtag_config import GtagConfig
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server.models.list_clients_response import ListClientsResponse
from openapi_server.models.list_container_versions_response import ListContainerVersionsResponse
from openapi_server.models.list_containers_response import ListContainersResponse
from openapi_server.models.list_destinations_response import ListDestinationsResponse
from openapi_server.models.list_enabled_built_in_variables_response import ListEnabledBuiltInVariablesResponse
from openapi_server.models.list_environments_response import ListEnvironmentsResponse
from openapi_server.models.list_folders_response import ListFoldersResponse
from openapi_server.models.list_gtag_config_response import ListGtagConfigResponse
from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.list_templates_response import ListTemplatesResponse
from openapi_server.models.list_transformations_response import ListTransformationsResponse
from openapi_server.models.list_triggers_response import ListTriggersResponse
from openapi_server.models.list_user_permissions_response import ListUserPermissionsResponse
from openapi_server.models.list_variables_response import ListVariablesResponse
from openapi_server.models.list_workspaces_response import ListWorkspacesResponse
from openapi_server.models.list_zones_response import ListZonesResponse
from openapi_server.models.publish_container_version_response import PublishContainerVersionResponse
from openapi_server.models.quick_preview_response import QuickPreviewResponse
from openapi_server.models.revert_built_in_variable_response import RevertBuiltInVariableResponse
from openapi_server.models.revert_zone_response import RevertZoneResponse
from openapi_server.models.sync_workspace_response import SyncWorkspaceResponse
from openapi_server.models.tag import Tag
from openapi_server.models.transformation import Transformation
from openapi_server.models.trigger import Trigger
from openapi_server.models.user_permission import UserPermission
from openapi_server.models.variable import Variable
from openapi_server.models.workspace import Workspace
from openapi_server.models.zone import Zone


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_combine(client):
    """Test case for tagmanager_accounts_containers_combine

    
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
                    ('allowUserPermissionFeatureUpdate', True),
                    ('containerId', 'container_id_example'),
                    ('settingSource', 'setting_source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v2/{pathcombin}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_create(client):
    """Test case for tagmanager_accounts_containers_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","usageContext":["usageContextUnspecified","usageContextUnspecified"],"notes":"notes","tagIds":["tagIds","tagIds"],"taggingServerUrls":["taggingServerUrls","taggingServerUrls"],"accountId":"accountId","features":{"supportEnvironments":True,"supportTriggers":True,"supportVersions":True,"supportGtagConfigs":True,"supportWorkspaces":True,"supportTags":True,"supportZones":True,"supportClients":True,"supportFolders":True,"supportTemplates":True,"supportTransformations":True,"supportUserPermissions":True,"supportVariables":True,"supportBuiltInVariables":True},"path":"path","domainName":["domainName","domainName"],"fingerprint":"fingerprint","name":"name","containerId":"containerId","publicId":"publicId"}
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
        path='/tagmanager/v2/{parent}/containers'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_destinations_link(client):
    """Test case for tagmanager_accounts_containers_destinations_link

    
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
                    ('allowUserPermissionFeatureUpdate', True),
                    ('destinationId', 'destination_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v2/{parent}/destinations:link'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_destinations_list(client):
    """Test case for tagmanager_accounts_containers_destinations_list

    
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
        path='/tagmanager/v2/{parent}/destinations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_environments_create(client):
    """Test case for tagmanager_accounts_containers_environments_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","enableDebug":True,"authorizationCode":"authorizationCode","description":"description","type":"user","url":"url","accountId":"accountId","path":"path","environmentId":"environmentId","fingerprint":"fingerprint","name":"name","containerVersionId":"containerVersionId","containerId":"containerId","authorizationTimestamp":"authorizationTimestamp","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        json=body,
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
                    ('uploadType', 'upload_type_example'),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/environments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_environments_reauthorize(client):
    """Test case for tagmanager_accounts_containers_environments_reauthorize

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","enableDebug":True,"authorizationCode":"authorizationCode","description":"description","type":"user","url":"url","accountId":"accountId","path":"path","environmentId":"environmentId","fingerprint":"fingerprint","name":"name","containerVersionId":"containerVersionId","containerId":"containerId","authorizationTimestamp":"authorizationTimestamp","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{pathreauthoriz}'.format(path='path_example'),
        headers=headers,
        json=body,
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
                    ('uploadType', 'upload_type_example'),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/containers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_lookup(client):
    """Test case for tagmanager_accounts_containers_lookup

    
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
                    ('destinationId', 'destination_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/accounts/containers:lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_move_tag_id(client):
    """Test case for tagmanager_accounts_containers_move_tag_id

    
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
                    ('allowUserPermissionFeatureUpdate', True),
                    ('copySettings', True),
                    ('copyTermsOfService', True),
                    ('copyUsers', True),
                    ('tagId', 'tag_id_example'),
                    ('tagName', 'tag_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v2/{pathmove_tag_i}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_snippet(client):
    """Test case for tagmanager_accounts_containers_snippet

    
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
        path='/tagmanager/v2/{pathsnippe}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_version_headers_latest(client):
    """Test case for tagmanager_accounts_containers_version_headers_latest

    
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
        path='/tagmanager/v2/{parent}/version_headers:latest'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_version_headers_list(client):
    """Test case for tagmanager_accounts_containers_version_headers_list

    
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
                    ('includeDeleted', True),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/version_headers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_live(client):
    """Test case for tagmanager_accounts_containers_versions_live

    
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
        path='/tagmanager/v2/{parent}/versions:live'.format(parent='parent_example'),
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
        path='/tagmanager/v2/{pathpublis}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_versions_set_latest(client):
    """Test case for tagmanager_accounts_containers_versions_set_latest

    
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
        path='/tagmanager/v2/{pathset_lates}'.format(path='path_example'),
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
        path='/tagmanager/v2/{pathundelet}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_built_in_variables_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_built_in_variables_create

    
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
                    ('type', ['type_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v2/{parent}/built_in_variables'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_built_in_variables_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_built_in_variables_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/built_in_variables'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_built_in_variables_revert(client):
    """Test case for tagmanager_accounts_containers_workspaces_built_in_variables_revert

    
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
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v2/{path}/built_in_variables:revert'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_clients_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_clients_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","clientId":"clientId","notes":"notes","parentFolderId":"parentFolderId","priority":0,"type":"type","accountId":"accountId","path":"path","parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","name":"name","containerId":"containerId","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/clients'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_clients_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_clients_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/clients'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","fingerprint":"fingerprint","name":"name","description":"description","containerId":"containerId","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/workspaces'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_create_version(client):
    """Test case for tagmanager_accounts_containers_workspaces_create_version

    
    """
    body = {"notes":"notes","name":"name"}
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
        path='/tagmanager/v2/{pathcreate_versio}'.format(path='path_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_folders_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_folders_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","notes":"notes","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/folders'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_folders_entities(client):
    """Test case for tagmanager_accounts_containers_workspaces_folders_entities

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v2/{pathentitie}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_folders_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_folders_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/folders'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_folders_move_entities_to_folder(client):
    """Test case for tagmanager_accounts_containers_workspaces_folders_move_entities_to_folder

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","notes":"notes","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId","workspaceId":"workspaceId"}
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
        method='POST',
        path='/tagmanager/v2/{pathmove_entities_to_folde}'.format(path='path_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_get_status(client):
    """Test case for tagmanager_accounts_containers_workspaces_get_status

    
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
        path='/tagmanager/v2/{path}/status'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_gtag_config_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_gtag_config_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","containerId":"containerId","type":"type","gtagConfigId":"gtagConfigId","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/gtag_config'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_gtag_config_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_gtag_config_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/gtag_config'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/workspaces'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_quick_preview(client):
    """Test case for tagmanager_accounts_containers_workspaces_quick_preview

    
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
        path='/tagmanager/v2/{pathquick_previe}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_resolve_conflict(client):
    """Test case for tagmanager_accounts_containers_workspaces_resolve_conflict

    
    """
    body = {"gtagConfig":{"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","containerId":"containerId","type":"type","gtagConfigId":"gtagConfigId","workspaceId":"workspaceId"},"folder":{"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","notes":"notes","fingerprint":"fingerprint","name":"name","containerId":"containerId","folderId":"folderId","workspaceId":"workspaceId"},"zone":{"boundary":{"condition":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"customEvaluationTriggerId":["customEvaluationTriggerId","customEvaluationTriggerId"]},"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","notes":"notes","typeRestriction":{"enable":True,"whitelistedTypeId":["whitelistedTypeId","whitelistedTypeId"]},"fingerprint":"fingerprint","name":"name","zoneId":"zoneId","containerId":"containerId","childContainer":[{"nickname":"nickname","publicId":"publicId"},{"nickname":"nickname","publicId":"publicId"}],"workspaceId":"workspaceId"},"variable":{"tagManagerUrl":"tagManagerUrl","notes":"notes","parentFolderId":"parentFolderId","enablingTriggerId":["enablingTriggerId","enablingTriggerId"],"type":"type","variableId":"variableId","accountId":"accountId","path":"path","formatValue":{"convertTrueToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"caseConversionType":"none","convertFalseToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"convertNullToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"convertUndefinedToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}},"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","disablingTriggerId":["disablingTriggerId","disablingTriggerId"],"containerId":"containerId","workspaceId":"workspaceId"},"client":{"tagManagerUrl":"tagManagerUrl","clientId":"clientId","notes":"notes","parentFolderId":"parentFolderId","priority":0,"type":"type","accountId":"accountId","path":"path","parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","name":"name","containerId":"containerId","workspaceId":"workspaceId"},"changeStatus":"changeStatusUnspecified","builtInVariable":{"accountId":"accountId","path":"path","name":"name","containerId":"containerId","type":"builtInVariableTypeUnspecified","workspaceId":"workspaceId"},"tag":{"tagManagerUrl":"tagManagerUrl","paused":True,"notes":"notes","firingRuleId":["firingRuleId","firingRuleId"],"liveOnly":True,"parentFolderId":"parentFolderId","tagId":"tagId","type":"type","setupTag":[{"stopOnSetupFailure":True,"tagName":"tagName"},{"stopOnSetupFailure":True,"tagName":"tagName"}],"blockingTriggerId":["blockingTriggerId","blockingTriggerId"],"monitoringMetadata":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"blockingRuleId":["blockingRuleId","blockingRuleId"],"path":"path","teardownTag":[{"stopTeardownOnFailure":True,"tagName":"tagName"},{"stopTeardownOnFailure":True,"tagName":"tagName"}],"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","consentSettings":{"consentStatus":"notSet","consentType":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}},"scheduleEndMs":"scheduleEndMs","containerId":"containerId","workspaceId":"workspaceId","tagFiringOption":"tagFiringOptionUnspecified","monitoringMetadataTagNameKey":"monitoringMetadataTagNameKey","priority":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"accountId":"accountId","firingTriggerId":["firingTriggerId","firingTriggerId"],"scheduleStartMs":"scheduleStartMs","name":"name"},"trigger":{"tagManagerUrl":"tagManagerUrl","maxTimerLengthSeconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"visibilitySelector":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"notes":"notes","waitForTags":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"parentFolderId":"parentFolderId","checkValidation":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"visiblePercentageMax":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"type":"eventTypeUnspecified","path":"path","visiblePercentageMin":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","limit":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"eventName":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"totalTimeMinMilliseconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"verticalScrollPercentageList":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"selector":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"containerId":"containerId","customEventFilter":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"workspaceId":"workspaceId","uniqueTriggerId":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"waitForTagsTimeout":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"autoEventFilter":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"triggerId":"triggerId","filter":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"accountId":"accountId","horizontalScrollPercentageList":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"name":"name","interval":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"continuousTimeMinMilliseconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"intervalSeconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}},"transformation":{"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","notes":"notes","parentFolderId":"parentFolderId","parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","name":"name","transformationId":"transformationId","containerId":"containerId","type":"type","workspaceId":"workspaceId"},"customTemplate":{"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","galleryReference":{"owner":"owner","isModified":True,"signature":"signature","host":"host","repository":"repository","version":"version"},"fingerprint":"fingerprint","name":"name","templateData":"templateData","containerId":"containerId","templateId":"templateId","workspaceId":"workspaceId"}}
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
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/tagmanager/v2/{pathresolve_conflic}'.format(path='path_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_sync(client):
    """Test case for tagmanager_accounts_containers_workspaces_sync

    
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
        path='/tagmanager/v2/{pathsyn}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_tags_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_tags_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","paused":True,"notes":"notes","firingRuleId":["firingRuleId","firingRuleId"],"liveOnly":True,"parentFolderId":"parentFolderId","tagId":"tagId","type":"type","setupTag":[{"stopOnSetupFailure":True,"tagName":"tagName"},{"stopOnSetupFailure":True,"tagName":"tagName"}],"blockingTriggerId":["blockingTriggerId","blockingTriggerId"],"monitoringMetadata":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"blockingRuleId":["blockingRuleId","blockingRuleId"],"path":"path","teardownTag":[{"stopTeardownOnFailure":True,"tagName":"tagName"},{"stopTeardownOnFailure":True,"tagName":"tagName"}],"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","consentSettings":{"consentStatus":"notSet","consentType":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}},"scheduleEndMs":"scheduleEndMs","containerId":"containerId","workspaceId":"workspaceId","tagFiringOption":"tagFiringOptionUnspecified","monitoringMetadataTagNameKey":"monitoringMetadataTagNameKey","priority":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"accountId":"accountId","firingTriggerId":["firingTriggerId","firingTriggerId"],"scheduleStartMs":"scheduleStartMs","name":"name"}
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
        path='/tagmanager/v2/{parent}/tags'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_tags_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_tags_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/tags'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_templates_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_templates_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","galleryReference":{"owner":"owner","isModified":True,"signature":"signature","host":"host","repository":"repository","version":"version"},"fingerprint":"fingerprint","name":"name","templateData":"templateData","containerId":"containerId","templateId":"templateId","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/templates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_templates_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_templates_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/templates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_transformations_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_transformations_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","notes":"notes","parentFolderId":"parentFolderId","parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","name":"name","transformationId":"transformationId","containerId":"containerId","type":"type","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/transformations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_transformations_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_transformations_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/transformations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_triggers_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_triggers_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","maxTimerLengthSeconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"visibilitySelector":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"notes":"notes","waitForTags":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"parentFolderId":"parentFolderId","checkValidation":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"visiblePercentageMax":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"type":"eventTypeUnspecified","path":"path","visiblePercentageMin":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"fingerprint":"fingerprint","limit":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"eventName":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"totalTimeMinMilliseconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"verticalScrollPercentageList":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"selector":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"containerId":"containerId","customEventFilter":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"workspaceId":"workspaceId","uniqueTriggerId":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"waitForTagsTimeout":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"autoEventFilter":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"triggerId":"triggerId","filter":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"accountId":"accountId","horizontalScrollPercentageList":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"name":"name","interval":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"continuousTimeMinMilliseconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"intervalSeconds":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}}
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
        path='/tagmanager/v2/{parent}/triggers'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_triggers_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_triggers_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/triggers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_variables_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_variables_create

    
    """
    body = {"tagManagerUrl":"tagManagerUrl","notes":"notes","parentFolderId":"parentFolderId","enablingTriggerId":["enablingTriggerId","enablingTriggerId"],"type":"type","variableId":"variableId","accountId":"accountId","path":"path","formatValue":{"convertTrueToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"caseConversionType":"none","convertFalseToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"convertNullToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},"convertUndefinedToValue":{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}},"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"scheduleStartMs":"scheduleStartMs","fingerprint":"fingerprint","name":"name","scheduleEndMs":"scheduleEndMs","disablingTriggerId":["disablingTriggerId","disablingTriggerId"],"containerId":"containerId","workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/variables'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_variables_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_variables_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/variables'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_zones_create(client):
    """Test case for tagmanager_accounts_containers_workspaces_zones_create

    
    """
    body = {"boundary":{"condition":[{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"},{"parameter":[{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"},{"list":[null,null],"type":"typeUnspecified","isWeakReference":True,"map":[null,null],"value":"value","key":"key"}],"type":"conditionTypeUnspecified"}],"customEvaluationTriggerId":["customEvaluationTriggerId","customEvaluationTriggerId"]},"tagManagerUrl":"tagManagerUrl","accountId":"accountId","path":"path","notes":"notes","typeRestriction":{"enable":True,"whitelistedTypeId":["whitelistedTypeId","whitelistedTypeId"]},"fingerprint":"fingerprint","name":"name","zoneId":"zoneId","containerId":"containerId","childContainer":[{"nickname":"nickname","publicId":"publicId"},{"nickname":"nickname","publicId":"publicId"}],"workspaceId":"workspaceId"}
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
        path='/tagmanager/v2/{parent}/zones'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_zones_list(client):
    """Test case for tagmanager_accounts_containers_workspaces_zones_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/zones'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_containers_workspaces_zones_revert(client):
    """Test case for tagmanager_accounts_containers_workspaces_zones_revert

    
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
        path='/tagmanager/v2/{pathrever}'.format(path='path_example'),
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
                    ('uploadType', 'upload_type_example'),
                    ('includeGoogleTags', True),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_user_permissions_create(client):
    """Test case for tagmanager_accounts_user_permissions_create

    
    """
    body = {"accountId":"accountId","path":"path","emailAddress":"emailAddress","accountAccess":{"permission":"accountPermissionUnspecified"},"containerAccess":[{"permission":"containerPermissionUnspecified","containerId":"containerId"},{"permission":"containerPermissionUnspecified","containerId":"containerId"}]}
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
        path='/tagmanager/v2/{parent}/user_permissions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_user_permissions_delete(client):
    """Test case for tagmanager_accounts_user_permissions_delete

    
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
                    ('type', ['type_example'])]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tagmanager/v2/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_user_permissions_get(client):
    """Test case for tagmanager_accounts_user_permissions_get

    
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
                    ('containerVersionId', 'container_version_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_user_permissions_list(client):
    """Test case for tagmanager_accounts_user_permissions_list

    
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
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tagmanager/v2/{parent}/user_permissions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tagmanager_accounts_user_permissions_update(client):
    """Test case for tagmanager_accounts_user_permissions_update

    
    """
    body = {"accountId":"accountId","path":"path","emailAddress":"emailAddress","accountAccess":{"permission":"accountPermissionUnspecified"},"containerAccess":[{"permission":"containerPermissionUnspecified","containerId":"containerId"},{"permission":"containerPermissionUnspecified","containerId":"containerId"}]}
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
        path='/tagmanager/v2/{path}'.format(path='path_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

