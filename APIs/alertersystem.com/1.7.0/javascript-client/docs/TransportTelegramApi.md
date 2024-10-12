# AlerterSystemApi.TransportTelegramApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportTelegramGetCollection**](TransportTelegramApi.md#apiTransportTelegramGetCollection) | **GET** /api/transport-telegram | Retrieves the collection of TransportTelegram resources.
[**apiTransportTelegramIdDelete**](TransportTelegramApi.md#apiTransportTelegramIdDelete) | **DELETE** /api/transport-telegram/{id} | Removes the TransportTelegram resource.
[**apiTransportTelegramIdGet**](TransportTelegramApi.md#apiTransportTelegramIdGet) | **GET** /api/transport-telegram/{id} | Retrieves a TransportTelegram resource.
[**apiTransportTelegramIdPatch**](TransportTelegramApi.md#apiTransportTelegramIdPatch) | **PATCH** /api/transport-telegram/{id} | Updates the TransportTelegram resource.
[**apiTransportTelegramIdPut**](TransportTelegramApi.md#apiTransportTelegramIdPut) | **PUT** /api/transport-telegram/{id} | Replaces the TransportTelegram resource.
[**apiTransportTelegramPost**](TransportTelegramApi.md#apiTransportTelegramPost) | **POST** /api/transport-telegram | Creates a TransportTelegram resource.



## apiTransportTelegramGetCollection

> [TransportTelegramGet] apiTransportTelegramGetCollection(opts)

Retrieves the collection of TransportTelegram resources.

Retrieves the collection of TransportTelegram resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelegramApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportTelegramGetCollection(opts, (error, data, response) => {
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

[**[TransportTelegramGet]**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelegramIdDelete

> apiTransportTelegramIdDelete(id)

Removes the TransportTelegram resource.

Removes the TransportTelegram resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelegramApi();
let id = "id_example"; // String | TransportTelegram identifier
apiInstance.apiTransportTelegramIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportTelegram identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportTelegramIdGet

> TransportTelegramGet apiTransportTelegramIdGet(id)

Retrieves a TransportTelegram resource.

Retrieves a TransportTelegram resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelegramApi();
let id = "id_example"; // String | TransportTelegram identifier
apiInstance.apiTransportTelegramIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportTelegram identifier | 

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelegramIdPatch

> TransportTelegramGet apiTransportTelegramIdPatch(id, transportTelegramPatch)

Updates the TransportTelegram resource.

Updates the TransportTelegram resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelegramApi();
let id = "id_example"; // String | TransportTelegram identifier
let transportTelegramPatch = new AlerterSystemApi.TransportTelegramPatch(); // TransportTelegramPatch | The updated TransportTelegram resource
apiInstance.apiTransportTelegramIdPatch(id, transportTelegramPatch, (error, data, response) => {
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
 **id** | **String**| TransportTelegram identifier | 
 **transportTelegramPatch** | [**TransportTelegramPatch**](TransportTelegramPatch.md)| The updated TransportTelegram resource | 

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelegramIdPut

> TransportTelegramGet apiTransportTelegramIdPut(id, transportTelegramPut)

Replaces the TransportTelegram resource.

Replaces the TransportTelegram resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelegramApi();
let id = "id_example"; // String | TransportTelegram identifier
let transportTelegramPut = new AlerterSystemApi.TransportTelegramPut(); // TransportTelegramPut | The updated TransportTelegram resource
apiInstance.apiTransportTelegramIdPut(id, transportTelegramPut, (error, data, response) => {
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
 **id** | **String**| TransportTelegram identifier | 
 **transportTelegramPut** | [**TransportTelegramPut**](TransportTelegramPut.md)| The updated TransportTelegram resource | 

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTelegramPost

> TransportTelegramGet apiTransportTelegramPost(transportTelegramPost)

Creates a TransportTelegram resource.

Creates a TransportTelegram resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTelegramApi();
let transportTelegramPost = new AlerterSystemApi.TransportTelegramPost(); // TransportTelegramPost | The new TransportTelegram resource
apiInstance.apiTransportTelegramPost(transportTelegramPost, (error, data, response) => {
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
 **transportTelegramPost** | [**TransportTelegramPost**](TransportTelegramPost.md)| The new TransportTelegram resource | 

### Return type

[**TransportTelegramGet**](TransportTelegramGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

