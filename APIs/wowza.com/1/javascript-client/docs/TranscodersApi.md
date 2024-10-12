# WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addStreamTargetToTranscoderOutput**](TranscodersApi.md#addStreamTargetToTranscoderOutput) | **POST** /transcoders/{transcoder_id}/outputs/{id}/add_stream_target | Deprecated operation
[**createTranscoder**](TranscodersApi.md#createTranscoder) | **POST** /transcoders | Create a transcoder
[**createTranscoderOutput**](TranscodersApi.md#createTranscoderOutput) | **POST** /transcoders/{transcoder_id}/outputs | Create an output
[**createTranscoderOutputOutputStreamTarget**](TranscodersApi.md#createTranscoderOutputOutputStreamTarget) | **POST** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets | Create an output stream target
[**createTranscoderProperty**](TranscodersApi.md#createTranscoderProperty) | **POST** /transcoders/{transcoder_id}/properties | Create a property for a transcoder
[**deleteTranscoder**](TranscodersApi.md#deleteTranscoder) | **DELETE** /transcoders/{id} | Delete a transcoder
[**deleteTranscoderOutput**](TranscodersApi.md#deleteTranscoderOutput) | **DELETE** /transcoders/{transcoder_id}/outputs/{id} | Delete an output
[**deleteTranscoderOutputOutputStreamTarget**](TranscodersApi.md#deleteTranscoderOutputOutputStreamTarget) | **DELETE** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id} | Delete an output stream target
[**deleteTranscoderProperty**](TranscodersApi.md#deleteTranscoderProperty) | **DELETE** /transcoders/{transcoder_id}/properties/{id} | Delete a transcoder&#39;s property
[**disableAllStreamTargetsTranscoder**](TranscodersApi.md#disableAllStreamTargetsTranscoder) | **PUT** /transcoders/{id}/disable_all_stream_targets | Disable a transcoder&#39;s stream targets
[**disableTranscoderOutputOutputStreamTarget**](TranscodersApi.md#disableTranscoderOutputOutputStreamTarget) | **PUT** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/disable | Disable an output stream target
[**enableAllStreamTargetsTranscoder**](TranscodersApi.md#enableAllStreamTargetsTranscoder) | **PUT** /transcoders/{id}/enable_all_stream_targets | Enable a transcoder&#39;s stream targets
[**enableTranscoderOutputOutputStreamTarget**](TranscodersApi.md#enableTranscoderOutputOutputStreamTarget) | **PUT** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/enable | Enable an output stream target
[**indexUptimes**](TranscodersApi.md#indexUptimes) | **GET** /transcoders/{transcoder_id}/uptimes | Fetch all uptime records for a transcoder
[**listTranscoderOutputOutputStreamTargets**](TranscodersApi.md#listTranscoderOutputOutputStreamTargets) | **GET** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets | Fetch all output stream targets of an output of a transcoder
[**listTranscoderOutputs**](TranscodersApi.md#listTranscoderOutputs) | **GET** /transcoders/{transcoder_id}/outputs | Fetch all outputs of a transcoder
[**listTranscoderProperties**](TranscodersApi.md#listTranscoderProperties) | **GET** /transcoders/{transcoder_id}/properties | Fetch a transcoder&#39;s properties
[**listTranscoderRecordings**](TranscodersApi.md#listTranscoderRecordings) | **GET** /transcoders/{id}/recordings | Fetch a transcoder&#39;s recordings
[**listTranscoderSchedules**](TranscodersApi.md#listTranscoderSchedules) | **GET** /transcoders/{id}/schedules | Fetch transcoder&#39;s schedules
[**listTranscoders**](TranscodersApi.md#listTranscoders) | **GET** /transcoders | Fetch all transcoders
[**removeStreamTargetToTranscoderOutput**](TranscodersApi.md#removeStreamTargetToTranscoderOutput) | **DELETE** /transcoders/{transcoder_id}/outputs/{id}/remove_stream_target | Deprecated operation
[**resetTranscoder**](TranscodersApi.md#resetTranscoder) | **PUT** /transcoders/{id}/reset | Reset a transcoder
[**restartTranscoderOutputOutputStreamTarget**](TranscodersApi.md#restartTranscoderOutputOutputStreamTarget) | **PUT** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id}/restart | Restart an output stream target
[**showTranscoder**](TranscodersApi.md#showTranscoder) | **GET** /transcoders/{id} | Fetch a transcoder
[**showTranscoderOutput**](TranscodersApi.md#showTranscoderOutput) | **GET** /transcoders/{transcoder_id}/outputs/{id} | Fetch an output
[**showTranscoderOutputOutputStreamTarget**](TranscodersApi.md#showTranscoderOutputOutputStreamTarget) | **GET** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id} | Fetch an output stream target
[**showTranscoderProperty**](TranscodersApi.md#showTranscoderProperty) | **GET** /transcoders/{transcoder_id}/properties/{id} | Fetch a property for a transcoder
[**showTranscoderState**](TranscodersApi.md#showTranscoderState) | **GET** /transcoders/{id}/state | Fetch the state and uptime ID of a transcoder
[**showTranscoderStats**](TranscodersApi.md#showTranscoderStats) | **GET** /transcoders/{id}/stats | Fetch statistics for a current transcoder
[**showTranscoderThumbnailUrl**](TranscodersApi.md#showTranscoderThumbnailUrl) | **GET** /transcoders/{id}/thumbnail_url | Fetch the thumbnail URL of a transcoder
[**showUptime**](TranscodersApi.md#showUptime) | **GET** /transcoders/{transcoder_id}/uptimes/{id} | Fetch an uptime record
[**showUptimeMetricsCurrent**](TranscodersApi.md#showUptimeMetricsCurrent) | **GET** /transcoders/{transcoder_id}/uptimes/{id}/metrics/current | Fetch current stream health metrics for an active transcoder
[**showUptimeMetricsHistoric**](TranscodersApi.md#showUptimeMetricsHistoric) | **GET** /transcoders/{transcoder_id}/uptimes/{id}/metrics/historic | Fetch historic stream health metrics for a transcoder
[**startTranscoder**](TranscodersApi.md#startTranscoder) | **PUT** /transcoders/{id}/start | Start a transcoder
[**stopTranscoder**](TranscodersApi.md#stopTranscoder) | **PUT** /transcoders/{id}/stop | Stop a transcoder
[**updateTranscoder**](TranscodersApi.md#updateTranscoder) | **PATCH** /transcoders/{id} | Update a transcoder
[**updateTranscoderOutput**](TranscodersApi.md#updateTranscoderOutput) | **PATCH** /transcoders/{transcoder_id}/outputs/{id} | Update an output
[**updateTranscoderOutputOutputStreamTarget**](TranscodersApi.md#updateTranscoderOutputOutputStreamTarget) | **PATCH** /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{stream_target_id} | Update an output stream target



## addStreamTargetToTranscoderOutput

> AddStreamTargetToTranscoderOutput200Response addStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget)

Deprecated operation

The operation POST /transcoders/{transcoder_id}/outputs/{id}/add_stream_target is deprecated. Use POST /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets to add an existing stream target to an output.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
let outputStreamTarget = new WowzaStreamingCloudRestApiReferenceDocumentation.OutputAddStreamTargetInput(); // OutputAddStreamTargetInput | Provide the details of the stream target to add in the body of the request.
apiInstance.addStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **outputStreamTarget** | [**OutputAddStreamTargetInput**](OutputAddStreamTargetInput.md)| Provide the details of the stream target to add in the body of the request. | 

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTranscoder

> CreateTranscoder200Response createTranscoder(transcoder)

Create a transcoder

This operation creates a transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoder = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscoderCreateInput(); // TranscoderCreateInput | Provide the details of the transcoder to create in the body of the request.
apiInstance.createTranscoder(transcoder, (error, data, response) => {
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
 **transcoder** | [**TranscoderCreateInput**](TranscoderCreateInput.md)| Provide the details of the transcoder to create in the body of the request. | 

### Return type

[**CreateTranscoder200Response**](CreateTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTranscoderOutput

> CreateTranscoderOutput200Response createTranscoderOutput(transcoderId, output)

Create an output

This operation creates an output rendition for a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let output = new WowzaStreamingCloudRestApiReferenceDocumentation.OutputCreateInput(); // OutputCreateInput | Provide the details of the output rendition to create in the body of the request.
apiInstance.createTranscoderOutput(transcoderId, output, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **output** | [**OutputCreateInput**](OutputCreateInput.md)| Provide the details of the output rendition to create in the body of the request. | 

### Return type

[**CreateTranscoderOutput200Response**](CreateTranscoderOutput200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTranscoderOutputOutputStreamTarget

> AddStreamTargetToTranscoderOutput200Response createTranscoderOutputOutputStreamTarget(transcoderId, outputId, outputStreamTarget)

Create an output stream target

This operation creates an output stream target. Targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; can&#39;t be added to output renditions.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
let outputStreamTarget = new WowzaStreamingCloudRestApiReferenceDocumentation.OutputStreamTargetCreateInput(); // OutputStreamTargetCreateInput | Provide the details of the output stream target to create in the body of the request. Targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong> can't be added to output renditions.
apiInstance.createTranscoderOutputOutputStreamTarget(transcoderId, outputId, outputStreamTarget, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **outputStreamTarget** | [**OutputStreamTargetCreateInput**](OutputStreamTargetCreateInput.md)| Provide the details of the output stream target to create in the body of the request. Targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; can&#39;t be added to output renditions. | 

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTranscoderProperty

> CreateTranscoderProperty200Response createTranscoderProperty(transcoderId, property)

Create a property for a transcoder

This operation creates a property for a transcoder. For more information see the technical article [How to set advanced properties by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-set-advanced-properties-by-using-the-wowza-streaming-cloud-rest-api).

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let property = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscoderPropertyCreateInput(); // TranscoderPropertyCreateInput | Provide the details of the property to create in the body of the request.
apiInstance.createTranscoderProperty(transcoderId, property, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **property** | [**TranscoderPropertyCreateInput**](TranscoderPropertyCreateInput.md)| Provide the details of the property to create in the body of the request. | 

### Return type

[**CreateTranscoderProperty200Response**](CreateTranscoderProperty200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTranscoder

> deleteTranscoder(id)

Delete a transcoder

This operation deletes a transcoder, including all of its assigned output renditions and stream targets.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.deleteTranscoder(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTranscoderOutput

> deleteTranscoderOutput(transcoderId, id)

Delete an output

This operation deletes an output, including all of its assigned targets.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
apiInstance.deleteTranscoderOutput(transcoderId, id, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the output rendition. | 

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTranscoderOutputOutputStreamTarget

> deleteTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Delete an output stream target

This operation deletes an output stream target, including all of its assigned targets.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.deleteTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTranscoderProperty

> deleteTranscoderProperty(transcoderId, id)

Delete a transcoder&#39;s property

This operation deletes a specific property from a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset.
apiInstance.deleteTranscoderProperty(transcoderId, id, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset. | 

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableAllStreamTargetsTranscoder

> DisableAllStreamTargetsTranscoder200Response disableAllStreamTargetsTranscoder(id)

Disable a transcoder&#39;s stream targets

This operation disables all of the stream targets assigned to a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.disableAllStreamTargetsTranscoder(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**DisableAllStreamTargetsTranscoder200Response**](DisableAllStreamTargetsTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableTranscoderOutputOutputStreamTarget

> DisableTranscoderOutputOutputStreamTarget200Response disableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Disable an output stream target

This operation disables an output stream target.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.disableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

[**DisableTranscoderOutputOutputStreamTarget200Response**](DisableTranscoderOutputOutputStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableAllStreamTargetsTranscoder

> DisableAllStreamTargetsTranscoder200Response enableAllStreamTargetsTranscoder(id)

Enable a transcoder&#39;s stream targets

This operation enables all of the stream targets assigned to a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.enableAllStreamTargetsTranscoder(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**DisableAllStreamTargetsTranscoder200Response**](DisableAllStreamTargetsTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableTranscoderOutputOutputStreamTarget

> EnableTranscoderOutputOutputStreamTarget200Response enableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Enable an output stream target

This operation enables an output stream target.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.enableTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

[**EnableTranscoderOutputOutputStreamTarget200Response**](EnableTranscoderOutputOutputStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## indexUptimes

> Uptimes indexUptimes(transcoderId, opts)

Fetch all uptime records for a transcoder

This operation shows all of the uptime records for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a specific transcoding session.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let opts = {
  'page': 56, // Number | Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. <strong>Next</strong> and <strong>Previous</strong> links allow you to navigate multiple pages of results. Omit the <em>page</em> parameter or specify an integer that's less than or equal to <strong>0</strong> to view all (unpaginated) results.
  'perPage': 56 // Number | For use with the <em>page</em> parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is <strong>10</strong>.
};
apiInstance.indexUptimes(transcoderId, opts, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **page** | **Number**| Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results. | [optional] 
 **perPage** | **Number**| For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;. | [optional] 

### Return type

[**Uptimes**](Uptimes.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscoderOutputOutputStreamTargets

> OutputStreamTarget listTranscoderOutputOutputStreamTargets(transcoderId, outputId)

Fetch all output stream targets of an output of a transcoder

This operation shows the details of all of the output stream targets of an output of a transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
apiInstance.listTranscoderOutputOutputStreamTargets(transcoderId, outputId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 

### Return type

[**OutputStreamTarget**](OutputStreamTarget.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscoderOutputs

> Outputs listTranscoderOutputs(transcoderId)

Fetch all outputs of a transcoder

This operation shows the details of all of the output renditions of a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.listTranscoderOutputs(transcoderId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**Outputs**](Outputs.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscoderProperties

> TranscoderProperties listTranscoderProperties(transcoderId)

Fetch a transcoder&#39;s properties

This operation shows all of the properties of a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.listTranscoderProperties(transcoderId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**TranscoderProperties**](TranscoderProperties.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscoderRecordings

> ListTranscoderRecordings200Response listTranscoderRecordings(id)

Fetch a transcoder&#39;s recordings

This operation shows the details of all of the recordings for a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.listTranscoderRecordings(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**ListTranscoderRecordings200Response**](ListTranscoderRecordings200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscoderSchedules

> ListTranscoderSchedules200Response listTranscoderSchedules(id)

Fetch transcoder&#39;s schedules

This operation shows the details of all of the schedules for a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.listTranscoderSchedules(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**ListTranscoderSchedules200Response**](ListTranscoderSchedules200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscoders

> Transcoders listTranscoders(opts)

Fetch all transcoders

This operation shows the details of all of your transcoders.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let opts = {
  'page': 56, // Number | Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. <strong>Next</strong> and <strong>Previous</strong> links allow you to navigate multiple pages of results. Omit the <em>page</em> parameter or specify an integer that's less than or equal to <strong>0</strong> to view all (unpaginated) results.
  'perPage': 56 // Number | For use with the <em>page</em> parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is <strong>10</strong>.
};
apiInstance.listTranscoders(opts, (error, data, response) => {
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
 **page** | **Number**| Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results. | [optional] 
 **perPage** | **Number**| For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;. | [optional] 

### Return type

[**Transcoders**](Transcoders.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeStreamTargetToTranscoderOutput

> removeStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget)

Deprecated operation

The operation DELETE /transcoders/{transcoder_id}/outputs/{id}/remove_stream_target is deprecated. Use DELETE /transcoders/{transcoder_id}/outputs/{output_id}/output_stream_targets/{id} to remove a stream target from an output.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
let outputStreamTarget = new WowzaStreamingCloudRestApiReferenceDocumentation.OutputRemoveStreamTargetInput(); // OutputRemoveStreamTargetInput | Provide the details of the stream target to remove in the body of the request.
apiInstance.removeStreamTargetToTranscoderOutput(transcoderId, id, outputStreamTarget, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **outputStreamTarget** | [**OutputRemoveStreamTargetInput**](OutputRemoveStreamTargetInput.md)| Provide the details of the stream target to remove in the body of the request. | 

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetTranscoder

> ResetTranscoder200Response resetTranscoder(id)

Reset a transcoder

This operation resets a transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.resetTranscoder(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**ResetTranscoder200Response**](ResetTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restartTranscoderOutputOutputStreamTarget

> RestartTranscoderOutputOutputStreamTarget200Response restartTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Restart an output stream target

This operation restarts an output stream target.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.restartTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

[**RestartTranscoderOutputOutputStreamTarget200Response**](RestartTranscoderOutputOutputStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showTranscoder

> CreateTranscoder200Response showTranscoder(id)

Fetch a transcoder

This operation shows the details of a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.showTranscoder(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**CreateTranscoder200Response**](CreateTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showTranscoderOutput

> CreateTranscoderOutput200Response showTranscoderOutput(transcoderId, id)

Fetch an output

This operation shows the details of a specific output rendition for a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
apiInstance.showTranscoderOutput(transcoderId, id, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the output rendition. | 

### Return type

[**CreateTranscoderOutput200Response**](CreateTranscoderOutput200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showTranscoderOutputOutputStreamTarget

> AddStreamTargetToTranscoderOutput200Response showTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId)

Fetch an output stream target

This operation shows the details of an output stream target.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.showTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showTranscoderProperty

> CreateTranscoderProperty200Response showTranscoderProperty(transcoderId, id)

Fetch a property for a transcoder

This operation shows the details of a specific property for a specific transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset.
apiInstance.showTranscoderProperty(transcoderId, id, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique string that identifies the transcoder property. The string contains the section and the key, connected by a dash. For example, cupertino-cupertinoProgramDateTimeOffset. | 

### Return type

[**CreateTranscoderProperty200Response**](CreateTranscoderProperty200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showTranscoderState

> ShowTranscoderState200Response showTranscoderState(id)

Fetch the state and uptime ID of a transcoder

This operation shows the current state and uptime ID of a transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.showTranscoderState(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**ShowTranscoderState200Response**](ShowTranscoderState200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showTranscoderStats

> ShowTranscoderStats200Response showTranscoderStats(id)

Fetch statistics for a current transcoder

This operation responds with a hash of metrics (keys) for a currently running transcoder. Each key has a &lt;strong&gt;status&lt;/strong&gt;, &lt;strong&gt;text&lt;/strong&gt; (description), &lt;strong&gt;units&lt;/strong&gt;, and &lt;strong&gt;value&lt;/strong&gt;.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.showTranscoderStats(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**ShowTranscoderStats200Response**](ShowTranscoderStats200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showTranscoderThumbnailUrl

> ShowTranscoderThumbnailUrl200Response showTranscoderThumbnailUrl(id)

Fetch the thumbnail URL of a transcoder

This operation shows the thumbnail URL of a started transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.showTranscoderThumbnailUrl(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**ShowTranscoderThumbnailUrl200Response**](ShowTranscoderThumbnailUrl200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showUptime

> Uptime showUptime(transcoderId, id)

Fetch an uptime record

This operation shows the details of a specific uptime record for a specific transcoder. An &lt;em&gt;uptime record&lt;/em&gt; identifies a transcoding session.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the uptime record.
apiInstance.showUptime(transcoderId, id, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the uptime record. | 

### Return type

[**Uptime**](Uptime.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showUptimeMetricsCurrent

> ShowUptimeMetricsCurrent200Response showUptimeMetricsCurrent(transcoderId, id, opts)

Fetch current stream health metrics for an active transcoder

This operation returns a snapshot of the current source connection and processing details of an active (running) transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the uptime record.
let opts = {
  'fields': "fields_example" // String | A comma-separated list of fields to return.
};
apiInstance.showUptimeMetricsCurrent(transcoderId, id, opts, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the uptime record. | 
 **fields** | **String**| A comma-separated list of fields to return. | [optional] 

### Return type

[**ShowUptimeMetricsCurrent200Response**](ShowUptimeMetricsCurrent200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showUptimeMetricsHistoric

> ShowUptimeMetricsHistoric200Response showUptimeMetricsHistoric(transcoderId, id, opts)

Fetch historic stream health metrics for a transcoder

This operation shows the historic source connection and processing details for a transcoding session (uptime record). The transcoder can be running or stopped. Metrics are recorded every 20 seconds.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the uptime record.
let opts = {
  'fields': "fields_example", // String | A comma-separated list of fields to return.
  'from': "from_example", // String | The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
  'to': "to_example" // String | The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
};
apiInstance.showUptimeMetricsHistoric(transcoderId, id, opts, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the uptime record. | 
 **fields** | **String**| A comma-separated list of fields to return. | [optional] 
 **from** | **String**| The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] 
 **to** | **String**| The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] 

### Return type

[**ShowUptimeMetricsHistoric200Response**](ShowUptimeMetricsHistoric200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startTranscoder

> StartTranscoder200Response startTranscoder(id)

Start a transcoder

This operation starts a transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.startTranscoder(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**StartTranscoder200Response**](StartTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopTranscoder

> StartTranscoder200Response stopTranscoder(id)

Stop a transcoder

This operation stops a transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
apiInstance.stopTranscoder(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 

### Return type

[**StartTranscoder200Response**](StartTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTranscoder

> CreateTranscoder200Response updateTranscoder(id, transcoder)

Update a transcoder

This operation updates a transcoder.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the transcoder.
let transcoder = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscoderUpdateInput(); // TranscoderUpdateInput | Provide the details of the transcoder to update in the body of the request.
apiInstance.updateTranscoder(id, transcoder, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **transcoder** | [**TranscoderUpdateInput**](TranscoderUpdateInput.md)| Provide the details of the transcoder to update in the body of the request. | 

### Return type

[**CreateTranscoder200Response**](CreateTranscoder200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTranscoderOutput

> CreateTranscoderOutput200Response updateTranscoderOutput(transcoderId, id, output)

Update an output

This operation updates an output rendition.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let id = "id_example"; // String | The unique alphanumeric string that identifies the output rendition.
let output = new WowzaStreamingCloudRestApiReferenceDocumentation.OutputUpdateInput(); // OutputUpdateInput | Provide the details of the output rendition to update in the body of the request.
apiInstance.updateTranscoderOutput(transcoderId, id, output, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **id** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **output** | [**OutputUpdateInput**](OutputUpdateInput.md)| Provide the details of the output rendition to update in the body of the request. | 

### Return type

[**CreateTranscoderOutput200Response**](CreateTranscoderOutput200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTranscoderOutputOutputStreamTarget

> AddStreamTargetToTranscoderOutput200Response updateTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, outputStreamTarget)

Update an output stream target

This operation updates an output stream target.

### Example

```javascript
import WowzaStreamingCloudRestApiReferenceDocumentation from 'wowza_streaming_cloud_rest_api_reference_documentation';
let defaultClient = WowzaStreamingCloudRestApiReferenceDocumentation.ApiClient.instance;
// Configure API key authorization: wsc-api-key
let wsc-api-key = defaultClient.authentications['wsc-api-key'];
wsc-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-api-key.apiKeyPrefix = 'Token';
// Configure API key authorization: wsc-access-key
let wsc-access-key = defaultClient.authentications['wsc-access-key'];
wsc-access-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//wsc-access-key.apiKeyPrefix = 'Token';

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.TranscodersApi();
let transcoderId = "transcoderId_example"; // String | The unique alphanumeric string that identifies the transcoder.
let outputId = "outputId_example"; // String | The unique alphanumeric string that identifies the output rendition.
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let outputStreamTarget = new WowzaStreamingCloudRestApiReferenceDocumentation.OutputStreamTargetUpdateInput(); // OutputStreamTargetUpdateInput | Provide the details of the output stream target to update in the body of the request.
apiInstance.updateTranscoderOutputOutputStreamTarget(transcoderId, outputId, streamTargetId, outputStreamTarget, (error, data, response) => {
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
 **transcoderId** | **String**| The unique alphanumeric string that identifies the transcoder. | 
 **outputId** | **String**| The unique alphanumeric string that identifies the output rendition. | 
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **outputStreamTarget** | [**OutputStreamTargetUpdateInput**](OutputStreamTargetUpdateInput.md)| Provide the details of the output stream target to update in the body of the request. | 

### Return type

[**AddStreamTargetToTranscoderOutput200Response**](AddStreamTargetToTranscoderOutput200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

