# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_permission_group_request import CreatePermissionGroupRequest
from openapi_server.models.permission_group_model import PermissionGroupModel
from openapi_server.models.permission_group_model_haljson import PermissionGroupModelHaljson
from openapi_server.models.update_permission_group_request import UpdatePermissionGroupRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_permission_group(client):
    """Test case for create_permission_group

    Create Permission Group
    """
    body = {"canViewProductStatistics":True,"canDeleteConfig":True,"canDeleteTag":True,"environmentAccesses":[{"environmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","color":"color","environmentAccessType":"full","name":"name","description":"description","order":0,"reasonRequired":True},{"environmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","color":"color","environmentAccessType":"full","name":"name","description":"description","order":0,"reasonRequired":True}],"canDeleteEnvironment":True,"canCreateOrUpdateConfig":True,"canManageIntegrations":True,"canManageProductPreferences":True,"canDeleteSegments":True,"accessType":"readOnly","canTagSetting":True,"canManageMembers":True,"canManageWebhook":True,"canUseExportImport":True,"canViewSdkKey":True,"canCreateOrUpdateEnvironment":True,"canDeleteSetting":True,"canRotateSdkKey":True,"canViewProductAuditLog":True,"name":"name","canCreateOrUpdateTag":True,"newEnvironmentAccessType":"full","canCreateOrUpdateSegments":True,"canCreateOrUpdateSetting":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/products/{product_id}/permissions'.format(product_id='product_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_group(client):
    """Test case for delete_permission_group

    Delete Permission Group
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/permissions/{permission_group_id}'.format(permission_group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_group(client):
    """Test case for get_permission_group

    Get Permission Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/permissions/{permission_group_id}'.format(permission_group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_groups(client):
    """Test case for get_permission_groups

    List Permission Groups
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/products/{product_id}/permissions'.format(product_id='product_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_permission_group(client):
    """Test case for update_permission_group

    Update Permission Group
    """
    body = {"canViewProductStatistics":True,"canDeleteConfig":True,"canDeleteTag":True,"environmentAccesses":[{"environmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","color":"color","environmentAccessType":"full","name":"name","description":"description","order":0,"reasonRequired":True},{"environmentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","color":"color","environmentAccessType":"full","name":"name","description":"description","order":0,"reasonRequired":True}],"canDeleteEnvironment":True,"canCreateOrUpdateConfig":True,"canManageIntegrations":True,"canManageProductPreferences":True,"canDeleteSegments":True,"accessType":"readOnly","canTagSetting":True,"canManageMembers":True,"canManageWebhook":True,"canUseExportImport":True,"canViewSdkKey":True,"canCreateOrUpdateEnvironment":True,"canDeleteSetting":True,"canRotateSdkKey":True,"canViewProductAuditLog":True,"name":"name","canCreateOrUpdateTag":True,"canCreateOrUpdateSegments":True,"canCreateOrUpdateSetting":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v1/permissions/{permission_group_id}'.format(permission_group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

