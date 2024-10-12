from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_change_set_response import CancelChangeSetResponse
from openapi_server.models.describe_change_set_response import DescribeChangeSetResponse
from openapi_server.models.describe_entity_response import DescribeEntityResponse
from openapi_server.models.get_resource_policy_response import GetResourcePolicyResponse
from openapi_server.models.list_change_sets_request import ListChangeSetsRequest
from openapi_server.models.list_change_sets_response import ListChangeSetsResponse
from openapi_server.models.list_entities_request import ListEntitiesRequest
from openapi_server.models.list_entities_response import ListEntitiesResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.start_change_set_request import StartChangeSetRequest
from openapi_server.models.start_change_set_response import StartChangeSetResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server import util


async def cancel_change_set(request: web.Request, catalog, change_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_change_set

    Used to cancel an open change request. Must be sent before the status of the request changes to &lt;code&gt;APPLYING&lt;/code&gt;, the final stage of completing your change request. You can describe a change during the 60-day request history retention period for API calls.

    :param catalog: Required. The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt;.
    :type catalog: str
    :param change_set_id: Required. The unique identifier of the &lt;code&gt;StartChangeSet&lt;/code&gt; request that you want to cancel.
    :type change_set_id: str
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


async def delete_resource_policy(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

    Deletes a resource-based policy on an Entity that is identified by its resource ARN.

    :param resource_arn: The Amazon Resource Name (ARN) of the Entity resource that is associated with the resource policy.
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


async def describe_change_set(request: web.Request, catalog, change_set_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_change_set

    Provides information about a given change set.

    :param catalog: Required. The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt; 
    :type catalog: str
    :param change_set_id: Required. The unique identifier for the &lt;code&gt;StartChangeSet&lt;/code&gt; request that you want to describe the details for.
    :type change_set_id: str
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


async def describe_entity(request: web.Request, catalog, entity_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_entity

    Returns the metadata and content of the entity.

    :param catalog: Required. The catalog related to the request. Fixed value: &lt;code&gt;AWSMarketplace&lt;/code&gt; 
    :type catalog: str
    :param entity_id: Required. The unique ID of the entity to describe.
    :type entity_id: str
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


async def get_resource_policy(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_resource_policy

    Gets a resource-based policy of an Entity that is identified by its resource ARN.

    :param resource_arn: The Amazon Resource Name (ARN) of the Entity resource that is associated with the resource policy.
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


async def list_change_sets(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_change_sets

    &lt;p&gt;Returns the list of change sets owned by the account being used to make the call. You can filter this list by providing any combination of &lt;code&gt;entityId&lt;/code&gt;, &lt;code&gt;ChangeSetName&lt;/code&gt;, and status. If you provide more than one filter, the API operation applies a logical AND between the filters.&lt;/p&gt; &lt;p&gt;You can describe a change during the 60-day request history retention period for API calls.&lt;/p&gt;

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListChangeSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_entities(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_entities

    Provides the list of entities of a given type.

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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListEntitiesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists all tags that have been added to a resource (either an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\&quot;&gt;entity&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt;change set&lt;/a&gt;).

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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def put_resource_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

    Attaches a resource-based policy to an Entity. Examples of an entity include: &lt;code&gt;AmiProduct&lt;/code&gt; and &lt;code&gt;ContainerProduct&lt;/code&gt;.

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
    body = PutResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def start_change_set(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_change_set

    &lt;p&gt;Allows you to request changes for your entities. Within a single &lt;code&gt;ChangeSet&lt;/code&gt;, you can&#39;t start the same change type against the same entity multiple times. Additionally, when a &lt;code&gt;ChangeSet&lt;/code&gt; is running, all the entities targeted by the different changes are locked until the change set has completed (either succeeded, cancelled, or failed). If you try to start a change set containing a change against an entity that is already locked, you will receive a &lt;code&gt;ResourceInUseException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;For example, you can&#39;t start the &lt;code&gt;ChangeSet&lt;/code&gt; described in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_Examples\&quot;&gt;example&lt;/a&gt; later in this topic because it contains two changes to run the same change type (&lt;code&gt;AddRevisions&lt;/code&gt;) against the same entity (&lt;code&gt;entity-id@1&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;For more information about working with change sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt; Working with change sets&lt;/a&gt;. For information on change types for single-AMI products, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products\&quot;&gt;Working with single-AMI products&lt;/a&gt;. Als, for more information on change types available for container-based products, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products\&quot;&gt;Working with container products&lt;/a&gt;.&lt;/p&gt;

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
    body = StartChangeSetRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Tags a resource (either an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\&quot;&gt;entity&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt;change set&lt;/a&gt;).

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


async def untag_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes a tag or list of tags from a resource (either an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities\&quot;&gt;entity&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets\&quot;&gt;change set&lt;/a&gt;).

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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)
