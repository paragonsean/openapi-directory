# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_iam_v1_get_iam_policy_request import GoogleIamV1GetIamPolicyRequest
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.managed_zone import ManagedZone
from openapi_server.models.managed_zones_list_response import ManagedZonesListResponse
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_create(client):
    """Test case for dns_managed_zones_create

    
    """
    body = {"forwardingConfig":{"kind":"dns#managedZoneForwardingConfig","targetNameServers":[{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#managedZoneForwardingConfigNameServerTarget","ipv4Address":"ipv4Address"},{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#managedZoneForwardingConfigNameServerTarget","ipv4Address":"ipv4Address"}]},"dnssecConfig":{"defaultKeySpecs":[{"keyLength":8,"kind":"dns#dnsKeySpec","keyType":"keySigning","algorithm":"rsasha1"},{"keyLength":8,"kind":"dns#dnsKeySpec","keyType":"keySigning","algorithm":"rsasha1"}],"kind":"dns#managedZoneDnsSecConfig","state":"false","nonExistence":"nsec"},"creationTime":"creationTime","visibility":"public","kind":"dns#managedZone","description":"description","dnsName":"dnsName","nameServers":["nameServers","nameServers"],"privateVisibilityConfig":{"kind":"dns#managedZonePrivateVisibilityConfig","networks":[{"kind":"dns#managedZonePrivateVisibilityConfigNetwork","networkUrl":"networkUrl"},{"kind":"dns#managedZonePrivateVisibilityConfigNetwork","networkUrl":"networkUrl"}],"gkeClusters":[{"gkeClusterName":"gkeClusterName","kind":"dns#managedZonePrivateVisibilityConfigGKECluster"},{"gkeClusterName":"gkeClusterName","kind":"dns#managedZonePrivateVisibilityConfigGKECluster"}]},"labels":{"key":"labels"},"reverseLookupConfig":{"kind":"dns#managedZoneReverseLookupConfig"},"peeringConfig":{"kind":"dns#managedZonePeeringConfig","targetNetwork":{"kind":"dns#managedZonePeeringConfigTargetNetwork","deactivateTime":"deactivateTime","networkUrl":"networkUrl"}},"serviceDirectoryConfig":{"kind":"dns#managedZoneServiceDirectoryConfig","namespace":{"kind":"dns#managedZoneServiceDirectoryConfigNamespace","deletionTime":"deletionTime","namespaceUrl":"namespaceUrl"}},"nameServerSet":"nameServerSet","name":"name","id":"id","cloudLoggingConfig":{"kind":"dns#managedZoneCloudLoggingConfig","enableLogging":True}}
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
        path='/dns/v1beta2/projects/{project}/managedZones'.format(project='project_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_delete(client):
    """Test case for dns_managed_zones_delete

    
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
        path='/dns/v1beta2/projects/{project}/managedZones/{managed_zone}'.format(project='project_example', managed_zone='managed_zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_get(client):
    """Test case for dns_managed_zones_get

    
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
        path='/dns/v1beta2/projects/{project}/managedZones/{managed_zone}'.format(project='project_example', managed_zone='managed_zone_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_get_iam_policy(client):
    """Test case for dns_managed_zones_get_iam_policy

    
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
        path='/dns/v1beta2/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_list(client):
    """Test case for dns_managed_zones_list

    
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
                    ('dnsName', 'dns_name_example'),
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/dns/v1beta2/projects/{project}/managedZones'.format(project='project_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_patch(client):
    """Test case for dns_managed_zones_patch

    
    """
    body = {"forwardingConfig":{"kind":"dns#managedZoneForwardingConfig","targetNameServers":[{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#managedZoneForwardingConfigNameServerTarget","ipv4Address":"ipv4Address"},{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#managedZoneForwardingConfigNameServerTarget","ipv4Address":"ipv4Address"}]},"dnssecConfig":{"defaultKeySpecs":[{"keyLength":8,"kind":"dns#dnsKeySpec","keyType":"keySigning","algorithm":"rsasha1"},{"keyLength":8,"kind":"dns#dnsKeySpec","keyType":"keySigning","algorithm":"rsasha1"}],"kind":"dns#managedZoneDnsSecConfig","state":"false","nonExistence":"nsec"},"creationTime":"creationTime","visibility":"public","kind":"dns#managedZone","description":"description","dnsName":"dnsName","nameServers":["nameServers","nameServers"],"privateVisibilityConfig":{"kind":"dns#managedZonePrivateVisibilityConfig","networks":[{"kind":"dns#managedZonePrivateVisibilityConfigNetwork","networkUrl":"networkUrl"},{"kind":"dns#managedZonePrivateVisibilityConfigNetwork","networkUrl":"networkUrl"}],"gkeClusters":[{"gkeClusterName":"gkeClusterName","kind":"dns#managedZonePrivateVisibilityConfigGKECluster"},{"gkeClusterName":"gkeClusterName","kind":"dns#managedZonePrivateVisibilityConfigGKECluster"}]},"labels":{"key":"labels"},"reverseLookupConfig":{"kind":"dns#managedZoneReverseLookupConfig"},"peeringConfig":{"kind":"dns#managedZonePeeringConfig","targetNetwork":{"kind":"dns#managedZonePeeringConfigTargetNetwork","deactivateTime":"deactivateTime","networkUrl":"networkUrl"}},"serviceDirectoryConfig":{"kind":"dns#managedZoneServiceDirectoryConfig","namespace":{"kind":"dns#managedZoneServiceDirectoryConfigNamespace","deletionTime":"deletionTime","namespaceUrl":"namespaceUrl"}},"nameServerSet":"nameServerSet","name":"name","id":"id","cloudLoggingConfig":{"kind":"dns#managedZoneCloudLoggingConfig","enableLogging":True}}
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
        path='/dns/v1beta2/projects/{project}/managedZones/{managed_zone}'.format(project='project_example', managed_zone='managed_zone_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_set_iam_policy(client):
    """Test case for dns_managed_zones_set_iam_policy

    
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
        path='/dns/v1beta2/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_test_iam_permissions(client):
    """Test case for dns_managed_zones_test_iam_permissions

    
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
        path='/dns/v1beta2/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dns_managed_zones_update(client):
    """Test case for dns_managed_zones_update

    
    """
    body = {"forwardingConfig":{"kind":"dns#managedZoneForwardingConfig","targetNameServers":[{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#managedZoneForwardingConfigNameServerTarget","ipv4Address":"ipv4Address"},{"forwardingPath":"default","ipv6Address":"ipv6Address","kind":"dns#managedZoneForwardingConfigNameServerTarget","ipv4Address":"ipv4Address"}]},"dnssecConfig":{"defaultKeySpecs":[{"keyLength":8,"kind":"dns#dnsKeySpec","keyType":"keySigning","algorithm":"rsasha1"},{"keyLength":8,"kind":"dns#dnsKeySpec","keyType":"keySigning","algorithm":"rsasha1"}],"kind":"dns#managedZoneDnsSecConfig","state":"false","nonExistence":"nsec"},"creationTime":"creationTime","visibility":"public","kind":"dns#managedZone","description":"description","dnsName":"dnsName","nameServers":["nameServers","nameServers"],"privateVisibilityConfig":{"kind":"dns#managedZonePrivateVisibilityConfig","networks":[{"kind":"dns#managedZonePrivateVisibilityConfigNetwork","networkUrl":"networkUrl"},{"kind":"dns#managedZonePrivateVisibilityConfigNetwork","networkUrl":"networkUrl"}],"gkeClusters":[{"gkeClusterName":"gkeClusterName","kind":"dns#managedZonePrivateVisibilityConfigGKECluster"},{"gkeClusterName":"gkeClusterName","kind":"dns#managedZonePrivateVisibilityConfigGKECluster"}]},"labels":{"key":"labels"},"reverseLookupConfig":{"kind":"dns#managedZoneReverseLookupConfig"},"peeringConfig":{"kind":"dns#managedZonePeeringConfig","targetNetwork":{"kind":"dns#managedZonePeeringConfigTargetNetwork","deactivateTime":"deactivateTime","networkUrl":"networkUrl"}},"serviceDirectoryConfig":{"kind":"dns#managedZoneServiceDirectoryConfig","namespace":{"kind":"dns#managedZoneServiceDirectoryConfigNamespace","deletionTime":"deletionTime","namespaceUrl":"namespaceUrl"}},"nameServerSet":"nameServerSet","name":"name","id":"id","cloudLoggingConfig":{"kind":"dns#managedZoneCloudLoggingConfig","enableLogging":True}}
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
        path='/dns/v1beta2/projects/{project}/managedZones/{managed_zone}'.format(project='project_example', managed_zone='managed_zone_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

