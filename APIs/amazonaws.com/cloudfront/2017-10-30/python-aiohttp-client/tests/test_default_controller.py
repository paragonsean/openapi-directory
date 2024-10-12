# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.batch_too_large import BatchTooLarge
from openapi_server.models.cname_already_exists import CNAMEAlreadyExists
from openapi_server.models.cannot_change_immutable_public_key_fields import CannotChangeImmutablePublicKeyFields
from openapi_server.models.cloud_front_origin_access_identity_already_exists import CloudFrontOriginAccessIdentityAlreadyExists
from openapi_server.models.cloud_front_origin_access_identity_in_use import CloudFrontOriginAccessIdentityInUse
from openapi_server.models.create_cloud_front_origin_access_identity20171030_request import CreateCloudFrontOriginAccessIdentity20171030Request
from openapi_server.models.create_cloud_front_origin_access_identity_result import CreateCloudFrontOriginAccessIdentityResult
from openapi_server.models.create_distribution20171030_request import CreateDistribution20171030Request
from openapi_server.models.create_distribution_result import CreateDistributionResult
from openapi_server.models.create_distribution_with_tags20171030_request import CreateDistributionWithTags20171030Request
from openapi_server.models.create_distribution_with_tags_result import CreateDistributionWithTagsResult
from openapi_server.models.create_field_level_encryption_config20171030_request import CreateFieldLevelEncryptionConfig20171030Request
from openapi_server.models.create_field_level_encryption_config_result import CreateFieldLevelEncryptionConfigResult
from openapi_server.models.create_field_level_encryption_profile20171030_request import CreateFieldLevelEncryptionProfile20171030Request
from openapi_server.models.create_field_level_encryption_profile_result import CreateFieldLevelEncryptionProfileResult
from openapi_server.models.create_invalidation20171030_request import CreateInvalidation20171030Request
from openapi_server.models.create_invalidation_result import CreateInvalidationResult
from openapi_server.models.create_public_key20171030_request import CreatePublicKey20171030Request
from openapi_server.models.create_public_key_result import CreatePublicKeyResult
from openapi_server.models.create_streaming_distribution20171030_request import CreateStreamingDistribution20171030Request
from openapi_server.models.create_streaming_distribution_result import CreateStreamingDistributionResult
from openapi_server.models.create_streaming_distribution_with_tags20171030_request import CreateStreamingDistributionWithTags20171030Request
from openapi_server.models.create_streaming_distribution_with_tags_result import CreateStreamingDistributionWithTagsResult
from openapi_server.models.distribution_already_exists import DistributionAlreadyExists
from openapi_server.models.distribution_not_disabled import DistributionNotDisabled
from openapi_server.models.field_level_encryption_config_already_exists import FieldLevelEncryptionConfigAlreadyExists
from openapi_server.models.field_level_encryption_config_in_use import FieldLevelEncryptionConfigInUse
from openapi_server.models.field_level_encryption_profile_already_exists import FieldLevelEncryptionProfileAlreadyExists
from openapi_server.models.field_level_encryption_profile_in_use import FieldLevelEncryptionProfileInUse
from openapi_server.models.field_level_encryption_profile_size_exceeded import FieldLevelEncryptionProfileSizeExceeded
from openapi_server.models.get_cloud_front_origin_access_identity_config_result import GetCloudFrontOriginAccessIdentityConfigResult
from openapi_server.models.get_cloud_front_origin_access_identity_result import GetCloudFrontOriginAccessIdentityResult
from openapi_server.models.get_distribution_config_result import GetDistributionConfigResult
from openapi_server.models.get_distribution_result import GetDistributionResult
from openapi_server.models.get_field_level_encryption_config_result import GetFieldLevelEncryptionConfigResult
from openapi_server.models.get_field_level_encryption_profile_config_result import GetFieldLevelEncryptionProfileConfigResult
from openapi_server.models.get_field_level_encryption_profile_result import GetFieldLevelEncryptionProfileResult
from openapi_server.models.get_field_level_encryption_result import GetFieldLevelEncryptionResult
from openapi_server.models.get_invalidation_result import GetInvalidationResult
from openapi_server.models.get_public_key_config_result import GetPublicKeyConfigResult
from openapi_server.models.get_public_key_result import GetPublicKeyResult
from openapi_server.models.get_streaming_distribution_config_result import GetStreamingDistributionConfigResult
from openapi_server.models.get_streaming_distribution_result import GetStreamingDistributionResult
from openapi_server.models.illegal_field_level_encryption_config_association_with_cache_behavior import IllegalFieldLevelEncryptionConfigAssociationWithCacheBehavior
from openapi_server.models.illegal_update import IllegalUpdate
from openapi_server.models.inconsistent_quantities import InconsistentQuantities
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.invalid_default_root_object import InvalidDefaultRootObject
from openapi_server.models.invalid_error_code import InvalidErrorCode
from openapi_server.models.invalid_forward_cookies import InvalidForwardCookies
from openapi_server.models.invalid_geo_restriction_parameter import InvalidGeoRestrictionParameter
from openapi_server.models.invalid_headers_for_s3_origin import InvalidHeadersForS3Origin
from openapi_server.models.invalid_if_match_version import InvalidIfMatchVersion
from openapi_server.models.invalid_lambda_function_association import InvalidLambdaFunctionAssociation
from openapi_server.models.invalid_location_code import InvalidLocationCode
from openapi_server.models.invalid_minimum_protocol_version import InvalidMinimumProtocolVersion
from openapi_server.models.invalid_origin import InvalidOrigin
from openapi_server.models.invalid_origin_access_identity import InvalidOriginAccessIdentity
from openapi_server.models.invalid_origin_keepalive_timeout import InvalidOriginKeepaliveTimeout
from openapi_server.models.invalid_origin_read_timeout import InvalidOriginReadTimeout
from openapi_server.models.invalid_protocol_settings import InvalidProtocolSettings
from openapi_server.models.invalid_query_string_parameters import InvalidQueryStringParameters
from openapi_server.models.invalid_relative_path import InvalidRelativePath
from openapi_server.models.invalid_required_protocol import InvalidRequiredProtocol
from openapi_server.models.invalid_response_code import InvalidResponseCode
from openapi_server.models.invalid_ttl_order import InvalidTTLOrder
from openapi_server.models.invalid_tagging import InvalidTagging
from openapi_server.models.invalid_viewer_certificate import InvalidViewerCertificate
from openapi_server.models.invalid_web_aclid import InvalidWebACLId
from openapi_server.models.list_cloud_front_origin_access_identities_result import ListCloudFrontOriginAccessIdentitiesResult
from openapi_server.models.list_distributions_by_web_aclid_result import ListDistributionsByWebACLIdResult
from openapi_server.models.list_distributions_result import ListDistributionsResult
from openapi_server.models.list_field_level_encryption_configs_result import ListFieldLevelEncryptionConfigsResult
from openapi_server.models.list_field_level_encryption_profiles_result import ListFieldLevelEncryptionProfilesResult
from openapi_server.models.list_invalidations_result import ListInvalidationsResult
from openapi_server.models.list_public_keys_result import ListPublicKeysResult
from openapi_server.models.list_streaming_distributions_result import ListStreamingDistributionsResult
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.missing_body import MissingBody
from openapi_server.models.no_such_cloud_front_origin_access_identity import NoSuchCloudFrontOriginAccessIdentity
from openapi_server.models.no_such_distribution import NoSuchDistribution
from openapi_server.models.no_such_field_level_encryption_config import NoSuchFieldLevelEncryptionConfig
from openapi_server.models.no_such_field_level_encryption_profile import NoSuchFieldLevelEncryptionProfile
from openapi_server.models.no_such_invalidation import NoSuchInvalidation
from openapi_server.models.no_such_origin import NoSuchOrigin
from openapi_server.models.no_such_public_key import NoSuchPublicKey
from openapi_server.models.no_such_resource import NoSuchResource
from openapi_server.models.no_such_streaming_distribution import NoSuchStreamingDistribution
from openapi_server.models.precondition_failed import PreconditionFailed
from openapi_server.models.public_key_already_exists import PublicKeyAlreadyExists
from openapi_server.models.public_key_in_use import PublicKeyInUse
from openapi_server.models.query_arg_profile_empty import QueryArgProfileEmpty
from openapi_server.models.streaming_distribution_already_exists import StreamingDistributionAlreadyExists
from openapi_server.models.streaming_distribution_not_disabled import StreamingDistributionNotDisabled
from openapi_server.models.tag_resource20171030_request import TagResource20171030Request
from openapi_server.models.too_many_cache_behaviors import TooManyCacheBehaviors
from openapi_server.models.too_many_certificates import TooManyCertificates
from openapi_server.models.too_many_cloud_front_origin_access_identities import TooManyCloudFrontOriginAccessIdentities
from openapi_server.models.too_many_cookie_names_in_white_list import TooManyCookieNamesInWhiteList
from openapi_server.models.too_many_distribution_cnames import TooManyDistributionCNAMEs
from openapi_server.models.too_many_distributions import TooManyDistributions
from openapi_server.models.too_many_distributions_associated_to_field_level_encryption_config import TooManyDistributionsAssociatedToFieldLevelEncryptionConfig
from openapi_server.models.too_many_distributions_with_lambda_associations import TooManyDistributionsWithLambdaAssociations
from openapi_server.models.too_many_field_level_encryption_configs import TooManyFieldLevelEncryptionConfigs
from openapi_server.models.too_many_field_level_encryption_content_type_profiles import TooManyFieldLevelEncryptionContentTypeProfiles
from openapi_server.models.too_many_field_level_encryption_encryption_entities import TooManyFieldLevelEncryptionEncryptionEntities
from openapi_server.models.too_many_field_level_encryption_field_patterns import TooManyFieldLevelEncryptionFieldPatterns
from openapi_server.models.too_many_field_level_encryption_profiles import TooManyFieldLevelEncryptionProfiles
from openapi_server.models.too_many_field_level_encryption_query_arg_profiles import TooManyFieldLevelEncryptionQueryArgProfiles
from openapi_server.models.too_many_headers_in_forwarded_values import TooManyHeadersInForwardedValues
from openapi_server.models.too_many_invalidations_in_progress import TooManyInvalidationsInProgress
from openapi_server.models.too_many_lambda_function_associations import TooManyLambdaFunctionAssociations
from openapi_server.models.too_many_origin_custom_headers import TooManyOriginCustomHeaders
from openapi_server.models.too_many_origins import TooManyOrigins
from openapi_server.models.too_many_public_keys import TooManyPublicKeys
from openapi_server.models.too_many_query_string_parameters import TooManyQueryStringParameters
from openapi_server.models.too_many_streaming_distribution_cnames import TooManyStreamingDistributionCNAMEs
from openapi_server.models.too_many_streaming_distributions import TooManyStreamingDistributions
from openapi_server.models.too_many_trusted_signers import TooManyTrustedSigners
from openapi_server.models.trusted_signer_does_not_exist import TrustedSignerDoesNotExist
from openapi_server.models.untag_resource20171030_request import UntagResource20171030Request
from openapi_server.models.update_cloud_front_origin_access_identity_result import UpdateCloudFrontOriginAccessIdentityResult
from openapi_server.models.update_distribution_result import UpdateDistributionResult
from openapi_server.models.update_field_level_encryption_config_result import UpdateFieldLevelEncryptionConfigResult
from openapi_server.models.update_field_level_encryption_profile_result import UpdateFieldLevelEncryptionProfileResult
from openapi_server.models.update_public_key_result import UpdatePublicKeyResult
from openapi_server.models.update_streaming_distribution_result import UpdateStreamingDistributionResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_cloud_front_origin_access_identity20171030(client):
    """Test case for create_cloud_front_origin_access_identity20171030

    
    """
    body = openapi_server.CreateCloudFrontOriginAccessIdentity20171030Request()
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
        path='/2017-10-30/origin-access-identity/cloudfront',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_distribution20171030(client):
    """Test case for create_distribution20171030

    
    """
    body = openapi_server.CreateDistribution20171030Request()
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
        path='/2017-10-30/distribution',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_distribution_with_tags20171030(client):
    """Test case for create_distribution_with_tags20171030

    
    """
    body = openapi_server.CreateDistributionWithTags20171030Request()
    params = [('WithTags', True)]
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
        path='/2017-10-30/distribution#WithTags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_field_level_encryption_config20171030(client):
    """Test case for create_field_level_encryption_config20171030

    
    """
    body = openapi_server.CreateFieldLevelEncryptionConfig20171030Request()
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
        path='/2017-10-30/field-level-encryption',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_field_level_encryption_profile20171030(client):
    """Test case for create_field_level_encryption_profile20171030

    
    """
    body = openapi_server.CreateFieldLevelEncryptionProfile20171030Request()
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
        path='/2017-10-30/field-level-encryption-profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_invalidation20171030(client):
    """Test case for create_invalidation20171030

    
    """
    body = openapi_server.CreateInvalidation20171030Request()
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
        path='/2017-10-30/distribution/{distribution_id}/invalidation'.format(distribution_id='distribution_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_public_key20171030(client):
    """Test case for create_public_key20171030

    
    """
    body = openapi_server.CreatePublicKey20171030Request()
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
        path='/2017-10-30/public-key',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_streaming_distribution20171030(client):
    """Test case for create_streaming_distribution20171030

    
    """
    body = openapi_server.CreateStreamingDistribution20171030Request()
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
        path='/2017-10-30/streaming-distribution',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_create_streaming_distribution_with_tags20171030(client):
    """Test case for create_streaming_distribution_with_tags20171030

    
    """
    body = openapi_server.CreateStreamingDistributionWithTags20171030Request()
    params = [('WithTags', True)]
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
        path='/2017-10-30/streaming-distribution#WithTags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cloud_front_origin_access_identity20171030(client):
    """Test case for delete_cloud_front_origin_access_identity20171030

    
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-10-30/origin-access-identity/cloudfront/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_distribution20171030(client):
    """Test case for delete_distribution20171030

    
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-10-30/distribution/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_field_level_encryption_config20171030(client):
    """Test case for delete_field_level_encryption_config20171030

    
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-10-30/field-level-encryption/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_field_level_encryption_profile20171030(client):
    """Test case for delete_field_level_encryption_profile20171030

    
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-10-30/field-level-encryption-profile/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_public_key20171030(client):
    """Test case for delete_public_key20171030

    
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-10-30/public-key/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_streaming_distribution20171030(client):
    """Test case for delete_streaming_distribution20171030

    
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/2017-10-30/streaming-distribution/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cloud_front_origin_access_identity20171030(client):
    """Test case for get_cloud_front_origin_access_identity20171030

    
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
        path='/2017-10-30/origin-access-identity/cloudfront/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cloud_front_origin_access_identity_config20171030(client):
    """Test case for get_cloud_front_origin_access_identity_config20171030

    
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
        path='/2017-10-30/origin-access-identity/cloudfront/{id}/config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_distribution20171030(client):
    """Test case for get_distribution20171030

    
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
        path='/2017-10-30/distribution/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_distribution_config20171030(client):
    """Test case for get_distribution_config20171030

    
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
        path='/2017-10-30/distribution/{id}/config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_level_encryption20171030(client):
    """Test case for get_field_level_encryption20171030

    
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
        path='/2017-10-30/field-level-encryption/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_level_encryption_config20171030(client):
    """Test case for get_field_level_encryption_config20171030

    
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
        path='/2017-10-30/field-level-encryption/{id}/config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_level_encryption_profile20171030(client):
    """Test case for get_field_level_encryption_profile20171030

    
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
        path='/2017-10-30/field-level-encryption-profile/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_level_encryption_profile_config20171030(client):
    """Test case for get_field_level_encryption_profile_config20171030

    
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
        path='/2017-10-30/field-level-encryption-profile/{id}/config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invalidation20171030(client):
    """Test case for get_invalidation20171030

    
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
        path='/2017-10-30/distribution/{distribution_id}/invalidation/{id}'.format(distribution_id='distribution_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_key20171030(client):
    """Test case for get_public_key20171030

    
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
        path='/2017-10-30/public-key/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_key_config20171030(client):
    """Test case for get_public_key_config20171030

    
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
        path='/2017-10-30/public-key/{id}/config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_streaming_distribution20171030(client):
    """Test case for get_streaming_distribution20171030

    
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
        path='/2017-10-30/streaming-distribution/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_streaming_distribution_config20171030(client):
    """Test case for get_streaming_distribution_config20171030

    
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
        path='/2017-10-30/streaming-distribution/{id}/config'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_cloud_front_origin_access_identities20171030(client):
    """Test case for list_cloud_front_origin_access_identities20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/origin-access-identity/cloudfront',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_distributions20171030(client):
    """Test case for list_distributions20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/distribution',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_distributions_by_web_aclid20171030(client):
    """Test case for list_distributions_by_web_aclid20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/distributionsByWebACLId/{web_aclid}'.format(web_aclid='web_aclid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_field_level_encryption_configs20171030(client):
    """Test case for list_field_level_encryption_configs20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/field-level-encryption',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_field_level_encryption_profiles20171030(client):
    """Test case for list_field_level_encryption_profiles20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/field-level-encryption-profile',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_invalidations20171030(client):
    """Test case for list_invalidations20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/distribution/{distribution_id}/invalidation'.format(distribution_id='distribution_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_public_keys20171030(client):
    """Test case for list_public_keys20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/public-key',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_streaming_distributions20171030(client):
    """Test case for list_streaming_distributions20171030

    
    """
    params = [('Marker', 'marker_example'),
                    ('MaxItems', 'max_items_example')]
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
        path='/2017-10-30/streaming-distribution',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource20171030(client):
    """Test case for list_tags_for_resource20171030

    
    """
    params = [('Resource', 'resource_example')]
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
        path='/2017-10-30/tagging#Resource',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_tag_resource20171030(client):
    """Test case for tag_resource20171030

    
    """
    body = openapi_server.TagResource20171030Request()
    params = [('Resource', 'resource_example'),
                    ('Operation', 'operation_example')]
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
        path='/2017-10-30/tagging#Operation=Tag&Resource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_untag_resource20171030(client):
    """Test case for untag_resource20171030

    
    """
    body = openapi_server.UntagResource20171030Request()
    params = [('Resource', 'resource_example'),
                    ('Operation', 'operation_example')]
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
        path='/2017-10-30/tagging#Operation=Untag&Resource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_cloud_front_origin_access_identity20171030(client):
    """Test case for update_cloud_front_origin_access_identity20171030

    
    """
    body = openapi_server.CreateCloudFrontOriginAccessIdentity20171030Request()
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-10-30/origin-access-identity/cloudfront/{id}/config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_distribution20171030(client):
    """Test case for update_distribution20171030

    
    """
    body = openapi_server.CreateDistribution20171030Request()
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-10-30/distribution/{id}/config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_field_level_encryption_config20171030(client):
    """Test case for update_field_level_encryption_config20171030

    
    """
    body = openapi_server.CreateFieldLevelEncryptionConfig20171030Request()
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-10-30/field-level-encryption/{id}/config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_field_level_encryption_profile20171030(client):
    """Test case for update_field_level_encryption_profile20171030

    
    """
    body = openapi_server.CreateFieldLevelEncryptionProfile20171030Request()
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-10-30/field-level-encryption-profile/{id}/config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_public_key20171030(client):
    """Test case for update_public_key20171030

    
    """
    body = openapi_server.CreatePublicKey20171030Request()
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-10-30/public-key/{id}/config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/xml not supported by Connexion")
async def test_update_streaming_distribution20171030(client):
    """Test case for update_streaming_distribution20171030

    
    """
    body = openapi_server.CreateStreamingDistribution20171030Request()
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
        'if_match': 'if_match_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/2017-10-30/streaming-distribution/{id}/config'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

