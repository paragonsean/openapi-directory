# AlerterSystemApi.TransportBandwidthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportBandwidthGetCollection**](TransportBandwidthApi.md#apiTransportBandwidthGetCollection) | **GET** /api/transport-bandwidth | Retrieves the collection of TransportBandwidth resources.
[**apiTransportBandwidthIdDelete**](TransportBandwidthApi.md#apiTransportBandwidthIdDelete) | **DELETE** /api/transport-bandwidth/{id} | Removes the TransportBandwidth resource.
[**apiTransportBandwidthIdGet**](TransportBandwidthApi.md#apiTransportBandwidthIdGet) | **GET** /api/transport-bandwidth/{id} | Retrieves a TransportBandwidth resource.
[**apiTransportBandwidthIdPatch**](TransportBandwidthApi.md#apiTransportBandwidthIdPatch) | **PATCH** /api/transport-bandwidth/{id} | Updates the TransportBandwidth resource.
[**apiTransportBandwidthIdPut**](TransportBandwidthApi.md#apiTransportBandwidthIdPut) | **PUT** /api/transport-bandwidth/{id} | Replaces the TransportBandwidth resource.
[**apiTransportBandwidthPost**](TransportBandwidthApi.md#apiTransportBandwidthPost) | **POST** /api/transport-bandwidth | Creates a TransportBandwidth resource.



## apiTransportBandwidthGetCollection

> [TransportBandwidthGet] apiTransportBandwidthGetCollection(opts)

Retrieves the collection of TransportBandwidth resources.

Retrieves the collection of TransportBandwidth resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportBandwidthApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportBandwidthGetCollection(opts, (error, data, response) => {
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

[**[TransportBandwidthGet]**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportBandwidthIdDelete

> apiTransportBandwidthIdDelete(id)

Removes the TransportBandwidth resource.

Removes the TransportBandwidth resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportBandwidthApi();
let id = "id_example"; // String | TransportBandwidth identifier
apiInstance.apiTransportBandwidthIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportBandwidth identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportBandwidthIdGet

> TransportBandwidthGet apiTransportBandwidthIdGet(id)

Retrieves a TransportBandwidth resource.

Retrieves a TransportBandwidth resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportBandwidthApi();
let id = "id_example"; // String | TransportBandwidth identifier
apiInstance.apiTransportBandwidthIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportBandwidth identifier | 

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportBandwidthIdPatch

> TransportBandwidthGet apiTransportBandwidthIdPatch(id, transportBandwidthPatch)

Updates the TransportBandwidth resource.

Updates the TransportBandwidth resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportBandwidthApi();
let id = "id_example"; // String | TransportBandwidth identifier
let transportBandwidthPatch = new AlerterSystemApi.TransportBandwidthPatch(); // TransportBandwidthPatch | The updated TransportBandwidth resource
apiInstance.apiTransportBandwidthIdPatch(id, transportBandwidthPatch, (error, data, response) => {
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
 **id** | **String**| TransportBandwidth identifier | 
 **transportBandwidthPatch** | [**TransportBandwidthPatch**](TransportBandwidthPatch.md)| The updated TransportBandwidth resource | 

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportBandwidthIdPut

> TransportBandwidthGet apiTransportBandwidthIdPut(id, transportBandwidthPut)

Replaces the TransportBandwidth resource.

Replaces the TransportBandwidth resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportBandwidthApi();
let id = "id_example"; // String | TransportBandwidth identifier
let transportBandwidthPut = new AlerterSystemApi.TransportBandwidthPut(); // TransportBandwidthPut | The updated TransportBandwidth resource
apiInstance.apiTransportBandwidthIdPut(id, transportBandwidthPut, (error, data, response) => {
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
 **id** | **String**| TransportBandwidth identifier | 
 **transportBandwidthPut** | [**TransportBandwidthPut**](TransportBandwidthPut.md)| The updated TransportBandwidth resource | 

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportBandwidthPost

> TransportBandwidthGet apiTransportBandwidthPost(transportBandwidthPost)

Creates a TransportBandwidth resource.

Creates a TransportBandwidth resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportBandwidthApi();
let transportBandwidthPost = new AlerterSystemApi.TransportBandwidthPost(); // TransportBandwidthPost | The new TransportBandwidth resource
apiInstance.apiTransportBandwidthPost(transportBandwidthPost, (error, data, response) => {
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
 **transportBandwidthPost** | [**TransportBandwidthPost**](TransportBandwidthPost.md)| The new TransportBandwidth resource | 

### Return type

[**TransportBandwidthGet**](TransportBandwidthGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

