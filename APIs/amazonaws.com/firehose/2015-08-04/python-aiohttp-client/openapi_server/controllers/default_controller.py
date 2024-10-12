from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_delivery_stream_input import CreateDeliveryStreamInput
from openapi_server.models.create_delivery_stream_output import CreateDeliveryStreamOutput
from openapi_server.models.delete_delivery_stream_input import DeleteDeliveryStreamInput
from openapi_server.models.describe_delivery_stream_input import DescribeDeliveryStreamInput
from openapi_server.models.describe_delivery_stream_output import DescribeDeliveryStreamOutput
from openapi_server.models.list_delivery_streams_input import ListDeliveryStreamsInput
from openapi_server.models.list_delivery_streams_output import ListDeliveryStreamsOutput
from openapi_server.models.list_tags_for_delivery_stream_input import ListTagsForDeliveryStreamInput
from openapi_server.models.list_tags_for_delivery_stream_output import ListTagsForDeliveryStreamOutput
from openapi_server.models.put_record_batch_input import PutRecordBatchInput
from openapi_server.models.put_record_batch_output import PutRecordBatchOutput
from openapi_server.models.put_record_input import PutRecordInput
from openapi_server.models.put_record_output import PutRecordOutput
from openapi_server.models.start_delivery_stream_encryption_input import StartDeliveryStreamEncryptionInput
from openapi_server.models.stop_delivery_stream_encryption_input import StopDeliveryStreamEncryptionInput
from openapi_server.models.tag_delivery_stream_input import TagDeliveryStreamInput
from openapi_server.models.untag_delivery_stream_input import UntagDeliveryStreamInput
from openapi_server.models.update_destination_input import UpdateDestinationInput
from openapi_server import util


async def create_delivery_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_delivery_stream

    &lt;p&gt;Creates a Kinesis Data Firehose delivery stream.&lt;/p&gt; &lt;p&gt;By default, you can create up to 50 delivery streams per Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;This is an asynchronous operation that immediately returns. The initial status of the delivery stream is &lt;code&gt;CREATING&lt;/code&gt;. After the delivery stream is created, its status is &lt;code&gt;ACTIVE&lt;/code&gt; and it now accepts data. If the delivery stream creation fails, the status transitions to &lt;code&gt;CREATING_FAILED&lt;/code&gt;. Attempts to send data to a delivery stream that is not in the &lt;code&gt;ACTIVE&lt;/code&gt; state cause an exception. To check the state of a delivery stream, use &lt;a&gt;DescribeDeliveryStream&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If the status of a delivery stream is &lt;code&gt;CREATING_FAILED&lt;/code&gt;, this status doesn&#39;t change, and you can&#39;t invoke &lt;code&gt;CreateDeliveryStream&lt;/code&gt; again on it. However, you can invoke the &lt;a&gt;DeleteDeliveryStream&lt;/a&gt; operation to delete it.&lt;/p&gt; &lt;p&gt;A Kinesis Data Firehose delivery stream can be configured to receive records directly from providers using &lt;a&gt;PutRecord&lt;/a&gt; or &lt;a&gt;PutRecordBatch&lt;/a&gt;, or it can be configured to use an existing Kinesis stream as its source. To specify a Kinesis data stream as input, set the &lt;code&gt;DeliveryStreamType&lt;/code&gt; parameter to &lt;code&gt;KinesisStreamAsSource&lt;/code&gt;, and provide the Kinesis stream Amazon Resource Name (ARN) and role ARN in the &lt;code&gt;KinesisStreamSourceConfiguration&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;To create a delivery stream with server-side encryption (SSE) enabled, include &lt;a&gt;DeliveryStreamEncryptionConfigurationInput&lt;/a&gt; in your request. This is optional. You can also invoke &lt;a&gt;StartDeliveryStreamEncryption&lt;/a&gt; to turn on SSE for an existing delivery stream that doesn&#39;t have SSE enabled.&lt;/p&gt; &lt;p&gt;A delivery stream is configured with a single destination: Amazon S3, Amazon ES, Amazon Redshift, or Splunk. You must specify only one of the following destination configuration parameters: &lt;code&gt;ExtendedS3DestinationConfiguration&lt;/code&gt;, &lt;code&gt;S3DestinationConfiguration&lt;/code&gt;, &lt;code&gt;ElasticsearchDestinationConfiguration&lt;/code&gt;, &lt;code&gt;RedshiftDestinationConfiguration&lt;/code&gt;, or &lt;code&gt;SplunkDestinationConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When you specify &lt;code&gt;S3DestinationConfiguration&lt;/code&gt;, you can also provide the following optional values: BufferingHints, &lt;code&gt;EncryptionConfiguration&lt;/code&gt;, and &lt;code&gt;CompressionFormat&lt;/code&gt;. By default, if no &lt;code&gt;BufferingHints&lt;/code&gt; value is provided, Kinesis Data Firehose buffers data up to 5 MB or for 5 minutes, whichever condition is satisfied first. &lt;code&gt;BufferingHints&lt;/code&gt; is a hint, so there are some cases where the service cannot adhere to these conditions strictly. For example, record boundaries might be such that the size is a little over or under the configured buffering size. By default, no encryption is performed. We strongly recommend that you enable encryption to ensure secure data storage in Amazon S3.&lt;/p&gt; &lt;p&gt;A few notes about Amazon Redshift as a destination:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An Amazon Redshift destination requires an S3 bucket as intermediate location. Kinesis Data Firehose first delivers data to Amazon S3 and then uses &lt;code&gt;COPY&lt;/code&gt; syntax to load data into an Amazon Redshift table. This is specified in the &lt;code&gt;RedshiftDestinationConfiguration.S3Configuration&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The compression formats &lt;code&gt;SNAPPY&lt;/code&gt; or &lt;code&gt;ZIP&lt;/code&gt; cannot be specified in &lt;code&gt;RedshiftDestinationConfiguration.S3Configuration&lt;/code&gt; because the Amazon Redshift &lt;code&gt;COPY&lt;/code&gt; operation that reads from the S3 bucket doesn&#39;t support these compression formats.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;We strongly recommend that you use the user name and password you provide exclusively with Kinesis Data Firehose, and that the permissions for the account are restricted for Amazon Redshift &lt;code&gt;INSERT&lt;/code&gt; permissions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Kinesis Data Firehose assumes the IAM role that is configured as part of the destination. The role should allow the Kinesis Data Firehose principal to assume the role, and the role should have permissions that allow the service to deliver the data. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3\&quot;&gt;Grant Kinesis Data Firehose Access to an Amazon S3 Destination&lt;/a&gt; in the &lt;i&gt;Amazon Kinesis Data Firehose Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateDeliveryStreamInput.from_dict(body)
    return web.Response(status=200)


async def delete_delivery_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_delivery_stream

    &lt;p&gt;Deletes a delivery stream and its data.&lt;/p&gt; &lt;p&gt;To check the state of a delivery stream, use &lt;a&gt;DescribeDeliveryStream&lt;/a&gt;. You can delete a delivery stream only if it is in one of the following states: &lt;code&gt;ACTIVE&lt;/code&gt;, &lt;code&gt;DELETING&lt;/code&gt;, &lt;code&gt;CREATING_FAILED&lt;/code&gt;, or &lt;code&gt;DELETING_FAILED&lt;/code&gt;. You can&#39;t delete a delivery stream that is in the &lt;code&gt;CREATING&lt;/code&gt; state. While the deletion request is in process, the delivery stream is in the &lt;code&gt;DELETING&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;While the delivery stream is in the &lt;code&gt;DELETING&lt;/code&gt; state, the service might continue to accept records, but it doesn&#39;t make any guarantees with respect to delivering the data. Therefore, as a best practice, first stop any applications that are sending records before you delete a delivery stream.&lt;/p&gt;

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
    body = DeleteDeliveryStreamInput.from_dict(body)
    return web.Response(status=200)


async def describe_delivery_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_delivery_stream

    &lt;p&gt;Describes the specified delivery stream and its status. For example, after your delivery stream is created, call &lt;code&gt;DescribeDeliveryStream&lt;/code&gt; to see whether the delivery stream is &lt;code&gt;ACTIVE&lt;/code&gt; and therefore ready for data to be sent to it. &lt;/p&gt; &lt;p&gt;If the status of a delivery stream is &lt;code&gt;CREATING_FAILED&lt;/code&gt;, this status doesn&#39;t change, and you can&#39;t invoke &lt;a&gt;CreateDeliveryStream&lt;/a&gt; again on it. However, you can invoke the &lt;a&gt;DeleteDeliveryStream&lt;/a&gt; operation to delete it. If the status is &lt;code&gt;DELETING_FAILED&lt;/code&gt;, you can force deletion by invoking &lt;a&gt;DeleteDeliveryStream&lt;/a&gt; again but with &lt;a&gt;DeleteDeliveryStreamInput$AllowForceDelete&lt;/a&gt; set to true.&lt;/p&gt;

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
    body = DescribeDeliveryStreamInput.from_dict(body)
    return web.Response(status=200)


async def list_delivery_streams(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_delivery_streams

    &lt;p&gt;Lists your delivery streams in alphabetical order of their names.&lt;/p&gt; &lt;p&gt;The number of delivery streams might be too large to return using a single call to &lt;code&gt;ListDeliveryStreams&lt;/code&gt;. You can limit the number of delivery streams returned, using the &lt;code&gt;Limit&lt;/code&gt; parameter. To determine whether there are more delivery streams to list, check the value of &lt;code&gt;HasMoreDeliveryStreams&lt;/code&gt; in the output. If there are more delivery streams to list, you can request them by calling this operation again and setting the &lt;code&gt;ExclusiveStartDeliveryStreamName&lt;/code&gt; parameter to the name of the last delivery stream returned in the last call.&lt;/p&gt;

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
    body = ListDeliveryStreamsInput.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_delivery_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_delivery_stream

    Lists the tags for the specified delivery stream. This operation has a limit of five transactions per second per account. 

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
    body = ListTagsForDeliveryStreamInput.from_dict(body)
    return web.Response(status=200)


async def put_record(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_record

    &lt;p&gt;Writes a single data record into an Amazon Kinesis Data Firehose delivery stream. To write multiple data records into a delivery stream, use &lt;a&gt;PutRecordBatch&lt;/a&gt;. Applications using these operations are referred to as producers.&lt;/p&gt; &lt;p&gt;By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use &lt;a&gt;PutRecord&lt;/a&gt; and &lt;a&gt;PutRecordBatch&lt;/a&gt;, the limits are an aggregate across these two operations for each delivery stream. For more information about limits and how to request an increase, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/firehose/latest/dev/limits.html\&quot;&gt;Amazon Kinesis Data Firehose Limits&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You must specify the name of the delivery stream and the data record when using &lt;a&gt;PutRecord&lt;/a&gt;. The data record consists of a data blob that can be up to 1,000 KiB in size, and any kind of data. For example, it can be a segment from a log file, geographic location data, website clickstream data, and so on.&lt;/p&gt; &lt;p&gt;Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (&lt;code&gt;\\n&lt;/code&gt;) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;PutRecord&lt;/code&gt; operation returns a &lt;code&gt;RecordId&lt;/code&gt;, which is a unique string assigned to each record. Producer applications can use this ID for purposes such as auditability and investigation.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;PutRecord&lt;/code&gt; operation throws a &lt;code&gt;ServiceUnavailableException&lt;/code&gt;, back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream. &lt;/p&gt; &lt;p&gt;Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it tries to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Don&#39;t concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.&lt;/p&gt; &lt;/important&gt;

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
    body = PutRecordInput.from_dict(body)
    return web.Response(status=200)


async def put_record_batch(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_record_batch

    &lt;p&gt;Writes multiple data records into a delivery stream in a single call, which can achieve higher throughput per producer than when writing single records. To write single data records into a delivery stream, use &lt;a&gt;PutRecord&lt;/a&gt;. Applications using these operations are referred to as producers.&lt;/p&gt; &lt;p&gt;For information about service quota, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/firehose/latest/dev/limits.html\&quot;&gt;Amazon Kinesis Data Firehose Quota&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each &lt;a&gt;PutRecordBatch&lt;/a&gt; request supports up to 500 records. Each record in the request can be as large as 1,000 KB (before base64 encoding), up to a limit of 4 MB for the entire request. These limits cannot be changed.&lt;/p&gt; &lt;p&gt;You must specify the name of the delivery stream and the data record when using &lt;a&gt;PutRecord&lt;/a&gt;. The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it could be a segment from a log file, geographic location data, website clickstream data, and so on.&lt;/p&gt; &lt;p&gt;Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (&lt;code&gt;\\n&lt;/code&gt;) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination.&lt;/p&gt; &lt;p&gt;The &lt;a&gt;PutRecordBatch&lt;/a&gt; response includes a count of failed records, &lt;code&gt;FailedPutCount&lt;/code&gt;, and an array of responses, &lt;code&gt;RequestResponses&lt;/code&gt;. Even if the &lt;a&gt;PutRecordBatch&lt;/a&gt; call succeeds, the value of &lt;code&gt;FailedPutCount&lt;/code&gt; may be greater than 0, indicating that there are records for which the operation didn&#39;t succeed. Each entry in the &lt;code&gt;RequestResponses&lt;/code&gt; array provides additional information about the processed record. It directly correlates with a record in the request array using the same ordering, from the top to the bottom. The response array always includes the same number of records as the request array. &lt;code&gt;RequestResponses&lt;/code&gt; includes both successfully and unsuccessfully processed records. Kinesis Data Firehose tries to process all records in each &lt;a&gt;PutRecordBatch&lt;/a&gt; request. A single record failure does not stop the processing of subsequent records. &lt;/p&gt; &lt;p&gt;A successfully processed record includes a &lt;code&gt;RecordId&lt;/code&gt; value, which is unique for the record. An unsuccessfully processed record includes &lt;code&gt;ErrorCode&lt;/code&gt; and &lt;code&gt;ErrorMessage&lt;/code&gt; values. &lt;code&gt;ErrorCode&lt;/code&gt; reflects the type of error, and is one of the following values: &lt;code&gt;ServiceUnavailableException&lt;/code&gt; or &lt;code&gt;InternalFailure&lt;/code&gt;. &lt;code&gt;ErrorMessage&lt;/code&gt; provides more detailed information about the error.&lt;/p&gt; &lt;p&gt;If there is an internal server error or a timeout, the write might have completed or it might have failed. If &lt;code&gt;FailedPutCount&lt;/code&gt; is greater than 0, retry the request, resending only those records that might have failed processing. This minimizes the possible duplicate records and also reduces the total bytes sent (and corresponding charges). We recommend that you handle any duplicates at the destination.&lt;/p&gt; &lt;p&gt;If &lt;a&gt;PutRecordBatch&lt;/a&gt; throws &lt;code&gt;ServiceUnavailableException&lt;/code&gt;, back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream.&lt;/p&gt; &lt;p&gt;Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Don&#39;t concatenate two or more base64 strings to form the data fields of your records. Instead, concatenate the raw data, then perform base64 encoding.&lt;/p&gt; &lt;/important&gt;

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
    body = PutRecordBatchInput.from_dict(body)
    return web.Response(status=200)


async def start_delivery_stream_encryption(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_delivery_stream_encryption

    &lt;p&gt;Enables server-side encryption (SSE) for the delivery stream. &lt;/p&gt; &lt;p&gt;This operation is asynchronous. It returns immediately. When you invoke it, Kinesis Data Firehose first sets the encryption status of the stream to &lt;code&gt;ENABLING&lt;/code&gt;, and then to &lt;code&gt;ENABLED&lt;/code&gt;. The encryption status of a delivery stream is the &lt;code&gt;Status&lt;/code&gt; property in &lt;a&gt;DeliveryStreamEncryptionConfiguration&lt;/a&gt;. If the operation fails, the encryption status changes to &lt;code&gt;ENABLING_FAILED&lt;/code&gt;. You can continue to read and write data to your delivery stream while the encryption status is &lt;code&gt;ENABLING&lt;/code&gt;, but the data is not encrypted. It can take up to 5 seconds after the encryption status changes to &lt;code&gt;ENABLED&lt;/code&gt; before all records written to the delivery stream are encrypted. To find out whether a record or a batch of records was encrypted, check the response elements &lt;a&gt;PutRecordOutput$Encrypted&lt;/a&gt; and &lt;a&gt;PutRecordBatchOutput$Encrypted&lt;/a&gt;, respectively.&lt;/p&gt; &lt;p&gt;To check the encryption status of a delivery stream, use &lt;a&gt;DescribeDeliveryStream&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Even if encryption is currently enabled for a delivery stream, you can still invoke this operation on it to change the ARN of the CMK or both its type and ARN. If you invoke this method to change the CMK, and the old CMK is of type &lt;code&gt;CUSTOMER_MANAGED_CMK&lt;/code&gt;, Kinesis Data Firehose schedules the grant it had on the old CMK for retirement. If the new CMK is of type &lt;code&gt;CUSTOMER_MANAGED_CMK&lt;/code&gt;, Kinesis Data Firehose creates a grant that enables it to use the new CMK to encrypt and decrypt data and to manage the grant.&lt;/p&gt; &lt;p&gt;If a delivery stream already has encryption enabled and then you invoke this operation to change the ARN of the CMK or both its type and ARN and you get &lt;code&gt;ENABLING_FAILED&lt;/code&gt;, this only means that the attempt to change the CMK failed. In this case, encryption remains enabled with the old CMK.&lt;/p&gt; &lt;p&gt;If the encryption status of your delivery stream is &lt;code&gt;ENABLING_FAILED&lt;/code&gt;, you can invoke this operation again with a valid CMK. The CMK must be enabled and the key policy mustn&#39;t explicitly deny the permission for Kinesis Data Firehose to invoke KMS encrypt and decrypt operations.&lt;/p&gt; &lt;p&gt;You can enable SSE for a delivery stream only if it&#39;s a delivery stream that uses &lt;code&gt;DirectPut&lt;/code&gt; as its source. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;StartDeliveryStreamEncryption&lt;/code&gt; and &lt;code&gt;StopDeliveryStreamEncryption&lt;/code&gt; operations have a combined limit of 25 calls per delivery stream per 24 hours. For example, you reach the limit if you call &lt;code&gt;StartDeliveryStreamEncryption&lt;/code&gt; 13 times and &lt;code&gt;StopDeliveryStreamEncryption&lt;/code&gt; 12 times for the same delivery stream in a 24-hour period.&lt;/p&gt;

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
    body = StartDeliveryStreamEncryptionInput.from_dict(body)
    return web.Response(status=200)


async def stop_delivery_stream_encryption(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_delivery_stream_encryption

    &lt;p&gt;Disables server-side encryption (SSE) for the delivery stream. &lt;/p&gt; &lt;p&gt;This operation is asynchronous. It returns immediately. When you invoke it, Kinesis Data Firehose first sets the encryption status of the stream to &lt;code&gt;DISABLING&lt;/code&gt;, and then to &lt;code&gt;DISABLED&lt;/code&gt;. You can continue to read and write data to your stream while its status is &lt;code&gt;DISABLING&lt;/code&gt;. It can take up to 5 seconds after the encryption status changes to &lt;code&gt;DISABLED&lt;/code&gt; before all records written to the delivery stream are no longer subject to encryption. To find out whether a record or a batch of records was encrypted, check the response elements &lt;a&gt;PutRecordOutput$Encrypted&lt;/a&gt; and &lt;a&gt;PutRecordBatchOutput$Encrypted&lt;/a&gt;, respectively.&lt;/p&gt; &lt;p&gt;To check the encryption state of a delivery stream, use &lt;a&gt;DescribeDeliveryStream&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;If SSE is enabled using a customer managed CMK and then you invoke &lt;code&gt;StopDeliveryStreamEncryption&lt;/code&gt;, Kinesis Data Firehose schedules the related KMS grant for retirement and then retires it after it ensures that it is finished delivering records to the destination.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;StartDeliveryStreamEncryption&lt;/code&gt; and &lt;code&gt;StopDeliveryStreamEncryption&lt;/code&gt; operations have a combined limit of 25 calls per delivery stream per 24 hours. For example, you reach the limit if you call &lt;code&gt;StartDeliveryStreamEncryption&lt;/code&gt; 13 times and &lt;code&gt;StopDeliveryStreamEncryption&lt;/code&gt; 12 times for the same delivery stream in a 24-hour period.&lt;/p&gt;

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
    body = StopDeliveryStreamEncryptionInput.from_dict(body)
    return web.Response(status=200)


async def tag_delivery_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_delivery_stream

    &lt;p&gt;Adds or updates tags for the specified delivery stream. A tag is a key-value pair that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Billing and Cost Management User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;Each delivery stream can have up to 50 tags. &lt;/p&gt; &lt;p&gt;This operation has a limit of five transactions per second per account. &lt;/p&gt;

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
    body = TagDeliveryStreamInput.from_dict(body)
    return web.Response(status=200)


async def untag_delivery_stream(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_delivery_stream

    &lt;p&gt;Removes tags from the specified delivery stream. Removed tags are deleted, and you can&#39;t recover them after this operation successfully completes.&lt;/p&gt; &lt;p&gt;If you specify a tag that doesn&#39;t exist, the operation ignores it.&lt;/p&gt; &lt;p&gt;This operation has a limit of five transactions per second per account. &lt;/p&gt;

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
    body = UntagDeliveryStreamInput.from_dict(body)
    return web.Response(status=200)


async def update_destination(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_destination

    &lt;p&gt;Updates the specified destination of the specified delivery stream.&lt;/p&gt; &lt;p&gt;Use this operation to change the destination type (for example, to replace the Amazon S3 destination with Amazon Redshift) or change the parameters associated with a destination (for example, to change the bucket name of the Amazon S3 destination). The update might not occur immediately. The target delivery stream remains active while the configurations are updated, so data writes to the delivery stream can continue during this process. The updated configurations are usually effective within a few minutes.&lt;/p&gt; &lt;p&gt;Switching between Amazon ES and other services is not supported. For an Amazon ES destination, you can only update to another Amazon ES destination.&lt;/p&gt; &lt;p&gt;If the destination type is the same, Kinesis Data Firehose merges the configuration parameters specified with the destination configuration that already exists on the delivery stream. If any of the parameters are not specified in the call, the existing values are retained. For example, in the Amazon S3 destination, if &lt;a&gt;EncryptionConfiguration&lt;/a&gt; is not specified, then the existing &lt;code&gt;EncryptionConfiguration&lt;/code&gt; is maintained on the destination.&lt;/p&gt; &lt;p&gt;If the destination type is not the same, for example, changing the destination from Amazon S3 to Amazon Redshift, Kinesis Data Firehose does not merge any parameters. In this case, all parameters must be specified.&lt;/p&gt; &lt;p&gt;Kinesis Data Firehose uses &lt;code&gt;CurrentDeliveryStreamVersionId&lt;/code&gt; to avoid race conditions and conflicting merges. This is a required field, and the service updates the configuration only if the existing configuration has a version ID that matches. After the update is applied successfully, the version ID is updated, and can be retrieved using &lt;a&gt;DescribeDeliveryStream&lt;/a&gt;. Use the new version ID to set &lt;code&gt;CurrentDeliveryStreamVersionId&lt;/code&gt; in the next call.&lt;/p&gt;

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
    body = UpdateDestinationInput.from_dict(body)
    return web.Response(status=200)
