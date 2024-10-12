from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.batch_too_large import BatchTooLarge
from openapi_server.models.cname_already_exists import CNAMEAlreadyExists
from openapi_server.models.cloud_front_origin_access_identity_already_exists import CloudFrontOriginAccessIdentityAlreadyExists
from openapi_server.models.cloud_front_origin_access_identity_in_use import CloudFrontOriginAccessIdentityInUse
from openapi_server.models.create_cloud_front_origin_access_identity20170325_request import CreateCloudFrontOriginAccessIdentity20170325Request
from openapi_server.models.create_cloud_front_origin_access_identity_result import CreateCloudFrontOriginAccessIdentityResult
from openapi_server.models.create_distribution20170325_request import CreateDistribution20170325Request
from openapi_server.models.create_distribution_result import CreateDistributionResult
from openapi_server.models.create_distribution_with_tags20170325_request import CreateDistributionWithTags20170325Request
from openapi_server.models.create_distribution_with_tags_result import CreateDistributionWithTagsResult
from openapi_server.models.create_invalidation20170325_request import CreateInvalidation20170325Request
from openapi_server.models.create_invalidation_result import CreateInvalidationResult
from openapi_server.models.create_streaming_distribution20170325_request import CreateStreamingDistribution20170325Request
from openapi_server.models.create_streaming_distribution_result import CreateStreamingDistributionResult
from openapi_server.models.create_streaming_distribution_with_tags20170325_request import CreateStreamingDistributionWithTags20170325Request
from openapi_server.models.create_streaming_distribution_with_tags_result import CreateStreamingDistributionWithTagsResult
from openapi_server.models.distribution_already_exists import DistributionAlreadyExists
from openapi_server.models.distribution_not_disabled import DistributionNotDisabled
from openapi_server.models.get_cloud_front_origin_access_identity_config_result import GetCloudFrontOriginAccessIdentityConfigResult
from openapi_server.models.get_cloud_front_origin_access_identity_result import GetCloudFrontOriginAccessIdentityResult
from openapi_server.models.get_distribution_config_result import GetDistributionConfigResult
from openapi_server.models.get_distribution_result import GetDistributionResult
from openapi_server.models.get_invalidation_result import GetInvalidationResult
from openapi_server.models.get_streaming_distribution_config_result import GetStreamingDistributionConfigResult
from openapi_server.models.get_streaming_distribution_result import GetStreamingDistributionResult
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
from openapi_server.models.list_invalidations_result import ListInvalidationsResult
from openapi_server.models.list_streaming_distributions_result import ListStreamingDistributionsResult
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.missing_body import MissingBody
from openapi_server.models.no_such_cloud_front_origin_access_identity import NoSuchCloudFrontOriginAccessIdentity
from openapi_server.models.no_such_distribution import NoSuchDistribution
from openapi_server.models.no_such_invalidation import NoSuchInvalidation
from openapi_server.models.no_such_origin import NoSuchOrigin
from openapi_server.models.no_such_resource import NoSuchResource
from openapi_server.models.no_such_streaming_distribution import NoSuchStreamingDistribution
from openapi_server.models.precondition_failed import PreconditionFailed
from openapi_server.models.resource_in_use import ResourceInUse
from openapi_server.models.streaming_distribution_already_exists import StreamingDistributionAlreadyExists
from openapi_server.models.streaming_distribution_not_disabled import StreamingDistributionNotDisabled
from openapi_server.models.tag_resource20170325_request import TagResource20170325Request
from openapi_server.models.too_many_cache_behaviors import TooManyCacheBehaviors
from openapi_server.models.too_many_certificates import TooManyCertificates
from openapi_server.models.too_many_cloud_front_origin_access_identities import TooManyCloudFrontOriginAccessIdentities
from openapi_server.models.too_many_cookie_names_in_white_list import TooManyCookieNamesInWhiteList
from openapi_server.models.too_many_distribution_cnames import TooManyDistributionCNAMEs
from openapi_server.models.too_many_distributions import TooManyDistributions
from openapi_server.models.too_many_distributions_with_lambda_associations import TooManyDistributionsWithLambdaAssociations
from openapi_server.models.too_many_headers_in_forwarded_values import TooManyHeadersInForwardedValues
from openapi_server.models.too_many_invalidations_in_progress import TooManyInvalidationsInProgress
from openapi_server.models.too_many_lambda_function_associations import TooManyLambdaFunctionAssociations
from openapi_server.models.too_many_origin_custom_headers import TooManyOriginCustomHeaders
from openapi_server.models.too_many_origins import TooManyOrigins
from openapi_server.models.too_many_query_string_parameters import TooManyQueryStringParameters
from openapi_server.models.too_many_streaming_distribution_cnames import TooManyStreamingDistributionCNAMEs
from openapi_server.models.too_many_streaming_distributions import TooManyStreamingDistributions
from openapi_server.models.too_many_trusted_signers import TooManyTrustedSigners
from openapi_server.models.trusted_signer_does_not_exist import TrustedSignerDoesNotExist
from openapi_server.models.untag_resource20170325_request import UntagResource20170325Request
from openapi_server.models.update_cloud_front_origin_access_identity_result import UpdateCloudFrontOriginAccessIdentityResult
from openapi_server.models.update_distribution_result import UpdateDistributionResult
from openapi_server.models.update_streaming_distribution_result import UpdateStreamingDistributionResult
from openapi_server import util


async def create_cloud_front_origin_access_identity20170325(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cloud_front_origin_access_identity20170325

    Creates a new origin access identity. If you&#39;re using Amazon S3 for your origin, you can use an origin access identity to require users to access your content using a CloudFront URL instead of the Amazon S3 URL. For more information about how to use origin access identities, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html\&quot;&gt;Serving Private Content through CloudFront&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.

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
    body = CreateCloudFrontOriginAccessIdentity20170325Request.from_dict(body)
    return web.Response(status=200)


async def create_distribution20170325(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_distribution20170325

    Creates a new web distribution. Send a &lt;code&gt;POST&lt;/code&gt; request to the &lt;code&gt;/&lt;i&gt;CloudFront API version&lt;/i&gt;/distribution&lt;/code&gt;/&lt;code&gt;distribution ID&lt;/code&gt; resource.

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
    body = CreateDistribution20170325Request.from_dict(body)
    return web.Response(status=200)


async def create_distribution_with_tags20170325(request: web.Request, with_tags, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_distribution_with_tags20170325

    Create a new distribution with tags.

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
    body = CreateDistributionWithTags20170325Request.from_dict(body)
    return web.Response(status=200)


async def create_invalidation20170325(request: web.Request, distribution_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_invalidation20170325

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
    body = CreateInvalidation20170325Request.from_dict(body)
    return web.Response(status=200)


async def create_streaming_distribution20170325(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_streaming_distribution20170325

    &lt;p&gt;Creates a new RMTP distribution. An RTMP distribution is similar to a web distribution, but an RTMP distribution streams media files using the Adobe Real-Time Messaging Protocol (RTMP) instead of serving files using HTTP. &lt;/p&gt; &lt;p&gt;To create a new web distribution, submit a &lt;code&gt;POST&lt;/code&gt; request to the &lt;i&gt;CloudFront API version&lt;/i&gt;/distribution resource. The request body must include a document with a &lt;i&gt;StreamingDistributionConfig&lt;/i&gt; element. The response echoes the &lt;code&gt;StreamingDistributionConfig&lt;/code&gt; element and returns other information about the RTMP distribution.&lt;/p&gt; &lt;p&gt;To get the status of your request, use the &lt;i&gt;GET StreamingDistribution&lt;/i&gt; API action. When the value of &lt;code&gt;Enabled&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt; and the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;, your distribution is ready. A distribution usually deploys in less than 15 minutes.&lt;/p&gt; &lt;p&gt;For more information about web distributions, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-rtmp.html\&quot;&gt;Working with RTMP Distributions&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a web distribution or an RTMP distribution, and when you invalidate objects. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there&#39;s a mismatch between the number of values you say you&#39;re specifying in the &lt;code&gt;Quantity&lt;/code&gt; element and the number of values specified.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateStreamingDistribution20170325Request.from_dict(body)
    return web.Response(status=200)


async def create_streaming_distribution_with_tags20170325(request: web.Request, with_tags, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_streaming_distribution_with_tags20170325

    Create a new streaming distribution with tags.

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
    body = CreateStreamingDistributionWithTags20170325Request.from_dict(body)
    return web.Response(status=200)


async def delete_cloud_front_origin_access_identity20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_cloud_front_origin_access_identity20170325

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


async def delete_distribution20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_distribution20170325

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


async def delete_service_linked_role20170325(request: web.Request, role_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_linked_role20170325

    

    :param role_name: 
    :type role_name: str
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


async def delete_streaming_distribution20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """delete_streaming_distribution20170325

    &lt;p&gt;Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To delete an RTMP distribution using the CloudFront API&lt;/b&gt;:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Disable the RTMP distribution.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to get the current configuration and the &lt;code&gt;Etag&lt;/code&gt; header for the distribution. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to change the value of &lt;code&gt;Enabled&lt;/code&gt; to &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;PUT Streaming Distribution Config&lt;/code&gt; request to confirm that the distribution was successfully disabled.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request. Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GET Streaming Distribution Config&lt;/code&gt; request in Step 2.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to your &lt;code&gt;DELETE Streaming Distribution&lt;/code&gt; request to confirm that the distribution was successfully deleted.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For information about deleting a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html\&quot;&gt;Deleting a Distribution&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt;

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


async def get_cloud_front_origin_access_identity20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cloud_front_origin_access_identity20170325

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


async def get_cloud_front_origin_access_identity_config20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cloud_front_origin_access_identity_config20170325

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


async def get_distribution20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_distribution20170325

    Get the information about a distribution. 

    :param id: The distribution&#39;s ID.
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


async def get_distribution_config20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_distribution_config20170325

    Get the configuration information about a distribution. 

    :param id: The distribution&#39;s ID.
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


async def get_invalidation20170325(request: web.Request, distribution_id, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_invalidation20170325

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


async def get_streaming_distribution20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_distribution20170325

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


async def get_streaming_distribution_config20170325(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_streaming_distribution_config20170325

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


async def list_cloud_front_origin_access_identities20170325(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_cloud_front_origin_access_identities20170325

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


async def list_distributions20170325(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions20170325

    List distributions. 

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


async def list_distributions_by_web_aclid20170325(request: web.Request, web_aclid, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_distributions_by_web_aclid20170325

    List the distributions that are associated with a specified AWS WAF web ACL. 

    :param web_aclid: The ID of the AWS WAF web ACL that you want to list the associated distributions. If you specify \&quot;null\&quot; for the ID, the request returns a list of the distributions that aren&#39;t associated with a web ACL. 
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


async def list_invalidations20170325(request: web.Request, distribution_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_invalidations20170325

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


async def list_streaming_distributions20170325(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, max_items=None) -> web.Response:
    """list_streaming_distributions20170325

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


async def list_tags_for_resource20170325(request: web.Request, resource, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource20170325

    List tags for a CloudFront resource.

    :param resource:  An ARN of a CloudFront resource.
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


async def tag_resource20170325(request: web.Request, resource, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource20170325

    Add tags to a CloudFront resource.

    :param resource:  An ARN of a CloudFront resource.
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
    body = TagResource20170325Request.from_dict(body)
    return web.Response(status=200)


async def untag_resource20170325(request: web.Request, resource, operation, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource20170325

    Remove tags from a CloudFront resource.

    :param resource:  An ARN of a CloudFront resource.
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
    body = UntagResource20170325Request.from_dict(body)
    return web.Response(status=200)


async def update_cloud_front_origin_access_identity20170325(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_cloud_front_origin_access_identity20170325

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
    body = CreateCloudFrontOriginAccessIdentity20170325Request.from_dict(body)
    return web.Response(status=200)


async def update_distribution20170325(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_distribution20170325

    &lt;p&gt;Updates the configuration for a web distribution. Perform the following steps.&lt;/p&gt; &lt;p&gt;For information about updating a distribution using the CloudFront console, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html\&quot;&gt;Creating or Updating a Web Distribution Using the CloudFront Console &lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;To update a web distribution using the CloudFront API&lt;/b&gt; &lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;a&gt;GetDistributionConfig&lt;/a&gt; request to get the current configuration and an &lt;code&gt;Etag&lt;/code&gt; header for the distribution.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you update the distribution again, you need to get a new &lt;code&gt;Etag&lt;/code&gt; header.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the XML document that was returned in the response to your &lt;code&gt;GetDistributionConfig&lt;/code&gt; request to include the desired changes. You can&#39;t change the value of &lt;code&gt;CallerReference&lt;/code&gt;. If you try to change this value, CloudFront returns an &lt;code&gt;IllegalUpdate&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The new configuration replaces the existing configuration; the values that you specify in an &lt;code&gt;UpdateDistribution&lt;/code&gt; request are not merged into the existing configuration. When you add, delete, or replace values in an element that allows multiple values (for example, &lt;code&gt;CNAME&lt;/code&gt;), you must specify all of the values that you want to appear in the updated distribution. In addition, you must update the corresponding &lt;code&gt;Quantity&lt;/code&gt; element.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateDistribution&lt;/code&gt; request to update the configuration for your distribution:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;In the request body, include the XML document that you updated in Step 2. The request body must include an XML document with a &lt;code&gt;DistributionConfig&lt;/code&gt; element.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Set the value of the HTTP &lt;code&gt;If-Match&lt;/code&gt; header to the value of the &lt;code&gt;ETag&lt;/code&gt; header that CloudFront returned when you submitted the &lt;code&gt;GetDistributionConfig&lt;/code&gt; request in Step 1.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Review the response to the &lt;code&gt;UpdateDistribution&lt;/code&gt; request to confirm that the configuration was successfully updated.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Optional: Submit a &lt;a&gt;GetDistribution&lt;/a&gt; request to confirm that your changes have propagated. When propagation is complete, the value of &lt;code&gt;Status&lt;/code&gt; is &lt;code&gt;Deployed&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Beginning with the 2012-05-05 version of the CloudFront API, we made substantial changes to the format of the XML document that you include in the request body when you create or update a distribution. With previous versions of the API, we discovered that it was too easy to accidentally delete one or more values for an element that accepts multiple values, for example, CNAMEs and trusted signers. Our changes for the 2012-05-05 release are intended to prevent these accidental deletions and to notify you when there&#39;s a mismatch between the number of values you say you&#39;re specifying in the &lt;code&gt;Quantity&lt;/code&gt; element and the number of values you&#39;re actually specifying.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = CreateDistribution20170325Request.from_dict(body)
    return web.Response(status=200)


async def update_streaming_distribution20170325(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, if_match=None) -> web.Response:
    """update_streaming_distribution20170325

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
    body = CreateStreamingDistribution20170325Request.from_dict(body)
    return web.Response(status=200)
