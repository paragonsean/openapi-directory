# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_create_delivery_stream(client):
    """Test case for create_delivery_stream

    
    """
    body = {"DeliveryStreamEncryptionConfigurationInput":{"KeyType":"","KeyARN":""},"HttpEndpointDestinationConfiguration":{"RequestConfiguration":{"CommonAttributes":"","ContentEncoding":""},"S3Configuration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"RetryOptions":{"DurationInSeconds":""},"EndpointConfiguration":{"AccessKey":"","Url":"","Name":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""},"RoleARN":"","S3BackupMode":""},"KinesisStreamSourceConfiguration":{"KinesisStreamARN":"","RoleARN":""},"DeliveryStreamType":"","RedshiftDestinationConfiguration":{"S3BackupConfiguration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"S3Configuration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"Username":"","CopyCommand":{"DataTableName":"","DataTableColumns":"","CopyOptions":""},"RetryOptions":{"DurationInSeconds":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"RoleARN":"","ClusterJDBCURL":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""},"Password":"","S3BackupMode":""},"AmazonopensearchserviceDestinationConfiguration":{"TypeName":"","IndexRotationPeriod":"","ProcessingConfiguration":{"Enabled":"","Processors":""},"ClusterEndpoint":"","RoleARN":"","DomainARN":"","S3BackupMode":"","IndexName":"","S3Configuration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"RetryOptions":{"DurationInSeconds":""},"VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":"","RoleARN":""},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"SplunkDestinationConfiguration":{"HECEndpoint":"","S3Configuration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"HECToken":"","RetryOptions":{"DurationInSeconds":""},"HECEndpointType":"","HECAcknowledgmentTimeoutInSeconds":"","ProcessingConfiguration":{"Enabled":"","Processors":""},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""},"S3BackupMode":""},"ExtendedS3DestinationConfiguration":{"ErrorOutputPrefix":"","S3BackupConfiguration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"BucketARN":"","CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"DataFormatConversionConfiguration":{"InputFormatConfiguration":{"Deserializer":{"HiveJsonSerDe":{"TimestampFormats":""},"OpenXJsonSerDe":{"ConvertDotsInJsonKeysToUnderscores":"","ColumnToJsonKeyMappings":"","CaseInsensitive":""}}},"Enabled":"","SchemaConfiguration":{"VersionId":"","TableName":"","DatabaseName":"","Region":"","CatalogId":"","RoleARN":""},"OutputFormatConfiguration":{"Serializer":{"OrcSerDe":{"PaddingTolerance":"","Compression":"","StripeSizeBytes":"","BloomFilterColumns":"","EnablePadding":"","BloomFilterFalsePositiveProbability":"","RowIndexStride":"","FormatVersion":"","BlockSizeBytes":"","DictionaryKeyThreshold":""},"ParquetSerDe":{"Compression":"","BlockSizeBytes":"","PageSizeBytes":"","EnableDictionaryCompression":"","MaxPaddingBytes":"","WriterVersion":""}}}},"Prefix":"","DynamicPartitioningConfiguration":{"RetryOptions":{"DurationInSeconds":""},"Enabled":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"RoleARN":"","S3BackupMode":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"AmazonOpenSearchServerlessDestinationConfiguration":{"IndexName":"","S3Configuration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"RetryOptions":{"DurationInSeconds":""},"CollectionEndpoint":"","VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":"","RoleARN":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""},"S3BackupMode":""},"ElasticsearchDestinationConfiguration":{"TypeName":"","IndexRotationPeriod":"","ProcessingConfiguration":{"Enabled":"","Processors":""},"ClusterEndpoint":"","RoleARN":"","DomainARN":"","S3BackupMode":"","IndexName":"","S3Configuration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"RetryOptions":{"DurationInSeconds":""},"VpcConfiguration":{"SubnetIds":"","SecurityGroupIds":"","RoleARN":""},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"S3DestinationConfiguration":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"DeliveryStreamName":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.CreateDeliveryStream',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_delivery_stream(client):
    """Test case for delete_delivery_stream

    
    """
    body = {"AllowForceDelete":"","DeliveryStreamName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.DeleteDeliveryStream',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_delivery_stream(client):
    """Test case for describe_delivery_stream

    
    """
    body = {"ExclusiveStartDestinationId":"","DeliveryStreamName":"","Limit":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.DescribeDeliveryStream',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_delivery_streams(client):
    """Test case for list_delivery_streams

    
    """
    body = {"DeliveryStreamType":"","Limit":"","ExclusiveStartDeliveryStreamName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.ListDeliveryStreams',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_delivery_stream(client):
    """Test case for list_tags_for_delivery_stream

    
    """
    body = {"ExclusiveStartTagKey":"","DeliveryStreamName":"","Limit":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.ListTagsForDeliveryStream',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_record(client):
    """Test case for put_record

    
    """
    body = {"DeliveryStreamName":"","Record":{"Data":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.PutRecord',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_record_batch(client):
    """Test case for put_record_batch

    
    """
    body = {"DeliveryStreamName":"","Records":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.PutRecordBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_delivery_stream_encryption(client):
    """Test case for start_delivery_stream_encryption

    
    """
    body = {"DeliveryStreamEncryptionConfigurationInput":{"KeyType":"","KeyARN":""},"DeliveryStreamName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.StartDeliveryStreamEncryption',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_delivery_stream_encryption(client):
    """Test case for stop_delivery_stream_encryption

    
    """
    body = {"DeliveryStreamName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.StopDeliveryStreamEncryption',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_delivery_stream(client):
    """Test case for tag_delivery_stream

    
    """
    body = {"DeliveryStreamName":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.TagDeliveryStream',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_delivery_stream(client):
    """Test case for untag_delivery_stream

    
    """
    body = {"DeliveryStreamName":"","TagKeys":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.UntagDeliveryStream',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_destination(client):
    """Test case for update_destination

    
    """
    body = {"HttpEndpointDestinationUpdate":{"RequestConfiguration":{"CommonAttributes":"","ContentEncoding":""},"BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"RetryOptions":{"DurationInSeconds":""},"EndpointConfiguration":{"AccessKey":"","Url":"","Name":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"S3Update":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""},"RoleARN":"","S3BackupMode":""},"S3DestinationUpdate":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"ElasticsearchDestinationUpdate":{"IndexName":"","TypeName":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"IndexRotationPeriod":"","RetryOptions":{"DurationInSeconds":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"ClusterEndpoint":"","S3Update":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"RoleARN":"","DomainARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"CurrentDeliveryStreamVersionId":"","RedshiftDestinationUpdate":{"Username":"","CopyCommand":{"DataTableName":"","DataTableColumns":"","CopyOptions":""},"RetryOptions":{"DurationInSeconds":""},"S3BackupUpdate":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"ProcessingConfiguration":{"Enabled":"","Processors":""},"S3Update":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"RoleARN":"","ClusterJDBCURL":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""},"Password":"","S3BackupMode":""},"ExtendedS3DestinationUpdate":{"ErrorOutputPrefix":"","BucketARN":"","CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"DataFormatConversionConfiguration":{"InputFormatConfiguration":{"Deserializer":{"HiveJsonSerDe":{"TimestampFormats":""},"OpenXJsonSerDe":{"ConvertDotsInJsonKeysToUnderscores":"","ColumnToJsonKeyMappings":"","CaseInsensitive":""}}},"Enabled":"","SchemaConfiguration":{"VersionId":"","TableName":"","DatabaseName":"","Region":"","CatalogId":"","RoleARN":""},"OutputFormatConfiguration":{"Serializer":{"OrcSerDe":{"PaddingTolerance":"","Compression":"","StripeSizeBytes":"","BloomFilterColumns":"","EnablePadding":"","BloomFilterFalsePositiveProbability":"","RowIndexStride":"","FormatVersion":"","BlockSizeBytes":"","DictionaryKeyThreshold":""},"ParquetSerDe":{"Compression":"","BlockSizeBytes":"","PageSizeBytes":"","EnableDictionaryCompression":"","MaxPaddingBytes":"","WriterVersion":""}}}},"Prefix":"","S3BackupUpdate":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"DynamicPartitioningConfiguration":{"RetryOptions":{"DurationInSeconds":""},"Enabled":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"RoleARN":"","S3BackupMode":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"DeliveryStreamName":"","SplunkDestinationUpdate":{"HECEndpoint":"","HECToken":"","RetryOptions":{"DurationInSeconds":""},"HECEndpointType":"","HECAcknowledgmentTimeoutInSeconds":"","ProcessingConfiguration":{"Enabled":"","Processors":""},"S3Update":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""},"S3BackupMode":""},"DestinationId":"","AmazonopensearchserviceDestinationUpdate":{"IndexName":"","TypeName":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"IndexRotationPeriod":"","RetryOptions":{"DurationInSeconds":""},"ProcessingConfiguration":{"Enabled":"","Processors":""},"ClusterEndpoint":"","S3Update":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"RoleARN":"","DomainARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"AmazonOpenSearchServerlessDestinationUpdate":{"IndexName":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"RetryOptions":{"DurationInSeconds":""},"CollectionEndpoint":"","ProcessingConfiguration":{"Enabled":"","Processors":""},"S3Update":{"ErrorOutputPrefix":"","BucketARN":"","BufferingHints":{"IntervalInSeconds":"","SizeInMBs":""},"CompressionFormat":"","EncryptionConfiguration":{"KMSEncryptionConfig":{"AWSKMSKeyARN":""},"NoEncryptionConfig":""},"Prefix":"","RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}},"RoleARN":"","CloudWatchLoggingOptions":{"LogStreamName":"","Enabled":"","LogGroupName":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=Firehose_20150804.UpdateDestination',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

