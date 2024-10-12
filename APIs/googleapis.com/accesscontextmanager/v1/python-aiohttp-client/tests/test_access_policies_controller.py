# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_level import AccessLevel
from openapi_server.models.access_policy import AccessPolicy
from openapi_server.models.authorized_orgs_desc import AuthorizedOrgsDesc
from openapi_server.models.commit_service_perimeters_request import CommitServicePerimetersRequest
from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.list_access_levels_response import ListAccessLevelsResponse
from openapi_server.models.list_access_policies_response import ListAccessPoliciesResponse
from openapi_server.models.list_authorized_orgs_descs_response import ListAuthorizedOrgsDescsResponse
from openapi_server.models.list_service_perimeters_response import ListServicePerimetersResponse
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.replace_access_levels_request import ReplaceAccessLevelsRequest
from openapi_server.models.replace_service_perimeters_request import ReplaceServicePerimetersRequest
from openapi_server.models.service_perimeter import ServicePerimeter
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_access_levels_create(client):
    """Test case for accesscontextmanager_access_policies_access_levels_create

    
    """
    body = {"custom":{"expr":{"expression":"expression","description":"description","location":"location","title":"title"}},"name":"name","description":"description","basic":{"combiningFunction":"AND","conditions":[{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"vpcNetworkSources":[{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}},{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}}],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}},{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"vpcNetworkSources":[{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}},{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}}],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}}]},"title":"title"}
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
        path='/v1/{parent}/accessLevels'.format(parent='parent_example'),
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
        path='/v1/{parent}/accessLevels'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_access_levels_replace_all(client):
    """Test case for accesscontextmanager_access_policies_access_levels_replace_all

    
    """
    body = {"accessLevels":[{"custom":{"expr":{"expression":"expression","description":"description","location":"location","title":"title"}},"name":"name","description":"description","basic":{"combiningFunction":"AND","conditions":[{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"vpcNetworkSources":[{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}},{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}}],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}},{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"vpcNetworkSources":[{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}},{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}}],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}}]},"title":"title"},{"custom":{"expr":{"expression":"expression","description":"description","location":"location","title":"title"}},"name":"name","description":"description","basic":{"combiningFunction":"AND","conditions":[{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"vpcNetworkSources":[{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}},{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}}],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}},{"regions":["regions","regions"],"requiredAccessLevels":["requiredAccessLevels","requiredAccessLevels"],"negate":True,"ipSubnetworks":["ipSubnetworks","ipSubnetworks"],"members":["members","members"],"vpcNetworkSources":[{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}},{"vpcSubnetwork":{"vpcIpSubnetworks":["vpcIpSubnetworks","vpcIpSubnetworks"],"network":"network"}}],"devicePolicy":{"osConstraints":[{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"},{"minimumVersion":"minimumVersion","requireVerifiedChromeOs":True,"osType":"OS_UNSPECIFIED"}],"requireScreenlock":True,"allowedDeviceManagementLevels":["MANAGEMENT_UNSPECIFIED","MANAGEMENT_UNSPECIFIED"],"requireAdminApproval":True,"requireCorpOwned":True,"allowedEncryptionStatuses":["ENCRYPTION_UNSPECIFIED","ENCRYPTION_UNSPECIFIED"]}}]},"title":"title"}],"etag":"etag"}
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
        path='/v1/{parent}/accessLevels:replaceAll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_authorized_orgs_descs_create(client):
    """Test case for accesscontextmanager_access_policies_authorized_orgs_descs_create

    
    """
    body = {"name":"name","authorizationType":"AUTHORIZATION_TYPE_UNSPECIFIED","orgs":["orgs","orgs"],"authorizationDirection":"AUTHORIZATION_DIRECTION_UNSPECIFIED","assetType":"ASSET_TYPE_UNSPECIFIED"}
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
        path='/v1/{parent}/authorizedOrgsDescs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_authorized_orgs_descs_list(client):
    """Test case for accesscontextmanager_access_policies_authorized_orgs_descs_list

    
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
        path='/v1/{parent}/authorizedOrgsDescs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_create(client):
    """Test case for accesscontextmanager_access_policies_create

    
    """
    body = {"parent":"parent","name":"name","etag":"etag","scopes":["scopes","scopes"],"title":"title"}
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
        path='/v1/accessPolicies',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_get_iam_policy(client):
    """Test case for accesscontextmanager_access_policies_get_iam_policy

    
    """
    body = {"options":{"requestedPolicyVersion":0}}
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
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
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
        path='/v1/accessPolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_commit(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_commit

    
    """
    body = {"etag":"etag"}
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
        path='/v1/{parent}/servicePerimeters:commit'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_create(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_create

    
    """
    body = {"perimeterType":"PERIMETER_TYPE_REGULAR","name":"name","useExplicitDryRunSpec":True,"description":"description","title":"title","spec":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"egressPolicies":[{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}},{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}}],"resources":["resources","resources"],"ingressPolicies":[{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}},{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}}],"restrictedServices":["restrictedServices","restrictedServices"]},"status":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"egressPolicies":[{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}},{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}}],"resources":["resources","resources"],"ingressPolicies":[{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}},{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}}],"restrictedServices":["restrictedServices","restrictedServices"]}}
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
        path='/v1/{parent}/servicePerimeters'.format(parent='parent_example'),
        headers=headers,
        json=body,
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
        path='/v1/{parent}/servicePerimeters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_replace_all(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_replace_all

    
    """
    body = {"servicePerimeters":[{"perimeterType":"PERIMETER_TYPE_REGULAR","name":"name","useExplicitDryRunSpec":True,"description":"description","title":"title","spec":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"egressPolicies":[{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}},{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}}],"resources":["resources","resources"],"ingressPolicies":[{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}},{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}}],"restrictedServices":["restrictedServices","restrictedServices"]},"status":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"egressPolicies":[{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}},{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}}],"resources":["resources","resources"],"ingressPolicies":[{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}},{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}}],"restrictedServices":["restrictedServices","restrictedServices"]}},{"perimeterType":"PERIMETER_TYPE_REGULAR","name":"name","useExplicitDryRunSpec":True,"description":"description","title":"title","spec":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"egressPolicies":[{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}},{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}}],"resources":["resources","resources"],"ingressPolicies":[{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}},{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}}],"restrictedServices":["restrictedServices","restrictedServices"]},"status":{"accessLevels":["accessLevels","accessLevels"],"vpcAccessibleServices":{"allowedServices":["allowedServices","allowedServices"],"enableRestriction":True},"egressPolicies":[{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}},{"egressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"],"externalResources":["externalResources","externalResources"]},"egressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel"},{"accessLevel":"accessLevel"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED","sourceRestriction":"SOURCE_RESTRICTION_UNSPECIFIED"}}],"resources":["resources","resources"],"ingressPolicies":[{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}},{"ingressTo":{"operations":[{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"},{"methodSelectors":[{"method":"method","permission":"permission"},{"method":"method","permission":"permission"}],"serviceName":"serviceName"}],"resources":["resources","resources"]},"ingressFrom":{"identities":["identities","identities"],"sources":[{"accessLevel":"accessLevel","resource":"resource"},{"accessLevel":"accessLevel","resource":"resource"}],"identityType":"IDENTITY_TYPE_UNSPECIFIED"}}],"restrictedServices":["restrictedServices","restrictedServices"]}}],"etag":"etag"}
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
        path='/v1/{parent}/servicePerimeters:replaceAll'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_service_perimeters_test_iam_permissions(client):
    """Test case for accesscontextmanager_access_policies_service_perimeters_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accesscontextmanager_access_policies_set_iam_policy(client):
    """Test case for accesscontextmanager_access_policies_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

