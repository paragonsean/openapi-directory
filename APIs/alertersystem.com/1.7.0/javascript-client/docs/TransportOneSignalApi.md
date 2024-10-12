# AlerterSystemApi.TransportOneSignalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportOneSignalGetCollection**](TransportOneSignalApi.md#apiTransportOneSignalGetCollection) | **GET** /api/transport-one-signal | Retrieves the collection of TransportOneSignal resources.
[**apiTransportOneSignalIdDelete**](TransportOneSignalApi.md#apiTransportOneSignalIdDelete) | **DELETE** /api/transport-one-signal/{id} | Removes the TransportOneSignal resource.
[**apiTransportOneSignalIdGet**](TransportOneSignalApi.md#apiTransportOneSignalIdGet) | **GET** /api/transport-one-signal/{id} | Retrieves a TransportOneSignal resource.
[**apiTransportOneSignalIdPatch**](TransportOneSignalApi.md#apiTransportOneSignalIdPatch) | **PATCH** /api/transport-one-signal/{id} | Updates the TransportOneSignal resource.
[**apiTransportOneSignalIdPut**](TransportOneSignalApi.md#apiTransportOneSignalIdPut) | **PUT** /api/transport-one-signal/{id} | Replaces the TransportOneSignal resource.
[**apiTransportOneSignalPost**](TransportOneSignalApi.md#apiTransportOneSignalPost) | **POST** /api/transport-one-signal | Creates a TransportOneSignal resource.



## apiTransportOneSignalGetCollection

> [TransportOneSignalGet] apiTransportOneSignalGetCollection(opts)

Retrieves the collection of TransportOneSignal resources.

Retrieves the collection of TransportOneSignal resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOneSignalApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportOneSignalGetCollection(opts, (error, data, response) => {
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

[**[TransportOneSignalGet]**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOneSignalIdDelete

> apiTransportOneSignalIdDelete(id)

Removes the TransportOneSignal resource.

Removes the TransportOneSignal resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOneSignalApi();
let id = "id_example"; // String | TransportOneSignal identifier
apiInstance.apiTransportOneSignalIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportOneSignal identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportOneSignalIdGet

> TransportOneSignalGet apiTransportOneSignalIdGet(id)

Retrieves a TransportOneSignal resource.

Retrieves a TransportOneSignal resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOneSignalApi();
let id = "id_example"; // String | TransportOneSignal identifier
apiInstance.apiTransportOneSignalIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportOneSignal identifier | 

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOneSignalIdPatch

> TransportOneSignalGet apiTransportOneSignalIdPatch(id, transportOneSignalPatch)

Updates the TransportOneSignal resource.

Updates the TransportOneSignal resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOneSignalApi();
let id = "id_example"; // String | TransportOneSignal identifier
let transportOneSignalPatch = new AlerterSystemApi.TransportOneSignalPatch(); // TransportOneSignalPatch | The updated TransportOneSignal resource
apiInstance.apiTransportOneSignalIdPatch(id, transportOneSignalPatch, (error, data, response) => {
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
 **id** | **String**| TransportOneSignal identifier | 
 **transportOneSignalPatch** | [**TransportOneSignalPatch**](TransportOneSignalPatch.md)| The updated TransportOneSignal resource | 

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOneSignalIdPut

> TransportOneSignalGet apiTransportOneSignalIdPut(id, transportOneSignalPut)

Replaces the TransportOneSignal resource.

Replaces the TransportOneSignal resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOneSignalApi();
let id = "id_example"; // String | TransportOneSignal identifier
let transportOneSignalPut = new AlerterSystemApi.TransportOneSignalPut(); // TransportOneSignalPut | The updated TransportOneSignal resource
apiInstance.apiTransportOneSignalIdPut(id, transportOneSignalPut, (error, data, response) => {
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
 **id** | **String**| TransportOneSignal identifier | 
 **transportOneSignalPut** | [**TransportOneSignalPut**](TransportOneSignalPut.md)| The updated TransportOneSignal resource | 

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOneSignalPost

> TransportOneSignalGet apiTransportOneSignalPost(transportOneSignalPost)

Creates a TransportOneSignal resource.

Creates a TransportOneSignal resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOneSignalApi();
let transportOneSignalPost = new AlerterSystemApi.TransportOneSignalPost(); // TransportOneSignalPost | The new TransportOneSignal resource
apiInstance.apiTransportOneSignalPost(transportOneSignalPost, (error, data, response) => {
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
 **transportOneSignalPost** | [**TransportOneSignalPost**](TransportOneSignalPost.md)| The new TransportOneSignal resource | 

### Return type

[**TransportOneSignalGet**](TransportOneSignalGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

