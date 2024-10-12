# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activate_key_signing_key_response import ActivateKeySigningKeyResponse
from openapi_server.models.associate_vpc_with_hosted_zone_request import AssociateVPCWithHostedZoneRequest
from openapi_server.models.associate_vpc_with_hosted_zone_response import AssociateVPCWithHostedZoneResponse
from openapi_server.models.change_cidr_collection_request import ChangeCidrCollectionRequest
from openapi_server.models.change_cidr_collection_response import ChangeCidrCollectionResponse
from openapi_server.models.change_tags_for_resource_request import ChangeTagsForResourceRequest
from openapi_server.models.create_cidr_collection_request import CreateCidrCollectionRequest
from openapi_server.models.create_cidr_collection_response import CreateCidrCollectionResponse
from openapi_server.models.create_health_check_request import CreateHealthCheckRequest
from openapi_server.models.create_health_check_response import CreateHealthCheckResponse
from openapi_server.models.create_hosted_zone_request import CreateHostedZoneRequest
from openapi_server.models.create_hosted_zone_response import CreateHostedZoneResponse
from openapi_server.models.create_key_signing_key_request import CreateKeySigningKeyRequest
from openapi_server.models.create_key_signing_key_response import CreateKeySigningKeyResponse
from openapi_server.models.create_query_logging_config_request import CreateQueryLoggingConfigRequest
from openapi_server.models.create_query_logging_config_response import CreateQueryLoggingConfigResponse
from openapi_server.models.create_reusable_delegation_set_request import CreateReusableDelegationSetRequest
from openapi_server.models.create_reusable_delegation_set_response import CreateReusableDelegationSetResponse
from openapi_server.models.create_traffic_policy_instance_request import CreateTrafficPolicyInstanceRequest
from openapi_server.models.create_traffic_policy_instance_response import CreateTrafficPolicyInstanceResponse
from openapi_server.models.create_traffic_policy_request import CreateTrafficPolicyRequest
from openapi_server.models.create_traffic_policy_response import CreateTrafficPolicyResponse
from openapi_server.models.create_traffic_policy_version_request import CreateTrafficPolicyVersionRequest
from openapi_server.models.create_traffic_policy_version_response import CreateTrafficPolicyVersionResponse
from openapi_server.models.create_vpc_association_authorization_request import CreateVPCAssociationAuthorizationRequest
from openapi_server.models.create_vpc_association_authorization_response import CreateVPCAssociationAuthorizationResponse
from openapi_server.models.deactivate_key_signing_key_response import DeactivateKeySigningKeyResponse
from openapi_server.models.delete_hosted_zone_response import DeleteHostedZoneResponse
from openapi_server.models.delete_key_signing_key_response import DeleteKeySigningKeyResponse
from openapi_server.models.disable_hosted_zone_dnssec_response import DisableHostedZoneDNSSECResponse
from openapi_server.models.disassociate_vpc_from_hosted_zone_request import DisassociateVPCFromHostedZoneRequest
from openapi_server.models.disassociate_vpc_from_hosted_zone_response import DisassociateVPCFromHostedZoneResponse
from openapi_server.models.enable_hosted_zone_dnssec_response import EnableHostedZoneDNSSECResponse
from openapi_server.models.get_account_limit_response import GetAccountLimitResponse
from openapi_server.models.get_change_response import GetChangeResponse
from openapi_server.models.get_checker_ip_ranges_response import GetCheckerIpRangesResponse
from openapi_server.models.get_dnssec_response import GetDNSSECResponse
from openapi_server.models.get_geo_location_response import GetGeoLocationResponse
from openapi_server.models.get_health_check_count_response import GetHealthCheckCountResponse
from openapi_server.models.get_health_check_last_failure_reason_response import GetHealthCheckLastFailureReasonResponse
from openapi_server.models.get_health_check_response import GetHealthCheckResponse
from openapi_server.models.get_health_check_status_response import GetHealthCheckStatusResponse
from openapi_server.models.get_hosted_zone_count_response import GetHostedZoneCountResponse
from openapi_server.models.get_hosted_zone_limit_response import GetHostedZoneLimitResponse
from openapi_server.models.get_hosted_zone_response import GetHostedZoneResponse
from openapi_server.models.get_query_logging_config_response import GetQueryLoggingConfigResponse
from openapi_server.models.get_reusable_delegation_set_limit_response import GetReusableDelegationSetLimitResponse
from openapi_server.models.get_reusable_delegation_set_response import GetReusableDelegationSetResponse
from openapi_server.models.get_traffic_policy_instance_count_response import GetTrafficPolicyInstanceCountResponse
from openapi_server.models.get_traffic_policy_instance_response import GetTrafficPolicyInstanceResponse
from openapi_server.models.get_traffic_policy_response import GetTrafficPolicyResponse
from openapi_server.models.list_cidr_blocks_response import ListCidrBlocksResponse
from openapi_server.models.list_cidr_collections_response import ListCidrCollectionsResponse
from openapi_server.models.list_cidr_locations_response import ListCidrLocationsResponse
from openapi_server.models.list_geo_locations_response import ListGeoLocationsResponse
from openapi_server.models.list_health_checks_response import ListHealthChecksResponse
from openapi_server.models.list_hosted_zones_by_name_response import ListHostedZonesByNameResponse
from openapi_server.models.list_hosted_zones_by_vpc_response import ListHostedZonesByVPCResponse
from openapi_server.models.list_hosted_zones_response import ListHostedZonesResponse
from openapi_server.models.list_query_logging_configs_response import ListQueryLoggingConfigsResponse
from openapi_server.models.list_resource_record_sets_response import ListResourceRecordSetsResponse
from openapi_server.models.list_reusable_delegation_sets_response import ListReusableDelegationSetsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_tags_for_resources_request import ListTagsForResourcesRequest
from openapi_server.models.list_tags_for_resources_response import ListTagsForResourcesResponse
from openapi_server.models.list_traffic_policies_response import ListTrafficPoliciesResponse
from openapi_server.models.list_traffic_policy_instances_by_hosted_zone_response import ListTrafficPolicyInstancesByHostedZoneResponse
from openapi_server.models.list_traffic_policy_instances_by_policy_response import ListTrafficPolicyInstancesByPolicyResponse
from openapi_server.models.list_traffic_policy_instances_response import ListTrafficPolicyInstancesResponse
from openapi_server.models.list_traffic_policy_versions_response import ListTrafficPolicyVersionsResponse
from openapi_server.models.list_vpc_association_authorizations_response import ListVPCAssociationAuthorizationsResponse
from openapi_server.models.test_dns_answer_response import TestDNSAnswerResponse
from openapi_server.models.update_health_check_request import UpdateHealthCheckRequest
from openapi_server.models.update_health_check_response import UpdateHealthCheckResponse
from openapi_server.models.update_hosted_zone_comment_request import UpdateHostedZoneCommentRequest
from openapi_server.models.update_hosted_zone_comment_response import UpdateHostedZoneCommentResponse
from openapi_server.models.update_traffic_policy_comment_request import UpdateTrafficPolicyCommentRequest
from openapi_server.models.update_traffic_policy_comment_response import UpdateTrafficPolicyCommentResponse
from openapi_server.models.update_traffic_policy_instance_request import UpdateTrafficPolicyInstanceRequest
from openapi_server.models.update_traffic_policy_instance_response import UpdateTrafficPolicyInstanceResponse


pytestmark = pytest.mark.asyncio

async def test_activate_key_signing_key(client):
    """Test case for activate_key_signing_key

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/keysigningkey/{hosted_zone_id}/{name}/activate'.format(hosted_zone_id='hosted_zone_id_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_associate_vpc_with_hosted_zone(client):
    """Test case for associate_vpc_with_hosted_zone

    
    """
    body = openapi_server.AssociateVPCWithHostedZoneRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone/{id}/associatevpc'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_change_cidr_collection(client):
    """Test case for change_cidr_collection

    
    """
    body = openapi_server.ChangeCidrCollectionRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/cidrcollection/{cidr_collection_id}'.format(cidr_collection_id='cidr_collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_change_tags_for_resource(client):
    """Test case for change_tags_for_resource

    
    """
    body = openapi_server.ChangeTagsForResourceRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/tags/{resource_type}/{resource_id}'.format(resource_type='resource_type_example', resource_id='resource_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_cidr_collection(client):
    """Test case for create_cidr_collection

    
    """
    body = openapi_server.CreateCidrCollectionRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/cidrcollection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_health_check(client):
    """Test case for create_health_check

    
    """
    body = openapi_server.CreateHealthCheckRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/healthcheck',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_hosted_zone(client):
    """Test case for create_hosted_zone

    
    """
    body = openapi_server.CreateHostedZoneRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_key_signing_key(client):
    """Test case for create_key_signing_key

    
    """
    body = openapi_server.CreateKeySigningKeyRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/keysigningkey',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_query_logging_config(client):
    """Test case for create_query_logging_config

    
    """
    body = openapi_server.CreateQueryLoggingConfigRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/queryloggingconfig',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_reusable_delegation_set(client):
    """Test case for create_reusable_delegation_set

    
    """
    body = openapi_server.CreateReusableDelegationSetRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/delegationset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_traffic_policy(client):
    """Test case for create_traffic_policy

    
    """
    body = openapi_server.CreateTrafficPolicyRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/trafficpolicy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_traffic_policy_instance(client):
    """Test case for create_traffic_policy_instance

    
    """
    body = openapi_server.CreateTrafficPolicyInstanceRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/trafficpolicyinstance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_traffic_policy_version(client):
    """Test case for create_traffic_policy_version

    
    """
    body = openapi_server.CreateTrafficPolicyVersionRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/trafficpolicy/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_vpc_association_authorization(client):
    """Test case for create_vpc_association_authorization

    
    """
    body = openapi_server.CreateVPCAssociationAuthorizationRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone/{id}/authorizevpcassociation'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_key_signing_key(client):
    """Test case for deactivate_key_signing_key

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/keysigningkey/{hosted_zone_id}/{name}/deactivate'.format(hosted_zone_id='hosted_zone_id_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cidr_collection(client):
    """Test case for delete_cidr_collection

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/cidrcollection/{cidr_collection_id}'.format(cidr_collection_id='cidr_collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_health_check(client):
    """Test case for delete_health_check

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/healthcheck/{health_check_id}'.format(health_check_id='health_check_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hosted_zone(client):
    """Test case for delete_hosted_zone

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/hostedzone/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_key_signing_key(client):
    """Test case for delete_key_signing_key

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/keysigningkey/{hosted_zone_id}/{name}'.format(hosted_zone_id='hosted_zone_id_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_query_logging_config(client):
    """Test case for delete_query_logging_config

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/queryloggingconfig/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_reusable_delegation_set(client):
    """Test case for delete_reusable_delegation_set

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/delegationset/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_traffic_policy(client):
    """Test case for delete_traffic_policy

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/trafficpolicy/{id}/{version}'.format(id='id_example', version=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_traffic_policy_instance(client):
    """Test case for delete_traffic_policy_instance

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2013-04-01/trafficpolicyinstance/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_delete_vpc_association_authorization(client):
    """Test case for delete_vpc_association_authorization

    
    """
    body = openapi_server.CreateVPCAssociationAuthorizationRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone/{id}/deauthorizevpcassociation'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_hosted_zone_dnssec(client):
    """Test case for disable_hosted_zone_dnssec

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone/{id}/disable-dnssec'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_disassociate_vpc_from_hosted_zone(client):
    """Test case for disassociate_vpc_from_hosted_zone

    
    """
    body = openapi_server.DisassociateVPCFromHostedZoneRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone/{id}/disassociatevpc'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_hosted_zone_dnssec(client):
    """Test case for enable_hosted_zone_dnssec

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone/{id}/enable-dnssec'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_limit(client):
    """Test case for get_account_limit

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/accountlimit/{type}'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_change(client):
    """Test case for get_change

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/change/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checker_ip_ranges(client):
    """Test case for get_checker_ip_ranges

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/checkeripranges',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dnssec(client):
    """Test case for get_dnssec

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzone/{id}/dnssec'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_geo_location(client):
    """Test case for get_geo_location

    
    """
    params = [('continentcode', 'continentcode_example'),
                    ('countrycode', 'countrycode_example'),
                    ('subdivisioncode', 'subdivisioncode_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/geolocation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_health_check(client):
    """Test case for get_health_check

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/healthcheck/{health_check_id}'.format(health_check_id='health_check_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_health_check_count(client):
    """Test case for get_health_check_count

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/healthcheckcount',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_health_check_last_failure_reason(client):
    """Test case for get_health_check_last_failure_reason

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/healthcheck/{health_check_id}/lastfailurereason'.format(health_check_id='health_check_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_health_check_status(client):
    """Test case for get_health_check_status

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/healthcheck/{health_check_id}/status'.format(health_check_id='health_check_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hosted_zone(client):
    """Test case for get_hosted_zone

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzone/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hosted_zone_count(client):
    """Test case for get_hosted_zone_count

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzonecount',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hosted_zone_limit(client):
    """Test case for get_hosted_zone_limit

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzonelimit/{id}/{type}'.format(type='type_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_logging_config(client):
    """Test case for get_query_logging_config

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/queryloggingconfig/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reusable_delegation_set(client):
    """Test case for get_reusable_delegation_set

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/delegationset/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reusable_delegation_set_limit(client):
    """Test case for get_reusable_delegation_set_limit

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/reusabledelegationsetlimit/{id}/{type}'.format(type='type_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_traffic_policy(client):
    """Test case for get_traffic_policy

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicy/{id}/{version}'.format(id='id_example', version=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_traffic_policy_instance(client):
    """Test case for get_traffic_policy_instance

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicyinstance/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_traffic_policy_instance_count(client):
    """Test case for get_traffic_policy_instance_count

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicyinstancecount',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cidr_blocks(client):
    """Test case for list_cidr_blocks

    
    """
    params = [('location', 'location_example'),
                    ('nexttoken', 'nexttoken_example'),
                    ('maxresults', 'maxresults_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/cidrcollection/{cidr_collection_id}/cidrblocks'.format(cidr_collection_id='cidr_collection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cidr_collections(client):
    """Test case for list_cidr_collections

    
    """
    params = [('nexttoken', 'nexttoken_example'),
                    ('maxresults', 'maxresults_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/cidrcollection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cidr_locations(client):
    """Test case for list_cidr_locations

    
    """
    params = [('nexttoken', 'nexttoken_example'),
                    ('maxresults', 'maxresults_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/cidrcollection/{cidr_collection_id}'.format(cidr_collection_id='cidr_collection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_geo_locations(client):
    """Test case for list_geo_locations

    
    """
    params = [('startcontinentcode', 'startcontinentcode_example'),
                    ('startcountrycode', 'startcountrycode_example'),
                    ('startsubdivisioncode', 'startsubdivisioncode_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/geolocations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_health_checks(client):
    """Test case for list_health_checks

    
    """
    params = [('marker', 'marker_example'),
                    ('maxitems', 'maxitems_example'),
                    ('MaxItems', 'max_items_example'),
                    ('Marker', 'marker_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/healthcheck',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hosted_zones(client):
    """Test case for list_hosted_zones

    
    """
    params = [('marker', 'marker_example'),
                    ('maxitems', 'maxitems_example'),
                    ('delegationsetid', 'delegationsetid_example'),
                    ('MaxItems', 'max_items_example'),
                    ('Marker', 'marker_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hosted_zones_by_name(client):
    """Test case for list_hosted_zones_by_name

    
    """
    params = [('dnsname', 'dnsname_example'),
                    ('hostedzoneid', 'hostedzoneid_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzonesbyname',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hosted_zones_by_vpc(client):
    """Test case for list_hosted_zones_by_vpc

    
    """
    params = [('vpcid', 'vpcid_example'),
                    ('vpcregion', 'vpcregion_example'),
                    ('maxitems', 'maxitems_example'),
                    ('nexttoken', 'nexttoken_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzonesbyvpc#vpcid&vpcregion',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_query_logging_configs(client):
    """Test case for list_query_logging_configs

    
    """
    params = [('hostedzoneid', 'hostedzoneid_example'),
                    ('nexttoken', 'nexttoken_example'),
                    ('maxresults', 'maxresults_example'),
                    ('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/queryloggingconfig',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_resource_record_sets(client):
    """Test case for list_resource_record_sets

    
    """
    params = [('name', 'name_example'),
                    ('type', 'type_example'),
                    ('identifier', 'identifier_example'),
                    ('maxitems', 'maxitems_example'),
                    ('MaxItems', 'max_items_example'),
                    ('StartRecordName', 'start_record_name_example'),
                    ('StartRecordType', 'start_record_type_example'),
                    ('StartRecordIdentifier', 'start_record_identifier_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzone/{id}/rrset'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_reusable_delegation_sets(client):
    """Test case for list_reusable_delegation_sets

    
    """
    params = [('marker', 'marker_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/delegationset',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/tags/{resource_type}/{resource_id}'.format(resource_type='resource_type_example', resource_id='resource_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_list_tags_for_resources(client):
    """Test case for list_tags_for_resources

    
    """
    body = openapi_server.ListTagsForResourcesRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/tags/{resource_type}'.format(resource_type='resource_type_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_traffic_policies(client):
    """Test case for list_traffic_policies

    
    """
    params = [('trafficpolicyid', 'trafficpolicyid_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_traffic_policy_instances(client):
    """Test case for list_traffic_policy_instances

    
    """
    params = [('hostedzoneid', 'hostedzoneid_example'),
                    ('trafficpolicyinstancename', 'trafficpolicyinstancename_example'),
                    ('trafficpolicyinstancetype', 'trafficpolicyinstancetype_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicyinstances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_traffic_policy_instances_by_hosted_zone(client):
    """Test case for list_traffic_policy_instances_by_hosted_zone

    
    """
    params = [('id', 'id_example'),
                    ('trafficpolicyinstancename', 'trafficpolicyinstancename_example'),
                    ('trafficpolicyinstancetype', 'trafficpolicyinstancetype_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicyinstances/hostedzone#id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_traffic_policy_instances_by_policy(client):
    """Test case for list_traffic_policy_instances_by_policy

    
    """
    params = [('id', 'id_example'),
                    ('version', 56),
                    ('hostedzoneid', 'hostedzoneid_example'),
                    ('trafficpolicyinstancename', 'trafficpolicyinstancename_example'),
                    ('trafficpolicyinstancetype', 'trafficpolicyinstancetype_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicyinstances/trafficpolicy#id&version',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_traffic_policy_versions(client):
    """Test case for list_traffic_policy_versions

    
    """
    params = [('trafficpolicyversion', 'trafficpolicyversion_example'),
                    ('maxitems', 'maxitems_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/trafficpolicies/{id}/versions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_vpc_association_authorizations(client):
    """Test case for list_vpc_association_authorizations

    
    """
    params = [('nexttoken', 'nexttoken_example'),
                    ('maxresults', 'maxresults_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/hostedzone/{id}/authorizevpcassociation'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_dns_answer(client):
    """Test case for test_dns_answer

    
    """
    params = [('hostedzoneid', 'hostedzoneid_example'),
                    ('recordname', 'recordname_example'),
                    ('recordtype', 'recordtype_example'),
                    ('resolverip', 'resolverip_example'),
                    ('edns0clientsubnetip', 'edns0clientsubnetip_example'),
                    ('edns0clientsubnetmask', 'edns0clientsubnetmask_example')]
    headers = { 
        'Accept': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/2013-04-01/testdnsanswer#hostedzoneid&recordname&recordtype',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_health_check(client):
    """Test case for update_health_check

    
    """
    body = openapi_server.UpdateHealthCheckRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/healthcheck/{health_check_id}'.format(health_check_id='health_check_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_hosted_zone_comment(client):
    """Test case for update_hosted_zone_comment

    
    """
    body = openapi_server.UpdateHostedZoneCommentRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/hostedzone/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_traffic_policy_comment(client):
    """Test case for update_traffic_policy_comment

    
    """
    body = openapi_server.UpdateTrafficPolicyCommentRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/trafficpolicy/{id}/{version}'.format(id='id_example', version=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_traffic_policy_instance(client):
    """Test case for update_traffic_policy_instance

    
    """
    body = openapi_server.UpdateTrafficPolicyInstanceRequest()
    headers = { 
        'Accept': 'text/xml',
        'Content-Type': 'text/xml',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/2013-04-01/trafficpolicyinstance/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

