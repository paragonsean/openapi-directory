from typing import List, Dict
from aiohttp import web

from openapi_server.models.describe_stream_input import DescribeStreamInput
from openapi_server.models.describe_stream_output import DescribeStreamOutput
from openapi_server.models.get_records_input import GetRecordsInput
from openapi_server.models.get_records_output import GetRecordsOutput
from openapi_server.models.get_shard_iterator_input import GetShardIteratorInput
from openapi_server.models.get_shard_iterator_output import GetShardIteratorOutput
from openapi_server.models.list_streams_input import ListStreamsInput
from openapi_server.models.list_streams_output import ListStreamsOutput
from openapi_server import util


async def describe_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_stream

    &lt;p&gt;Returns information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can call &lt;code&gt;DescribeStream&lt;/code&gt; at a maximum rate of 10 times per second.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Each shard in the stream has a &lt;code&gt;SequenceNumberRange&lt;/code&gt; associated with it. If the &lt;code&gt;SequenceNumberRange&lt;/code&gt; has a &lt;code&gt;StartingSequenceNumber&lt;/code&gt; but no &lt;code&gt;EndingSequenceNumber&lt;/code&gt;, then the shard is still open (able to receive more stream records). If both &lt;code&gt;StartingSequenceNumber&lt;/code&gt; and &lt;code&gt;EndingSequenceNumber&lt;/code&gt; are present, then that shard is closed and can no longer receive more data.&lt;/p&gt;

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
    body = DescribeStreamInput.from_dict(body)
    return web.Response(status=200)


async def get_records(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_records

    &lt;p&gt;Retrieves the stream records from a given shard.&lt;/p&gt; &lt;p&gt;Specify a shard iterator using the &lt;code&gt;ShardIterator&lt;/code&gt; parameter. The shard iterator specifies the position in the shard from which you want to start reading stream records sequentially. If there are no stream records available in the portion of the shard that the iterator points to, &lt;code&gt;GetRecords&lt;/code&gt; returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains stream records.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;GetRecords&lt;/code&gt; can retrieve a maximum of 1 MB of data or 1000 stream records, whichever comes first.&lt;/p&gt; &lt;/note&gt;

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
    body = GetRecordsInput.from_dict(body)
    return web.Response(status=200)


async def get_shard_iterator(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_shard_iterator

    &lt;p&gt;Returns a shard iterator. A shard iterator provides information about how to retrieve the stream records from within a shard. Use the shard iterator in a subsequent &lt;code&gt;GetRecords&lt;/code&gt; request to read the stream records from the shard.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A shard iterator expires 15 minutes after it is returned to the requester.&lt;/p&gt; &lt;/note&gt;

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
    body = GetShardIteratorInput.from_dict(body)
    return web.Response(status=200)


async def list_streams(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_streams

    &lt;p&gt;Returns an array of stream ARNs associated with the current account and endpoint. If the &lt;code&gt;TableName&lt;/code&gt; parameter is present, then &lt;code&gt;ListStreams&lt;/code&gt; will return only the streams ARNs for that table.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can call &lt;code&gt;ListStreams&lt;/code&gt; at a maximum rate of 5 times per second.&lt;/p&gt; &lt;/note&gt;

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
    body = ListStreamsInput.from_dict(body)
    return web.Response(status=200)
