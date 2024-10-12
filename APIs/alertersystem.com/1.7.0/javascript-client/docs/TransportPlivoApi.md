# AlerterSystemApi.TransportPlivoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportPlivoGetCollection**](TransportPlivoApi.md#apiTransportPlivoGetCollection) | **GET** /api/transport-plivo | Retrieves the collection of TransportPlivo resources.
[**apiTransportPlivoIdDelete**](TransportPlivoApi.md#apiTransportPlivoIdDelete) | **DELETE** /api/transport-plivo/{id} | Removes the TransportPlivo resource.
[**apiTransportPlivoIdGet**](TransportPlivoApi.md#apiTransportPlivoIdGet) | **GET** /api/transport-plivo/{id} | Retrieves a TransportPlivo resource.
[**apiTransportPlivoIdPatch**](TransportPlivoApi.md#apiTransportPlivoIdPatch) | **PATCH** /api/transport-plivo/{id} | Updates the TransportPlivo resource.
[**apiTransportPlivoIdPut**](TransportPlivoApi.md#apiTransportPlivoIdPut) | **PUT** /api/transport-plivo/{id} | Replaces the TransportPlivo resource.
[**apiTransportPlivoPost**](TransportPlivoApi.md#apiTransportPlivoPost) | **POST** /api/transport-plivo | Creates a TransportPlivo resource.



## apiTransportPlivoGetCollection

> [TransportPlivoGet] apiTransportPlivoGetCollection(opts)

Retrieves the collection of TransportPlivo resources.

Retrieves the collection of TransportPlivo resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPlivoApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportPlivoGetCollection(opts, (error, data, response) => {
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

[**[TransportPlivoGet]**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPlivoIdDelete

> apiTransportPlivoIdDelete(id)

Removes the TransportPlivo resource.

Removes the TransportPlivo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPlivoApi();
let id = "id_example"; // String | TransportPlivo identifier
apiInstance.apiTransportPlivoIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportPlivo identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportPlivoIdGet

> TransportPlivoGet apiTransportPlivoIdGet(id)

Retrieves a TransportPlivo resource.

Retrieves a TransportPlivo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPlivoApi();
let id = "id_example"; // String | TransportPlivo identifier
apiInstance.apiTransportPlivoIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportPlivo identifier | 

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPlivoIdPatch

> TransportPlivoGet apiTransportPlivoIdPatch(id, transportPlivoPatch)

Updates the TransportPlivo resource.

Updates the TransportPlivo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPlivoApi();
let id = "id_example"; // String | TransportPlivo identifier
let transportPlivoPatch = new AlerterSystemApi.TransportPlivoPatch(); // TransportPlivoPatch | The updated TransportPlivo resource
apiInstance.apiTransportPlivoIdPatch(id, transportPlivoPatch, (error, data, response) => {
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
 **id** | **String**| TransportPlivo identifier | 
 **transportPlivoPatch** | [**TransportPlivoPatch**](TransportPlivoPatch.md)| The updated TransportPlivo resource | 

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPlivoIdPut

> TransportPlivoGet apiTransportPlivoIdPut(id, transportPlivoPut)

Replaces the TransportPlivo resource.

Replaces the TransportPlivo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPlivoApi();
let id = "id_example"; // String | TransportPlivo identifier
let transportPlivoPut = new AlerterSystemApi.TransportPlivoPut(); // TransportPlivoPut | The updated TransportPlivo resource
apiInstance.apiTransportPlivoIdPut(id, transportPlivoPut, (error, data, response) => {
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
 **id** | **String**| TransportPlivo identifier | 
 **transportPlivoPut** | [**TransportPlivoPut**](TransportPlivoPut.md)| The updated TransportPlivo resource | 

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPlivoPost

> TransportPlivoGet apiTransportPlivoPost(transportPlivoPost)

Creates a TransportPlivo resource.

Creates a TransportPlivo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPlivoApi();
let transportPlivoPost = new AlerterSystemApi.TransportPlivoPost(); // TransportPlivoPost | The new TransportPlivo resource
apiInstance.apiTransportPlivoPost(transportPlivoPost, (error, data, response) => {
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
 **transportPlivoPost** | [**TransportPlivoPost**](TransportPlivoPost.md)| The new TransportPlivo resource | 

### Return type

[**TransportPlivoGet**](TransportPlivoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

