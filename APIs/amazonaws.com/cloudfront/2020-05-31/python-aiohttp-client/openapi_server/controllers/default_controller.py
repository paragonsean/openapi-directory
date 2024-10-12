from typing import List, Dict
from aiohttp import web

from openapi_server.models.copy_distribution20200531_request import CopyDistribution20200531Request
from openapi_server.models.copy_distribution_result import CopyDistributionResult
from openapi_server.models.create_cache_policy20200531_request import CreateCachePolicy20200531Request
from openapi_server.models.create_cache_policy_result import CreateCachePolicyResult
from openapi_server.models.create_cloud_front_origin_access_identity20200531_request import CreateCloudFrontOriginAccessIdentity20200531Request
from openapi_server.models.create_cloud_front_origin_access_identity_result import CreateCloudFrontOriginAccessIdentityResult
from openapi_server.models.create_continuous_deployment_policy20200531_request import CreateContinuousDeploymentPolicy20200531Request
from openapi_server.models.create_continuous_deployment_policy_result import CreateContinuousDeploymentPolicyResult
from openapi_server.models.create_distribution20200531_request import CreateDistribution20200531Request
from openapi_server.models.create_distribution_result import CreateDistributionResult
from openapi_server.models.create_distribution_with_tags20200531_request import CreateDistributionWithTags20200531Request
from openapi_server.models.create_distribution_with_tags_result import CreateDistributionWithTagsResult
from openapi_server.models.create_field_level_encryption_config20200531_request import CreateFieldLevelEncryptionConfig20200531Request
from openapi_server.models.create_field_level_encryption_config_result import CreateFieldLevelEncryptionConfigResult
from openapi_server.models.create_field_level_encryption_profile20200531_request import CreateFieldLevelEncryptionProfile20200531Request
from openapi_server.models.create_field_level_encryption_profile_result import CreateFieldLevelEncryptionProfileResult
from openapi_server.models.create_function20200531_request import CreateFunction20200531Request
from openapi_server.models.create_function_result import CreateFunctionResult
from openapi_server.models.create_invalidation20200531_request import CreateInvalidation20200531Request
from openapi_server.models.create_invalidation_result import CreateInvalidationResult
from openapi_server.models.create_key_group20200531_request import CreateKeyGroup20200531Request
from openapi_server.models.create_key_group_result import CreateKeyGroupResult
from openapi_server.models.create_monitoring_subscription20200531_request import CreateMonitoringSubscription20200531Request
from openapi_server.models.create_monitoring_subscription_result import CreateMonitoringSubscriptionResult
from openapi_server.models.create_origin_access_control20200531_request import CreateOriginAccessControl20200531Request
from openapi_server.models.create_origin_access_control_result import CreateOriginAccessControlResult
from openapi_server.models.create_origin_request_policy20200531_request import CreateOriginRequestPolicy20200531Request
from openapi_server.models.create_origin_request_policy_result import CreateOriginRequestPolicyResult
from openapi_server.models.create_public_key20200531_request import CreatePublicKey20200531Request
from openapi_server.models.create_public_key_result import CreatePublicKeyResult
from openapi_server.models.create_realtime_log_config20200531_request import CreateRealtimeLogConfig20200531Request
from openapi_server.models.create_realtime_log_config_result import CreateRealtimeLogConfigResult
from openapi_server.models.create_response_headers_policy20200531_request import CreateResponseHeadersPolicy20200531Request
from openapi_server.models.create_response_headers_policy_result import CreateResponseHeadersPolicyResult
from openapi_server.models.create_streaming_distribution20200531_request import CreateStreamingDistribution20200531Request
from openapi_server.models.create_streaming_distribution_result import CreateStreamingDistributionResult
from openapi_server.models.create_streaming_distribution_with_tags20200531_request import CreateStreamingDistributionWithTags20200531Request
from openapi_server.models.create_streaming_distribution_with_tags_result import CreateStreamingDistributionWithTagsResult
from openapi_server.models.delete_realtime_log_config20200531_request import DeleteRealtimeLogConfig20200531Request
from openapi_server.models.describe_function_result import DescribeFunctionResult
from openapi_server.models.get_cache_policy_config_result import GetCachePolicyConfigResult
from openapi_server.models.get_cache_policy_result import GetCachePolicyResult
from openapi_server.models.get_cloud_front_origin_access_identity_config_result import GetCloudFrontOriginAccessIdentityConfigResult
from openapi_server.models.get_cloud_front_origin_access_identity_result import GetCloudFrontOriginAccessIdentityResult
from openapi_server.models.get_continuous_deployment_policy_config_result import GetContinuousDeploymentPolicyConfigResult
from openapi_server.models.get_continuous_deployment_policy_result import GetContinuousDeploymentPolicyResult
from openapi_server.models.get_distribution_config_result import GetDistributionConfigResult
from openapi_server.models.get_distribution_result import GetDistributionResult
from openapi_server.models.get_field_level_encryption_config_result import GetFieldLevelEncryptionConfigResult
from openapi_server.models.get_field_level_encryption_profile_config_result import GetFieldLevelEncryptionProfileConfigResult
from openapi_server.models.get_field_level_encryption_profile_result import GetFieldLevelEncryptionProfileResult
from openapi_server.models.get_field_level_encryption_result import GetFieldLevelEncryptionResult
from openapi_server.models.get_function_result import GetFunctionResult
from openapi_server.models.get_invalidation_result import GetInvalidationResult
from openapi_server.models.get_key_group_config_result import GetKeyGroupConfigResult
from openapi_server.models.get_key_group_result import GetKeyGroupResult
from openapi_server.models.get_monitoring_subscription_result import GetMonitoringSubscriptionResult
from openapi_server.models.get_origin_access_control_config_result import GetOriginAccessControlConfigResult
from openapi_server.models.get_origin_access_control_result import GetOriginAccessControlResult
from openapi_server.models.get_origin_request_policy_config_result import GetOriginRequestPolicyConfigResult
from openapi_server.models.get_origin_request_policy_result import GetOriginRequestPolicyResult
from openapi_server.models.get_public_key_config_result import GetPublicKeyConfigResult
from openapi_server.models.get_public_key_result import GetPublicKeyResult
from openapi_server.models.get_realtime_log_config20200531_request import GetRealtimeLogConfig20200531Request
from openapi_server.models.get_realtime_log_config_result import GetRealtimeLogConfigResult
from openapi_server.models.get_response_headers_policy_config_result import GetResponseHeadersPolicyConfigResult
from openapi_server.models.get_response_headers_policy_result import GetResponseHeadersPolicyResult
from openapi_server.models.get_streaming_distribution_config_result import GetStreamingDistributionConfigResult
from openapi_server.models.get_streaming_distribution_result import GetStreamingDistributionResult
from openapi_server.models.list_cache_policies_result import ListCachePoliciesResult
from openapi_server.models.list_cloud_front_origin_access_identities_result import ListCloudFrontOriginAccessIdentitiesResult
from openapi_server.models.list_conflicting_aliases_result import ListConflictingAliasesResult
from openapi_server.models.list_continuous_deployment_policies_result import ListContinuousDeploymentPoliciesResult
from openapi_server.models.list_distributions_by_cache_policy_id_result import ListDistributionsByCachePolicyIdResult
from openapi_server.models.list_distributions_by_key_group_result import ListDistributionsByKeyGroupResult
from openapi_server.models.list_distributions_by_origin_request_policy_id_result import ListDistributionsByOriginRequestPolicyIdResult
from openapi_server.models.list_distributions_by_realtime_log_config20200531_request import ListDistributionsByRealtimeLogConfig20200531Request
from openapi_server.models.list_distributions_by_realtime_log_config_result import ListDistributionsByRealtimeLogConfigResult
from openapi_server.models.list_distributions_by_response_headers_policy_id_result import ListDistributionsByResponseHeadersPolicyIdResult
from openapi_server.models.list_distributions_by_web_aclid_result import ListDistributionsByWebACLIdResult
from openapi_server.models.list_distributions_result import ListDistributionsResult
from openapi_server.models.list_field_level_encryption_configs_result import ListFieldLevelEncryptionConfigsResult
from openapi_server.models.list_field_level_encryption_profiles_result import ListFieldLevelEncryptionProfilesResult
from openapi_server.models.list_functions_result import ListFunctionsResult
from openapi_server.models.list_invalidations_result import ListInvalidationsResult
from openapi_server.models.list_key_groups_result import ListKeyGroupsResult
from openapi_server.models.list_origin_access_controls_result import ListOriginAccessControlsResult
from openapi_server.models.list_origin_request_policies_result import ListOriginRequestPoliciesResult
from openapi_server.models.list_public_keys_result import ListPublicKeysResult
from openapi_server.models.list_realtime_log_configs_result import ListRealtimeLogConfigsResult
from openapi_server.models.list_response_headers_policies_result import ListResponseHeadersPoliciesResult
from openapi_server.models.list_streaming_distributions_result import ListStreamingDistributionsResult
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.publish_function_result import PublishFunctionResult
from openapi_server.models.tag_resource20200531_request import TagResource20200531Request
from openapi_server.models.test_function20200531_request import TestFunction20200531Request
from openapi_server.models.test_function_result import TestFunctionResult
from openapi_server.models.untag_resource20200531_request import UntagResource20200531Request
from openapi_server.models.update_cache_policy_result import UpdateCachePolicyResult
from openapi_server.models.update_cloud_front_origin_access_identity_result import UpdateCloudFrontOriginAccessIdentityResult
from openapi_server.models.update_continuous_deployment_policy_result import UpdateContinuousDeploymentPolicyResult
from openapi_server.models.update_distribution_result import UpdateDistributionResult
from openapi_server.models.update_distribution_with_staging_config_result import UpdateDistributionWithStagingConfigResult
from openapi_server.models.update_field_level_encryption_config_result import UpdateFieldLevelEncryptionConfigResult
from openapi_server.models.update_field_level_encryption_profile_result import UpdateFieldLevelEncryptionProfileResult
from openapi_server.models.update_function20200531_request import UpdateFunction20200531Request
from openapi_server.models.update_function_result import UpdateFunctionResult
from openapi_server.models.update_key_group_result import UpdateKeyGroupResult
from openapi_server.models.update_origin_access_control_result import UpdateOriginAccessControlResult
from openapi_server.models.update_origin_request_policy_result import UpdateOriginRequestPolicyResult
from openapi_server.models.update_public_key_result import UpdatePublicKeyResult
from openapi_server.models.update_realtime_log_config20200531_request import UpdateRealtimeLogConfig20200531Request
from openapi_server.models.update_realtime_log_config_result import UpdateRealtimeLogConfigResult
from openapi_server.models.update_response_headers_policy_result import UpdateResponseHeadersPolicyResult
from openapi_server.models.update_streaming_distribution_result import UpdateStreamingDistributionResult
from openapi_server import util


async def associate_alias20200531(request: web.Request, target_distribution_id, alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_alias20200531

    &lt;p&gt;Associates an alias (also known as a CNAME or an alternate domain name) with a CloudFront distribution.&lt;/p&gt; &lt;p&gt;With this operation you can move an alias that&#39;s already in use on a CloudFront distribution to a different distribution in one step. This prevents the downtime that could occur if you first remove the alias from one distribution and then separately add the alias to another distribution.&lt;/p&gt; &lt;p&gt;To use this operation to associate an alias with a distribution, you provide the alias and the ID of the target distribution for the alias. For more information, including how to set up the target distribution, prerequisites that you must complete, and other restrictions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\&quot;&gt;Moving an alternate domain name to a different distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param target_distribution_id: The ID of the distribution that you&#39;re associating the alias with.
    :type target_distribution_id: str
    :param alias: The alias (also known as a CNAME) to add to the target distribution.
    :type alias: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def copy_distribution20200531(request: web.Request, primary_distribution_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, staging=None, if_match=None) -> web.Response:
    """copy_distribution20200531

    &lt;p&gt;Creates a staging distribution using the configuration of the provided primary distribution. A staging distribution is a copy of an existing distribution (called the primary distribution) that you can use in a continuous deployment workflow.&lt;/p&gt; &lt;p&gt;After you create a staging distribution, you can use &lt;code&gt;UpdateDistribution&lt;/code&gt; to modify the staging distribution&#39;s configuration. Then you can use &lt;code&gt;CreateContinuousDeploymentPolicy&lt;/code&gt; to incrementally move traffic to the staging distribution.&lt;/p&gt; &lt;p&gt;This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\&quot;&gt;GetDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\&quot;&gt;CreateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CopyDistribution.html\&quot;&gt;CopyDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param primary_distribution_id: The identifier of the primary distribution whose configuration you are copying. To get a distribution ID, use &lt;code&gt;ListDistributions&lt;/code&gt;.
    :type primary_distribution_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param staging: The type of distribution that your primary distribution will be copied to. The only valid value is &lt;code&gt;True&lt;/code&gt;, indicating that you are copying to a staging distribution.
    :type staging: bool
    :param if_match: The version identifier of the primary distribution whose configuration you are copying. This is the &lt;code&gt;ETag&lt;/code&gt; value returned in the response to &lt;code&gt;GetDistribution&lt;/code&gt; and &lt;code&gt;GetDistributionConfig&lt;/code&gt;.
    :type if_match: str

    """
    body = CopyDistribution20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_cache_policy20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cache_policy20200531

    &lt;p&gt;Creates a cache policy.&lt;/p&gt; &lt;p&gt;After you create a cache policy, you can attach it to one or more cache behaviors. When it&#39;s attached to a cache behavior, the cache policy determines the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The values that CloudFront includes in the &lt;i&gt;cache key&lt;/i&gt;. These values can include HTTP headers, cookies, and URL query strings. CloudFront uses the cache key to find an object in its cache that it can return to the viewer.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The default, minimum, and maximum time to live (TTL) values that you want objects to stay in the CloudFront cache.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The headers, cookies, and query strings that are included in the cache key are also included in requests that CloudFront sends to the origin. CloudFront sends a request when it can&#39;t find an object in its cache that matches the request&#39;s cache key. If you want to send values to the origin but &lt;i&gt;not&lt;/i&gt; include them in the cache key, use &lt;code&gt;OriginRequestPolicy&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about cache policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html\&quot;&gt;Controlling the cache key&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateCachePolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_cloud_front_origin_access_identity20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cloud_front_origin_access_identity20200531

    Creates a new origin access identity. If you&#39;re using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving Private Content through CloudFront&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateCloudFrontOriginAccessIdentity20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_continuous_deployment_policy20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_continuous_deployment_policy20200531

    &lt;p&gt;Creates a continuous deployment policy that distributes traffic for a custom domain name to two different CloudFront distributions.&lt;/p&gt; &lt;p&gt;To use a continuous deployment policy, first use &lt;code&gt;CopyDistribution&lt;/code&gt; to create a staging distribution, then use &lt;code&gt;UpdateDistribution&lt;/code&gt; to modify the staging distribution&#39;s configuration.&lt;/p&gt; &lt;p&gt;After you create and update a staging distribution, you can use a continuous deployment policy to incrementally move traffic to the staging distribution. This workflow enables you to test changes to a distribution&#39;s configuration before moving all of your domain&#39;s production traffic to the new configuration.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateContinuousDeploymentPolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_distribution20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_distribution20200531

    Creates a CloudFront distribution.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDistribution20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_distribution_with_tags20200531(request: web.Request, with_tags, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_distribution_with_tags20200531

    &lt;p&gt;Create a new distribution with tags. This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistribution.html\&quot;&gt;CreateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param with_tags: 
    :type with_tags: bool
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDistributionWithTags20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_field_level_encryption_config20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_field_level_encryption_config20200531

    Create a new field-level encryption configuration.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateFieldLevelEncryptionConfig20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_field_level_encryption_profile20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_field_level_encryption_profile20200531

    Create a field-level encryption profile.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateFieldLevelEncryptionProfile20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_function20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_function20200531

    &lt;p&gt;Creates a CloudFront function.&lt;/p&gt; &lt;p&gt;To create a function, you provide the function code and some configuration information about the function. The response contains an Amazon Resource Name (ARN) that uniquely identifies the function.&lt;/p&gt; &lt;p&gt;When you create a function, it&#39;s in the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage. In this stage, you can test the function with &lt;code&gt;TestFunction&lt;/code&gt;, and update it with &lt;code&gt;UpdateFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When you&#39;re ready to use your function with a CloudFront distribution, use &lt;code&gt;PublishFunction&lt;/code&gt; to copy the function from the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage to &lt;code&gt;LIVE&lt;/code&gt;. When it&#39;s live, you can attach the function to a distribution&#39;s cache behavior, using the function&#39;s ARN.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateFunction20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_invalidation20200531(request: web.Request, distribution_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_invalidation20200531

    Create a new invalidation.

    :param distribution_id: The distribution&#39;s id.
    :type distribution_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateInvalidation20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_key_group20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_key_group20200531

    &lt;p&gt;Creates a key group that you can use with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;CloudFront signed URLs and signed cookies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To create a key group, you must specify at least one public key for the key group. After you create a key group, you can reference it from one or more cache behaviors. When you reference a key group in a cache behavior, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving private content&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateKeyGroup20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_monitoring_subscription20200531(request: web.Request, distribution_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_monitoring_subscription20200531

    &lt;p&gt;Enables additional CloudWatch metrics for the specified CloudFront distribution. The additional metrics incur an additional cost.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html#monitoring-console.distributions-additional\&quot;&gt;Viewing additional CloudFront distribution metrics&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param distribution_id: The ID of the distribution that you are enabling metrics for.
    :type distribution_id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateMonitoringSubscription20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_origin_access_control20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_origin_access_control20200531

    &lt;p&gt;Creates a new origin access control in CloudFront. After you create an origin access control, you can add it to an origin in a CloudFront distribution so that CloudFront sends authenticated (signed) requests to the origin.&lt;/p&gt; &lt;p&gt;This makes it possible to block public access to the origin, allowing viewers (users) to access the origin&#39;s content only through CloudFront.&lt;/p&gt; &lt;p&gt;For more information about using a CloudFront origin access control, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html\&quot;&gt;Restricting access to an Amazon Web Services origin&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateOriginAccessControl20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_origin_request_policy20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_origin_request_policy20200531

    &lt;p&gt;Creates an origin request policy.&lt;/p&gt; &lt;p&gt;After you create an origin request policy, you can attach it to one or more cache behaviors. When it&#39;s attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The request body and the URL path (without the domain name) from the viewer request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The headers that CloudFront automatically includes in every origin request, including &lt;code&gt;Host&lt;/code&gt;, &lt;code&gt;User-Agent&lt;/code&gt;, and &lt;code&gt;X-Amz-Cf-Id&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;CloudFront sends a request when it can&#39;t find a valid object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use &lt;code&gt;CachePolicy&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information about origin request policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html\&quot;&gt;Controlling origin requests&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateOriginRequestPolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_public_key20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_public_key20200531

    Uploads a public key to CloudFront that you can use with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;signed URLs and signed cookies&lt;/a&gt;, or with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html\&quot;&gt;field-level encryption&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreatePublicKey20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_realtime_log_config20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_realtime_log_config20200531

    &lt;p&gt;Creates a real-time log configuration.&lt;/p&gt; &lt;p&gt;After you create a real-time log configuration, you can attach it to one or more cache behaviors to send real-time log data to the specified Amazon Kinesis data stream.&lt;/p&gt; &lt;p&gt;For more information about real-time log configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html\&quot;&gt;Real-time logs&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRealtimeLogConfig20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_response_headers_policy20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_response_headers_policy20200531

    &lt;p&gt;Creates a response headers policy.&lt;/p&gt; &lt;p&gt;A response headers policy contains information about a set of HTTP headers. To create a response headers policy, you provide some metadata about the policy and a set of configurations that specify the headers.&lt;/p&gt; &lt;p&gt;After you create a response headers policy, you can use its ID to attach it to one or more cache behaviors in a CloudFront distribution. When it&#39;s attached to a cache behavior, the response headers policy affects the HTTP headers that CloudFront includes in HTTP responses to requests that match the cache behavior. CloudFront adds or removes response headers according to the configuration of the response headers policy.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/modifying-response-headers.html\&quot;&gt;Adding or removing HTTP headers in CloudFront responses&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateResponseHeadersPolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_streaming_distribution20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_streaming_distribution20200531

    This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/ann.jspa?annID&#x3D;7356\&quot;&gt;read the announcement&lt;/a&gt; on the Amazon CloudFront discussion forum.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateStreamingDistribution20200531Request.from_dict(body)
    return web.Response(status=200)


async def create_streaming_distribution_with_tags20200531(request: web.Request, with_tags, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_streaming_distribution_with_tags20200531

    This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/ann.jspa?annID&#x3D;7356\&quot;&gt;read the announcement&lt;/a&gt; on the Amazon CloudFront discussion forum.

    :param with_tags: 
    :type with_tags: bool
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateStreamingDistributionWithTags20200531Request.from_dict(body)
    return web.Response(status=200)


async def delete_cache_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_cache_policy20200531

    &lt;p&gt;Deletes a cache policy.&lt;/p&gt; &lt;p&gt;You cannot delete a cache policy if it&#39;s attached to a cache behavior. First update your distributions to remove the cache policy from all cache behaviors, then delete the cache policy.&lt;/p&gt; &lt;p&gt;To delete a cache policy, you must provide the policy&#39;s identifier and version. To get these values, you can use &lt;code&gt;ListCachePolicies&lt;/code&gt; or &lt;code&gt;GetCachePolicy&lt;/code&gt;.&lt;/p&gt;

    :param id: The unique identifier for the cache policy that you are deleting. To get the identifier, you can use &lt;code&gt;ListCachePolicies&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The version of the cache policy that you are deleting. The version is the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListCachePolicies&lt;/code&gt;, &lt;code&gt;GetCachePolicy&lt;/code&gt;, or &lt;code&gt;GetCachePolicyConfig&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_cloud_front_origin_access_identity20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_cloud_front_origin_access_identity20200531

    Delete an origin access identity.

    :param id: The origin access identity&#39;s ID.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header you received from a previous &lt;code&gt;GET&lt;/code&gt; or &lt;code&gt;PUT&lt;/code&gt; request. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_continuous_deployment_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_continuous_deployment_policy20200531

    &lt;p&gt;Deletes a continuous deployment policy.&lt;/p&gt; &lt;p&gt;You cannot delete a continuous deployment policy that&#39;s attached to a primary distribution. First update your distribution to remove the continuous deployment policy, then you can delete the policy.&lt;/p&gt;

    :param id: The identifier of the continuous deployment policy that you are deleting.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the continuous deployment policy that you are deleting.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_distribution20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_distribution20200531

    Delete a distribution.

    :param id: The distribution ID.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_field_level_encryption_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_field_level_encryption_config20200531

    Remove a field-level encryption configuration.

    :param id: The ID of the configuration you want to delete from CloudFront.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the configuration identity to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_field_level_encryption_profile20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_field_level_encryption_profile20200531

    Remove a field-level encryption profile.

    :param id: Request the ID of the profile you want to delete from CloudFront.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the profile to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_function20200531(request: web.Request, name, if_match, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_function20200531

    &lt;p&gt;Deletes a CloudFront function.&lt;/p&gt; &lt;p&gt;You cannot delete a function if it&#39;s associated with a cache behavior. First, update your distributions to remove the function association from all cache behaviors, then delete the function.&lt;/p&gt; &lt;p&gt;To delete a function, you must provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value). To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

    :param name: The name of the function that you are deleting.
    :type name: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are deleting, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;.
    :type if_match: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_key_group20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_key_group20200531

    &lt;p&gt;Deletes a key group.&lt;/p&gt; &lt;p&gt;You cannot delete a key group that is referenced in a cache behavior. First update your distributions to remove the key group from all cache behaviors, then delete the key group.&lt;/p&gt; &lt;p&gt;To delete a key group, you must provide the key group&#39;s identifier and version. To get these values, use &lt;code&gt;ListKeyGroups&lt;/code&gt; followed by &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;.&lt;/p&gt;

    :param id: The identifier of the key group that you are deleting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The version of the key group that you are deleting. The version is the key group&#39;s &lt;code&gt;ETag&lt;/code&gt; value. To get the &lt;code&gt;ETag&lt;/code&gt;, use &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_monitoring_subscription20200531(request: web.Request, distribution_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_monitoring_subscription20200531

    Disables additional CloudWatch metrics for the specified CloudFront distribution.

    :param distribution_id: The ID of the distribution that you are disabling metrics for.
    :type distribution_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_origin_access_control20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_origin_access_control20200531

    &lt;p&gt;Deletes a CloudFront origin access control.&lt;/p&gt; &lt;p&gt;You cannot delete an origin access control if it&#39;s in use. First, update all distributions to remove the origin access control from all origins, then delete the origin access control.&lt;/p&gt;

    :param id: The unique identifier of the origin access control that you are deleting.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the origin access control that you are deleting.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_origin_request_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_origin_request_policy20200531

    &lt;p&gt;Deletes an origin request policy.&lt;/p&gt; &lt;p&gt;You cannot delete an origin request policy if it&#39;s attached to any cache behaviors. First update your distributions to remove the origin request policy from all cache behaviors, then delete the origin request policy.&lt;/p&gt; &lt;p&gt;To delete an origin request policy, you must provide the policy&#39;s identifier and version. To get the identifier, you can use &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt; or &lt;code&gt;GetOriginRequestPolicy&lt;/code&gt;.&lt;/p&gt;

    :param id: The unique identifier for the origin request policy that you are deleting. To get the identifier, you can use &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The version of the origin request policy that you are deleting. The version is the origin request policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;, &lt;code&gt;GetOriginRequestPolicy&lt;/code&gt;, or &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_public_key20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_public_key20200531

    Remove a public key you previously added to CloudFront.

    :param id: The ID of the public key you want to remove from CloudFront.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the public key identity to delete. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_realtime_log_config20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_realtime_log_config20200531

    &lt;p&gt;Deletes a real-time log configuration.&lt;/p&gt; &lt;p&gt;You cannot delete a real-time log configuration if it&#39;s attached to a cache behavior. First update your distributions to remove the real-time log configuration from all cache behaviors, then delete the real-time log configuration.&lt;/p&gt; &lt;p&gt;To delete a real-time log configuration, you can provide the configuration&#39;s name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to delete.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteRealtimeLogConfig20200531Request.from_dict(body)
    return web.Response(status=200)


async def delete_response_headers_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_response_headers_policy20200531

    &lt;p&gt;Deletes a response headers policy.&lt;/p&gt; &lt;p&gt;You cannot delete a response headers policy if it&#39;s attached to a cache behavior. First update your distributions to remove the response headers policy from all cache behaviors, then delete the response headers policy.&lt;/p&gt; &lt;p&gt;To delete a response headers policy, you must provide the policy&#39;s identifier and version. To get these values, you can use &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt; or &lt;code&gt;GetResponseHeadersPolicy&lt;/code&gt;.&lt;/p&gt;

    :param id: &lt;p&gt;The identifier for the response headers policy that you are deleting.&lt;/p&gt; &lt;p&gt;To get the identifier, you can use &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: &lt;p&gt;The version of the response headers policy that you are deleting.&lt;/p&gt; &lt;p&gt;The version is the response headers policy&#39;s &lt;code&gt;ETag&lt;/code&gt; value, which you can get using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;, &lt;code&gt;GetResponseHeadersPolicy&lt;/code&gt;, or &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt;.&lt;/p&gt;
    :type if_match: str

    """
    return web.Response(status=200)


async def delete_streaming_distribution20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_streaming_distribution20200531

    &lt;p&gt;Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To delete an RTMP distribution using the CloudFront API&lt;/b&gt;:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Disable the RTMP distribution.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to get the current configuration and the &lt;code&gt;Etag&lt;/code&gt; header for the distribution. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to change the value of &lt;code&gt;Enabled&lt;/code&gt; to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to confirm that the distribution was successfully disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request. Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to your &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request to confirm that the distribution was successfully deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For information about deleting a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html\&quot;&gt;Deleting a Distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param id: The distribution ID.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when you disabled the streaming distribution. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    return web.Response(status=200)


async def describe_function20200531(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stage=None) -> web.Response:
    """describe_function20200531

    &lt;p&gt;Gets configuration information and metadata about a CloudFront function, but not the function&#39;s code. To get a function&#39;s code, use &lt;code&gt;GetFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get configuration information and metadata about a function, you must provide the function&#39;s name and stage. To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt;.&lt;/p&gt;

    :param name: The name of the function that you are getting information about.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param stage: The function&#39;s stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;.
    :type stage: str

    """
    return web.Response(status=200)


async def get_cache_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cache_policy20200531

    &lt;p&gt;Gets a cache policy, including the following metadata:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The policy&#39;s identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The date and time when the policy was last modified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get a cache policy, you must provide the policy&#39;s identifier. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.&lt;/p&gt;

    :param id: The unique identifier for the cache policy. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_cache_policy_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cache_policy_config20200531

    &lt;p&gt;Gets a cache policy configuration.&lt;/p&gt; &lt;p&gt;To get a cache policy configuration, you must provide the policy&#39;s identifier. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.&lt;/p&gt;

    :param id: The unique identifier for the cache policy. If the cache policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the cache policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListCachePolicies&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_cloud_front_origin_access_identity20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cloud_front_origin_access_identity20200531

    Get the information about an origin access identity.

    :param id: The identity&#39;s ID.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_cloud_front_origin_access_identity_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cloud_front_origin_access_identity_config20200531

    Get the configuration information about an origin access identity.

    :param id: The identity&#39;s ID.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_continuous_deployment_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_continuous_deployment_policy20200531

    Gets a continuous deployment policy, including metadata (the policy&#39;s identifier and the date and time when the policy was last modified).

    :param id: The identifier of the continuous deployment policy that you are getting.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_continuous_deployment_policy_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_continuous_deployment_policy_config20200531

    Gets configuration information about a continuous deployment policy.

    :param id: The identifier of the continuous deployment policy whose configuration you are getting.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_distribution20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_distribution20200531

    Get the information about a distribution.

    :param id: The distribution&#39;s ID. If the ID is empty, an empty distribution configuration is returned.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_distribution_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_distribution_config20200531

    Get the configuration information about a distribution.

    :param id: The distribution&#39;s ID. If the ID is empty, an empty distribution configuration is returned.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_field_level_encryption20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_field_level_encryption20200531

    Get the field-level encryption configuration information.

    :param id: Request the ID for the field-level encryption configuration information.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_field_level_encryption_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_field_level_encryption_config20200531

    Get the field-level encryption configuration information.

    :param id: Request the ID for the field-level encryption configuration information.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_field_level_encryption_profile20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_field_level_encryption_profile20200531

    Get the field-level encryption profile information.

    :param id: Get the ID for the field-level encryption profile information.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_field_level_encryption_profile_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_field_level_encryption_profile_config20200531

    Get the field-level encryption profile configuration information.

    :param id: Get the ID for the field-level encryption profile configuration information.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_function20200531(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, stage=None) -> web.Response:
    """get_function20200531

    &lt;p&gt;Gets the code of a CloudFront function. To get configuration information and metadata about a function, use &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To get a function&#39;s code, you must provide the function&#39;s name and stage. To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt;.&lt;/p&gt;

    :param name: The name of the function whose code you are getting.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param stage: The function&#39;s stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;.
    :type stage: str

    """
    return web.Response(status=200)


async def get_invalidation20200531(request: web.Request, distribution_id, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_invalidation20200531

    Get the information about an invalidation.

    :param distribution_id: The distribution&#39;s ID.
    :type distribution_id: str
    :param id: The identifier for the invalidation request, for example, &lt;code&gt;IDFDVBD632BHDS5&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_key_group20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_key_group20200531

    &lt;p&gt;Gets a key group, including the date and time when the key group was last modified.&lt;/p&gt; &lt;p&gt;To get a key group, you must provide the key group&#39;s identifier. If the key group is referenced in a distribution&#39;s cache behavior, you can get the key group&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the key group is not referenced in a cache behavior, you can get the identifier using &lt;code&gt;ListKeyGroups&lt;/code&gt;.&lt;/p&gt;

    :param id: The identifier of the key group that you are getting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_key_group_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_key_group_config20200531

    &lt;p&gt;Gets a key group configuration.&lt;/p&gt; &lt;p&gt;To get a key group configuration, you must provide the key group&#39;s identifier. If the key group is referenced in a distribution&#39;s cache behavior, you can get the key group&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the key group is not referenced in a cache behavior, you can get the identifier using &lt;code&gt;ListKeyGroups&lt;/code&gt;.&lt;/p&gt;

    :param id: The identifier of the key group whose configuration you are getting. To get the identifier, use &lt;code&gt;ListKeyGroups&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_monitoring_subscription20200531(request: web.Request, distribution_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_monitoring_subscription20200531

    Gets information about whether additional CloudWatch metrics are enabled for the specified CloudFront distribution.

    :param distribution_id: The ID of the distribution that you are getting metrics information for.
    :type distribution_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_origin_access_control20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_origin_access_control20200531

    Gets a CloudFront origin access control, including its unique identifier.

    :param id: The unique identifier of the origin access control.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_origin_access_control_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_origin_access_control_config20200531

    Gets a CloudFront origin access control configuration.

    :param id: The unique identifier of the origin access control.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_origin_request_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_origin_request_policy20200531

    &lt;p&gt;Gets an origin request policy, including the following metadata:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The policy&#39;s identifier.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The date and time when the policy was last modified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get an origin request policy, you must provide the policy&#39;s identifier. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.&lt;/p&gt;

    :param id: The unique identifier for the origin request policy. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_origin_request_policy_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_origin_request_policy_config20200531

    &lt;p&gt;Gets an origin request policy configuration.&lt;/p&gt; &lt;p&gt;To get an origin request policy configuration, you must provide the policy&#39;s identifier. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.&lt;/p&gt;

    :param id: The unique identifier for the origin request policy. If the origin request policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the origin request policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListOriginRequestPolicies&lt;/code&gt;.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_public_key20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_public_key20200531

    Gets a public key.

    :param id: The identifier of the public key you are getting.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_public_key_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_public_key_config20200531

    Gets a public key configuration.

    :param id: The identifier of the public key whose configuration you are getting.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_realtime_log_config20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_realtime_log_config20200531

    &lt;p&gt;Gets a real-time log configuration.&lt;/p&gt; &lt;p&gt;To get a real-time log configuration, you can provide the configuration&#39;s name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to get.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetRealtimeLogConfig20200531Request.from_dict(body)
    return web.Response(status=200)


async def get_response_headers_policy20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_response_headers_policy20200531

    &lt;p&gt;Gets a response headers policy, including metadata (the policy&#39;s identifier and the date and time when the policy was last modified).&lt;/p&gt; &lt;p&gt;To get a response headers policy, you must provide the policy&#39;s identifier. If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;

    :param id: &lt;p&gt;The identifier for the response headers policy.&lt;/p&gt; &lt;p&gt;If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_response_headers_policy_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_response_headers_policy_config20200531

    &lt;p&gt;Gets a response headers policy configuration.&lt;/p&gt; &lt;p&gt;To get a response headers policy configuration, you must provide the policy&#39;s identifier. If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;

    :param id: &lt;p&gt;The identifier for the response headers policy.&lt;/p&gt; &lt;p&gt;If the response headers policy is attached to a distribution&#39;s cache behavior, you can get the policy&#39;s identifier using &lt;code&gt;ListDistributions&lt;/code&gt; or &lt;code&gt;GetDistribution&lt;/code&gt;. If the response headers policy is not attached to a cache behavior, you can get the identifier using &lt;code&gt;ListResponseHeadersPolicies&lt;/code&gt;.&lt;/p&gt;
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_streaming_distribution20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_distribution20200531

    Gets information about a specified RTMP distribution, including the distribution configuration.

    :param id: The streaming distribution&#39;s ID.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_streaming_distribution_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_distribution_config20200531

    Get the configuration information about a streaming distribution.

    :param id: The streaming distribution&#39;s ID.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_cache_policies20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, marker=None, max_items=None) -> web.Response:
    """list_cache_policies20200531

    &lt;p&gt;Gets a list of cache policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param type: &lt;p&gt;A filter to return only the specified kinds of cache policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Returns only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Returns only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type type: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of cache policies. The response includes cache policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of cache policies that you want in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_cloud_front_origin_access_identities20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_cloud_front_origin_access_identities20200531

    Lists origin access identities.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last identity on that page).
    :type marker: str
    :param max_items: The maximum number of origin access identities you want in the response body.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_conflicting_aliases20200531(request: web.Request, distribution_id, alias, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_conflicting_aliases20200531

    &lt;p&gt;Gets a list of aliases (also called CNAMEs or alternate domain names) that conflict or overlap with the provided alias, and the associated CloudFront distributions and Amazon Web Services accounts for each conflicting alias. In the returned list, the distribution and account IDs are partially hidden, which allows you to identify the distributions and accounts that you own, but helps to protect the information of ones that you don&#39;t own.&lt;/p&gt; &lt;p&gt;Use this operation to find aliases that are in use in CloudFront that conflict or overlap with the provided alias. For example, if you provide &lt;code&gt;www.example.com&lt;/code&gt; as input, the returned list can include &lt;code&gt;www.example.com&lt;/code&gt; and the overlapping wildcard alternate domain name (&lt;code&gt;*.example.com&lt;/code&gt;), if they exist. If you provide &lt;code&gt;*.example.com&lt;/code&gt; as input, the returned list can include &lt;code&gt;*.example.com&lt;/code&gt; and any alternate domain names covered by that wildcard (for example, &lt;code&gt;www.example.com&lt;/code&gt;, &lt;code&gt;test.example.com&lt;/code&gt;, &lt;code&gt;dev.example.com&lt;/code&gt;, and so on), if they exist.&lt;/p&gt; &lt;p&gt;To list conflicting aliases, you provide the alias to search and the ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias. For more information, including how to set up the distribution and certificate, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move\&quot;&gt;Moving an alternate domain name to a different distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param distribution_id: The ID of a distribution in your account that has an attached SSL/TLS certificate that includes the provided alias.
    :type distribution_id: str
    :param alias: The alias (also called a CNAME) to search for conflicting aliases.
    :type alias: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of conflicting aliases that you want in the response.
    :type max_items: int

    """
    return web.Response(status=200)


async def list_continuous_deployment_policies20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_continuous_deployment_policies20200531

    &lt;p&gt;Gets a list of the continuous deployment policies in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of continuous deployment policies that you want returned in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_distributions20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions20200531

    List CloudFront distributions.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this when paginating results to indicate where to begin in your list of distributions. The results include distributions in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last distribution on that page).
    :type marker: str
    :param max_items: The maximum number of distributions you want in the response body.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_distributions_by_cache_policy_id20200531(request: web.Request, cache_policy_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions_by_cache_policy_id20200531

    &lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified cache policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param cache_policy_id: The ID of the cache policy whose associated distribution IDs you want to list.
    :type cache_policy_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of distribution IDs that you want in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_distributions_by_key_group20200531(request: web.Request, key_group_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions_by_key_group20200531

    &lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that references the specified key group.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param key_group_id: The ID of the key group whose associated distribution IDs you are listing.
    :type key_group_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of distribution IDs that you want in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_distributions_by_origin_request_policy_id20200531(request: web.Request, origin_request_policy_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions_by_origin_request_policy_id20200531

    &lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified origin request policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param origin_request_policy_id: The ID of the origin request policy whose associated distribution IDs you want to list.
    :type origin_request_policy_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of distribution IDs that you want in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_distributions_by_realtime_log_config20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_distributions_by_realtime_log_config20200531

    &lt;p&gt;Gets a list of distributions that have a cache behavior that&#39;s associated with the specified real-time log configuration.&lt;/p&gt; &lt;p&gt;You can specify the real-time log configuration by its name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to list distributions for.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListDistributionsByRealtimeLogConfig20200531Request.from_dict(body)
    return web.Response(status=200)


async def list_distributions_by_response_headers_policy_id20200531(request: web.Request, response_headers_policy_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions_by_response_headers_policy_id20200531

    &lt;p&gt;Gets a list of distribution IDs for distributions that have a cache behavior that&#39;s associated with the specified response headers policy.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param response_headers_policy_id: The ID of the response headers policy whose associated distribution IDs you want to list.
    :type response_headers_policy_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of distribution IDs. The response includes distribution IDs in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of distribution IDs that you want to get in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_distributions_by_web_aclid20200531(request: web.Request, web_aclid, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions_by_web_aclid20200531

    List the distributions that are associated with a specified WAF web ACL.

    :param web_aclid: The ID of the WAF web ACL that you want to list the associated distributions. If you specify \&quot;null\&quot; for the ID, the request returns a list of the distributions that aren&#39;t associated with a web ACL.
    :type web_aclid: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use &lt;code&gt;Marker&lt;/code&gt; and &lt;code&gt;MaxItems&lt;/code&gt; to control pagination of results. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; distributions that satisfy the request, the response includes a &lt;code&gt;NextMarker&lt;/code&gt; element. To get the next page of results, submit another request. For the value of &lt;code&gt;Marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the last response. (For the first request, omit &lt;code&gt;Marker&lt;/code&gt;.)
    :type marker: str
    :param max_items: The maximum number of distributions that you want CloudFront to return in the response body. The maximum and default values are both 100.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_field_level_encryption_configs20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_field_level_encryption_configs20200531

    List all field-level encryption configurations that have been created in CloudFront for this account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this when paginating results to indicate where to begin in your list of configurations. The results include configurations in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last configuration on that page).
    :type marker: str
    :param max_items: The maximum number of field-level encryption configurations you want in the response body.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_field_level_encryption_profiles20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_field_level_encryption_profiles20200531

    Request a list of field-level encryption profiles that have been created in CloudFront for this account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last profile on that page).
    :type marker: str
    :param max_items: The maximum number of field-level encryption profiles you want in the response body. 
    :type max_items: str

    """
    return web.Response(status=200)


async def list_functions20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None, stage=None) -> web.Response:
    """list_functions20200531

    &lt;p&gt;Gets a list of all CloudFront functions in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the functions that are in the specified stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of functions that you want in the response.
    :type max_items: str
    :param stage: An optional filter to return only the functions that are in the specified stage, either &lt;code&gt;DEVELOPMENT&lt;/code&gt; or &lt;code&gt;LIVE&lt;/code&gt;.
    :type stage: str

    """
    return web.Response(status=200)


async def list_invalidations20200531(request: web.Request, distribution_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_invalidations20200531

    Lists invalidation batches.

    :param distribution_id: The distribution&#39;s ID.
    :type distribution_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this parameter when paginating results to indicate where to begin in your list of invalidation batches. Because the results are returned in decreasing order from most recent to oldest, the most recent results are on the first page, the second page will contain earlier results, and so on. To get the next page of results, set &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response. This value is the same as the ID of the last invalidation batch on that page.
    :type marker: str
    :param max_items: The maximum number of invalidation batches that you want in the response body.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_key_groups20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_key_groups20200531

    &lt;p&gt;Gets a list of key groups.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of key groups. The response includes key groups in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of key groups that you want in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_origin_access_controls20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_origin_access_controls20200531

    &lt;p&gt;Gets the list of CloudFront origin access controls in this Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send another request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the next request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of origin access controls. The response includes the items in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of origin access controls that you want in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_origin_request_policies20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, marker=None, max_items=None) -> web.Response:
    """list_origin_request_policies20200531

    &lt;p&gt;Gets a list of origin request policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to return only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param type: &lt;p&gt;A filter to return only the specified kinds of origin request policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Returns only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Returns only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type type: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of origin request policies. The response includes origin request policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of origin request policies that you want in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_public_keys20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_public_keys20200531

    List all public keys that have been added to CloudFront for this account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: Use this when paginating results to indicate where to begin in your list of public keys. The results include public keys in the list that occur after the marker. To get the next page of results, set the &lt;code&gt;Marker&lt;/code&gt; to the value of the &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response (which is also the ID of the last public key on that page).
    :type marker: str
    :param max_items: The maximum number of public keys you want in the response body.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_realtime_log_configs20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_items=None, marker=None) -> web.Response:
    """list_realtime_log_configs20200531

    &lt;p&gt;Gets a list of real-time log configurations.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_items: The maximum number of real-time log configurations that you want in the response.
    :type max_items: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str

    """
    return web.Response(status=200)


async def list_response_headers_policies20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, type=None, marker=None, max_items=None) -> web.Response:
    """list_response_headers_policies20200531

    &lt;p&gt;Gets a list of response headers policies.&lt;/p&gt; &lt;p&gt;You can optionally apply a filter to get only the managed policies created by Amazon Web Services, or only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the &lt;code&gt;NextMarker&lt;/code&gt; value from the current response as the &lt;code&gt;Marker&lt;/code&gt; value in the subsequent request.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param type: &lt;p&gt;A filter to get only the specified kind of response headers policies. Valid values are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;managed&lt;/code&gt; – Gets only the managed policies created by Amazon Web Services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;custom&lt;/code&gt; – Gets only the custom policies created in your Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type type: str
    :param marker: Use this field when paginating results to indicate where to begin in your list of response headers policies. The response includes response headers policies in the list that occur after the marker. To get the next page of the list, set this field&#39;s value to the value of &lt;code&gt;NextMarker&lt;/code&gt; from the current page&#39;s response.
    :type marker: str
    :param max_items: The maximum number of response headers policies that you want to get in the response.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_streaming_distributions20200531(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_streaming_distributions20200531

    List streaming distributions.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: The value that you provided for the &lt;code&gt;Marker&lt;/code&gt; request parameter.
    :type marker: str
    :param max_items: The value that you provided for the &lt;code&gt;MaxItems&lt;/code&gt; request parameter.
    :type max_items: str

    """
    return web.Response(status=200)


async def list_tags_for_resource20200531(request: web.Request, resource, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource20200531

    List tags for a CloudFront resource.

    :param resource: An ARN of a CloudFront resource.
    :type resource: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def publish_function20200531(request: web.Request, name, if_match, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """publish_function20200531

    &lt;p&gt;Publishes a CloudFront function by copying the function code from the &lt;code&gt;DEVELOPMENT&lt;/code&gt; stage to &lt;code&gt;LIVE&lt;/code&gt;. This automatically updates all cache behaviors that are using this function to use the newly published copy in the &lt;code&gt;LIVE&lt;/code&gt; stage.&lt;/p&gt; &lt;p&gt;When a function is published to the &lt;code&gt;LIVE&lt;/code&gt; stage, you can attach the function to a distribution&#39;s cache behavior, using the function&#39;s Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;To publish a function, you must provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value). To get these values, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

    :param name: The name of the function that you are publishing.
    :type name: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are publishing, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;.
    :type if_match: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def tag_resource20200531(request: web.Request, resource, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource20200531

    Add tags to a CloudFront resource.

    :param resource: An ARN of a CloudFront resource.
    :type resource: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResource20200531Request.from_dict(body)
    return web.Response(status=200)


async def test_function20200531(request: web.Request, name, if_match, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """test_function20200531

    &lt;p&gt;Tests a CloudFront function.&lt;/p&gt; &lt;p&gt;To test a function, you provide an &lt;i&gt;event object&lt;/i&gt; that represents an HTTP request or response that your CloudFront distribution could receive in production. CloudFront runs the function, passing it the event object that you provided, and returns the function&#39;s result (the modified event object) in the response. The response also contains function logs and error messages, if any exist. For more information about testing functions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function\&quot;&gt;Testing functions&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To test a function, you provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value) along with the event object. To get the function&#39;s name and version, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

    :param name: The name of the function that you are testing.
    :type name: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are testing, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;.
    :type if_match: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TestFunction20200531Request.from_dict(body)
    return web.Response(status=200)


async def untag_resource20200531(request: web.Request, resource, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource20200531

    Remove tags from a CloudFront resource.

    :param resource: An ARN of a CloudFront resource.
    :type resource: str
    :param operation: 
    :type operation: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagResource20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_cache_policy20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_cache_policy20200531

    &lt;p&gt;Updates a cache policy configuration.&lt;/p&gt; &lt;p&gt;When you update a cache policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a cache policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetCachePolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the cache policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateCachePolicy&lt;/code&gt; by providing the entire cache policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param id: The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behavior&#39;s &lt;code&gt;CachePolicyId&lt;/code&gt; field in the response to &lt;code&gt;GetDistributionConfig&lt;/code&gt;.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The version of the cache policy that you are updating. The version is returned in the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetCachePolicyConfig&lt;/code&gt;.
    :type if_match: str

    """
    body = CreateCachePolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_cloud_front_origin_access_identity20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_cloud_front_origin_access_identity20200531

    Update an origin access identity.

    :param id: The identity&#39;s id.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the identity&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    body = CreateCloudFrontOriginAccessIdentity20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_continuous_deployment_policy20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_continuous_deployment_policy20200531

    &lt;p&gt;Updates a continuous deployment policy. You can update a continuous deployment policy to enable or disable it, to change the percentage of traffic that it sends to the staging distribution, or to change the staging distribution that it sends traffic to.&lt;/p&gt; &lt;p&gt;When you update a continuous deployment policy configuration, all the fields are updated with the values that are provided in the request. You cannot update some fields independent of others. To update a continuous deployment policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetContinuousDeploymentPolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the continuous deployment policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;UpdateContinuousDeploymentPolicy&lt;/code&gt;, providing the entire continuous deployment policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param id: The identifier of the continuous deployment policy that you are updating.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the continuous deployment policy that you are updating.
    :type if_match: str

    """
    body = CreateContinuousDeploymentPolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_distribution20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_distribution20200531

    &lt;p&gt;Updates the configuration for a CloudFront distribution.&lt;/p&gt; &lt;p&gt;The update process includes getting the current distribution configuration, updating it to make your changes, and then submitting an &lt;code&gt;UpdateDistribution&lt;/code&gt; request to make the updates.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To update a web distribution using the CloudFront API&lt;/b&gt; &lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetDistributionConfig&lt;/code&gt; to get the current configuration, including the version identifier (&lt;code&gt;ETag&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the distribution configuration that was returned in the response. Note the following important requirements and restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must rename the &lt;code&gt;ETag&lt;/code&gt; field to &lt;code&gt;IfMatch&lt;/code&gt;, leaving the value unchanged. (Set the value of &lt;code&gt;IfMatch&lt;/code&gt; to the value of &lt;code&gt;ETag&lt;/code&gt;, then remove the &lt;code&gt;ETag&lt;/code&gt; field.)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t change the value of &lt;code&gt;CallerReference&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateDistribution&lt;/code&gt; request, providing the distribution configuration. The new configuration replaces the existing configuration. The values that you specify in an &lt;code&gt;UpdateDistribution&lt;/code&gt; request are not merged into your existing configuration. Make sure to include all fields: the ones that you modified and also the ones that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param id: The distribution&#39;s id.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the distribution&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    body = CreateDistribution20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_distribution_with_staging_config20200531(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, staging_distribution_id=None, if_match=None) -> web.Response:
    """update_distribution_with_staging_config20200531

    &lt;p&gt;Copies the staging distribution&#39;s configuration to its corresponding primary distribution. The primary distribution retains its &lt;code&gt;Aliases&lt;/code&gt; (also known as alternate domain names or CNAMEs) and &lt;code&gt;ContinuousDeploymentPolicyId&lt;/code&gt; value, but otherwise its configuration is overwritten to match the staging distribution.&lt;/p&gt; &lt;p&gt;You can use this operation in a continuous deployment workflow after you have tested configuration changes on the staging distribution. After using a continuous deployment policy to move a portion of your domain name&#39;s traffic to the staging distribution and verifying that it works as intended, you can use this operation to copy the staging distribution&#39;s configuration to the primary distribution. This action will disable the continuous deployment policy and move your domain&#39;s traffic back to the primary distribution.&lt;/p&gt; &lt;p&gt;This API operation requires the following IAM permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetDistribution.html\&quot;&gt;GetDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistribution.html\&quot;&gt;UpdateDistribution&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param id: The identifier of the primary distribution to which you are copying a staging distribution&#39;s configuration.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param staging_distribution_id: The identifier of the staging distribution whose configuration you are copying to the primary distribution.
    :type staging_distribution_id: str
    :param if_match: &lt;p&gt;The current versions (&lt;code&gt;ETag&lt;/code&gt; values) of both primary and staging distributions. Provide these in the following format:&lt;/p&gt; &lt;p&gt; &lt;code&gt;&amp;lt;primary ETag&amp;gt;, &amp;lt;staging ETag&amp;gt;&lt;/code&gt; &lt;/p&gt;
    :type if_match: str

    """
    return web.Response(status=200)


async def update_field_level_encryption_config20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_field_level_encryption_config20200531

    Update a field-level encryption configuration.

    :param id: The ID of the configuration you want to update.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the configuration identity to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    body = CreateFieldLevelEncryptionConfig20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_field_level_encryption_profile20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_field_level_encryption_profile20200531

    Update a field-level encryption profile.

    :param id: The ID of the field-level encryption profile request.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the profile identity to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    body = CreateFieldLevelEncryptionProfile20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_function20200531(request: web.Request, name, if_match, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_function20200531

    &lt;p&gt;Updates a CloudFront function.&lt;/p&gt; &lt;p&gt;You can update a function&#39;s code or the comment that describes the function. You cannot update a function&#39;s name.&lt;/p&gt; &lt;p&gt;To update a function, you provide the function&#39;s name and version (&lt;code&gt;ETag&lt;/code&gt; value) along with the updated function code. To get the name and version, you can use &lt;code&gt;ListFunctions&lt;/code&gt; and &lt;code&gt;DescribeFunction&lt;/code&gt;.&lt;/p&gt;

    :param name: The name of the function that you are updating.
    :type name: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the function that you are updating, which you can get using &lt;code&gt;DescribeFunction&lt;/code&gt;.
    :type if_match: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateFunction20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_key_group20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_key_group20200531

    &lt;p&gt;Updates a key group.&lt;/p&gt; &lt;p&gt;When you update a key group, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a key group:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Get the current key group with &lt;code&gt;GetKeyGroup&lt;/code&gt; or &lt;code&gt;GetKeyGroupConfig&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the key group that you want to update. For example, add or remove public key IDs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateKeyGroup&lt;/code&gt; with the entire key group object, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param id: The identifier of the key group that you are updating.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The version of the key group that you are updating. The version is the key group&#39;s &lt;code&gt;ETag&lt;/code&gt; value.
    :type if_match: str

    """
    body = CreateKeyGroup20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_origin_access_control20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_origin_access_control20200531

    Updates a CloudFront origin access control.

    :param id: The unique identifier of the origin access control that you are updating.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The current version (&lt;code&gt;ETag&lt;/code&gt; value) of the origin access control that you are updating.
    :type if_match: str

    """
    body = CreateOriginAccessControl20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_origin_request_policy20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_origin_request_policy20200531

    &lt;p&gt;Updates an origin request policy configuration.&lt;/p&gt; &lt;p&gt;When you update an origin request policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update an origin request policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt; to get the current configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the fields in the origin request policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateOriginRequestPolicy&lt;/code&gt; by providing the entire origin request policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param id: The unique identifier for the origin request policy that you are updating. The identifier is returned in a cache behavior&#39;s &lt;code&gt;OriginRequestPolicyId&lt;/code&gt; field in the response to &lt;code&gt;GetDistributionConfig&lt;/code&gt;.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The version of the origin request policy that you are updating. The version is returned in the origin request policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetOriginRequestPolicyConfig&lt;/code&gt;.
    :type if_match: str

    """
    body = CreateOriginRequestPolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_public_key20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_public_key20200531

    Update public key information. Note that the only value you can change is the comment.

    :param id: The identifier of the public key that you are updating.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the public key to update. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    body = CreatePublicKey20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_realtime_log_config20200531(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_realtime_log_config20200531

    &lt;p&gt;Updates a real-time log configuration.&lt;/p&gt; &lt;p&gt;When you update a real-time log configuration, all the parameters are updated with the values provided in the request. You cannot update some parameters independent of others. To update a real-time log configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;GetRealtimeLogConfig&lt;/code&gt; to get the current real-time log configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Locally modify the parameters in the real-time log configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call this API (&lt;code&gt;UpdateRealtimeLogConfig&lt;/code&gt;) by providing the entire real-time log configuration, including the parameters that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;You cannot update a real-time log configuration&#39;s &lt;code&gt;Name&lt;/code&gt; or &lt;code&gt;ARN&lt;/code&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateRealtimeLogConfig20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_response_headers_policy20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_response_headers_policy20200531

    &lt;p&gt;Updates a response headers policy.&lt;/p&gt; &lt;p&gt;When you update a response headers policy, the entire policy is replaced. You cannot update some policy fields independent of others. To update a response headers policy configuration:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt; to get the current policy&#39;s configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Modify the fields in the response headers policy configuration that you want to update.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Call &lt;code&gt;UpdateResponseHeadersPolicy&lt;/code&gt;, providing the entire response headers policy configuration, including the fields that you modified and those that you didn&#39;t.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param id: The identifier for the response headers policy that you are updating.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: &lt;p&gt;The version of the response headers policy that you are updating.&lt;/p&gt; &lt;p&gt;The version is returned in the cache policy&#39;s &lt;code&gt;ETag&lt;/code&gt; field in the response to &lt;code&gt;GetResponseHeadersPolicyConfig&lt;/code&gt;.&lt;/p&gt;
    :type if_match: str

    """
    body = CreateResponseHeadersPolicy20200531Request.from_dict(body)
    return web.Response(status=200)


async def update_streaming_distribution20200531(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_streaming_distribution20200531

    Update a streaming distribution.

    :param id: The streaming distribution&#39;s id.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param if_match: The value of the &lt;code&gt;ETag&lt;/code&gt; header that you received when retrieving the streaming distribution&#39;s configuration. For example: &lt;code&gt;E2QWRUHAPOMQZL&lt;/code&gt;.
    :type if_match: str

    """
    body = CreateStreamingDistribution20200531Request.from_dict(body)
    return web.Response(status=200)
