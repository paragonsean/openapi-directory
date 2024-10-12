# AmazonDynamoDbStreams.DefaultApi

All URIs are relative to *http://streams.dynamodb.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describeStream**](DefaultApi.md#describeStream) | **POST** /#X-Amz-Target&#x3D;DynamoDBStreams_20120810.DescribeStream | 
[**getRecords**](DefaultApi.md#getRecords) | **POST** /#X-Amz-Target&#x3D;DynamoDBStreams_20120810.GetRecords | 
[**getShardIterator**](DefaultApi.md#getShardIterator) | **POST** /#X-Amz-Target&#x3D;DynamoDBStreams_20120810.GetShardIterator | 
[**listStreams**](DefaultApi.md#listStreams) | **POST** /#X-Amz-Target&#x3D;DynamoDBStreams_20120810.ListStreams | 



## describeStream

> DescribeStreamOutput describeStream(xAmzTarget, describeStreamInput, opts)



&lt;p&gt;Returns information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can call &lt;code&gt;DescribeStream&lt;/code&gt; at a maximum rate of 10 times per second.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Each shard in the stream has a &lt;code&gt;SequenceNumberRange&lt;/code&gt; associated with it. If the &lt;code&gt;SequenceNumberRange&lt;/code&gt; has a &lt;code&gt;StartingSequenceNumber&lt;/code&gt; but no &lt;code&gt;EndingSequenceNumber&lt;/code&gt;, then the shard is still open (able to receive more stream records). If both &lt;code&gt;StartingSequenceNumber&lt;/code&gt; and &lt;code&gt;EndingSequenceNumber&lt;/code&gt; are present, then that shard is closed and can no longer receive more data.&lt;/p&gt;

### Example

```javascript
import AmazonDynamoDbStreams from 'amazon_dynamo_db_streams';
let defaultClient = AmazonDynamoDbStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDbStreams.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeStreamInput = new AmazonDynamoDbStreams.DescribeStreamInput(); // DescribeStreamInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeStream(xAmzTarget, describeStreamInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **describeStreamInput** | [**DescribeStreamInput**](DescribeStreamInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeStreamOutput**](DescribeStreamOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRecords

> GetRecordsOutput getRecords(xAmzTarget, getRecordsInput, opts)



&lt;p&gt;Retrieves the stream records from a given shard.&lt;/p&gt; &lt;p&gt;Specify a shard iterator using the &lt;code&gt;ShardIterator&lt;/code&gt; parameter. The shard iterator specifies the position in the shard from which you want to start reading stream records sequentially. If there are no stream records available in the portion of the shard that the iterator points to, &lt;code&gt;GetRecords&lt;/code&gt; returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains stream records.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;GetRecords&lt;/code&gt; can retrieve a maximum of 1 MB of data or 1000 stream records, whichever comes first.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonDynamoDbStreams from 'amazon_dynamo_db_streams';
let defaultClient = AmazonDynamoDbStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDbStreams.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getRecordsInput = new AmazonDynamoDbStreams.GetRecordsInput(); // GetRecordsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRecords(xAmzTarget, getRecordsInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **getRecordsInput** | [**GetRecordsInput**](GetRecordsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRecordsOutput**](GetRecordsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getShardIterator

> GetShardIteratorOutput getShardIterator(xAmzTarget, getShardIteratorInput, opts)



&lt;p&gt;Returns a shard iterator. A shard iterator provides information about how to retrieve the stream records from within a shard. Use the shard iterator in a subsequent &lt;code&gt;GetRecords&lt;/code&gt; request to read the stream records from the shard.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A shard iterator expires 15 minutes after it is returned to the requester.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonDynamoDbStreams from 'amazon_dynamo_db_streams';
let defaultClient = AmazonDynamoDbStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDbStreams.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getShardIteratorInput = new AmazonDynamoDbStreams.GetShardIteratorInput(); // GetShardIteratorInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getShardIterator(xAmzTarget, getShardIteratorInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **getShardIteratorInput** | [**GetShardIteratorInput**](GetShardIteratorInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetShardIteratorOutput**](GetShardIteratorOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listStreams

> ListStreamsOutput listStreams(xAmzTarget, listStreamsInput, opts)



&lt;p&gt;Returns an array of stream ARNs associated with the current account and endpoint. If the &lt;code&gt;TableName&lt;/code&gt; parameter is present, then &lt;code&gt;ListStreams&lt;/code&gt; will return only the streams ARNs for that table.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can call &lt;code&gt;ListStreams&lt;/code&gt; at a maximum rate of 5 times per second.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonDynamoDbStreams from 'amazon_dynamo_db_streams';
let defaultClient = AmazonDynamoDbStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonDynamoDbStreams.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listStreamsInput = new AmazonDynamoDbStreams.ListStreamsInput(); // ListStreamsInput | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listStreams(xAmzTarget, listStreamsInput, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzTarget** | **String**|  | 
 **listStreamsInput** | [**ListStreamsInput**](ListStreamsInput.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListStreamsOutput**](ListStreamsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

