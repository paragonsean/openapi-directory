from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_get_item_input import BatchGetItemInput
from openapi_server.models.batch_get_item_output import BatchGetItemOutput
from openapi_server.models.batch_write_item_input import BatchWriteItemInput
from openapi_server.models.batch_write_item_output import BatchWriteItemOutput
from openapi_server.models.create_table_input import CreateTableInput
from openapi_server.models.create_table_output import CreateTableOutput
from openapi_server.models.delete_item_input import DeleteItemInput
from openapi_server.models.delete_item_output import DeleteItemOutput
from openapi_server.models.delete_table_input import DeleteTableInput
from openapi_server.models.delete_table_output import DeleteTableOutput
from openapi_server.models.describe_table_input import DescribeTableInput
from openapi_server.models.describe_table_output import DescribeTableOutput
from openapi_server.models.get_item_input import GetItemInput
from openapi_server.models.get_item_output import GetItemOutput
from openapi_server.models.list_tables_input import ListTablesInput
from openapi_server.models.list_tables_output import ListTablesOutput
from openapi_server.models.put_item_input import PutItemInput
from openapi_server.models.put_item_output import PutItemOutput
from openapi_server.models.query_input import QueryInput
from openapi_server.models.query_output import QueryOutput
from openapi_server.models.scan_input import ScanInput
from openapi_server.models.scan_output import ScanOutput
from openapi_server.models.update_item_input import UpdateItemInput
from openapi_server.models.update_item_output import UpdateItemOutput
from openapi_server.models.update_table_input import UpdateTableInput
from openapi_server.models.update_table_output import UpdateTableOutput
from openapi_server import util


async def batch_get_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, request_items=None) -> web.Response:
    """batch_get_item

    &lt;p&gt;Retrieves the attributes for multiple items from multiple tables using their primary keys.&lt;/p&gt; &lt;p&gt;The maximum number of item attributes that can be retrieved for a single operation is 100. Also, the number of items retrieved is constrained by a 1 MB the size limit. If the response size limit is exceeded or a partial result is returned due to an internal processing failure, Amazon DynamoDB returns an &lt;code&gt;UnprocessedKeys&lt;/code&gt; value so you can retry the operation starting with the next item to get.&lt;/p&gt; &lt;p&gt;Amazon DynamoDB automatically adjusts the number of items returned per page to enforce this limit. For example, even if you ask to retrieve 100 items, but each individual item is 50k in size, the system returns 20 items and an appropriate &lt;code&gt;UnprocessedKeys&lt;/code&gt; value so you can get the next page of results. If necessary, your application needs its own logic to assemble the pages of results into one set.&lt;/p&gt;

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
    :param request_items: Pagination token
    :type request_items: str

    """
    body = BatchGetItemInput.from_dict(body)
    return web.Response(status=200)


async def batch_write_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_write_item

    &lt;p&gt;Allows to execute a batch of Put and/or Delete Requests for many tables in a single call. A total of 25 requests are allowed.&lt;/p&gt; &lt;p&gt;There are no transaction guarantees provided by this API. It does not allow conditional puts nor does it support return values.&lt;/p&gt;

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
    body = BatchWriteItemInput.from_dict(body)
    return web.Response(status=200)


async def create_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_table

    &lt;p&gt;Adds a new table to your account.&lt;/p&gt; &lt;p&gt;The table name must be unique among those associated with the AWS Account issuing the request, and the AWS Region that receives the request (e.g. &lt;code&gt;us-east-1&lt;/code&gt;).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;CreateTable&lt;/code&gt; operation triggers an asynchronous workflow to begin creating the table. Amazon DynamoDB immediately returns the state of the table (&lt;code&gt;CREATING&lt;/code&gt;) until the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state. Once the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state, you can perform data plane operations.&lt;/p&gt;

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
    body = CreateTableInput.from_dict(body)
    return web.Response(status=200)


async def delete_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_item

    &lt;p&gt;Deletes a single item in a table by primary key.&lt;/p&gt; &lt;p&gt;You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected attribute value.&lt;/p&gt;

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
    body = DeleteItemInput.from_dict(body)
    return web.Response(status=200)


async def delete_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_table

    &lt;p&gt;Deletes a table and all of its items.&lt;/p&gt; &lt;p&gt;If the table is in the &lt;code&gt;ACTIVE&lt;/code&gt; state, you can delete it. If a table is in &lt;code&gt;CREATING&lt;/code&gt; or &lt;code&gt;UPDATING&lt;/code&gt; states then Amazon DynamoDB returns a &lt;code&gt;ResourceInUseException&lt;/code&gt;. If the specified table does not exist, Amazon DynamoDB returns a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt;

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
    body = DeleteTableInput.from_dict(body)
    return web.Response(status=200)


async def describe_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_table

    &lt;p&gt;Retrieves information about the table, including the current status of the table, the primary key schema and when the table was created.&lt;/p&gt; &lt;p&gt;If the table does not exist, Amazon DynamoDB returns a &lt;code&gt;ResourceNotFoundException&lt;/code&gt;.&lt;/p&gt;

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
    body = DescribeTableInput.from_dict(body)
    return web.Response(status=200)


async def get_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_item

    &lt;p&gt;Retrieves a set of Attributes for an item that matches the primary key.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;GetItem&lt;/code&gt; operation provides an eventually-consistent read by default. If eventually-consistent reads are not acceptable for your application, use &lt;code&gt;ConsistentRead&lt;/code&gt;. Although this operation might take longer than a standard read, it always returns the last updated value.&lt;/p&gt;

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
    body = GetItemInput.from_dict(body)
    return web.Response(status=200)


async def list_tables(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, exclusive_start_table_name=None) -> web.Response:
    """list_tables

    Retrieves a paginated list of table names created by the AWS Account of the caller in the AWS Region (e.g. &lt;code&gt;us-east-1&lt;/code&gt;).

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
    :param limit: Pagination limit
    :type limit: str
    :param exclusive_start_table_name: Pagination token
    :type exclusive_start_table_name: str

    """
    body = ListTablesInput.from_dict(body)
    return web.Response(status=200)


async def put_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_item

    &lt;p&gt;Creates a new item, or replaces an old item with a new item (including all the attributes).&lt;/p&gt; &lt;p&gt;If an item already exists in the specified table with the same primary key, the new item completely replaces the existing item. You can perform a conditional put (insert a new item if one with the specified primary key doesn&#39;t exist), or replace an existing item if it has certain attribute values.&lt;/p&gt;

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
    body = PutItemInput.from_dict(body)
    return web.Response(status=200)


async def query(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, exclusive_start_key=None) -> web.Response:
    """query

    &lt;p&gt;Gets the values of one or more items and its attributes by primary key (composite primary key, only).&lt;/p&gt; &lt;p&gt;Narrow the scope of the query using comparison operators on the &lt;code&gt;RangeKeyValue&lt;/code&gt; of the composite key. Use the &lt;code&gt;ScanIndexForward&lt;/code&gt; parameter to get results in forward or reverse order by range key.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param exclusive_start_key: Pagination token
    :type exclusive_start_key: str

    """
    body = QueryInput.from_dict(body)
    return web.Response(status=200)


async def scan(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, exclusive_start_key=None) -> web.Response:
    """scan

    &lt;p&gt;Retrieves one or more items and its attributes by performing a full scan of a table.&lt;/p&gt; &lt;p&gt;Provide a &lt;code&gt;ScanFilter&lt;/code&gt; to get more specific results.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param exclusive_start_key: Pagination token
    :type exclusive_start_key: str

    """
    body = ScanInput.from_dict(body)
    return web.Response(status=200)


async def update_item(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_item

    &lt;p&gt;Edits an existing item&#39;s attributes.&lt;/p&gt; &lt;p&gt;You can perform a conditional update (insert a new attribute name-value pair if it doesn&#39;t exist, or replace an existing name-value pair if it has certain expected attribute values).&lt;/p&gt;

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
    body = UpdateItemInput.from_dict(body)
    return web.Response(status=200)


async def update_table(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_table

    &lt;p&gt;Updates the provisioned throughput for the given table.&lt;/p&gt; &lt;p&gt;Setting the throughput for a table helps you manage performance and is part of the Provisioned Throughput feature of Amazon DynamoDB.&lt;/p&gt;

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
    body = UpdateTableInput.from_dict(body)
    return web.Response(status=200)
