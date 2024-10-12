from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_default_view_output import AssociateDefaultViewOutput
from openapi_server.models.associate_default_view_request import AssociateDefaultViewRequest
from openapi_server.models.batch_get_view_output import BatchGetViewOutput
from openapi_server.models.batch_get_view_request import BatchGetViewRequest
from openapi_server.models.create_index_output import CreateIndexOutput
from openapi_server.models.create_index_request import CreateIndexRequest
from openapi_server.models.create_view_output import CreateViewOutput
from openapi_server.models.create_view_request import CreateViewRequest
from openapi_server.models.delete_index_output import DeleteIndexOutput
from openapi_server.models.delete_index_request import DeleteIndexRequest
from openapi_server.models.delete_view_output import DeleteViewOutput
from openapi_server.models.delete_view_request import DeleteViewRequest
from openapi_server.models.get_default_view_output import GetDefaultViewOutput
from openapi_server.models.get_index_output import GetIndexOutput
from openapi_server.models.get_view_output import GetViewOutput
from openapi_server.models.get_view_request import GetViewRequest
from openapi_server.models.list_indexes_output import ListIndexesOutput
from openapi_server.models.list_indexes_request import ListIndexesRequest
from openapi_server.models.list_supported_resource_types_output import ListSupportedResourceTypesOutput
from openapi_server.models.list_supported_resource_types_request import ListSupportedResourceTypesRequest
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.list_views_output import ListViewsOutput
from openapi_server.models.list_views_request import ListViewsRequest
from openapi_server.models.search_output import SearchOutput
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_index_type_output import UpdateIndexTypeOutput
from openapi_server.models.update_index_type_request import UpdateIndexTypeRequest
from openapi_server.models.update_view_output import UpdateViewOutput
from openapi_server.models.update_view_request import UpdateViewRequest
from openapi_server import util


async def associate_default_view(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_default_view

    &lt;p&gt;Sets the specified view as the default for the Amazon Web Services Region in which you call this operation. When a user performs a &lt;a&gt;Search&lt;/a&gt; that doesn&#39;t explicitly specify which view to use, then Amazon Web Services Resource Explorer automatically chooses this default view for searches performed in this Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;If an Amazon Web Services Region doesn&#39;t have a default view configured, then users must explicitly specify a view with every &lt;code&gt;Search&lt;/code&gt; operation performed in that Region.&lt;/p&gt;

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
    body = AssociateDefaultViewRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_view(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_view

    Retrieves details about a list of views.

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
    body = BatchGetViewRequest.from_dict(body)
    return web.Response(status=200)


async def create_index(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_index

    &lt;p&gt;Turns on Amazon Web Services Resource Explorer in the Amazon Web Services Region in which you called this operation by creating an index. Resource Explorer begins discovering the resources in this Region and stores the details about the resources in the index so that they can be queried by using the &lt;a&gt;Search&lt;/a&gt; operation. You can create only one index in a Region.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation creates only a &lt;i&gt;local&lt;/i&gt; index. To promote the local index in one Amazon Web Services Region into the aggregator index for the Amazon Web Services account, use the &lt;a&gt;UpdateIndexType&lt;/a&gt; operation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html\&quot;&gt;Turning on cross-Region search by creating an aggregator index&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more details about what happens when you turn on Resource Explorer in an Amazon Web Services Region, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-activate.html\&quot;&gt;Turn on Resource Explorer to index your resources in an Amazon Web Services Region&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If this is the first Amazon Web Services Region in which you&#39;ve created an index for Resource Explorer, then this operation also &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html\&quot;&gt;creates a service-linked role&lt;/a&gt; in your Amazon Web Services account that allows Resource Explorer to enumerate your resources to populate the index.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Action&lt;/b&gt;: &lt;code&gt;resource-explorer-2:CreateIndex&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Resource&lt;/b&gt;: The ARN of the index (as it will exist after the operation completes) in the Amazon Web Services Region and account in which you&#39;re trying to create the index. Use the wildcard character (&lt;code&gt;*&lt;/code&gt;) at the end of the string to match the eventual UUID. For example, the following &lt;code&gt;Resource&lt;/code&gt; element restricts the role or user to creating an index in only the &lt;code&gt;us-east-2&lt;/code&gt; Region of the specified account.&lt;/p&gt; &lt;p&gt; &lt;code&gt;\&quot;Resource\&quot;: \&quot;arn:aws:resource-explorer-2:us-west-2:&lt;i&gt;&amp;lt;account-id&amp;gt;&lt;/i&gt;:index/*\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Alternatively, you can use &lt;code&gt;\&quot;Resource\&quot;: \&quot;*\&quot;&lt;/code&gt; to allow the role or user to create an index in any Region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Action&lt;/b&gt;: &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Resource&lt;/b&gt;: No specific resource (*). &lt;/p&gt; &lt;p&gt;This permission is required only the first time you create an index to turn on Resource Explorer in the account. Resource Explorer uses this to create the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html\&quot;&gt;service-linked role needed to index the resources in your account&lt;/a&gt;. Resource Explorer uses the same service-linked role for all additional indexes you create afterwards.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateIndexRequest.from_dict(body)
    return web.Response(status=200)


async def create_view(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_view

    &lt;p&gt;Creates a view that users can query by using the &lt;a&gt;Search&lt;/a&gt; operation. Results from queries that you make using this view include only resources that match the view&#39;s &lt;code&gt;Filters&lt;/code&gt;. For more information about Amazon Web Services Resource Explorer views, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views.html\&quot;&gt;Managing views&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Only the principals with an IAM identity-based policy that grants &lt;code&gt;Allow&lt;/code&gt; to the &lt;code&gt;Search&lt;/code&gt; action on a &lt;code&gt;Resource&lt;/code&gt; with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon resource name (ARN)&lt;/a&gt; of this view can &lt;a&gt;Search&lt;/a&gt; using views you create with this operation.&lt;/p&gt;

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
    body = CreateViewRequest.from_dict(body)
    return web.Response(status=200)


async def delete_index(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_index

    &lt;p&gt;Deletes the specified index and turns off Amazon Web Services Resource Explorer in the specified Amazon Web Services Region. When you delete an index, Resource Explorer stops discovering and indexing resources in that Region. Resource Explorer also deletes all views in that Region. These actions occur as asynchronous background tasks. You can check to see when the actions are complete by using the &lt;a&gt;GetIndex&lt;/a&gt; operation and checking the &lt;code&gt;Status&lt;/code&gt; response value.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If the index you delete is the aggregator index for the Amazon Web Services account, you must wait 24 hours before you can promote another local index to be the aggregator index for the account. Users can&#39;t perform account-wide searches using Resource Explorer until another aggregator index is configured.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteIndexRequest.from_dict(body)
    return web.Response(status=200)


async def delete_view(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_view

    &lt;p&gt;Deletes the specified view.&lt;/p&gt; &lt;p&gt;If the specified view is the default view for its Amazon Web Services Region, then all &lt;a&gt;Search&lt;/a&gt; operations in that Region must explicitly specify the view to use until you configure a new default by calling the &lt;a&gt;AssociateDefaultView&lt;/a&gt; operation.&lt;/p&gt;

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
    body = DeleteViewRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_default_view(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_default_view

    &lt;p&gt;After you call this operation, the affected Amazon Web Services Region no longer has a default view. All &lt;a&gt;Search&lt;/a&gt; operations in that Region must explicitly specify a view or the operation fails. You can configure a new default by calling the &lt;a&gt;AssociateDefaultView&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;If an Amazon Web Services Region doesn&#39;t have a default view configured, then users must explicitly specify a view with every &lt;code&gt;Search&lt;/code&gt; operation performed in that Region.&lt;/p&gt;

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


async def get_default_view(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_default_view

    Retrieves the Amazon Resource Name (ARN) of the view that is the default for the Amazon Web Services Region in which you call this operation. You can then call &lt;a&gt;GetView&lt;/a&gt; to retrieve the details of that view.

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


async def get_index(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_index

    Retrieves details about the Amazon Web Services Resource Explorer index in the Amazon Web Services Region in which you invoked the operation.

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


async def get_view(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_view

    Retrieves details of the specified view.

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
    body = GetViewRequest.from_dict(body)
    return web.Response(status=200)


async def list_indexes(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_indexes

    Retrieves a list of all of the indexes in Amazon Web Services Regions that are currently collecting resource information for Amazon Web Services Resource Explorer.

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
    body = ListIndexesRequest.from_dict(body)
    return web.Response(status=200)


async def list_supported_resource_types(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_supported_resource_types

    Retrieves a list of all resource types currently supported by Amazon Web Services Resource Explorer.

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
    body = ListSupportedResourceTypesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags that are attached to the specified resource.

    :param resource_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon resource name (ARN)&lt;/a&gt; of the view or index that you want to attach tags to.
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


async def list_views(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_views

    &lt;p&gt;Lists the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon resource names (ARNs)&lt;/a&gt; of the views available in the Amazon Web Services Region in which you call this operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Always check the &lt;code&gt;NextToken&lt;/code&gt; response parameter for a &lt;code&gt;null&lt;/code&gt; value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The &lt;code&gt;NextToken&lt;/code&gt; response parameter value is &lt;code&gt;null&lt;/code&gt; &lt;i&gt;only&lt;/i&gt; when there are no more results to display.&lt;/p&gt; &lt;/note&gt;

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
    body = ListViewsRequest.from_dict(body)
    return web.Response(status=200)


async def search(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search

    &lt;p&gt;Searches for resources and displays details about all resources that match the specified criteria. You must specify a query string.&lt;/p&gt; &lt;p&gt;All search queries must use a view. If you don&#39;t explicitly specify a view, then Amazon Web Services Resource Explorer uses the default view for the Amazon Web Services Region in which you call this operation. The results are the logical intersection of the results that match both the &lt;code&gt;QueryString&lt;/code&gt; parameter supplied to this operation and the &lt;code&gt;SearchFilter&lt;/code&gt; parameter attached to the view.&lt;/p&gt; &lt;p&gt;For the complete syntax supported by the &lt;code&gt;QueryString&lt;/code&gt; parameter, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/APIReference/about-query-syntax.html\&quot;&gt;Search query syntax reference for Resource Explorer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If your search results are empty, or are missing results that you think should be there, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html\&quot;&gt;Troubleshooting Resource Explorer search&lt;/a&gt;.&lt;/p&gt;

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
    body = SearchRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds one or more tag key and value pairs to an Amazon Web Services Resource Explorer view or index.

    :param resource_arn: The Amazon Resource Name (ARN) of the view or index that you want to attach tags to.
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

    Removes one or more tag key and value pairs from an Amazon Web Services Resource Explorer view or index.

    :param resource_arn: The Amazon Resource Name (ARN) of the view or index that you want to remove tags from.
    :type resource_arn: str
    :param tag_keys: A list of the keys for the tags that you want to remove from the specified view or index.
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


async def update_index_type(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_index_type

    &lt;p&gt;Changes the type of the index from one of the following types to the other. For more information about indexes and the role they perform in Amazon Web Services Resource Explorer, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html\&quot;&gt;Turning on cross-Region search by creating an aggregator index&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Resource Explorer User Guide&lt;/i&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;AGGREGATOR&lt;/code&gt; index type&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The index contains information about resources from all Amazon Web Services Regions in the Amazon Web Services account in which you&#39;ve created a Resource Explorer index. Resource information from all other Regions is replicated to this Region&#39;s index.&lt;/p&gt; &lt;p&gt;When you change the index type to &lt;code&gt;AGGREGATOR&lt;/code&gt;, Resource Explorer turns on replication of all discovered resource information from the other Amazon Web Services Regions in your account to this index. You can then, from this Region only, perform resource search queries that span all Amazon Web Services Regions in the Amazon Web Services account. Turning on replication from all other Regions is performed by asynchronous background tasks. You can check the status of the asynchronous tasks by using the &lt;a&gt;GetIndex&lt;/a&gt; operation. When the asynchronous tasks complete, the &lt;code&gt;Status&lt;/code&gt; response of that operation changes from &lt;code&gt;UPDATING&lt;/code&gt; to &lt;code&gt;ACTIVE&lt;/code&gt;. After that, you can start to see results from other Amazon Web Services Regions in query results. However, it can take several hours for replication from all other Regions to complete.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can have only one aggregator index per Amazon Web Services account. Before you can promote a different index to be the aggregator index for the account, you must first demote the existing aggregator index to type &lt;code&gt;LOCAL&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;LOCAL&lt;/code&gt; index type&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The index contains information about resources in only the Amazon Web Services Region in which the index exists. If an aggregator index in another Region exists, then information in this local index is replicated to the aggregator index.&lt;/p&gt; &lt;p&gt;When you change the index type to &lt;code&gt;LOCAL&lt;/code&gt;, Resource Explorer turns off the replication of resource information from all other Amazon Web Services Regions in the Amazon Web Services account to this Region. The aggregator index remains in the &lt;code&gt;UPDATING&lt;/code&gt; state until all replication with other Regions successfully stops. You can check the status of the asynchronous task by using the &lt;a&gt;GetIndex&lt;/a&gt; operation. When Resource Explorer successfully stops all replication with other Regions, the &lt;code&gt;Status&lt;/code&gt; response of that operation changes from &lt;code&gt;UPDATING&lt;/code&gt; to &lt;code&gt;ACTIVE&lt;/code&gt;. Separately, the resource information from other Regions that was previously stored in the index is deleted within 30 days by another background task. Until that asynchronous task completes, some results from other Regions can continue to appear in search results.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After you demote an aggregator index to a local index, you must wait 24 hours before you can promote another index to be the new aggregator index for the account.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UpdateIndexTypeRequest.from_dict(body)
    return web.Response(status=200)


async def update_view(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_view

    Modifies some of the details of a view. You can change the filter string and the list of included properties. You can&#39;t change the name of the view.

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
    body = UpdateViewRequest.from_dict(body)
    return web.Response(status=200)
