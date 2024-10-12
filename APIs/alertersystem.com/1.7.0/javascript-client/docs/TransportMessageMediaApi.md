# AlerterSystemApi.TransportMessageMediaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMessageMediaGetCollection**](TransportMessageMediaApi.md#apiTransportMessageMediaGetCollection) | **GET** /api/transport-message-media | Retrieves the collection of TransportMessageMedia resources.
[**apiTransportMessageMediaIdDelete**](TransportMessageMediaApi.md#apiTransportMessageMediaIdDelete) | **DELETE** /api/transport-message-media/{id} | Removes the TransportMessageMedia resource.
[**apiTransportMessageMediaIdGet**](TransportMessageMediaApi.md#apiTransportMessageMediaIdGet) | **GET** /api/transport-message-media/{id} | Retrieves a TransportMessageMedia resource.
[**apiTransportMessageMediaIdPatch**](TransportMessageMediaApi.md#apiTransportMessageMediaIdPatch) | **PATCH** /api/transport-message-media/{id} | Updates the TransportMessageMedia resource.
[**apiTransportMessageMediaIdPut**](TransportMessageMediaApi.md#apiTransportMessageMediaIdPut) | **PUT** /api/transport-message-media/{id} | Replaces the TransportMessageMedia resource.
[**apiTransportMessageMediaPost**](TransportMessageMediaApi.md#apiTransportMessageMediaPost) | **POST** /api/transport-message-media | Creates a TransportMessageMedia resource.



## apiTransportMessageMediaGetCollection

> [TransportMessageMediaGet] apiTransportMessageMediaGetCollection(opts)

Retrieves the collection of TransportMessageMedia resources.

Retrieves the collection of TransportMessageMedia resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageMediaApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMessageMediaGetCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] [default to 1]
 **dataSegmentCode** | **String**|  | [optional] 
 **dataSegmentCode2** | [**[String]**](String.md)|  | [optional] 
 **partition** | **String**|  | [optional] 
 **partition2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[TransportMessageMediaGet]**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageMediaIdDelete

> apiTransportMessageMediaIdDelete(id)

Removes the TransportMessageMedia resource.

Removes the TransportMessageMedia resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageMediaApi();
let id = "id_example"; // String | TransportMessageMedia identifier
apiInstance.apiTransportMessageMediaIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMessageMedia identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMessageMediaIdGet

> TransportMessageMediaGet apiTransportMessageMediaIdGet(id)

Retrieves a TransportMessageMedia resource.

Retrieves a TransportMessageMedia resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageMediaApi();
let id = "id_example"; // String | TransportMessageMedia identifier
apiInstance.apiTransportMessageMediaIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMessageMedia identifier | 

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageMediaIdPatch

> TransportMessageMediaGet apiTransportMessageMediaIdPatch(id, transportMessageMediaPatch)

Updates the TransportMessageMedia resource.

Updates the TransportMessageMedia resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageMediaApi();
let id = "id_example"; // String | TransportMessageMedia identifier
let transportMessageMediaPatch = new AlerterSystemApi.TransportMessageMediaPatch(); // TransportMessageMediaPatch | The updated TransportMessageMedia resource
apiInstance.apiTransportMessageMediaIdPatch(id, transportMessageMediaPatch, (error, data, response) => {
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
 **id** | **String**| TransportMessageMedia identifier | 
 **transportMessageMediaPatch** | [**TransportMessageMediaPatch**](TransportMessageMediaPatch.md)| The updated TransportMessageMedia resource | 

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageMediaIdPut

> TransportMessageMediaGet apiTransportMessageMediaIdPut(id, transportMessageMediaPut)

Replaces the TransportMessageMedia resource.

Replaces the TransportMessageMedia resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageMediaApi();
let id = "id_example"; // String | TransportMessageMedia identifier
let transportMessageMediaPut = new AlerterSystemApi.TransportMessageMediaPut(); // TransportMessageMediaPut | The updated TransportMessageMedia resource
apiInstance.apiTransportMessageMediaIdPut(id, transportMessageMediaPut, (error, data, response) => {
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
 **id** | **String**| TransportMessageMedia identifier | 
 **transportMessageMediaPut** | [**TransportMessageMediaPut**](TransportMessageMediaPut.md)| The updated TransportMessageMedia resource | 

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageMediaPost

> TransportMessageMediaGet apiTransportMessageMediaPost(transportMessageMediaPost)

Creates a TransportMessageMedia resource.

Creates a TransportMessageMedia resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageMediaApi();
let transportMessageMediaPost = new AlerterSystemApi.TransportMessageMediaPost(); // TransportMessageMediaPost | The new TransportMessageMedia resource
apiInstance.apiTransportMessageMediaPost(transportMessageMediaPost, (error, data, response) => {
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
 **transportMessageMediaPost** | [**TransportMessageMediaPost**](TransportMessageMediaPost.md)| The new TransportMessageMedia resource | 

### Return type

[**TransportMessageMediaGet**](TransportMessageMediaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

