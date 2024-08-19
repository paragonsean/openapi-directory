from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_lifecycle_policy_request import CreateLifecyclePolicyRequest
from openapi_server.models.create_lifecycle_policy_response import CreateLifecyclePolicyResponse
from openapi_server.models.get_lifecycle_policies_response import GetLifecyclePoliciesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.resource_type_values import ResourceTypeValues
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_lifecycle_policy_request import UpdateLifecyclePolicyRequest
from openapi_server import util


async def create_lifecycle_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_lifecycle_policy

    Creates a policy to manage the lifecycle of the specified Amazon Web Services resources. You can create up to 100 lifecycle policies.

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
    body = CreateLifecyclePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def get_lifecycle_policies(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, policy_ids=None, state=None, resource_types=None, target_tags=None, tags_to_add=None) -> web.Response:
    """get_lifecycle_policies

    &lt;p&gt;Gets summary information about all or the specified data lifecycle policies.&lt;/p&gt; &lt;p&gt;To get complete information about a policy, use &lt;a&gt;GetLifecyclePolicy&lt;/a&gt;.&lt;/p&gt;

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
    :param policy_ids: The identifiers of the data lifecycle policies.
    :type policy_ids: List[str]
    :param state: The activation state.
    :type state: str
    :param resource_types: The resource type.
    :type resource_types: list | bytes
    :param target_tags: &lt;p&gt;The target tag for a policy.&lt;/p&gt; &lt;p&gt;Tags are strings in the format &lt;code&gt;key&#x3D;value&lt;/code&gt;.&lt;/p&gt;
    :type target_tags: List[str]
    :param tags_to_add: &lt;p&gt;The tags to add to objects created by the policy.&lt;/p&gt; &lt;p&gt;Tags are strings in the format &lt;code&gt;key&#x3D;value&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;These user-defined tags are added in addition to the Amazon Web Services-added lifecycle tags.&lt;/p&gt;
    :type tags_to_add: List[str]

    """
    resource_types = [ResourceTypeValues.from_dict(d) for d in resource_types]
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags for the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
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


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds the specified tags to the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the specified tags from the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
    :param tag_keys: The tag keys.
    :type tag_keys: List[str]
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


async def update_lifecycle_policy(request: web.Request, policy_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_lifecycle_policy

    &lt;p&gt;Updates the specified lifecycle policy.&lt;/p&gt; &lt;p&gt;For more information about updating a policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-modify-delete.html#modify\&quot;&gt;Modify lifecycle policies&lt;/a&gt;.&lt;/p&gt;

    :param policy_id: The identifier of the lifecycle policy.
    :type policy_id: str
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
    body = UpdateLifecyclePolicyRequest.from_dict(body)
    return web.Response(status=200)
