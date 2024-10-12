# WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi

All URIs are relative to *https://api-sandbox.cloud.wowza.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addStreamTarget**](StreamTargetsApi.md#addStreamTarget) | **POST** /stream_targets/add | Deprecated operation
[**createStreamTarget**](StreamTargetsApi.md#createStreamTarget) | **POST** /stream_targets | Create a stream target
[**createStreamTargetGeoblock**](StreamTargetsApi.md#createStreamTargetGeoblock) | **POST** /stream_targets/{stream_target_id}/geoblock | Create geo-blocking for a stream target
[**createStreamTargetProperty**](StreamTargetsApi.md#createStreamTargetProperty) | **POST** /stream_targets/{stream_target_id}/properties | Create a property for a stream target
[**createStreamTargetTokenAuth**](StreamTargetsApi.md#createStreamTargetTokenAuth) | **POST** /stream_targets/{stream_target_id}/token_auth | Create token authorization for a stream target
[**deleteStreamTarget**](StreamTargetsApi.md#deleteStreamTarget) | **DELETE** /stream_targets/{id} | Delete a stream target
[**deleteStreamTargetProperty**](StreamTargetsApi.md#deleteStreamTargetProperty) | **DELETE** /stream_targets/{stream_target_id}/properties/{id} | Delete a stream target property
[**listStreamTargetProperties**](StreamTargetsApi.md#listStreamTargetProperties) | **GET** /stream_targets/{stream_target_id}/properties | Fetch all properties of a stream target
[**listStreamTargets**](StreamTargetsApi.md#listStreamTargets) | **GET** /stream_targets | Fetch all stream targets
[**regenerateConnectionCodeStreamTarget**](StreamTargetsApi.md#regenerateConnectionCodeStreamTarget) | **PUT** /stream_targets/{id}/regenerate_connection_code | Regenerate the connection code for a stream target
[**showStreamTarget**](StreamTargetsApi.md#showStreamTarget) | **GET** /stream_targets/{id} | Fetch a stream target
[**showStreamTargetGeoblock**](StreamTargetsApi.md#showStreamTargetGeoblock) | **GET** /stream_targets/{stream_target_id}/geoblock | Fetch geo-blocking for a stream target
[**showStreamTargetMetricsCurrent**](StreamTargetsApi.md#showStreamTargetMetricsCurrent) | **GET** /stream_targets/{id}/metrics/current | Fetch current health metrics for an active Wowza ultra low latency stream target
[**showStreamTargetMetricsHistoric**](StreamTargetsApi.md#showStreamTargetMetricsHistoric) | **GET** /stream_targets/{id}/metrics/historic | Fetch historic health metrics for a Wowza ultra low latency stream target
[**showStreamTargetProperty**](StreamTargetsApi.md#showStreamTargetProperty) | **GET** /stream_targets/{stream_target_id}/properties/{id} | Fetch a property of a stream target
[**showStreamTargetTokenAuth**](StreamTargetsApi.md#showStreamTargetTokenAuth) | **GET** /stream_targets/{stream_target_id}/token_auth | Fetch token authorization for a stream target
[**updateStreamTarget**](StreamTargetsApi.md#updateStreamTarget) | **PATCH** /stream_targets/{id} | Update a stream target
[**updateStreamTargetGeoblock**](StreamTargetsApi.md#updateStreamTargetGeoblock) | **PATCH** /stream_targets/{stream_target_id}/geoblock | Update geo-blocking for a stream target
[**updateStreamTargetTokenAuth**](StreamTargetsApi.md#updateStreamTargetTokenAuth) | **PATCH** /stream_targets/{stream_target_id}/token_auth | Update token authorization for a stream target



## addStreamTarget

> CreateStreamTarget200Response addStreamTarget(streamTarget)

Deprecated operation

POST /stream_targets/add/ is deprecated. To add a stream target, use POST /stream_targets instead.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTarget = new WowzaStreamingCloudRestApiReferenceDocumentation.WowzaStreamTargetInput(); // WowzaStreamTargetInput | Provide the details of the stream target to add in the body of the request.
apiInstance.addStreamTarget(streamTarget, (error, data, response) => {
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
 **streamTarget** | [**WowzaStreamTargetInput**](WowzaStreamTargetInput.md)| Provide the details of the stream target to add in the body of the request. | 

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStreamTarget

> CreateStreamTarget200Response createStreamTarget(streamTarget)

Create a stream target

This operation creates a stream target. There are three types of targets that you can create: &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; for an an external, third-party destination; &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; for a Wowza CDN target; or &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt; for an ultra low latency Wowza CDN target. The availability of many parameters depends on the type of target you create.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTarget = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetCreateInput(); // StreamTargetCreateInput | Provide the details of the stream target to create in the body of the request.
apiInstance.createStreamTarget(streamTarget, (error, data, response) => {
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
 **streamTarget** | [**StreamTargetCreateInput**](StreamTargetCreateInput.md)| Provide the details of the stream target to create in the body of the request. | 

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStreamTargetGeoblock

> ShowStreamTargetGeoblock200Response createStreamTargetGeoblock(streamTargetId, geoblock)

Create geo-blocking for a stream target

This operation allows you to block or whitelist viewing of a stream target by geographic location. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked. For more information see the technical article [How to geo-block stream targets by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-geo-block-stream-targets-by-using-the-wowza-streaming-cloud-rest-api).

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let geoblock = new WowzaStreamingCloudRestApiReferenceDocumentation.GeoblockCreateInput(); // GeoblockCreateInput | Provide the details of the geo-blocking to create in the body of the request.
apiInstance.createStreamTargetGeoblock(streamTargetId, geoblock, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **geoblock** | [**GeoblockCreateInput**](GeoblockCreateInput.md)| Provide the details of the geo-blocking to create in the body of the request. | 

### Return type

[**ShowStreamTargetGeoblock200Response**](ShowStreamTargetGeoblock200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStreamTargetProperty

> CreateStreamTargetProperty200Response createStreamTargetProperty(streamTargetId, property)

Create a property for a stream target

This operation creates a property for a stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;. For more information see the technical article [How to set advanced properties by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-set-advanced-properties-by-using-the-wowza-streaming-cloud-rest-api).

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let property = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetPropertyCreateInput(); // StreamTargetPropertyCreateInput | Provide the details of the property to create in the body of the request.
apiInstance.createStreamTargetProperty(streamTargetId, property, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **property** | [**StreamTargetPropertyCreateInput**](StreamTargetPropertyCreateInput.md)| Provide the details of the property to create in the body of the request. | 

### Return type

[**CreateStreamTargetProperty200Response**](CreateStreamTargetProperty200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createStreamTargetTokenAuth

> ShowStreamTargetTokenAuth200Response createStreamTargetTokenAuth(streamTargetId, tokenAuth)

Create token authorization for a stream target

This operation creates token authorization for a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization. For more information see the technical article [How to protect stream targets with token authorization by using the Wowza Streaming Cloud REST API](https://www.wowza.com/docs/how-to-protect-streams-with-token-authorization-by-using-the-wowza-streaming-cloud-rest-api).

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let tokenAuth = new WowzaStreamingCloudRestApiReferenceDocumentation.TokenAuthCreateInput(); // TokenAuthCreateInput | Provide the details of the token authorization to create in the body of the request.
apiInstance.createStreamTargetTokenAuth(streamTargetId, tokenAuth, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **tokenAuth** | [**TokenAuthCreateInput**](TokenAuthCreateInput.md)| Provide the details of the token authorization to create in the body of the request. | 

### Return type

[**ShowStreamTargetTokenAuth200Response**](ShowStreamTargetTokenAuth200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStreamTarget

> deleteStreamTarget(id)

Delete a stream target

This operation deletes a stream target.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.deleteStreamTarget(id, (error, data, response) => {
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
 **id** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteStreamTargetProperty

> deleteStreamTargetProperty(streamTargetId, id)

Delete a stream target property

This operation removes a property from a stream target.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let id = "id_example"; // String | The unique string that identifies the stream target property. The string contains the <em>section</em> and the <em>key</em>, connected by a dash. For example, <strong>hls-chunkSize</strong>.
apiInstance.deleteStreamTargetProperty(streamTargetId, id, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **id** | **String**| The unique string that identifies the stream target property. The string contains the &lt;em&gt;section&lt;/em&gt; and the &lt;em&gt;key&lt;/em&gt;, connected by a dash. For example, &lt;strong&gt;hls-chunkSize&lt;/strong&gt;. | 

### Return type

null (empty response body)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStreamTargetProperties

> StreamTargetProperties listStreamTargetProperties(streamTargetId)

Fetch all properties of a stream target

This operation shows the details of all of the properties assigned to a specific stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.listStreamTargetProperties(streamTargetId, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

[**StreamTargetProperties**](StreamTargetProperties.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listStreamTargets

> StreamTargets listStreamTargets(opts)

Fetch all stream targets

This operation lists the details of all of your stream targets.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let opts = {
  'page': 56, // Number | Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. <strong>Next</strong> and <strong>Previous</strong> links allow you to navigate multiple pages of results. Omit the <em>page</em> parameter or specify an integer that's less than or equal to <strong>0</strong> to view all (unpaginated) results.
  'perPage': 56 // Number | For use with the <em>page</em> parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is <strong>10</strong>.
};
apiInstance.listStreamTargets(opts, (error, data, response) => {
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

[**StreamTargets**](StreamTargets.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regenerateConnectionCodeStreamTarget

> RegenerateConnectionCodeStreamTarget200Response regenerateConnectionCodeStreamTarget(id)

Regenerate the connection code for a stream target

This operation regenerates the connection code of a stream target.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.regenerateConnectionCodeStreamTarget(id, (error, data, response) => {
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

### Return type

[**RegenerateConnectionCodeStreamTarget200Response**](RegenerateConnectionCodeStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showStreamTarget

> CreateStreamTarget200Response showStreamTarget(id)

Fetch a stream target

This operation shows details of a specific stream target.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.showStreamTarget(id, (error, data, response) => {
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

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showStreamTargetGeoblock

> ShowStreamTargetGeoblock200Response showStreamTargetGeoblock(streamTargetId)

Fetch geo-blocking for a stream target

This operation shows the details of geo-blocking applied to a specific stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.showStreamTargetGeoblock(streamTargetId, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

[**ShowStreamTargetGeoblock200Response**](ShowStreamTargetGeoblock200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showStreamTargetMetricsCurrent

> ShowStreamTargetMetricsCurrent200Response showStreamTargetMetricsCurrent(id)

Fetch current health metrics for an active Wowza ultra low latency stream target

This operation returns a snapshot of the current connection and throughput details for an active target whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;. The interval for current metrics is 30 seconds from the moment of the query.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.showStreamTargetMetricsCurrent(id, (error, data, response) => {
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

### Return type

[**ShowStreamTargetMetricsCurrent200Response**](ShowStreamTargetMetricsCurrent200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showStreamTargetMetricsHistoric

> ShowStreamTargetMetricsHistoric200Response showStreamTargetMetricsHistoric(id, opts)

Fetch historic health metrics for a Wowza ultra low latency stream target

This operation shows historic connection and throughput details for target whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;UltraLowLatencyStreamTarget&lt;/strong&gt;.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
let opts = {
  'from': "from_example", // String | The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
  'to': "to_example", // String | The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of <strong>YYYY-MM-DDTHH:MM:SSZ</strong> where <strong>HH</strong> is a 24-hour clock in UTC.
  'interval': "interval_example" // String | The length of time for a block of metrics. The default is **10m** (10 minutes).
};
apiInstance.showStreamTargetMetricsHistoric(id, opts, (error, data, response) => {
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
 **from** | **String**| The start of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] 
 **to** | **String**| The end of the range of time used to aggregate the metrics. Express the value by using the ISO 8601 standard of &lt;strong&gt;YYYY-MM-DDTHH:MM:SSZ&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. | [optional] 
 **interval** | **String**| The length of time for a block of metrics. The default is **10m** (10 minutes). | [optional] 

### Return type

[**ShowStreamTargetMetricsHistoric200Response**](ShowStreamTargetMetricsHistoric200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showStreamTargetProperty

> CreateStreamTargetProperty200Response showStreamTargetProperty(streamTargetId, id)

Fetch a property of a stream target

This operation shows the details of a specific property assigned to a specific stream target. Properties can be applied to a &lt;strong&gt;CustomStreamTarget&lt;/strong&gt; or &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; whose &lt;em&gt;provider&lt;/em&gt; is &lt;strong&gt;akamai_cupertino&lt;/strong&gt;.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let id = "id_example"; // String | The unique string that identifies the stream target property. The string contains the <em>section</em> and the <em>key</em>, connected by a dash. For example, <strong>hls-chunkSize</strong>.
apiInstance.showStreamTargetProperty(streamTargetId, id, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **id** | **String**| The unique string that identifies the stream target property. The string contains the &lt;em&gt;section&lt;/em&gt; and the &lt;em&gt;key&lt;/em&gt;, connected by a dash. For example, &lt;strong&gt;hls-chunkSize&lt;/strong&gt;. | 

### Return type

[**CreateStreamTargetProperty200Response**](CreateStreamTargetProperty200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showStreamTargetTokenAuth

> ShowStreamTargetTokenAuth200Response showStreamTargetTokenAuth(streamTargetId)

Fetch token authorization for a stream target

This operation shows the details of the token authorization applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
apiInstance.showStreamTargetTokenAuth(streamTargetId, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 

### Return type

[**ShowStreamTargetTokenAuth200Response**](ShowStreamTargetTokenAuth200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateStreamTarget

> CreateStreamTarget200Response updateStreamTarget(id, streamTarget)

Update a stream target

This operation updates a stream target.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let id = "id_example"; // String | The unique alphanumeric string that identifies the stream target.
let streamTarget = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetUpdateInput(); // StreamTargetUpdateInput | Provide the details of the stream target to update in the body of the request.
apiInstance.updateStreamTarget(id, streamTarget, (error, data, response) => {
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
 **streamTarget** | [**StreamTargetUpdateInput**](StreamTargetUpdateInput.md)| Provide the details of the stream target to update in the body of the request. | 

### Return type

[**CreateStreamTarget200Response**](CreateStreamTarget200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStreamTargetGeoblock

> ShowStreamTargetGeoblock200Response updateStreamTargetGeoblock(streamTargetId, geoblock)

Update geo-blocking for a stream target

This operation updates the geo-blocking applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can be geo-blocked.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let geoblock = new WowzaStreamingCloudRestApiReferenceDocumentation.GeoblockUpdateInput(); // GeoblockUpdateInput | Provide the details of the geo-blocking to update in the body of the request.
apiInstance.updateStreamTargetGeoblock(streamTargetId, geoblock, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **geoblock** | [**GeoblockUpdateInput**](GeoblockUpdateInput.md)| Provide the details of the geo-blocking to update in the body of the request. | 

### Return type

[**ShowStreamTargetGeoblock200Response**](ShowStreamTargetGeoblock200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStreamTargetTokenAuth

> ShowStreamTargetTokenAuth200Response updateStreamTargetTokenAuth(streamTargetId, tokenAuth)

Update token authorization for a stream target

This operation updates the token authorization applied to a stream target. Only stream targets whose &lt;em&gt;type&lt;/em&gt; is &lt;strong&gt;WowzaStreamTarget&lt;/strong&gt; can use token authorization.

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

let apiInstance = new WowzaStreamingCloudRestApiReferenceDocumentation.StreamTargetsApi();
let streamTargetId = "streamTargetId_example"; // String | The unique alphanumeric string that identifies the stream target.
let tokenAuth = new WowzaStreamingCloudRestApiReferenceDocumentation.TokenAuthUpdateInput(); // TokenAuthUpdateInput | Provide the details of the token authorization to update in the body of the request.
apiInstance.updateStreamTargetTokenAuth(streamTargetId, tokenAuth, (error, data, response) => {
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
 **streamTargetId** | **String**| The unique alphanumeric string that identifies the stream target. | 
 **tokenAuth** | [**TokenAuthUpdateInput**](TokenAuthUpdateInput.md)| Provide the details of the token authorization to update in the body of the request. | 

### Return type

[**ShowStreamTargetTokenAuth200Response**](ShowStreamTargetTokenAuth200Response.md)

### Authorization

[wsc-api-key](../README.md#wsc-api-key), [wsc-access-key](../README.md#wsc-access-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

