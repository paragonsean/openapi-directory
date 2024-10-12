# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_level import AccessLevel
from openapi_server.models.access_policy import AccessPolicy
from openapi_server.models.list_access_levels_response import ListAccessLevelsResponse
from openapi_server.models.list_access_policies_response import ListAccessPoliciesResponse
from openapi_server.models.list_service_perimeters_response import ListServicePerimetersResponse
from openapi_server.models.operation import Operation
from openapi_server.models.service_perimeter import ServicePerimeter


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_access_levels_create(client):
    """Test case for accesscontextmanager_access_policies_access_levels_create

    
    """
    body = {"custom":{"expr":{"expression":"expression","description":"description","location":"location","title":"title"}},"name":"name","description":"description","basic":{"combiningFunction":"AND","conditions":[{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}},{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}}]},"title":"title"}
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
        path='/v1beta/{parent}/accessLevels'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_access_levels_list(client):
    """Test case for accesscontextmanager_access_policies_access_levels_list

    
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
                    ('accessLevelFormat', 'access_level_format_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{parent}/accessLevels'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_create(client):
    """Test case for accesscontextmanager_access_policies_create

    
    """
    body = {"parent":"parent","name":"name","title":"title"}
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
        path='/v1beta/accessPolicies',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_list(client):
    """Test case for accesscontextmanager_access_policies_list

    
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
                    ('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/accessPolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_create(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_create

    
    """
    body = {"perimeterType":"PERIMETER_TYPE_REGULAR","name":"name","description":"description","title":"title","status":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"unrestrictedServices":["unrestrictedServices","unrestrictedServices"],"resources":["resources","resources"],"restrictedServices":["restrictedServices","restrictedServices"]}}
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
        path='/v1beta/{parent}/servicePerimeters'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_delete(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_delete

    
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
        method='DELETE',
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_list(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_list

    
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
        path='/v1beta/{parent}/servicePerimeters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_patch(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_patch

    
    """
    body = {"perimeterType":"PERIMETER_TYPE_REGULAR","name":"name","description":"description","title":"title","status":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"unrestrictedServices":["unrestrictedServices","unrestrictedServices"],"resources":["resources","resources"],"restrictedServices":["restrictedServices","restrictedServices"]}}
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
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

