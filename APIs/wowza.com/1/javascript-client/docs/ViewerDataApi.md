# WowzaStreamingCloudRestApiReferenceDocumentation.ViewerDataApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**showViewerDataStreamTarget**](ViewerDataApi.md#showViewerDataStreamTarget) | **GET** /usage/viewer_data/stream_targets/{id} | Fetch viewer data for a stream target



## showViewerDataStreamTarget

> UsageViewerDataStreamTarget showViewerDataStreamTarget(id, opts)

Fetch viewer data for a stream target

This operation shows viewer data for a specific stream target. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.ViewerDataApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
let opts = {
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
};
apiInstance.showViewerDataStreamTarget(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **from** | **Date**| The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date. | [optional] 
 **to** | **Date**| The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day. | [optional] 

### Return type

[**UsageViewerDataStreamTarget**](UsageViewerDataStreamTarget.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

