# AlerterSystemApi.TransportTelnyxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportTelnyxGetCollection**](TransportTelnyxApi.md#apiTransportTelnyxGetCollection) | **GET** /api/transport-telnyx | Retrieves the collection of TransportTelnyx resources.
[**apiTransportTelnyxIdDelete**](TransportTelnyxApi.md#apiTransportTelnyxIdDelete) | **DELETE** /api/transport-telnyx/{id} | Removes the TransportTelnyx resource.
[**apiTransportTelnyxIdGet**](TransportTelnyxApi.md#apiTransportTelnyxIdGet) | **GET** /api/transport-telnyx/{id} | Retrieves a TransportTelnyx resource.
[**apiTransportTelnyxIdPatch**](TransportTelnyxApi.md#apiTransportTelnyxIdPatch) | **PATCH** /api/transport-telnyx/{id} | Updates the TransportTelnyx resource.
[**apiTransportTelnyxIdPut**](TransportTelnyxApi.md#apiTransportTelnyxIdPut) | **PUT** /api/transport-telnyx/{id} | Replaces the TransportTelnyx resource.
[**apiTransportTelnyxPost**](TransportTelnyxApi.md#apiTransportTelnyxPost) | **POST** /api/transport-telnyx | Creates a TransportTelnyx resource.



## apiTransportTelnyxGetCollection

> [TransportTelnyxGet] apiTransportTelnyxGetCollection(opts)

Retrieves the collection of TransportTelnyx resources.

Retrieves the collection of TransportTelnyx resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelnyxApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportTelnyxGetCollection(opts, (error, data, response) => {
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

[**[TransportTelnyxGet]**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelnyxIdDelete

> apiTransportTelnyxIdDelete(id)

Removes the TransportTelnyx resource.

Removes the TransportTelnyx resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelnyxApi();
let id = "id_example"; // String | TransportTelnyx identifier
apiInstance.apiTransportTelnyxIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportTelnyx identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportTelnyxIdGet

> TransportTelnyxGet apiTransportTelnyxIdGet(id)

Retrieves a TransportTelnyx resource.

Retrieves a TransportTelnyx resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelnyxApi();
let id = "id_example"; // String | TransportTelnyx identifier
apiInstance.apiTransportTelnyxIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportTelnyx identifier | 

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelnyxIdPatch

> TransportTelnyxGet apiTransportTelnyxIdPatch(id, transportTelnyxPatch)

Updates the TransportTelnyx resource.

Updates the TransportTelnyx resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelnyxApi();
let id = "id_example"; // String | TransportTelnyx identifier
let transportTelnyxPatch = new AlerterSystemApi.TransportTelnyxPatch(); // TransportTelnyxPatch | The updated TransportTelnyx resource
apiInstance.apiTransportTelnyxIdPatch(id, transportTelnyxPatch, (error, data, response) => {
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
 **id** | **String**| TransportTelnyx identifier | 
 **transportTelnyxPatch** | [**TransportTelnyxPatch**](TransportTelnyxPatch.md)| The updated TransportTelnyx resource | 

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelnyxIdPut

> TransportTelnyxGet apiTransportTelnyxIdPut(id, transportTelnyxPut)

Replaces the TransportTelnyx resource.

Replaces the TransportTelnyx resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelnyxApi();
let id = "id_example"; // String | TransportTelnyx identifier
let transportTelnyxPut = new AlerterSystemApi.TransportTelnyxPut(); // TransportTelnyxPut | The updated TransportTelnyx resource
apiInstance.apiTransportTelnyxIdPut(id, transportTelnyxPut, (error, data, response) => {
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
 **id** | **String**| TransportTelnyx identifier | 
 **transportTelnyxPut** | [**TransportTelnyxPut**](TransportTelnyxPut.md)| The updated TransportTelnyx resource | 

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelnyxPost

> TransportTelnyxGet apiTransportTelnyxPost(transportTelnyxPost)

Creates a TransportTelnyx resource.

Creates a TransportTelnyx resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelnyxApi();
let transportTelnyxPost = new AlerterSystemApi.TransportTelnyxPost(); // TransportTelnyxPost | The new TransportTelnyx resource
apiInstance.apiTransportTelnyxPost(transportTelnyxPost, (error, data, response) => {
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
 **transportTelnyxPost** | [**TransportTelnyxPost**](TransportTelnyxPost.md)| The new TransportTelnyx resource | 

### Return type

[**TransportTelnyxGet**](TransportTelnyxGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

