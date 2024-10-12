# AlerterSystemApi.TransportRocketChatApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportRocketChatGetCollection**](TransportRocketChatApi.md#apiTransportRocketChatGetCollection) | **GET** /api/transport-rocket-chat | Retrieves the collection of TransportRocketChat resources.
[**apiTransportRocketChatIdDelete**](TransportRocketChatApi.md#apiTransportRocketChatIdDelete) | **DELETE** /api/transport-rocket-chat/{id} | Removes the TransportRocketChat resource.
[**apiTransportRocketChatIdGet**](TransportRocketChatApi.md#apiTransportRocketChatIdGet) | **GET** /api/transport-rocket-chat/{id} | Retrieves a TransportRocketChat resource.
[**apiTransportRocketChatIdPatch**](TransportRocketChatApi.md#apiTransportRocketChatIdPatch) | **PATCH** /api/transport-rocket-chat/{id} | Updates the TransportRocketChat resource.
[**apiTransportRocketChatIdPut**](TransportRocketChatApi.md#apiTransportRocketChatIdPut) | **PUT** /api/transport-rocket-chat/{id} | Replaces the TransportRocketChat resource.
[**apiTransportRocketChatPost**](TransportRocketChatApi.md#apiTransportRocketChatPost) | **POST** /api/transport-rocket-chat | Creates a TransportRocketChat resource.



## apiTransportRocketChatGetCollection

> [TransportRocketChatGet] apiTransportRocketChatGetCollection(opts)

Retrieves the collection of TransportRocketChat resources.

Retrieves the collection of TransportRocketChat resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRocketChatApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportRocketChatGetCollection(opts, (error, data, response) => {
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

[**[TransportRocketChatGet]**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRocketChatIdDelete

> apiTransportRocketChatIdDelete(id)

Removes the TransportRocketChat resource.

Removes the TransportRocketChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRocketChatApi();
let id = "id_example"; // String | TransportRocketChat identifier
apiInstance.apiTransportRocketChatIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportRocketChat identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportRocketChatIdGet

> TransportRocketChatGet apiTransportRocketChatIdGet(id)

Retrieves a TransportRocketChat resource.

Retrieves a TransportRocketChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRocketChatApi();
let id = "id_example"; // String | TransportRocketChat identifier
apiInstance.apiTransportRocketChatIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportRocketChat identifier | 

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRocketChatIdPatch

> TransportRocketChatGet apiTransportRocketChatIdPatch(id, transportRocketChatPatch)

Updates the TransportRocketChat resource.

Updates the TransportRocketChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRocketChatApi();
let id = "id_example"; // String | TransportRocketChat identifier
let transportRocketChatPatch = new AlerterSystemApi.TransportRocketChatPatch(); // TransportRocketChatPatch | The updated TransportRocketChat resource
apiInstance.apiTransportRocketChatIdPatch(id, transportRocketChatPatch, (error, data, response) => {
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
 **id** | **String**| TransportRocketChat identifier | 
 **transportRocketChatPatch** | [**TransportRocketChatPatch**](TransportRocketChatPatch.md)| The updated TransportRocketChat resource | 

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRocketChatIdPut

> TransportRocketChatGet apiTransportRocketChatIdPut(id, transportRocketChatPut)

Replaces the TransportRocketChat resource.

Replaces the TransportRocketChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRocketChatApi();
let id = "id_example"; // String | TransportRocketChat identifier
let transportRocketChatPut = new AlerterSystemApi.TransportRocketChatPut(); // TransportRocketChatPut | The updated TransportRocketChat resource
apiInstance.apiTransportRocketChatIdPut(id, transportRocketChatPut, (error, data, response) => {
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
 **id** | **String**| TransportRocketChat identifier | 
 **transportRocketChatPut** | [**TransportRocketChatPut**](TransportRocketChatPut.md)| The updated TransportRocketChat resource | 

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRocketChatPost

> TransportRocketChatGet apiTransportRocketChatPost(transportRocketChatPost)

Creates a TransportRocketChat resource.

Creates a TransportRocketChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRocketChatApi();
let transportRocketChatPost = new AlerterSystemApi.TransportRocketChatPost(); // TransportRocketChatPost | The new TransportRocketChat resource
apiInstance.apiTransportRocketChatPost(transportRocketChatPost, (error, data, response) => {
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
 **transportRocketChatPost** | [**TransportRocketChatPost**](TransportRocketChatPost.md)| The new TransportRocketChat resource | 

### Return type

[**TransportRocketChatGet**](TransportRocketChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

