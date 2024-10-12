# WowzaStreamingCloudRestApiReferenceDocumentation.NetworkApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usageNetworkStreamSourcesIndex**](NetworkApi.md#usageNetworkStreamSourcesIndex) | **GET** /usage/network/stream_sources | Fetch network usage for all stream sources
[**usageNetworkStreamTargetsIndex**](NetworkApi.md#usageNetworkStreamTargetsIndex) | **GET** /usage/network/stream_targets | Fetch network usage for all stream targets
[**usageNetworkTranscodersIndex**](NetworkApi.md#usageNetworkTranscodersIndex) | **GET** /usage/network/transcoders | Fetch network usage for all transcoders



## usageNetworkStreamSourcesIndex

> UsageNetworkStreamSources usageNetworkStreamSourcesIndex(opts)

Fetch network usage for all stream sources

This operation shows the amount of network usage for all stream sources in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.NetworkApi();
let opts = {
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
};
apiInstance.usageNetworkStreamSourcesIndex(opts, (error, data, response) => {
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
 **from** | **Date**| The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date. | [optional] 
 **to** | **Date**| The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day. | [optional] 

### Return type

[**UsageNetworkStreamSources**](UsageNetworkStreamSources.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usageNetworkStreamTargetsIndex

> UsageNetworkStreamTargets usageNetworkStreamTargetsIndex(opts)

Fetch network usage for all stream targets

This operation shows the amount of network usage for all stream targets in the account cumulatively and individually. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.NetworkApi();
let opts = {
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
};
apiInstance.usageNetworkStreamTargetsIndex(opts, (error, data, response) => {
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
 **from** | **Date**| The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date. | [optional] 
 **to** | **Date**| The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day. | [optional] 

### Return type

[**UsageNetworkStreamTargets**](UsageNetworkStreamTargets.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usageNetworkTranscodersIndex

> UsageNetworkTranscoders usageNetworkTranscodersIndex(opts)

Fetch network usage for all transcoders

This operation shows the amount of network usage (egress) for all transcoders in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.NetworkApi();
let opts = {
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>from</em> default is the last billing date.
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | The end of the range of time you want to view. Specify <strong>YYYY-MM-DD HH:MM:SS</strong> where <strong>HH</strong> is a 24-hour clock in UTC. The <em>to</em> default is the end of the current day.
  'transcoderType': "transcoderType_example", // String | The type of transcoder. The default is <strong>transcoded</strong>.
  'billingMode': "billingMode_example" // String | The billing mode for the transcoder. The default is <strong>pay_as_you_go</strong>.
};
apiInstance.usageNetworkTranscodersIndex(opts, (error, data, response) => {
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
 **from** | **Date**| The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date. | [optional] 
 **to** | **Date**| The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day. | [optional] 
 **transcoderType** | **String**| The type of transcoder. The default is &lt;strong&gt;transcoded&lt;/strong&gt;. | [optional] 
 **billingMode** | **String**| The billing mode for the transcoder. The default is &lt;strong&gt;pay_as_you_go&lt;/strong&gt;. | [optional] 

### Return type

[**UsageNetworkTranscoders**](UsageNetworkTranscoders.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

