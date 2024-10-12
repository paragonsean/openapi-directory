# AlerterSystemApi.TransportRingCentralApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportRingCentralGetCollection**](TransportRingCentralApi.md#apiTransportRingCentralGetCollection) | **GET** /api/transport-ring-central | Retrieves the collection of TransportRingCentral resources.
[**apiTransportRingCentralIdDelete**](TransportRingCentralApi.md#apiTransportRingCentralIdDelete) | **DELETE** /api/transport-ring-central/{id} | Removes the TransportRingCentral resource.
[**apiTransportRingCentralIdGet**](TransportRingCentralApi.md#apiTransportRingCentralIdGet) | **GET** /api/transport-ring-central/{id} | Retrieves a TransportRingCentral resource.
[**apiTransportRingCentralIdPatch**](TransportRingCentralApi.md#apiTransportRingCentralIdPatch) | **PATCH** /api/transport-ring-central/{id} | Updates the TransportRingCentral resource.
[**apiTransportRingCentralIdPut**](TransportRingCentralApi.md#apiTransportRingCentralIdPut) | **PUT** /api/transport-ring-central/{id} | Replaces the TransportRingCentral resource.
[**apiTransportRingCentralPost**](TransportRingCentralApi.md#apiTransportRingCentralPost) | **POST** /api/transport-ring-central | Creates a TransportRingCentral resource.



## apiTransportRingCentralGetCollection

> [TransportRingCentralGet] apiTransportRingCentralGetCollection(opts)

Retrieves the collection of TransportRingCentral resources.

Retrieves the collection of TransportRingCentral resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRingCentralApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportRingCentralGetCollection(opts, (error, data, response) => {
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

[**[TransportRingCentralGet]**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRingCentralIdDelete

> apiTransportRingCentralIdDelete(id)

Removes the TransportRingCentral resource.

Removes the TransportRingCentral resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRingCentralApi();
let id = "id_example"; // String | TransportRingCentral identifier
apiInstance.apiTransportRingCentralIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportRingCentral identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportRingCentralIdGet

> TransportRingCentralGet apiTransportRingCentralIdGet(id)

Retrieves a TransportRingCentral resource.

Retrieves a TransportRingCentral resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRingCentralApi();
let id = "id_example"; // String | TransportRingCentral identifier
apiInstance.apiTransportRingCentralIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportRingCentral identifier | 

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRingCentralIdPatch

> TransportRingCentralGet apiTransportRingCentralIdPatch(id, transportRingCentralPatch)

Updates the TransportRingCentral resource.

Updates the TransportRingCentral resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRingCentralApi();
let id = "id_example"; // String | TransportRingCentral identifier
let transportRingCentralPatch = new AlerterSystemApi.TransportRingCentralPatch(); // TransportRingCentralPatch | The updated TransportRingCentral resource
apiInstance.apiTransportRingCentralIdPatch(id, transportRingCentralPatch, (error, data, response) => {
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
 **id** | **String**| TransportRingCentral identifier | 
 **transportRingCentralPatch** | [**TransportRingCentralPatch**](TransportRingCentralPatch.md)| The updated TransportRingCentral resource | 

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRingCentralIdPut

> TransportRingCentralGet apiTransportRingCentralIdPut(id, transportRingCentralPut)

Replaces the TransportRingCentral resource.

Replaces the TransportRingCentral resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRingCentralApi();
let id = "id_example"; // String | TransportRingCentral identifier
let transportRingCentralPut = new AlerterSystemApi.TransportRingCentralPut(); // TransportRingCentralPut | The updated TransportRingCentral resource
apiInstance.apiTransportRingCentralIdPut(id, transportRingCentralPut, (error, data, response) => {
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
 **id** | **String**| TransportRingCentral identifier | 
 **transportRingCentralPut** | [**TransportRingCentralPut**](TransportRingCentralPut.md)| The updated TransportRingCentral resource | 

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportRingCentralPost

> TransportRingCentralGet apiTransportRingCentralPost(transportRingCentralPost)

Creates a TransportRingCentral resource.

Creates a TransportRingCentral resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportRingCentralApi();
let transportRingCentralPost = new AlerterSystemApi.TransportRingCentralPost(); // TransportRingCentralPost | The new TransportRingCentral resource
apiInstance.apiTransportRingCentralPost(transportRingCentralPost, (error, data, response) => {
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
 **transportRingCentralPost** | [**TransportRingCentralPost**](TransportRingCentralPost.md)| The new TransportRingCentral resource | 

### Return type

[**TransportRingCentralGet**](TransportRingCentralGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

