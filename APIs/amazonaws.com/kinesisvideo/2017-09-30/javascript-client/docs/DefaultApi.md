# AmazonKinesisVideoStreams.DefaultApi

All URIs are relative to *http://kinesisvideo.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSignalingChannel**](DefaultApi.md#createSignalingChannel) | **POST** /createSignalingChannel | 
[**createStream**](DefaultApi.md#createStream) | **POST** /createStream | 
[**deleteEdgeConfiguration**](DefaultApi.md#deleteEdgeConfiguration) | **POST** /deleteEdgeConfiguration | 
[**deleteSignalingChannel**](DefaultApi.md#deleteSignalingChannel) | **POST** /deleteSignalingChannel | 
[**deleteStream**](DefaultApi.md#deleteStream) | **POST** /deleteStream | 
[**describeEdgeConfiguration**](DefaultApi.md#describeEdgeConfiguration) | **POST** /describeEdgeConfiguration | 
[**describeImageGenerationConfiguration**](DefaultApi.md#describeImageGenerationConfiguration) | **POST** /describeImageGenerationConfiguration | 
[**describeMappedResourceConfiguration**](DefaultApi.md#describeMappedResourceConfiguration) | **POST** /describeMappedResourceConfiguration | 
[**describeMediaStorageConfiguration**](DefaultApi.md#describeMediaStorageConfiguration) | **POST** /describeMediaStorageConfiguration | 
[**describeNotificationConfiguration**](DefaultApi.md#describeNotificationConfiguration) | **POST** /describeNotificationConfiguration | 
[**describeSignalingChannel**](DefaultApi.md#describeSignalingChannel) | **POST** /describeSignalingChannel | 
[**describeStream**](DefaultApi.md#describeStream) | **POST** /describeStream | 
[**getDataEndpoint**](DefaultApi.md#getDataEndpoint) | **POST** /getDataEndpoint | 
[**getSignalingChannelEndpoint**](DefaultApi.md#getSignalingChannelEndpoint) | **POST** /getSignalingChannelEndpoint | 
[**listEdgeAgentConfigurations**](DefaultApi.md#listEdgeAgentConfigurations) | **POST** /listEdgeAgentConfigurations | 
[**listSignalingChannels**](DefaultApi.md#listSignalingChannels) | **POST** /listSignalingChannels | 
[**listStreams**](DefaultApi.md#listStreams) | **POST** /listStreams | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /ListTagsForResource | 
[**listTagsForStream**](DefaultApi.md#listTagsForStream) | **POST** /listTagsForStream | 
[**startEdgeConfigurationUpdate**](DefaultApi.md#startEdgeConfigurationUpdate) | **POST** /startEdgeConfigurationUpdate | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /TagResource | 
[**tagStream**](DefaultApi.md#tagStream) | **POST** /tagStream | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /UntagResource | 
[**untagStream**](DefaultApi.md#untagStream) | **POST** /untagStream | 
[**updateDataRetention**](DefaultApi.md#updateDataRetention) | **POST** /updateDataRetention | 
[**updateImageGenerationConfiguration**](DefaultApi.md#updateImageGenerationConfiguration) | **POST** /updateImageGenerationConfiguration | 
[**updateMediaStorageConfiguration**](DefaultApi.md#updateMediaStorageConfiguration) | **POST** /updateMediaStorageConfiguration | 
[**updateNotificationConfiguration**](DefaultApi.md#updateNotificationConfiguration) | **POST** /updateNotificationConfiguration | 
[**updateSignalingChannel**](DefaultApi.md#updateSignalingChannel) | **POST** /updateSignalingChannel | 
[**updateStream**](DefaultApi.md#updateStream) | **POST** /updateStream | 



## createSignalingChannel

> CreateSignalingChannelOutput createSignalingChannel(createSignalingChannelRequest, opts)



&lt;p&gt;Creates a signaling channel. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateSignalingChannel&lt;/code&gt; is an asynchronous operation.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let createSignalingChannelRequest = new AmazonKinesisVideoStreams.CreateSignalingChannelRequest(); // CreateSignalingChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSignalingChannel(createSignalingChannelRequest, opts, (error, data, response) => {
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
 **createSignalingChannelRequest** | [**CreateSignalingChannelRequest**](CreateSignalingChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSignalingChannelOutput**](CreateSignalingChannelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStream

> CreateStreamOutput createStream(createStreamRequest, opts)



&lt;p&gt;Creates a new Kinesis video stream. &lt;/p&gt; &lt;p&gt;When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream&#39;s metadata, Kinesis Video Streams updates the version. &lt;/p&gt; &lt;p&gt; &lt;code&gt;CreateStream&lt;/code&gt; is an asynchronous operation.&lt;/p&gt; &lt;p&gt;For information about how the service works, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html\&quot;&gt;How it Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You must have permissions for the &lt;code&gt;KinesisVideo:CreateStream&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let createStreamRequest = new AmazonKinesisVideoStreams.CreateStreamRequest(); // CreateStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createStream(createStreamRequest, opts, (error, data, response) => {
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
 **createStreamRequest** | [**CreateStreamRequest**](CreateStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateStreamOutput**](CreateStreamOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEdgeConfiguration

> Object deleteEdgeConfiguration(deleteEdgeConfigurationRequest, opts)



&lt;p&gt;An asynchronous API that deletes a stream’s existing edge configuration, as well as the corresponding media from the Edge Agent.&lt;/p&gt; &lt;p&gt;When you invoke this API, the sync status is set to &lt;code&gt;DELETING&lt;/code&gt;. A deletion process starts, in which active edge jobs are stopped and all media is deleted from the edge device. The time to delete varies, depending on the total amount of stored media. If the deletion process fails, the sync status changes to &lt;code&gt;DELETE_FAILED&lt;/code&gt;. You will need to re-try the deletion.&lt;/p&gt; &lt;p&gt;When the deletion process has completed successfully, the edge configuration is no longer accessible.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let deleteEdgeConfigurationRequest = new AmazonKinesisVideoStreams.DeleteEdgeConfigurationRequest(); // DeleteEdgeConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEdgeConfiguration(deleteEdgeConfigurationRequest, opts, (error, data, response) => {
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
 **deleteEdgeConfigurationRequest** | [**DeleteEdgeConfigurationRequest**](DeleteEdgeConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSignalingChannel

> Object deleteSignalingChannel(deleteSignalingChannelRequest, opts)



Deletes a specified signaling channel. &lt;code&gt;DeleteSignalingChannel&lt;/code&gt; is an asynchronous operation. If you don&#39;t specify the channel&#39;s current version, the most recent version is deleted.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let deleteSignalingChannelRequest = new AmazonKinesisVideoStreams.DeleteSignalingChannelRequest(); // DeleteSignalingChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSignalingChannel(deleteSignalingChannelRequest, opts, (error, data, response) => {
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
 **deleteSignalingChannelRequest** | [**DeleteSignalingChannelRequest**](DeleteSignalingChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStream

> Object deleteStream(deleteStreamRequest, opts)



&lt;p&gt;Deletes a Kinesis video stream and the data contained in the stream. &lt;/p&gt; &lt;p&gt;This method marks the stream for deletion, and makes the data in the stream inaccessible immediately.&lt;/p&gt; &lt;p&gt; &lt;/p&gt; &lt;p&gt; To ensure that you have the latest version of the stream before deleting it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the &lt;code&gt;DescribeStream&lt;/code&gt; API. &lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;KinesisVideo:DeleteStream&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let deleteStreamRequest = new AmazonKinesisVideoStreams.DeleteStreamRequest(); // DeleteStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteStream(deleteStreamRequest, opts, (error, data, response) => {
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
 **deleteStreamRequest** | [**DeleteStreamRequest**](DeleteStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeEdgeConfiguration

> DescribeEdgeConfigurationOutput describeEdgeConfiguration(describeEdgeConfigurationRequest, opts)



Describes a stream’s edge configuration that was set using the &lt;code&gt;StartEdgeConfigurationUpdate&lt;/code&gt; API and the latest status of the edge agent&#39;s recorder and uploader jobs. Use this API to get the status of the configuration to determine if the configuration is in sync with the Edge Agent. Use this API to evaluate the health of the Edge Agent.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let describeEdgeConfigurationRequest = new AmazonKinesisVideoStreams.DescribeEdgeConfigurationRequest(); // DescribeEdgeConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEdgeConfiguration(describeEdgeConfigurationRequest, opts, (error, data, response) => {
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
 **describeEdgeConfigurationRequest** | [**DescribeEdgeConfigurationRequest**](DescribeEdgeConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeEdgeConfigurationOutput**](DescribeEdgeConfigurationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeImageGenerationConfiguration

> DescribeImageGenerationConfigurationOutput describeImageGenerationConfiguration(describeImageGenerationConfigurationRequest, opts)



Gets the &lt;code&gt;ImageGenerationConfiguration&lt;/code&gt; for a given Kinesis video stream.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let describeImageGenerationConfigurationRequest = new AmazonKinesisVideoStreams.DescribeImageGenerationConfigurationRequest(); // DescribeImageGenerationConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeImageGenerationConfiguration(describeImageGenerationConfigurationRequest, opts, (error, data, response) => {
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
 **describeImageGenerationConfigurationRequest** | [**DescribeImageGenerationConfigurationRequest**](DescribeImageGenerationConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeImageGenerationConfigurationOutput**](DescribeImageGenerationConfigurationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeMappedResourceConfiguration

> DescribeMappedResourceConfigurationOutput describeMappedResourceConfiguration(describeMappedResourceConfigurationRequest, opts)



Returns the most current information about the stream. The &lt;code&gt;streamName&lt;/code&gt; or &lt;code&gt;streamARN&lt;/code&gt; should be provided in the input.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let describeMappedResourceConfigurationRequest = new AmazonKinesisVideoStreams.DescribeMappedResourceConfigurationRequest(); // DescribeMappedResourceConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.describeMappedResourceConfiguration(describeMappedResourceConfigurationRequest, opts, (error, data, response) => {
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
 **describeMappedResourceConfigurationRequest** | [**DescribeMappedResourceConfigurationRequest**](DescribeMappedResourceConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**DescribeMappedResourceConfigurationOutput**](DescribeMappedResourceConfigurationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeMediaStorageConfiguration

> DescribeMediaStorageConfigurationOutput describeMediaStorageConfiguration(describeMediaStorageConfigurationRequest, opts)



Returns the most current information about the channel. Specify the &lt;code&gt;ChannelName&lt;/code&gt; or &lt;code&gt;ChannelARN&lt;/code&gt; in the input.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let describeMediaStorageConfigurationRequest = new AmazonKinesisVideoStreams.DescribeMediaStorageConfigurationRequest(); // DescribeMediaStorageConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeMediaStorageConfiguration(describeMediaStorageConfigurationRequest, opts, (error, data, response) => {
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
 **describeMediaStorageConfigurationRequest** | [**DescribeMediaStorageConfigurationRequest**](DescribeMediaStorageConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeMediaStorageConfigurationOutput**](DescribeMediaStorageConfigurationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeNotificationConfiguration

> DescribeNotificationConfigurationOutput describeNotificationConfiguration(describeNotificationConfigurationRequest, opts)



Gets the &lt;code&gt;NotificationConfiguration&lt;/code&gt; for a given Kinesis video stream.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let describeNotificationConfigurationRequest = new AmazonKinesisVideoStreams.DescribeNotificationConfigurationRequest(); // DescribeNotificationConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeNotificationConfiguration(describeNotificationConfigurationRequest, opts, (error, data, response) => {
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
 **describeNotificationConfigurationRequest** | [**DescribeNotificationConfigurationRequest**](DescribeNotificationConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeNotificationConfigurationOutput**](DescribeNotificationConfigurationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeSignalingChannel

> DescribeSignalingChannelOutput describeSignalingChannel(describeSignalingChannelRequest, opts)



Returns the most current information about the signaling channel. You must specify either the name or the Amazon Resource Name (ARN) of the channel that you want to describe.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let describeSignalingChannelRequest = new AmazonKinesisVideoStreams.DescribeSignalingChannelRequest(); // DescribeSignalingChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeSignalingChannel(describeSignalingChannelRequest, opts, (error, data, response) => {
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
 **describeSignalingChannelRequest** | [**DescribeSignalingChannelRequest**](DescribeSignalingChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeSignalingChannelOutput**](DescribeSignalingChannelOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeStream

> DescribeStreamOutput describeStream(describeStreamRequest, opts)



Returns the most current information about the specified stream. You must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. 

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let describeStreamRequest = new AmazonKinesisVideoStreams.DescribeStreamRequest(); // DescribeStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeStream(describeStreamRequest, opts, (error, data, response) => {
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
 **describeStreamRequest** | [**DescribeStreamRequest**](DescribeStreamRequest.md)|  | 
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


## getDataEndpoint

> GetDataEndpointOutput getDataEndpoint(getDataEndpointRequest, opts)



&lt;p&gt;Gets an endpoint for a specified stream for either reading or writing. Use this endpoint in your application to read from the specified stream (using the &lt;code&gt;GetMedia&lt;/code&gt; or &lt;code&gt;GetMediaForFragmentList&lt;/code&gt; operations) or write to it (using the &lt;code&gt;PutMedia&lt;/code&gt; operation). &lt;/p&gt; &lt;note&gt; &lt;p&gt;The returned endpoint does not have the API name appended. The client needs to add the API name to the returned endpoint.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;In the request, specify the stream either by &lt;code&gt;StreamName&lt;/code&gt; or &lt;code&gt;StreamARN&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let getDataEndpointRequest = new AmazonKinesisVideoStreams.GetDataEndpointRequest(); // GetDataEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDataEndpoint(getDataEndpointRequest, opts, (error, data, response) => {
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
 **getDataEndpointRequest** | [**GetDataEndpointRequest**](GetDataEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDataEndpointOutput**](GetDataEndpointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSignalingChannelEndpoint

> GetSignalingChannelEndpointOutput getSignalingChannelEndpoint(getSignalingChannelEndpointRequest, opts)



&lt;p&gt;Provides an endpoint for the specified signaling channel to send and receive messages. This API uses the &lt;code&gt;SingleMasterChannelEndpointConfiguration&lt;/code&gt; input parameter, which consists of the &lt;code&gt;Protocols&lt;/code&gt; and &lt;code&gt;Role&lt;/code&gt; properties.&lt;/p&gt; &lt;p&gt; &lt;code&gt;Protocols&lt;/code&gt; is used to determine the communication mechanism. For example, if you specify &lt;code&gt;WSS&lt;/code&gt; as the protocol, this API produces a secure websocket endpoint. If you specify &lt;code&gt;HTTPS&lt;/code&gt; as the protocol, this API generates an HTTPS endpoint. &lt;/p&gt; &lt;p&gt; &lt;code&gt;Role&lt;/code&gt; determines the messaging permissions. A &lt;code&gt;MASTER&lt;/code&gt; role results in this API generating an endpoint that a client can use to communicate with any of the viewers on the channel. A &lt;code&gt;VIEWER&lt;/code&gt; role results in this API generating an endpoint that a client can use to communicate only with a &lt;code&gt;MASTER&lt;/code&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let getSignalingChannelEndpointRequest = new AmazonKinesisVideoStreams.GetSignalingChannelEndpointRequest(); // GetSignalingChannelEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSignalingChannelEndpoint(getSignalingChannelEndpointRequest, opts, (error, data, response) => {
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
 **getSignalingChannelEndpointRequest** | [**GetSignalingChannelEndpointRequest**](GetSignalingChannelEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSignalingChannelEndpointOutput**](GetSignalingChannelEndpointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEdgeAgentConfigurations

> ListEdgeAgentConfigurationsOutput listEdgeAgentConfigurations(listEdgeAgentConfigurationsRequest, opts)



&lt;p&gt;Returns an array of edge configurations associated with the specified Edge Agent.&lt;/p&gt; &lt;p&gt;In the request, you must specify the Edge Agent &lt;code&gt;HubDeviceArn&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let listEdgeAgentConfigurationsRequest = new AmazonKinesisVideoStreams.ListEdgeAgentConfigurationsRequest(); // ListEdgeAgentConfigurationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listEdgeAgentConfigurations(listEdgeAgentConfigurationsRequest, opts, (error, data, response) => {
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
 **listEdgeAgentConfigurationsRequest** | [**ListEdgeAgentConfigurationsRequest**](ListEdgeAgentConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListEdgeAgentConfigurationsOutput**](ListEdgeAgentConfigurationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSignalingChannels

> ListSignalingChannelsOutput listSignalingChannels(listSignalingChannelsRequest, opts)



Returns an array of &lt;code&gt;ChannelInfo&lt;/code&gt; objects. Each object describes a signaling channel. To retrieve only those channels that satisfy a specific condition, you can specify a &lt;code&gt;ChannelNameCondition&lt;/code&gt;.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let listSignalingChannelsRequest = new AmazonKinesisVideoStreams.ListSignalingChannelsRequest(); // ListSignalingChannelsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listSignalingChannels(listSignalingChannelsRequest, opts, (error, data, response) => {
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
 **listSignalingChannelsRequest** | [**ListSignalingChannelsRequest**](ListSignalingChannelsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSignalingChannelsOutput**](ListSignalingChannelsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listStreams

> ListStreamsOutput listStreams(listStreamsRequest, opts)



Returns an array of &lt;code&gt;StreamInfo&lt;/code&gt; objects. Each object describes a stream. To retrieve only streams that satisfy a specific condition, you can specify a &lt;code&gt;StreamNameCondition&lt;/code&gt;. 

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let listStreamsRequest = new AmazonKinesisVideoStreams.ListStreamsRequest(); // ListStreamsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listStreams(listStreamsRequest, opts, (error, data, response) => {
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
 **listStreamsRequest** | [**ListStreamsRequest**](ListStreamsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListStreamsOutput**](ListStreamsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(listTagsForResourceRequest, opts)



Returns a list of tags associated with the specified signaling channel.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let listTagsForResourceRequest = new AmazonKinesisVideoStreams.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(listTagsForResourceRequest, opts, (error, data, response) => {
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
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForStream

> ListTagsForStreamOutput listTagsForStream(listTagsForStreamRequest, opts)



&lt;p&gt;Returns a list of tags associated with the specified stream.&lt;/p&gt; &lt;p&gt;In the request, you must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let listTagsForStreamRequest = new AmazonKinesisVideoStreams.ListTagsForStreamRequest(); // ListTagsForStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForStream(listTagsForStreamRequest, opts, (error, data, response) => {
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
 **listTagsForStreamRequest** | [**ListTagsForStreamRequest**](ListTagsForStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForStreamOutput**](ListTagsForStreamOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startEdgeConfigurationUpdate

> StartEdgeConfigurationUpdateOutput startEdgeConfigurationUpdate(startEdgeConfigurationUpdateRequest, opts)



&lt;p&gt;An asynchronous API that updates a stream’s existing edge configuration. The Kinesis Video Stream will sync the stream’s edge configuration with the Edge Agent IoT Greengrass component that runs on an IoT Hub Device, setup at your premise. The time to sync can vary and depends on the connectivity of the Hub Device. The &lt;code&gt;SyncStatus&lt;/code&gt; will be updated as the edge configuration is acknowledged, and synced with the Edge Agent. &lt;/p&gt; &lt;p&gt;If this API is invoked for the first time, a new edge configuration will be created for the stream, and the sync status will be set to &lt;code&gt;SYNCING&lt;/code&gt;. You will have to wait for the sync status to reach a terminal state such as: &lt;code&gt;IN_SYNC&lt;/code&gt;, or &lt;code&gt;SYNC_FAILED&lt;/code&gt;, before using this API again. If you invoke this API during the syncing process, a &lt;code&gt;ResourceInUseException&lt;/code&gt; will be thrown. The connectivity of the stream’s edge configuration and the Edge Agent will be retried for 15 minutes. After 15 minutes, the status will transition into the &lt;code&gt;SYNC_FAILED&lt;/code&gt; state.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let startEdgeConfigurationUpdateRequest = new AmazonKinesisVideoStreams.StartEdgeConfigurationUpdateRequest(); // StartEdgeConfigurationUpdateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startEdgeConfigurationUpdate(startEdgeConfigurationUpdateRequest, opts, (error, data, response) => {
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
 **startEdgeConfigurationUpdateRequest** | [**StartEdgeConfigurationUpdateRequest**](StartEdgeConfigurationUpdateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartEdgeConfigurationUpdateOutput**](StartEdgeConfigurationUpdateOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(tagResourceRequest, opts)



Adds one or more tags to a signaling channel. A &lt;i&gt;tag&lt;/i&gt; is a key-value pair (the value is optional) that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management and Cost Management User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let tagResourceRequest = new AmazonKinesisVideoStreams.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(tagResourceRequest, opts, (error, data, response) => {
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
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagStream

> Object tagStream(tagStreamRequest, opts)



&lt;p&gt;Adds one or more tags to a stream. A &lt;i&gt;tag&lt;/i&gt; is a key-value pair (the value is optional) that you can define and assign to Amazon Web Services resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management and Cost Management User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;You must provide either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;KinesisVideo:TagStream&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;A Kinesis video stream can support up to 50 tags.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let tagStreamRequest = new AmazonKinesisVideoStreams.TagStreamRequest(); // TagStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagStream(tagStreamRequest, opts, (error, data, response) => {
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
 **tagStreamRequest** | [**TagStreamRequest**](TagStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(untagResourceRequest, opts)



Removes one or more tags from a signaling channel. In the request, specify only a tag key or keys; don&#39;t specify the value. If you specify a tag key that does not exist, it&#39;s ignored.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let untagResourceRequest = new AmazonKinesisVideoStreams.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(untagResourceRequest, opts, (error, data, response) => {
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
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagStream

> Object untagStream(untagStreamRequest, opts)



&lt;p&gt;Removes one or more tags from a stream. In the request, specify only a tag key or keys; don&#39;t specify the value. If you specify a tag key that does not exist, it&#39;s ignored.&lt;/p&gt; &lt;p&gt;In the request, you must provide the &lt;code&gt;StreamName&lt;/code&gt; or &lt;code&gt;StreamARN&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let untagStreamRequest = new AmazonKinesisVideoStreams.UntagStreamRequest(); // UntagStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagStream(untagStreamRequest, opts, (error, data, response) => {
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
 **untagStreamRequest** | [**UntagStreamRequest**](UntagStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDataRetention

> Object updateDataRetention(updateDataRetentionRequest, opts)



&lt;p&gt; Increases or decreases the stream&#39;s data retention period by the value that you specify. To indicate whether you want to increase or decrease the data retention period, specify the &lt;code&gt;Operation&lt;/code&gt; parameter in the request body. In the request, you must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The retention period that you specify replaces the current value.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;KinesisVideo:UpdateDataRetention&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;Changing the data retention period affects the data in the stream as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the data retention period is increased, existing data is retained for the new retention period. For example, if the data retention period is increased from one hour to seven hours, all existing data is retained for seven hours.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the data retention period is decreased, existing data is retained for the new retention period. For example, if the data retention period is decreased from seven hours to one hour, all existing data is retained for one hour, and any data older than one hour is deleted immediately.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let updateDataRetentionRequest = new AmazonKinesisVideoStreams.UpdateDataRetentionRequest(); // UpdateDataRetentionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDataRetention(updateDataRetentionRequest, opts, (error, data, response) => {
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
 **updateDataRetentionRequest** | [**UpdateDataRetentionRequest**](UpdateDataRetentionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateImageGenerationConfiguration

> Object updateImageGenerationConfiguration(updateImageGenerationConfigurationRequest, opts)



Updates the &lt;code&gt;StreamInfo&lt;/code&gt; and &lt;code&gt;ImageProcessingConfiguration&lt;/code&gt; fields.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let updateImageGenerationConfigurationRequest = new AmazonKinesisVideoStreams.UpdateImageGenerationConfigurationRequest(); // UpdateImageGenerationConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateImageGenerationConfiguration(updateImageGenerationConfigurationRequest, opts, (error, data, response) => {
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
 **updateImageGenerationConfigurationRequest** | [**UpdateImageGenerationConfigurationRequest**](UpdateImageGenerationConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMediaStorageConfiguration

> Object updateMediaStorageConfiguration(updateMediaStorageConfigurationRequest, opts)



&lt;p&gt;Associates a &lt;code&gt;SignalingChannel&lt;/code&gt; to a stream to store the media. There are two signaling modes that can specified :&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the &lt;code&gt;StorageStatus&lt;/code&gt; is disabled, no data will be stored, and the &lt;code&gt;StreamARN&lt;/code&gt; parameter will not be needed. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the &lt;code&gt;StorageStatus&lt;/code&gt; is enabled, the data will be stored in the &lt;code&gt;StreamARN&lt;/code&gt; provided. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;If &lt;code&gt;StorageStatus&lt;/code&gt; is enabled, direct peer-to-peer (master-viewer) connections no longer occur. Peers connect directly to the storage session. You must call the &lt;code&gt;JoinStorageSession&lt;/code&gt; API to trigger an SDP offer send and establish a connection between a peer and the storage session. &lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let updateMediaStorageConfigurationRequest = new AmazonKinesisVideoStreams.UpdateMediaStorageConfigurationRequest(); // UpdateMediaStorageConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMediaStorageConfiguration(updateMediaStorageConfigurationRequest, opts, (error, data, response) => {
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
 **updateMediaStorageConfigurationRequest** | [**UpdateMediaStorageConfigurationRequest**](UpdateMediaStorageConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNotificationConfiguration

> Object updateNotificationConfiguration(updateNotificationConfigurationRequest, opts)



Updates the notification information for a stream.

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let updateNotificationConfigurationRequest = new AmazonKinesisVideoStreams.UpdateNotificationConfigurationRequest(); // UpdateNotificationConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateNotificationConfiguration(updateNotificationConfigurationRequest, opts, (error, data, response) => {
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
 **updateNotificationConfigurationRequest** | [**UpdateNotificationConfigurationRequest**](UpdateNotificationConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSignalingChannel

> Object updateSignalingChannel(updateSignalingChannelRequest, opts)



&lt;p&gt;Updates the existing signaling channel. This is an asynchronous operation and takes time to complete. &lt;/p&gt; &lt;p&gt;If the &lt;code&gt;MessageTtlSeconds&lt;/code&gt; value is updated (either increased or reduced), it only applies to new messages sent via this channel after it&#39;s been updated. Existing messages are still expired as per the previous &lt;code&gt;MessageTtlSeconds&lt;/code&gt; value.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let updateSignalingChannelRequest = new AmazonKinesisVideoStreams.UpdateSignalingChannelRequest(); // UpdateSignalingChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSignalingChannel(updateSignalingChannelRequest, opts, (error, data, response) => {
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
 **updateSignalingChannelRequest** | [**UpdateSignalingChannelRequest**](UpdateSignalingChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStream

> Object updateStream(updateStreamRequest, opts)



&lt;p&gt;Updates stream metadata, such as the device name and media type.&lt;/p&gt; &lt;p&gt;You must provide the stream name or the Amazon Resource Name (ARN) of the stream.&lt;/p&gt; &lt;p&gt;To make sure that you have the latest version of the stream before updating it, you can specify the stream version. Kinesis Video Streams assigns a version to each stream. When you update a stream, Kinesis Video Streams assigns a new version number. To get the latest stream version, use the &lt;code&gt;DescribeStream&lt;/code&gt; API. &lt;/p&gt; &lt;p&gt; &lt;code&gt;UpdateStream&lt;/code&gt; is an asynchronous operation, and takes time to complete.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoStreams from 'amazon_kinesis_video_streams';
let defaultClient = AmazonKinesisVideoStreams.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoStreams.DefaultApi();
let updateStreamRequest = new AmazonKinesisVideoStreams.UpdateStreamRequest(); // UpdateStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateStream(updateStreamRequest, opts, (error, data, response) => {
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
 **updateStreamRequest** | [**UpdateStreamRequest**](UpdateStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

