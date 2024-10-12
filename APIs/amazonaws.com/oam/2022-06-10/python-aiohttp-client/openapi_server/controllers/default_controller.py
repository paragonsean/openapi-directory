from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_link_output import CreateLinkOutput
from openapi_server.models.create_link_request import CreateLinkRequest
from openapi_server.models.create_sink_output import CreateSinkOutput
from openapi_server.models.create_sink_request import CreateSinkRequest
from openapi_server.models.delete_link_request import DeleteLinkRequest
from openapi_server.models.delete_sink_request import DeleteSinkRequest
from openapi_server.models.get_link_output import GetLinkOutput
from openapi_server.models.get_link_request import GetLinkRequest
from openapi_server.models.get_sink_output import GetSinkOutput
from openapi_server.models.get_sink_policy_output import GetSinkPolicyOutput
from openapi_server.models.get_sink_policy_request import GetSinkPolicyRequest
from openapi_server.models.get_sink_request import GetSinkRequest
from openapi_server.models.list_attached_links_output import ListAttachedLinksOutput
from openapi_server.models.list_attached_links_request import ListAttachedLinksRequest
from openapi_server.models.list_links_output import ListLinksOutput
from openapi_server.models.list_links_request import ListLinksRequest
from openapi_server.models.list_sinks_output import ListSinksOutput
from openapi_server.models.list_sinks_request import ListSinksRequest
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.put_sink_policy_output import PutSinkPolicyOutput
from openapi_server.models.put_sink_policy_request import PutSinkPolicyRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_link_output import UpdateLinkOutput
from openapi_server.models.update_link_request import UpdateLinkRequest
from openapi_server import util


async def create_link(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_link

    &lt;p&gt;Creates a link between a source account and a sink that you have created in a monitoring account.&lt;/p&gt; &lt;p&gt;Before you create a link, you must create a sink in the monitoring account and create a sink policy in that account. The sink policy must permit the source account to link to it. You can grant permission to source accounts by granting permission to an entire organization or to individual accounts.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html\&quot;&gt;CreateSink&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html\&quot;&gt;PutSinkPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each monitoring account can be linked to as many as 100,000 source accounts.&lt;/p&gt; &lt;p&gt;Each source account can be linked to as many as five monitoring accounts.&lt;/p&gt;

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
    body = CreateLinkRequest.from_dict(body)
    return web.Response(status=200)


async def create_sink(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sink

    &lt;p&gt;Use this to create a &lt;i&gt;sink&lt;/i&gt; in the current account, so that it can be used as a monitoring account in CloudWatch cross-account observability. A sink is a resource that represents an attachment point in a monitoring account. Source accounts can link to the sink to send observability data.&lt;/p&gt; &lt;p&gt;After you create a sink, you must create a sink policy that allows source accounts to attach to it. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html\&quot;&gt;PutSinkPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each account can contain one sink. If you delete a sink, you can then create a new one in that account.&lt;/p&gt;

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
    body = CreateSinkRequest.from_dict(body)
    return web.Response(status=200)


async def delete_link(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_link

    Deletes a link between a monitoring account sink and a source account. You must run this operation in the source account.

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
    body = DeleteLinkRequest.from_dict(body)
    return web.Response(status=200)


async def delete_sink(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sink

    Deletes a sink. You must delete all links to a sink before you can delete that sink.

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
    body = DeleteSinkRequest.from_dict(body)
    return web.Response(status=200)


async def get_link(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_link

    &lt;p&gt;Returns complete information about one link.&lt;/p&gt; &lt;p&gt;To use this operation, provide the link ARN. To retrieve a list of link ARNs, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html\&quot;&gt;ListLinks&lt;/a&gt;.&lt;/p&gt;

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
    body = GetLinkRequest.from_dict(body)
    return web.Response(status=200)


async def get_sink(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sink

    &lt;p&gt;Returns complete information about one monitoring account sink.&lt;/p&gt; &lt;p&gt;To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html\&quot;&gt;ListSinks&lt;/a&gt;.&lt;/p&gt;

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
    body = GetSinkRequest.from_dict(body)
    return web.Response(status=200)


async def get_sink_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sink_policy

    Returns the current sink policy attached to this sink. The sink policy specifies what accounts can attach to this sink as source accounts, and what types of data they can share.

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
    body = GetSinkPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def list_attached_links(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_attached_links

    &lt;p&gt;Returns a list of source account links that are linked to this monitoring account sink.&lt;/p&gt; &lt;p&gt;To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html\&quot;&gt;ListSinks&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To find a list of links for one source account, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html\&quot;&gt;ListLinks&lt;/a&gt;.&lt;/p&gt;

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
    body = ListAttachedLinksRequest.from_dict(body)
    return web.Response(status=200)


async def list_links(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_links

    &lt;p&gt;Use this operation in a source account to return a list of links to monitoring account sinks that this source account has.&lt;/p&gt; &lt;p&gt;To find a list of links for one monitoring account sink, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html\&quot;&gt;ListAttachedLinks&lt;/a&gt; from within the monitoring account.&lt;/p&gt;

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
    body = ListLinksRequest.from_dict(body)
    return web.Response(status=200)


async def list_sinks(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_sinks

    Use this operation in a monitoring account to return the list of sinks created in that account.

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
    body = ListSinksRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with a resource. Both sinks and links support tagging.

    :param resource_arn: &lt;p&gt;The ARN of the resource that you want to view tags for.&lt;/p&gt; &lt;p&gt;The ARN format of a sink is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:sink/&lt;i&gt;sink-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a link is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:link/&lt;i&gt;link-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\&quot;&gt;CloudWatch Logs resources and operations&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Unlike tagging permissions in other Amazon Web Services services, to retrieve the list of tags for links or sinks you must have the &lt;code&gt;oam:RequestTag&lt;/code&gt; permission. The &lt;code&gt;aws:ReguestTag&lt;/code&gt; permission does not allow you to tag and untag links and sinks.&lt;/p&gt; &lt;/important&gt;
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


async def put_sink_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_sink_policy

    &lt;p&gt;Creates or updates the resource policy that grants permissions to source accounts to link to the monitoring account sink. When you create a sink policy, you can grant permissions to all accounts in an organization or to individual accounts.&lt;/p&gt; &lt;p&gt;You can also use a sink policy to limit the types of data that is shared. The three types that you can allow or deny are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Metrics&lt;/b&gt; - Specify with &lt;code&gt;AWS::CloudWatch::Metric&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Log groups&lt;/b&gt; - Specify with &lt;code&gt;AWS::Logs::LogGroup&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Traces&lt;/b&gt; - Specify with &lt;code&gt;AWS::XRay::Trace&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;See the examples in this section to see how to specify permitted source accounts and data types.&lt;/p&gt;

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
    body = PutSinkPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified resource. Both sinks and links can be tagged. &lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with a resource that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Unlike tagging permissions in other Amazon Web Services services, to tag or untag links and sinks you must have the &lt;code&gt;oam:ResourceTag&lt;/code&gt; permission. The &lt;code&gt;iam:ResourceTag&lt;/code&gt; permission does not allow you to tag and untag links and sinks.&lt;/p&gt; &lt;/important&gt;

    :param resource_arn: &lt;p&gt;The ARN of the resource that you&#39;re adding tags to.&lt;/p&gt; &lt;p&gt;The ARN format of a sink is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:sink/&lt;i&gt;sink-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a link is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:link/&lt;i&gt;link-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\&quot;&gt;CloudWatch Logs resources and operations&lt;/a&gt;.&lt;/p&gt;
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

    &lt;p&gt;Removes one or more tags from the specified resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Unlike tagging permissions in other Amazon Web Services services, to tag or untag links and sinks you must have the &lt;code&gt;oam:ResourceTag&lt;/code&gt; permission. The &lt;code&gt;iam:TagResource&lt;/code&gt; permission does not allow you to tag and untag links and sinks.&lt;/p&gt; &lt;/important&gt;

    :param resource_arn: &lt;p&gt;The ARN of the resource that you&#39;re removing tags from.&lt;/p&gt; &lt;p&gt;The ARN format of a sink is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:sink/&lt;i&gt;sink-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a link is &lt;code&gt;arn:aws:oam:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:link/&lt;i&gt;link-id&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html\&quot;&gt;CloudWatch Logs resources and operations&lt;/a&gt;.&lt;/p&gt;
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the resource.
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


async def update_link(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_link

    &lt;p&gt;Use this operation to change what types of data are shared from a source account to its linked monitoring account sink. You can&#39;t change the sink or change the monitoring account with this operation.&lt;/p&gt; &lt;p&gt;To update the list of tags associated with the sink, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateLinkRequest.from_dict(body)
    return web.Response(status=200)
