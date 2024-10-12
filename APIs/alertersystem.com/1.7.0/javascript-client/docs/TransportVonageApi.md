# AlerterSystemApi.TransportVonageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportVonageGetCollection**](TransportVonageApi.md#apiTransportVonageGetCollection) | **GET** /api/transport-vonage | Retrieves the collection of TransportVonage resources.
[**apiTransportVonageIdDelete**](TransportVonageApi.md#apiTransportVonageIdDelete) | **DELETE** /api/transport-vonage/{id} | Removes the TransportVonage resource.
[**apiTransportVonageIdGet**](TransportVonageApi.md#apiTransportVonageIdGet) | **GET** /api/transport-vonage/{id} | Retrieves a TransportVonage resource.
[**apiTransportVonageIdPatch**](TransportVonageApi.md#apiTransportVonageIdPatch) | **PATCH** /api/transport-vonage/{id} | Updates the TransportVonage resource.
[**apiTransportVonageIdPut**](TransportVonageApi.md#apiTransportVonageIdPut) | **PUT** /api/transport-vonage/{id} | Replaces the TransportVonage resource.
[**apiTransportVonagePost**](TransportVonageApi.md#apiTransportVonagePost) | **POST** /api/transport-vonage | Creates a TransportVonage resource.



## apiTransportVonageGetCollection

> [TransportVonageGet] apiTransportVonageGetCollection(opts)

Retrieves the collection of TransportVonage resources.

Retrieves the collection of TransportVonage resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportVonageApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportVonageGetCollection(opts, (error, data, response) => {
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

[**[TransportVonageGet]**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportVonageIdDelete

> apiTransportVonageIdDelete(id)

Removes the TransportVonage resource.

Removes the TransportVonage resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportVonageApi();
let id = "id_example"; // String | TransportVonage identifier
apiInstance.apiTransportVonageIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportVonage identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportVonageIdGet

> TransportVonageGet apiTransportVonageIdGet(id)

Retrieves a TransportVonage resource.

Retrieves a TransportVonage resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportVonageApi();
let id = "id_example"; // String | TransportVonage identifier
apiInstance.apiTransportVonageIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportVonage identifier | 

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportVonageIdPatch

> TransportVonageGet apiTransportVonageIdPatch(id, transportVonagePatch)

Updates the TransportVonage resource.

Updates the TransportVonage resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportVonageApi();
let id = "id_example"; // String | TransportVonage identifier
let transportVonagePatch = new AlerterSystemApi.TransportVonagePatch(); // TransportVonagePatch | The updated TransportVonage resource
apiInstance.apiTransportVonageIdPatch(id, transportVonagePatch, (error, data, response) => {
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
 **id** | **String**| TransportVonage identifier | 
 **transportVonagePatch** | [**TransportVonagePatch**](TransportVonagePatch.md)| The updated TransportVonage resource | 

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportVonageIdPut

> TransportVonageGet apiTransportVonageIdPut(id, transportVonagePut)

Replaces the TransportVonage resource.

Replaces the TransportVonage resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportVonageApi();
let id = "id_example"; // String | TransportVonage identifier
let transportVonagePut = new AlerterSystemApi.TransportVonagePut(); // TransportVonagePut | The updated TransportVonage resource
apiInstance.apiTransportVonageIdPut(id, transportVonagePut, (error, data, response) => {
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
 **id** | **String**| TransportVonage identifier | 
 **transportVonagePut** | [**TransportVonagePut**](TransportVonagePut.md)| The updated TransportVonage resource | 

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportVonagePost

> TransportVonageGet apiTransportVonagePost(transportVonagePost)

Creates a TransportVonage resource.

Creates a TransportVonage resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportVonageApi();
let transportVonagePost = new AlerterSystemApi.TransportVonagePost(); // TransportVonagePost | The new TransportVonage resource
apiInstance.apiTransportVonagePost(transportVonagePost, (error, data, response) => {
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
 **transportVonagePost** | [**TransportVonagePost**](TransportVonagePost.md)| The new TransportVonage resource | 

### Return type

[**TransportVonageGet**](TransportVonageGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

