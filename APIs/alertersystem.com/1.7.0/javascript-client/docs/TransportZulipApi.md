# AlerterSystemApi.TransportZulipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportZulipGetCollection**](TransportZulipApi.md#apiTransportZulipGetCollection) | **GET** /api/transport-zulip | Retrieves the collection of TransportZulip resources.
[**apiTransportZulipIdDelete**](TransportZulipApi.md#apiTransportZulipIdDelete) | **DELETE** /api/transport-zulip/{id} | Removes the TransportZulip resource.
[**apiTransportZulipIdGet**](TransportZulipApi.md#apiTransportZulipIdGet) | **GET** /api/transport-zulip/{id} | Retrieves a TransportZulip resource.
[**apiTransportZulipIdPatch**](TransportZulipApi.md#apiTransportZulipIdPatch) | **PATCH** /api/transport-zulip/{id} | Updates the TransportZulip resource.
[**apiTransportZulipIdPut**](TransportZulipApi.md#apiTransportZulipIdPut) | **PUT** /api/transport-zulip/{id} | Replaces the TransportZulip resource.
[**apiTransportZulipPost**](TransportZulipApi.md#apiTransportZulipPost) | **POST** /api/transport-zulip | Creates a TransportZulip resource.



## apiTransportZulipGetCollection

> [TransportZulipGet] apiTransportZulipGetCollection(opts)

Retrieves the collection of TransportZulip resources.

Retrieves the collection of TransportZulip resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZulipApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportZulipGetCollection(opts, (error, data, response) => {
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

[**[TransportZulipGet]**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZulipIdDelete

> apiTransportZulipIdDelete(id)

Removes the TransportZulip resource.

Removes the TransportZulip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZulipApi();
let id = "id_example"; // String | TransportZulip identifier
apiInstance.apiTransportZulipIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportZulip identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportZulipIdGet

> TransportZulipGet apiTransportZulipIdGet(id)

Retrieves a TransportZulip resource.

Retrieves a TransportZulip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZulipApi();
let id = "id_example"; // String | TransportZulip identifier
apiInstance.apiTransportZulipIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportZulip identifier | 

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZulipIdPatch

> TransportZulipGet apiTransportZulipIdPatch(id, transportZulipPatch)

Updates the TransportZulip resource.

Updates the TransportZulip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZulipApi();
let id = "id_example"; // String | TransportZulip identifier
let transportZulipPatch = new AlerterSystemApi.TransportZulipPatch(); // TransportZulipPatch | The updated TransportZulip resource
apiInstance.apiTransportZulipIdPatch(id, transportZulipPatch, (error, data, response) => {
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
 **id** | **String**| TransportZulip identifier | 
 **transportZulipPatch** | [**TransportZulipPatch**](TransportZulipPatch.md)| The updated TransportZulip resource | 

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZulipIdPut

> TransportZulipGet apiTransportZulipIdPut(id, transportZulipPut)

Replaces the TransportZulip resource.

Replaces the TransportZulip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZulipApi();
let id = "id_example"; // String | TransportZulip identifier
let transportZulipPut = new AlerterSystemApi.TransportZulipPut(); // TransportZulipPut | The updated TransportZulip resource
apiInstance.apiTransportZulipIdPut(id, transportZulipPut, (error, data, response) => {
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
 **id** | **String**| TransportZulip identifier | 
 **transportZulipPut** | [**TransportZulipPut**](TransportZulipPut.md)| The updated TransportZulip resource | 

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZulipPost

> TransportZulipGet apiTransportZulipPost(transportZulipPost)

Creates a TransportZulip resource.

Creates a TransportZulip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZulipApi();
let transportZulipPost = new AlerterSystemApi.TransportZulipPost(); // TransportZulipPost | The new TransportZulip resource
apiInstance.apiTransportZulipPost(transportZulipPost, (error, data, response) => {
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
 **transportZulipPost** | [**TransportZulipPost**](TransportZulipPost.md)| The new TransportZulip resource | 

### Return type

[**TransportZulipGet**](TransportZulipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

