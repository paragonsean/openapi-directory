# AlerterSystemApi.TransportInfobipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportInfobipGetCollection**](TransportInfobipApi.md#apiTransportInfobipGetCollection) | **GET** /api/transport-infobip | Retrieves the collection of TransportInfobip resources.
[**apiTransportInfobipIdDelete**](TransportInfobipApi.md#apiTransportInfobipIdDelete) | **DELETE** /api/transport-infobip/{id} | Removes the TransportInfobip resource.
[**apiTransportInfobipIdGet**](TransportInfobipApi.md#apiTransportInfobipIdGet) | **GET** /api/transport-infobip/{id} | Retrieves a TransportInfobip resource.
[**apiTransportInfobipIdPatch**](TransportInfobipApi.md#apiTransportInfobipIdPatch) | **PATCH** /api/transport-infobip/{id} | Updates the TransportInfobip resource.
[**apiTransportInfobipIdPut**](TransportInfobipApi.md#apiTransportInfobipIdPut) | **PUT** /api/transport-infobip/{id} | Replaces the TransportInfobip resource.
[**apiTransportInfobipPost**](TransportInfobipApi.md#apiTransportInfobipPost) | **POST** /api/transport-infobip | Creates a TransportInfobip resource.



## apiTransportInfobipGetCollection

> [TransportInfobipGet] apiTransportInfobipGetCollection(opts)

Retrieves the collection of TransportInfobip resources.

Retrieves the collection of TransportInfobip resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportInfobipApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportInfobipGetCollection(opts, (error, data, response) => {
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

[**[TransportInfobipGet]**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportInfobipIdDelete

> apiTransportInfobipIdDelete(id)

Removes the TransportInfobip resource.

Removes the TransportInfobip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportInfobipApi();
let id = "id_example"; // String | TransportInfobip identifier
apiInstance.apiTransportInfobipIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportInfobip identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportInfobipIdGet

> TransportInfobipGet apiTransportInfobipIdGet(id)

Retrieves a TransportInfobip resource.

Retrieves a TransportInfobip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportInfobipApi();
let id = "id_example"; // String | TransportInfobip identifier
apiInstance.apiTransportInfobipIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportInfobip identifier | 

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportInfobipIdPatch

> TransportInfobipGet apiTransportInfobipIdPatch(id, transportInfobipPatch)

Updates the TransportInfobip resource.

Updates the TransportInfobip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportInfobipApi();
let id = "id_example"; // String | TransportInfobip identifier
let transportInfobipPatch = new AlerterSystemApi.TransportInfobipPatch(); // TransportInfobipPatch | The updated TransportInfobip resource
apiInstance.apiTransportInfobipIdPatch(id, transportInfobipPatch, (error, data, response) => {
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
 **id** | **String**| TransportInfobip identifier | 
 **transportInfobipPatch** | [**TransportInfobipPatch**](TransportInfobipPatch.md)| The updated TransportInfobip resource | 

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportInfobipIdPut

> TransportInfobipGet apiTransportInfobipIdPut(id, transportInfobipPut)

Replaces the TransportInfobip resource.

Replaces the TransportInfobip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportInfobipApi();
let id = "id_example"; // String | TransportInfobip identifier
let transportInfobipPut = new AlerterSystemApi.TransportInfobipPut(); // TransportInfobipPut | The updated TransportInfobip resource
apiInstance.apiTransportInfobipIdPut(id, transportInfobipPut, (error, data, response) => {
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
 **id** | **String**| TransportInfobip identifier | 
 **transportInfobipPut** | [**TransportInfobipPut**](TransportInfobipPut.md)| The updated TransportInfobip resource | 

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportInfobipPost

> TransportInfobipGet apiTransportInfobipPost(transportInfobipPost)

Creates a TransportInfobip resource.

Creates a TransportInfobip resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportInfobipApi();
let transportInfobipPost = new AlerterSystemApi.TransportInfobipPost(); // TransportInfobipPost | The new TransportInfobip resource
apiInstance.apiTransportInfobipPost(transportInfobipPost, (error, data, response) => {
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
 **transportInfobipPost** | [**TransportInfobipPost**](TransportInfobipPost.md)| The new TransportInfobip resource | 

### Return type

[**TransportInfobipGet**](TransportInfobipGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

