# AlerterSystemApi.TransportSmsmodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSmsmodeGetCollection**](TransportSmsmodeApi.md#apiTransportSmsmodeGetCollection) | **GET** /api/transport-smsmode | Retrieves the collection of TransportSmsmode resources.
[**apiTransportSmsmodeIdDelete**](TransportSmsmodeApi.md#apiTransportSmsmodeIdDelete) | **DELETE** /api/transport-smsmode/{id} | Removes the TransportSmsmode resource.
[**apiTransportSmsmodeIdGet**](TransportSmsmodeApi.md#apiTransportSmsmodeIdGet) | **GET** /api/transport-smsmode/{id} | Retrieves a TransportSmsmode resource.
[**apiTransportSmsmodeIdPatch**](TransportSmsmodeApi.md#apiTransportSmsmodeIdPatch) | **PATCH** /api/transport-smsmode/{id} | Updates the TransportSmsmode resource.
[**apiTransportSmsmodeIdPut**](TransportSmsmodeApi.md#apiTransportSmsmodeIdPut) | **PUT** /api/transport-smsmode/{id} | Replaces the TransportSmsmode resource.
[**apiTransportSmsmodePost**](TransportSmsmodeApi.md#apiTransportSmsmodePost) | **POST** /api/transport-smsmode | Creates a TransportSmsmode resource.



## apiTransportSmsmodeGetCollection

> [TransportSmsmodeGet] apiTransportSmsmodeGetCollection(opts)

Retrieves the collection of TransportSmsmode resources.

Retrieves the collection of TransportSmsmode resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsmodeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSmsmodeGetCollection(opts, (error, data, response) => {
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

[**[TransportSmsmodeGet]**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsmodeIdDelete

> apiTransportSmsmodeIdDelete(id)

Removes the TransportSmsmode resource.

Removes the TransportSmsmode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsmodeApi();
let id = "id_example"; // String | TransportSmsmode identifier
apiInstance.apiTransportSmsmodeIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsmode identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSmsmodeIdGet

> TransportSmsmodeGet apiTransportSmsmodeIdGet(id)

Retrieves a TransportSmsmode resource.

Retrieves a TransportSmsmode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsmodeApi();
let id = "id_example"; // String | TransportSmsmode identifier
apiInstance.apiTransportSmsmodeIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsmode identifier | 

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsmodeIdPatch

> TransportSmsmodeGet apiTransportSmsmodeIdPatch(id, transportSmsmodePatch)

Updates the TransportSmsmode resource.

Updates the TransportSmsmode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsmodeApi();
let id = "id_example"; // String | TransportSmsmode identifier
let transportSmsmodePatch = new AlerterSystemApi.TransportSmsmodePatch(); // TransportSmsmodePatch | The updated TransportSmsmode resource
apiInstance.apiTransportSmsmodeIdPatch(id, transportSmsmodePatch, (error, data, response) => {
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
 **id** | **String**| TransportSmsmode identifier | 
 **transportSmsmodePatch** | [**TransportSmsmodePatch**](TransportSmsmodePatch.md)| The updated TransportSmsmode resource | 

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsmodeIdPut

> TransportSmsmodeGet apiTransportSmsmodeIdPut(id, transportSmsmodePut)

Replaces the TransportSmsmode resource.

Replaces the TransportSmsmode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsmodeApi();
let id = "id_example"; // String | TransportSmsmode identifier
let transportSmsmodePut = new AlerterSystemApi.TransportSmsmodePut(); // TransportSmsmodePut | The updated TransportSmsmode resource
apiInstance.apiTransportSmsmodeIdPut(id, transportSmsmodePut, (error, data, response) => {
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
 **id** | **String**| TransportSmsmode identifier | 
 **transportSmsmodePut** | [**TransportSmsmodePut**](TransportSmsmodePut.md)| The updated TransportSmsmode resource | 

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsmodePost

> TransportSmsmodeGet apiTransportSmsmodePost(transportSmsmodePost)

Creates a TransportSmsmode resource.

Creates a TransportSmsmode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsmodeApi();
let transportSmsmodePost = new AlerterSystemApi.TransportSmsmodePost(); // TransportSmsmodePost | The new TransportSmsmode resource
apiInstance.apiTransportSmsmodePost(transportSmsmodePost, (error, data, response) => {
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
 **transportSmsmodePost** | [**TransportSmsmodePost**](TransportSmsmodePost.md)| The new TransportSmsmode resource | 

### Return type

[**TransportSmsmodeGet**](TransportSmsmodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

