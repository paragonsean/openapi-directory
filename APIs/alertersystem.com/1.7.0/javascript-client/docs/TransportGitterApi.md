# AlerterSystemApi.TransportGitterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportGitterGetCollection**](TransportGitterApi.md#apiTransportGitterGetCollection) | **GET** /api/transport-gitter | Retrieves the collection of TransportGitter resources.
[**apiTransportGitterIdDelete**](TransportGitterApi.md#apiTransportGitterIdDelete) | **DELETE** /api/transport-gitter/{id} | Removes the TransportGitter resource.
[**apiTransportGitterIdGet**](TransportGitterApi.md#apiTransportGitterIdGet) | **GET** /api/transport-gitter/{id} | Retrieves a TransportGitter resource.
[**apiTransportGitterIdPatch**](TransportGitterApi.md#apiTransportGitterIdPatch) | **PATCH** /api/transport-gitter/{id} | Updates the TransportGitter resource.
[**apiTransportGitterIdPut**](TransportGitterApi.md#apiTransportGitterIdPut) | **PUT** /api/transport-gitter/{id} | Replaces the TransportGitter resource.
[**apiTransportGitterPost**](TransportGitterApi.md#apiTransportGitterPost) | **POST** /api/transport-gitter | Creates a TransportGitter resource.



## apiTransportGitterGetCollection

> [TransportGitterGet] apiTransportGitterGetCollection(opts)

Retrieves the collection of TransportGitter resources.

Retrieves the collection of TransportGitter resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGitterApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportGitterGetCollection(opts, (error, data, response) => {
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

[**[TransportGitterGet]**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGitterIdDelete

> apiTransportGitterIdDelete(id)

Removes the TransportGitter resource.

Removes the TransportGitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGitterApi();
let id = "id_example"; // String | TransportGitter identifier
apiInstance.apiTransportGitterIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportGitter identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportGitterIdGet

> TransportGitterGet apiTransportGitterIdGet(id)

Retrieves a TransportGitter resource.

Retrieves a TransportGitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGitterApi();
let id = "id_example"; // String | TransportGitter identifier
apiInstance.apiTransportGitterIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportGitter identifier | 

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGitterIdPatch

> TransportGitterGet apiTransportGitterIdPatch(id, transportGitterPatch)

Updates the TransportGitter resource.

Updates the TransportGitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGitterApi();
let id = "id_example"; // String | TransportGitter identifier
let transportGitterPatch = new AlerterSystemApi.TransportGitterPatch(); // TransportGitterPatch | The updated TransportGitter resource
apiInstance.apiTransportGitterIdPatch(id, transportGitterPatch, (error, data, response) => {
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
 **id** | **String**| TransportGitter identifier | 
 **transportGitterPatch** | [**TransportGitterPatch**](TransportGitterPatch.md)| The updated TransportGitter resource | 

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGitterIdPut

> TransportGitterGet apiTransportGitterIdPut(id, transportGitterPut)

Replaces the TransportGitter resource.

Replaces the TransportGitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGitterApi();
let id = "id_example"; // String | TransportGitter identifier
let transportGitterPut = new AlerterSystemApi.TransportGitterPut(); // TransportGitterPut | The updated TransportGitter resource
apiInstance.apiTransportGitterIdPut(id, transportGitterPut, (error, data, response) => {
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
 **id** | **String**| TransportGitter identifier | 
 **transportGitterPut** | [**TransportGitterPut**](TransportGitterPut.md)| The updated TransportGitter resource | 

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGitterPost

> TransportGitterGet apiTransportGitterPost(transportGitterPost)

Creates a TransportGitter resource.

Creates a TransportGitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGitterApi();
let transportGitterPost = new AlerterSystemApi.TransportGitterPost(); // TransportGitterPost | The new TransportGitter resource
apiInstance.apiTransportGitterPost(transportGitterPost, (error, data, response) => {
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
 **transportGitterPost** | [**TransportGitterPost**](TransportGitterPost.md)| The new TransportGitter resource | 

### Return type

[**TransportGitterGet**](TransportGitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

