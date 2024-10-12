# AlerterSystemApi.TransportMessageBirdApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMessageBirdGetCollection**](TransportMessageBirdApi.md#apiTransportMessageBirdGetCollection) | **GET** /api/transport-message-bird | Retrieves the collection of TransportMessageBird resources.
[**apiTransportMessageBirdIdDelete**](TransportMessageBirdApi.md#apiTransportMessageBirdIdDelete) | **DELETE** /api/transport-message-bird/{id} | Removes the TransportMessageBird resource.
[**apiTransportMessageBirdIdGet**](TransportMessageBirdApi.md#apiTransportMessageBirdIdGet) | **GET** /api/transport-message-bird/{id} | Retrieves a TransportMessageBird resource.
[**apiTransportMessageBirdIdPatch**](TransportMessageBirdApi.md#apiTransportMessageBirdIdPatch) | **PATCH** /api/transport-message-bird/{id} | Updates the TransportMessageBird resource.
[**apiTransportMessageBirdIdPut**](TransportMessageBirdApi.md#apiTransportMessageBirdIdPut) | **PUT** /api/transport-message-bird/{id} | Replaces the TransportMessageBird resource.
[**apiTransportMessageBirdPost**](TransportMessageBirdApi.md#apiTransportMessageBirdPost) | **POST** /api/transport-message-bird | Creates a TransportMessageBird resource.



## apiTransportMessageBirdGetCollection

> [TransportMessageBirdGet] apiTransportMessageBirdGetCollection(opts)

Retrieves the collection of TransportMessageBird resources.

Retrieves the collection of TransportMessageBird resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageBirdApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMessageBirdGetCollection(opts, (error, data, response) => {
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

[**[TransportMessageBirdGet]**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageBirdIdDelete

> apiTransportMessageBirdIdDelete(id)

Removes the TransportMessageBird resource.

Removes the TransportMessageBird resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageBirdApi();
let id = "id_example"; // String | TransportMessageBird identifier
apiInstance.apiTransportMessageBirdIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMessageBird identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMessageBirdIdGet

> TransportMessageBirdGet apiTransportMessageBirdIdGet(id)

Retrieves a TransportMessageBird resource.

Retrieves a TransportMessageBird resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageBirdApi();
let id = "id_example"; // String | TransportMessageBird identifier
apiInstance.apiTransportMessageBirdIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMessageBird identifier | 

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageBirdIdPatch

> TransportMessageBirdGet apiTransportMessageBirdIdPatch(id, transportMessageBirdPatch)

Updates the TransportMessageBird resource.

Updates the TransportMessageBird resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageBirdApi();
let id = "id_example"; // String | TransportMessageBird identifier
let transportMessageBirdPatch = new AlerterSystemApi.TransportMessageBirdPatch(); // TransportMessageBirdPatch | The updated TransportMessageBird resource
apiInstance.apiTransportMessageBirdIdPatch(id, transportMessageBirdPatch, (error, data, response) => {
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
 **id** | **String**| TransportMessageBird identifier | 
 **transportMessageBirdPatch** | [**TransportMessageBirdPatch**](TransportMessageBirdPatch.md)| The updated TransportMessageBird resource | 

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageBirdIdPut

> TransportMessageBirdGet apiTransportMessageBirdIdPut(id, transportMessageBirdPut)

Replaces the TransportMessageBird resource.

Replaces the TransportMessageBird resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageBirdApi();
let id = "id_example"; // String | TransportMessageBird identifier
let transportMessageBirdPut = new AlerterSystemApi.TransportMessageBirdPut(); // TransportMessageBirdPut | The updated TransportMessageBird resource
apiInstance.apiTransportMessageBirdIdPut(id, transportMessageBirdPut, (error, data, response) => {
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
 **id** | **String**| TransportMessageBird identifier | 
 **transportMessageBirdPut** | [**TransportMessageBirdPut**](TransportMessageBirdPut.md)| The updated TransportMessageBird resource | 

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMessageBirdPost

> TransportMessageBirdGet apiTransportMessageBirdPost(transportMessageBirdPost)

Creates a TransportMessageBird resource.

Creates a TransportMessageBird resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMessageBirdApi();
let transportMessageBirdPost = new AlerterSystemApi.TransportMessageBirdPost(); // TransportMessageBirdPost | The new TransportMessageBird resource
apiInstance.apiTransportMessageBirdPost(transportMessageBirdPost, (error, data, response) => {
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
 **transportMessageBirdPost** | [**TransportMessageBirdPost**](TransportMessageBirdPost.md)| The new TransportMessageBird resource | 

### Return type

[**TransportMessageBirdGet**](TransportMessageBirdGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

