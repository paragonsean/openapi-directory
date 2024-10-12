# AlerterSystemApi.TransportSinchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSinchGetCollection**](TransportSinchApi.md#apiTransportSinchGetCollection) | **GET** /api/transport-sinch | Retrieves the collection of TransportSinch resources.
[**apiTransportSinchIdDelete**](TransportSinchApi.md#apiTransportSinchIdDelete) | **DELETE** /api/transport-sinch/{id} | Removes the TransportSinch resource.
[**apiTransportSinchIdGet**](TransportSinchApi.md#apiTransportSinchIdGet) | **GET** /api/transport-sinch/{id} | Retrieves a TransportSinch resource.
[**apiTransportSinchIdPatch**](TransportSinchApi.md#apiTransportSinchIdPatch) | **PATCH** /api/transport-sinch/{id} | Updates the TransportSinch resource.
[**apiTransportSinchIdPut**](TransportSinchApi.md#apiTransportSinchIdPut) | **PUT** /api/transport-sinch/{id} | Replaces the TransportSinch resource.
[**apiTransportSinchPost**](TransportSinchApi.md#apiTransportSinchPost) | **POST** /api/transport-sinch | Creates a TransportSinch resource.



## apiTransportSinchGetCollection

> [TransportSinchGet] apiTransportSinchGetCollection(opts)

Retrieves the collection of TransportSinch resources.

Retrieves the collection of TransportSinch resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSinchApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSinchGetCollection(opts, (error, data, response) => {
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

[**[TransportSinchGet]**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSinchIdDelete

> apiTransportSinchIdDelete(id)

Removes the TransportSinch resource.

Removes the TransportSinch resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSinchApi();
let id = "id_example"; // String | TransportSinch identifier
apiInstance.apiTransportSinchIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSinch identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSinchIdGet

> TransportSinchGet apiTransportSinchIdGet(id)

Retrieves a TransportSinch resource.

Retrieves a TransportSinch resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSinchApi();
let id = "id_example"; // String | TransportSinch identifier
apiInstance.apiTransportSinchIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSinch identifier | 

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSinchIdPatch

> TransportSinchGet apiTransportSinchIdPatch(id, transportSinchPatch)

Updates the TransportSinch resource.

Updates the TransportSinch resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSinchApi();
let id = "id_example"; // String | TransportSinch identifier
let transportSinchPatch = new AlerterSystemApi.TransportSinchPatch(); // TransportSinchPatch | The updated TransportSinch resource
apiInstance.apiTransportSinchIdPatch(id, transportSinchPatch, (error, data, response) => {
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
 **id** | **String**| TransportSinch identifier | 
 **transportSinchPatch** | [**TransportSinchPatch**](TransportSinchPatch.md)| The updated TransportSinch resource | 

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSinchIdPut

> TransportSinchGet apiTransportSinchIdPut(id, transportSinchPut)

Replaces the TransportSinch resource.

Replaces the TransportSinch resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSinchApi();
let id = "id_example"; // String | TransportSinch identifier
let transportSinchPut = new AlerterSystemApi.TransportSinchPut(); // TransportSinchPut | The updated TransportSinch resource
apiInstance.apiTransportSinchIdPut(id, transportSinchPut, (error, data, response) => {
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
 **id** | **String**| TransportSinch identifier | 
 **transportSinchPut** | [**TransportSinchPut**](TransportSinchPut.md)| The updated TransportSinch resource | 

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSinchPost

> TransportSinchGet apiTransportSinchPost(transportSinchPost)

Creates a TransportSinch resource.

Creates a TransportSinch resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSinchApi();
let transportSinchPost = new AlerterSystemApi.TransportSinchPost(); // TransportSinchPost | The new TransportSinch resource
apiInstance.apiTransportSinchPost(transportSinchPost, (error, data, response) => {
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
 **transportSinchPost** | [**TransportSinchPost**](TransportSinchPost.md)| The new TransportSinch resource | 

### Return type

[**TransportSinchGet**](TransportSinchGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

