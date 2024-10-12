# AlerterSystemApi.TransportYunpianApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportYunpianGetCollection**](TransportYunpianApi.md#apiTransportYunpianGetCollection) | **GET** /api/transport-yunpian | Retrieves the collection of TransportYunpian resources.
[**apiTransportYunpianIdDelete**](TransportYunpianApi.md#apiTransportYunpianIdDelete) | **DELETE** /api/transport-yunpian/{id} | Removes the TransportYunpian resource.
[**apiTransportYunpianIdGet**](TransportYunpianApi.md#apiTransportYunpianIdGet) | **GET** /api/transport-yunpian/{id} | Retrieves a TransportYunpian resource.
[**apiTransportYunpianIdPatch**](TransportYunpianApi.md#apiTransportYunpianIdPatch) | **PATCH** /api/transport-yunpian/{id} | Updates the TransportYunpian resource.
[**apiTransportYunpianIdPut**](TransportYunpianApi.md#apiTransportYunpianIdPut) | **PUT** /api/transport-yunpian/{id} | Replaces the TransportYunpian resource.
[**apiTransportYunpianPost**](TransportYunpianApi.md#apiTransportYunpianPost) | **POST** /api/transport-yunpian | Creates a TransportYunpian resource.



## apiTransportYunpianGetCollection

> [TransportYunpianGet] apiTransportYunpianGetCollection(opts)

Retrieves the collection of TransportYunpian resources.

Retrieves the collection of TransportYunpian resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportYunpianApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportYunpianGetCollection(opts, (error, data, response) => {
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

[**[TransportYunpianGet]**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportYunpianIdDelete

> apiTransportYunpianIdDelete(id)

Removes the TransportYunpian resource.

Removes the TransportYunpian resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportYunpianApi();
let id = "id_example"; // String | TransportYunpian identifier
apiInstance.apiTransportYunpianIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportYunpian identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportYunpianIdGet

> TransportYunpianGet apiTransportYunpianIdGet(id)

Retrieves a TransportYunpian resource.

Retrieves a TransportYunpian resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportYunpianApi();
let id = "id_example"; // String | TransportYunpian identifier
apiInstance.apiTransportYunpianIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportYunpian identifier | 

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportYunpianIdPatch

> TransportYunpianGet apiTransportYunpianIdPatch(id, transportYunpianPatch)

Updates the TransportYunpian resource.

Updates the TransportYunpian resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportYunpianApi();
let id = "id_example"; // String | TransportYunpian identifier
let transportYunpianPatch = new AlerterSystemApi.TransportYunpianPatch(); // TransportYunpianPatch | The updated TransportYunpian resource
apiInstance.apiTransportYunpianIdPatch(id, transportYunpianPatch, (error, data, response) => {
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
 **id** | **String**| TransportYunpian identifier | 
 **transportYunpianPatch** | [**TransportYunpianPatch**](TransportYunpianPatch.md)| The updated TransportYunpian resource | 

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportYunpianIdPut

> TransportYunpianGet apiTransportYunpianIdPut(id, transportYunpianPut)

Replaces the TransportYunpian resource.

Replaces the TransportYunpian resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportYunpianApi();
let id = "id_example"; // String | TransportYunpian identifier
let transportYunpianPut = new AlerterSystemApi.TransportYunpianPut(); // TransportYunpianPut | The updated TransportYunpian resource
apiInstance.apiTransportYunpianIdPut(id, transportYunpianPut, (error, data, response) => {
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
 **id** | **String**| TransportYunpian identifier | 
 **transportYunpianPut** | [**TransportYunpianPut**](TransportYunpianPut.md)| The updated TransportYunpian resource | 

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportYunpianPost

> TransportYunpianGet apiTransportYunpianPost(transportYunpianPost)

Creates a TransportYunpian resource.

Creates a TransportYunpian resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportYunpianApi();
let transportYunpianPost = new AlerterSystemApi.TransportYunpianPost(); // TransportYunpianPost | The new TransportYunpian resource
apiInstance.apiTransportYunpianPost(transportYunpianPost, (error, data, response) => {
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
 **transportYunpianPost** | [**TransportYunpianPost**](TransportYunpianPost.md)| The new TransportYunpian resource | 

### Return type

[**TransportYunpianGet**](TransportYunpianGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

