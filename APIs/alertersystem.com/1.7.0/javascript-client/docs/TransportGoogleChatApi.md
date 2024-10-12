# AlerterSystemApi.TransportGoogleChatApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportGoogleChatGetCollection**](TransportGoogleChatApi.md#apiTransportGoogleChatGetCollection) | **GET** /api/transport-google-chat | Retrieves the collection of TransportGoogleChat resources.
[**apiTransportGoogleChatIdDelete**](TransportGoogleChatApi.md#apiTransportGoogleChatIdDelete) | **DELETE** /api/transport-google-chat/{id} | Removes the TransportGoogleChat resource.
[**apiTransportGoogleChatIdGet**](TransportGoogleChatApi.md#apiTransportGoogleChatIdGet) | **GET** /api/transport-google-chat/{id} | Retrieves a TransportGoogleChat resource.
[**apiTransportGoogleChatIdPatch**](TransportGoogleChatApi.md#apiTransportGoogleChatIdPatch) | **PATCH** /api/transport-google-chat/{id} | Updates the TransportGoogleChat resource.
[**apiTransportGoogleChatIdPut**](TransportGoogleChatApi.md#apiTransportGoogleChatIdPut) | **PUT** /api/transport-google-chat/{id} | Replaces the TransportGoogleChat resource.
[**apiTransportGoogleChatPost**](TransportGoogleChatApi.md#apiTransportGoogleChatPost) | **POST** /api/transport-google-chat | Creates a TransportGoogleChat resource.



## apiTransportGoogleChatGetCollection

> [TransportGoogleChatGet] apiTransportGoogleChatGetCollection(opts)

Retrieves the collection of TransportGoogleChat resources.

Retrieves the collection of TransportGoogleChat resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGoogleChatApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportGoogleChatGetCollection(opts, (error, data, response) => {
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

[**[TransportGoogleChatGet]**](TransportGoogleChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGoogleChatIdDelete

> apiTransportGoogleChatIdDelete(id)

Removes the TransportGoogleChat resource.

Removes the TransportGoogleChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGoogleChatApi();
let id = "id_example"; // String | TransportGoogleChat identifier
apiInstance.apiTransportGoogleChatIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportGoogleChat identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportGoogleChatIdGet

> TransportGoogleChatGet apiTransportGoogleChatIdGet(id)

Retrieves a TransportGoogleChat resource.

Retrieves a TransportGoogleChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGoogleChatApi();
let id = "id_example"; // String | TransportGoogleChat identifier
apiInstance.apiTransportGoogleChatIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportGoogleChat identifier | 

### Return type

[**TransportGoogleChatGet**](TransportGoogleChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGoogleChatIdPatch

> TransportGoogleChatGet apiTransportGoogleChatIdPatch(id, transportGoogleChatPatch)

Updates the TransportGoogleChat resource.

Updates the TransportGoogleChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGoogleChatApi();
let id = "id_example"; // String | TransportGoogleChat identifier
let transportGoogleChatPatch = new AlerterSystemApi.TransportGoogleChatPatch(); // TransportGoogleChatPatch | The updated TransportGoogleChat resource
apiInstance.apiTransportGoogleChatIdPatch(id, transportGoogleChatPatch, (error, data, response) => {
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
 **id** | **String**| TransportGoogleChat identifier | 
 **transportGoogleChatPatch** | [**TransportGoogleChatPatch**](TransportGoogleChatPatch.md)| The updated TransportGoogleChat resource | 

### Return type

[**TransportGoogleChatGet**](TransportGoogleChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGoogleChatIdPut

> TransportGoogleChatGet apiTransportGoogleChatIdPut(id, transportGoogleChatPut)

Replaces the TransportGoogleChat resource.

Replaces the TransportGoogleChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGoogleChatApi();
let id = "id_example"; // String | TransportGoogleChat identifier
let transportGoogleChatPut = new AlerterSystemApi.TransportGoogleChatPut(); // TransportGoogleChatPut | The updated TransportGoogleChat resource
apiInstance.apiTransportGoogleChatIdPut(id, transportGoogleChatPut, (error, data, response) => {
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
 **id** | **String**| TransportGoogleChat identifier | 
 **transportGoogleChatPut** | [**TransportGoogleChatPut**](TransportGoogleChatPut.md)| The updated TransportGoogleChat resource | 

### Return type

[**TransportGoogleChatGet**](TransportGoogleChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGoogleChatPost

> TransportGoogleChatGet apiTransportGoogleChatPost(transportGoogleChatPost)

Creates a TransportGoogleChat resource.

Creates a TransportGoogleChat resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGoogleChatApi();
let transportGoogleChatPost = new AlerterSystemApi.TransportGoogleChatPost(); // TransportGoogleChatPost | The new TransportGoogleChat resource
apiInstance.apiTransportGoogleChatPost(transportGoogleChatPost, (error, data, response) => {
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
 **transportGoogleChatPost** | [**TransportGoogleChatPost**](TransportGoogleChatPost.md)| The new TransportGoogleChat resource | 

### Return type

[**TransportGoogleChatGet**](TransportGoogleChatGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

