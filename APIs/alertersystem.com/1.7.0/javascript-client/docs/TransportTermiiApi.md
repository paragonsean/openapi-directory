# AlerterSystemApi.TransportTermiiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportTermiiGetCollection**](TransportTermiiApi.md#apiTransportTermiiGetCollection) | **GET** /api/transport-termii | Retrieves the collection of TransportTermii resources.
[**apiTransportTermiiIdDelete**](TransportTermiiApi.md#apiTransportTermiiIdDelete) | **DELETE** /api/transport-termii/{id} | Removes the TransportTermii resource.
[**apiTransportTermiiIdGet**](TransportTermiiApi.md#apiTransportTermiiIdGet) | **GET** /api/transport-termii/{id} | Retrieves a TransportTermii resource.
[**apiTransportTermiiIdPatch**](TransportTermiiApi.md#apiTransportTermiiIdPatch) | **PATCH** /api/transport-termii/{id} | Updates the TransportTermii resource.
[**apiTransportTermiiIdPut**](TransportTermiiApi.md#apiTransportTermiiIdPut) | **PUT** /api/transport-termii/{id} | Replaces the TransportTermii resource.
[**apiTransportTermiiPost**](TransportTermiiApi.md#apiTransportTermiiPost) | **POST** /api/transport-termii | Creates a TransportTermii resource.



## apiTransportTermiiGetCollection

> [TransportTermiiGet] apiTransportTermiiGetCollection(opts)

Retrieves the collection of TransportTermii resources.

Retrieves the collection of TransportTermii resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTermiiApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportTermiiGetCollection(opts, (error, data, response) => {
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

[**[TransportTermiiGet]**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTermiiIdDelete

> apiTransportTermiiIdDelete(id)

Removes the TransportTermii resource.

Removes the TransportTermii resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTermiiApi();
let id = "id_example"; // String | TransportTermii identifier
apiInstance.apiTransportTermiiIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportTermii identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportTermiiIdGet

> TransportTermiiGet apiTransportTermiiIdGet(id)

Retrieves a TransportTermii resource.

Retrieves a TransportTermii resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTermiiApi();
let id = "id_example"; // String | TransportTermii identifier
apiInstance.apiTransportTermiiIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportTermii identifier | 

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTermiiIdPatch

> TransportTermiiGet apiTransportTermiiIdPatch(id, transportTermiiPatch)

Updates the TransportTermii resource.

Updates the TransportTermii resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTermiiApi();
let id = "id_example"; // String | TransportTermii identifier
let transportTermiiPatch = new AlerterSystemApi.TransportTermiiPatch(); // TransportTermiiPatch | The updated TransportTermii resource
apiInstance.apiTransportTermiiIdPatch(id, transportTermiiPatch, (error, data, response) => {
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
 **id** | **String**| TransportTermii identifier | 
 **transportTermiiPatch** | [**TransportTermiiPatch**](TransportTermiiPatch.md)| The updated TransportTermii resource | 

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTermiiIdPut

> TransportTermiiGet apiTransportTermiiIdPut(id, transportTermiiPut)

Replaces the TransportTermii resource.

Replaces the TransportTermii resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTermiiApi();
let id = "id_example"; // String | TransportTermii identifier
let transportTermiiPut = new AlerterSystemApi.TransportTermiiPut(); // TransportTermiiPut | The updated TransportTermii resource
apiInstance.apiTransportTermiiIdPut(id, transportTermiiPut, (error, data, response) => {
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
 **id** | **String**| TransportTermii identifier | 
 **transportTermiiPut** | [**TransportTermiiPut**](TransportTermiiPut.md)| The updated TransportTermii resource | 

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTermiiPost

> TransportTermiiGet apiTransportTermiiPost(transportTermiiPost)

Creates a TransportTermii resource.

Creates a TransportTermii resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTermiiApi();
let transportTermiiPost = new AlerterSystemApi.TransportTermiiPost(); // TransportTermiiPost | The new TransportTermii resource
apiInstance.apiTransportTermiiPost(transportTermiiPost, (error, data, response) => {
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
 **transportTermiiPost** | [**TransportTermiiPost**](TransportTermiiPost.md)| The new TransportTermii resource | 

### Return type

[**TransportTermiiGet**](TransportTermiiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

