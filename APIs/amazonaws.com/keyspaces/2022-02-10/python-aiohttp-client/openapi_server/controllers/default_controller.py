from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_keyspace_request import CreateKeyspaceRequest
from openapi_server.models.create_keyspace_response import CreateKeyspaceResponse
from openapi_server.models.create_table_request import CreateTableRequest
from openapi_server.models.create_table_response import CreateTableResponse
from openapi_server.models.delete_keyspace_request import DeleteKeyspaceRequest
from openapi_server.models.delete_table_request import DeleteTableRequest
from openapi_server.models.get_keyspace_request import GetKeyspaceRequest
from openapi_server.models.get_keyspace_response import GetKeyspaceResponse
from openapi_server.models.get_table_request import GetTableRequest
from openapi_server.models.get_table_response import GetTableResponse
from openapi_server.models.list_keyspaces_request import ListKeyspacesRequest
from openapi_server.models.list_keyspaces_response import ListKeyspacesResponse
from openapi_server.models.list_tables_request import ListTablesRequest
from openapi_server.models.list_tables_response import ListTablesResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.restore_table_request import RestoreTableRequest
from openapi_server.models.restore_table_response import RestoreTableResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_table_request import UpdateTableRequest
from openapi_server.models.update_table_response import UpdateTableResponse
from openapi_server import util


async def create_keyspace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_keyspace

    &lt;p&gt;The &lt;code&gt;CreateKeyspace&lt;/code&gt; operation adds a new keyspace to your account. In an Amazon Web Services account, keyspace names must be unique within each Region.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateKeyspace&lt;/code&gt; is an asynchronous operation. You can monitor the creation status of the new keyspace by using the &lt;code&gt;GetKeyspace&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-keyspaces.html#keyspaces-create\&quot;&gt;Creating keyspaces&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateKeyspaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_table

    &lt;p&gt;The &lt;code&gt;CreateTable&lt;/code&gt; operation adds a new table to the specified keyspace. Within a keyspace, table names must be unique.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateTable&lt;/code&gt; is an asynchronous operation. When the request is received, the status of the table is set to &lt;code&gt;CREATING&lt;/code&gt;. You can monitor the creation status of the new table by using the &lt;code&gt;GetTable&lt;/code&gt; operation, which returns the current &lt;code&gt;status&lt;/code&gt; of the table. You can start using a table when the status is &lt;code&gt;ACTIVE&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-tables.html#tables-create\&quot;&gt;Creating tables&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateTableRequest.from_dict(body)
    return web.Response(status=200)


async def delete_keyspace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_keyspace

    The &lt;code&gt;DeleteKeyspace&lt;/code&gt; operation deletes a keyspace and all of its tables. 

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteKeyspaceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_table

    The &lt;code&gt;DeleteTable&lt;/code&gt; operation deletes a table and all of its data. After a &lt;code&gt;DeleteTable&lt;/code&gt; request is received, the specified table is in the &lt;code&gt;DELETING&lt;/code&gt; state until Amazon Keyspaces completes the deletion. If the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state, you can delete it. If a table is either in the &lt;code&gt;CREATING&lt;/code&gt; or &lt;code&gt;UPDATING&lt;/code&gt; states, then Amazon Keyspaces returns a &lt;code&gt;ResourceInUseException&lt;/code&gt;. If the specified table does not exist, Amazon Keyspaces returns a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;. If the table is already in the &lt;code&gt;DELETING&lt;/code&gt; state, no error is returned.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteTableRequest.from_dict(body)
    return web.Response(status=200)


async def get_keyspace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_keyspace

    Returns the name and the Amazon Resource Name (ARN) of the specified table.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetKeyspaceRequest.from_dict(body)
    return web.Response(status=200)


async def get_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_table

    &lt;p&gt;Returns information about the table, including the table&#39;s name and current status, the keyspace name, configuration settings, and metadata.&lt;/p&gt; &lt;p&gt;To read table metadata using &lt;code&gt;GetTable&lt;/code&gt;, &lt;code&gt;Select&lt;/code&gt; action permissions for the table and system tables are required to complete the operation.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = GetTableRequest.from_dict(body)
    return web.Response(status=200)


async def list_keyspaces(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_keyspaces

    Returns a list of keyspaces.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListKeyspacesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tables(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tables

    Returns a list of tables for a specified keyspace.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTablesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    Returns a list of all tags associated with the specified Amazon Keyspaces resource.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def restore_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """restore_table

    &lt;p&gt;Restores the specified table to the specified point in time within the &lt;code&gt;earliest_restorable_timestamp&lt;/code&gt; and the current time. For more information about restore points, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_window\&quot;&gt; Time window for PITR continuous backups&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.&lt;/p&gt; &lt;p&gt;When you restore using point in time recovery, Amazon Keyspaces restores your source table&#39;s schema and data to the state based on the selected timestamp &lt;code&gt;(day:hour:minute:second)&lt;/code&gt; to a new table. The Time to Live (TTL) settings are also restored to the state based on the selected timestamp.&lt;/p&gt; &lt;p&gt;In addition to the table&#39;s schema, data, and TTL settings, &lt;code&gt;RestoreTable&lt;/code&gt; restores the capacity mode, encryption, and point-in-time recovery settings from the source table. Unlike the table&#39;s schema data and TTL settings, which are restored based on the selected timestamp, these settings are always restored based on the table&#39;s settings as of the current time or when the table was deleted.&lt;/p&gt; &lt;p&gt;You can also overwrite these settings during restore:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Read/write capacity mode&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Provisioned throughput capacity settings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Point-in-time (PITR) settings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tags&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html#howitworks_backup_settings\&quot;&gt;PITR restore settings&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Note that the following settings are not restored, and you must configure them manually for the new table:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Automatic scaling policies (for tables that use provisioned capacity mode)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Identity and Access Management (IAM) policies&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon CloudWatch metrics and alarms&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RestoreTableRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Associates a set of tags with a Amazon Keyspaces resource. You can then activate these user-defined tags so that they appear on the Cost Management Console for cost allocation tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html\&quot;&gt;Adding tags and labels to Amazon Keyspaces resources&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For IAM policy examples that show how to control access to Amazon Keyspaces resources based on tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-tags\&quot;&gt;Amazon Keyspaces resource access based on tags&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes the association of tags from a Amazon Keyspaces resource.

    :param x_amz_target: 
    :type x_amz_target: str
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


async def update_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_table

    Adds new columns to the table or updates one of the table&#39;s settings, for example capacity mode, encryption, point-in-time recovery, or ttl settings. Note that you can only update one specific table setting per update operation.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateTableRequest.from_dict(body)
    return web.Response(status=200)
