# AmazonChimeSdkMediaPipelines.DefaultApi

All URIs are relative to *http://media-pipelines-chime.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMediaCapturePipeline**](DefaultApi.md#createMediaCapturePipeline) | **POST** /sdk-media-capture-pipelines | 
[**createMediaConcatenationPipeline**](DefaultApi.md#createMediaConcatenationPipeline) | **POST** /sdk-media-concatenation-pipelines | 
[**createMediaInsightsPipeline**](DefaultApi.md#createMediaInsightsPipeline) | **POST** /media-insights-pipelines | 
[**createMediaInsightsPipelineConfiguration**](DefaultApi.md#createMediaInsightsPipelineConfiguration) | **POST** /media-insights-pipeline-configurations | 
[**createMediaLiveConnectorPipeline**](DefaultApi.md#createMediaLiveConnectorPipeline) | **POST** /sdk-media-live-connector-pipelines | 
[**deleteMediaCapturePipeline**](DefaultApi.md#deleteMediaCapturePipeline) | **DELETE** /sdk-media-capture-pipelines/{mediaPipelineId} | 
[**deleteMediaInsightsPipelineConfiguration**](DefaultApi.md#deleteMediaInsightsPipelineConfiguration) | **DELETE** /media-insights-pipeline-configurations/{identifier} | 
[**deleteMediaPipeline**](DefaultApi.md#deleteMediaPipeline) | **DELETE** /sdk-media-pipelines/{mediaPipelineId} | 
[**getMediaCapturePipeline**](DefaultApi.md#getMediaCapturePipeline) | **GET** /sdk-media-capture-pipelines/{mediaPipelineId} | 
[**getMediaInsightsPipelineConfiguration**](DefaultApi.md#getMediaInsightsPipelineConfiguration) | **GET** /media-insights-pipeline-configurations/{identifier} | 
[**getMediaPipeline**](DefaultApi.md#getMediaPipeline) | **GET** /sdk-media-pipelines/{mediaPipelineId} | 
[**listMediaCapturePipelines**](DefaultApi.md#listMediaCapturePipelines) | **GET** /sdk-media-capture-pipelines | 
[**listMediaInsightsPipelineConfigurations**](DefaultApi.md#listMediaInsightsPipelineConfigurations) | **GET** /media-insights-pipeline-configurations | 
[**listMediaPipelines**](DefaultApi.md#listMediaPipelines) | **GET** /sdk-media-pipelines | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#arn | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#operation&#x3D;tag-resource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /tags#operation&#x3D;untag-resource | 
[**updateMediaInsightsPipelineConfiguration**](DefaultApi.md#updateMediaInsightsPipelineConfiguration) | **PUT** /media-insights-pipeline-configurations/{identifier} | 
[**updateMediaInsightsPipelineStatus**](DefaultApi.md#updateMediaInsightsPipelineStatus) | **PUT** /media-insights-pipeline-status/{identifier} | 



## createMediaCapturePipeline

> CreateMediaCapturePipelineResponse createMediaCapturePipeline(createMediaCapturePipelineRequest, opts)



Creates a media pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let createMediaCapturePipelineRequest = new AmazonChimeSdkMediaPipelines.CreateMediaCapturePipelineRequest(); // CreateMediaCapturePipelineRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMediaCapturePipeline(createMediaCapturePipelineRequest, opts, (error, data, response) => {
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
 **createMediaCapturePipelineRequest** | [**CreateMediaCapturePipelineRequest**](CreateMediaCapturePipelineRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMediaCapturePipelineResponse**](CreateMediaCapturePipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMediaConcatenationPipeline

> CreateMediaConcatenationPipelineResponse createMediaConcatenationPipeline(createMediaConcatenationPipelineRequest, opts)



Creates a media concatenation pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let createMediaConcatenationPipelineRequest = new AmazonChimeSdkMediaPipelines.CreateMediaConcatenationPipelineRequest(); // CreateMediaConcatenationPipelineRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMediaConcatenationPipeline(createMediaConcatenationPipelineRequest, opts, (error, data, response) => {
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
 **createMediaConcatenationPipelineRequest** | [**CreateMediaConcatenationPipelineRequest**](CreateMediaConcatenationPipelineRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMediaConcatenationPipelineResponse**](CreateMediaConcatenationPipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMediaInsightsPipeline

> CreateMediaInsightsPipelineResponse createMediaInsightsPipeline(createMediaInsightsPipelineRequest, opts)



Creates a media insights pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let createMediaInsightsPipelineRequest = new AmazonChimeSdkMediaPipelines.CreateMediaInsightsPipelineRequest(); // CreateMediaInsightsPipelineRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMediaInsightsPipeline(createMediaInsightsPipelineRequest, opts, (error, data, response) => {
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
 **createMediaInsightsPipelineRequest** | [**CreateMediaInsightsPipelineRequest**](CreateMediaInsightsPipelineRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMediaInsightsPipelineResponse**](CreateMediaInsightsPipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMediaInsightsPipelineConfiguration

> CreateMediaInsightsPipelineConfigurationResponse createMediaInsightsPipelineConfiguration(createMediaInsightsPipelineConfigurationRequest, opts)



A structure that contains the static configurations for a media insights pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let createMediaInsightsPipelineConfigurationRequest = new AmazonChimeSdkMediaPipelines.CreateMediaInsightsPipelineConfigurationRequest(); // CreateMediaInsightsPipelineConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMediaInsightsPipelineConfiguration(createMediaInsightsPipelineConfigurationRequest, opts, (error, data, response) => {
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
 **createMediaInsightsPipelineConfigurationRequest** | [**CreateMediaInsightsPipelineConfigurationRequest**](CreateMediaInsightsPipelineConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMediaInsightsPipelineConfigurationResponse**](CreateMediaInsightsPipelineConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMediaLiveConnectorPipeline

> CreateMediaLiveConnectorPipelineResponse createMediaLiveConnectorPipeline(createMediaLiveConnectorPipelineRequest, opts)



Creates a media live connector pipeline in an Amazon Chime SDK meeting.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let createMediaLiveConnectorPipelineRequest = new AmazonChimeSdkMediaPipelines.CreateMediaLiveConnectorPipelineRequest(); // CreateMediaLiveConnectorPipelineRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMediaLiveConnectorPipeline(createMediaLiveConnectorPipelineRequest, opts, (error, data, response) => {
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
 **createMediaLiveConnectorPipelineRequest** | [**CreateMediaLiveConnectorPipelineRequest**](CreateMediaLiveConnectorPipelineRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMediaLiveConnectorPipelineResponse**](CreateMediaLiveConnectorPipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMediaCapturePipeline

> deleteMediaCapturePipeline(mediaPipelineId, opts)



Deletes the media pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the media pipeline being deleted. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMediaCapturePipeline(mediaPipelineId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaPipelineId** | **String**| The ID of the media pipeline being deleted.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMediaInsightsPipelineConfiguration

> deleteMediaInsightsPipelineConfiguration(identifier, opts)



Deletes the specified configuration settings.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let identifier = "identifier_example"; // String | The unique identifier of the resource to be deleted. Valid values include the name and ARN of the media insights pipeline configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMediaInsightsPipelineConfiguration(identifier, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **String**| The unique identifier of the resource to be deleted. Valid values include the name and ARN of the media insights pipeline configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMediaPipeline

> deleteMediaPipeline(mediaPipelineId, opts)



Deletes the media pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the media pipeline to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMediaPipeline(mediaPipelineId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaPipelineId** | **String**| The ID of the media pipeline to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaCapturePipeline

> GetMediaCapturePipelineResponse getMediaCapturePipeline(mediaPipelineId, opts)



Gets an existing media pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the pipeline that you want to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMediaCapturePipeline(mediaPipelineId, opts, (error, data, response) => {
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
 **mediaPipelineId** | **String**| The ID of the pipeline that you want to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMediaCapturePipelineResponse**](GetMediaCapturePipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaInsightsPipelineConfiguration

> GetMediaInsightsPipelineConfigurationResponse getMediaInsightsPipelineConfiguration(identifier, opts)



Gets the configuration settings for a media insights pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let identifier = "identifier_example"; // String | The unique identifier of the requested resource. Valid values include the name and ARN of the media insights pipeline configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMediaInsightsPipelineConfiguration(identifier, opts, (error, data, response) => {
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
 **identifier** | **String**| The unique identifier of the requested resource. Valid values include the name and ARN of the media insights pipeline configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMediaInsightsPipelineConfigurationResponse**](GetMediaInsightsPipelineConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaPipeline

> GetMediaPipelineResponse getMediaPipeline(mediaPipelineId, opts)



Gets an existing media pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the pipeline that you want to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMediaPipeline(mediaPipelineId, opts, (error, data, response) => {
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
 **mediaPipelineId** | **String**| The ID of the pipeline that you want to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMediaPipelineResponse**](GetMediaPipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMediaCapturePipelines

> ListMediaCapturePipelinesResponse listMediaCapturePipelines(opts)



Returns a list of media pipelines.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token used to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call. Valid Range: 1 - 99.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMediaCapturePipelines(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token used to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. Valid Range: 1 - 99. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMediaCapturePipelinesResponse**](ListMediaCapturePipelinesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMediaInsightsPipelineConfigurations

> ListMediaInsightsPipelineConfigurationsResponse listMediaInsightsPipelineConfigurations(opts)



Lists the available media insights pipeline configurations.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token used to return the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMediaInsightsPipelineConfigurations(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token used to return the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMediaInsightsPipelineConfigurationsResponse**](ListMediaInsightsPipelineConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMediaPipelines

> ListMediaPipelinesResponse listMediaPipelines(opts)



Returns a list of media pipelines.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token used to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call. Valid Range: 1 - 99.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMediaPipelines(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token used to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. Valid Range: 1 - 99. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMediaPipelinesResponse**](ListMediaPipelinesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(arn, opts)



Lists the tags available for a media pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let arn = "arn_example"; // String | The ARN of the media pipeline associated with any tags. The ARN consists of the pipeline's region, resource ID, and pipeline ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The ARN of the media pipeline associated with any tags. The ARN consists of the pipeline&#39;s region, resource ID, and pipeline ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> Object tagResource(operation, tagResourceRequest, opts)



The ARN of the media pipeline that you want to tag. Consists of the pipeline&#39;s endpoint region, resource ID, and pipeline ID.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let operation = "operation_example"; // String | 
let tagResourceRequest = new AmazonChimeSdkMediaPipelines.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(operation, tagResourceRequest, opts, (error, data, response) => {
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
 **operation** | **String**|  | 
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


## untagResource

> Object untagResource(operation, untagResourceRequest, opts)



Removes any tags from a media pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let operation = "operation_example"; // String | 
let untagResourceRequest = new AmazonChimeSdkMediaPipelines.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(operation, untagResourceRequest, opts, (error, data, response) => {
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
 **operation** | **String**|  | 
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


## updateMediaInsightsPipelineConfiguration

> UpdateMediaInsightsPipelineConfigurationResponse updateMediaInsightsPipelineConfiguration(identifier, updateMediaInsightsPipelineConfigurationRequest, opts)



Updates the media insights pipeline&#39;s configuration settings.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let identifier = "identifier_example"; // String | The unique identifier for the resource to be updated. Valid values include the name and ARN of the media insights pipeline configuration.
let updateMediaInsightsPipelineConfigurationRequest = new AmazonChimeSdkMediaPipelines.UpdateMediaInsightsPipelineConfigurationRequest(); // UpdateMediaInsightsPipelineConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMediaInsightsPipelineConfiguration(identifier, updateMediaInsightsPipelineConfigurationRequest, opts, (error, data, response) => {
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
 **identifier** | **String**| The unique identifier for the resource to be updated. Valid values include the name and ARN of the media insights pipeline configuration. | 
 **updateMediaInsightsPipelineConfigurationRequest** | [**UpdateMediaInsightsPipelineConfigurationRequest**](UpdateMediaInsightsPipelineConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMediaInsightsPipelineConfigurationResponse**](UpdateMediaInsightsPipelineConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMediaInsightsPipelineStatus

> updateMediaInsightsPipelineStatus(identifier, updateMediaInsightsPipelineStatusRequest, opts)



Updates the status of a media insights pipeline.

### Example

```javascript
import AmazonChimeSdkMediaPipelines from 'amazon_chime_sdk_media_pipelines';
let defaultClient = AmazonChimeSdkMediaPipelines.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMediaPipelines.DefaultApi();
let identifier = "identifier_example"; // String | The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.
let updateMediaInsightsPipelineStatusRequest = new AmazonChimeSdkMediaPipelines.UpdateMediaInsightsPipelineStatusRequest(); // UpdateMediaInsightsPipelineStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMediaInsightsPipelineStatus(identifier, updateMediaInsightsPipelineStatusRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **String**| The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline. | 
 **updateMediaInsightsPipelineStatusRequest** | [**UpdateMediaInsightsPipelineStatusRequest**](UpdateMediaInsightsPipelineStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

