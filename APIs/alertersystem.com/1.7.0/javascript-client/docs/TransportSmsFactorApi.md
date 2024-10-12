# AlerterSystemApi.TransportSmsFactorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSmsFactorGetCollection**](TransportSmsFactorApi.md#apiTransportSmsFactorGetCollection) | **GET** /api/transport-sms-factor | Retrieves the collection of TransportSmsFactor resources.
[**apiTransportSmsFactorIdDelete**](TransportSmsFactorApi.md#apiTransportSmsFactorIdDelete) | **DELETE** /api/transport-sms-factor/{id} | Removes the TransportSmsFactor resource.
[**apiTransportSmsFactorIdGet**](TransportSmsFactorApi.md#apiTransportSmsFactorIdGet) | **GET** /api/transport-sms-factor/{id} | Retrieves a TransportSmsFactor resource.
[**apiTransportSmsFactorIdPatch**](TransportSmsFactorApi.md#apiTransportSmsFactorIdPatch) | **PATCH** /api/transport-sms-factor/{id} | Updates the TransportSmsFactor resource.
[**apiTransportSmsFactorIdPut**](TransportSmsFactorApi.md#apiTransportSmsFactorIdPut) | **PUT** /api/transport-sms-factor/{id} | Replaces the TransportSmsFactor resource.
[**apiTransportSmsFactorPost**](TransportSmsFactorApi.md#apiTransportSmsFactorPost) | **POST** /api/transport-sms-factor | Creates a TransportSmsFactor resource.



## apiTransportSmsFactorGetCollection

> [TransportSmsFactorGet] apiTransportSmsFactorGetCollection(opts)

Retrieves the collection of TransportSmsFactor resources.

Retrieves the collection of TransportSmsFactor resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsFactorApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSmsFactorGetCollection(opts, (error, data, response) => {
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

[**[TransportSmsFactorGet]**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsFactorIdDelete

> apiTransportSmsFactorIdDelete(id)

Removes the TransportSmsFactor resource.

Removes the TransportSmsFactor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsFactorApi();
let id = "id_example"; // String | TransportSmsFactor identifier
apiInstance.apiTransportSmsFactorIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsFactor identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSmsFactorIdGet

> TransportSmsFactorGet apiTransportSmsFactorIdGet(id)

Retrieves a TransportSmsFactor resource.

Retrieves a TransportSmsFactor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsFactorApi();
let id = "id_example"; // String | TransportSmsFactor identifier
apiInstance.apiTransportSmsFactorIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsFactor identifier | 

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsFactorIdPatch

> TransportSmsFactorGet apiTransportSmsFactorIdPatch(id, transportSmsFactorPatch)

Updates the TransportSmsFactor resource.

Updates the TransportSmsFactor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsFactorApi();
let id = "id_example"; // String | TransportSmsFactor identifier
let transportSmsFactorPatch = new AlerterSystemApi.TransportSmsFactorPatch(); // TransportSmsFactorPatch | The updated TransportSmsFactor resource
apiInstance.apiTransportSmsFactorIdPatch(id, transportSmsFactorPatch, (error, data, response) => {
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
 **id** | **String**| TransportSmsFactor identifier | 
 **transportSmsFactorPatch** | [**TransportSmsFactorPatch**](TransportSmsFactorPatch.md)| The updated TransportSmsFactor resource | 

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsFactorIdPut

> TransportSmsFactorGet apiTransportSmsFactorIdPut(id, transportSmsFactorPut)

Replaces the TransportSmsFactor resource.

Replaces the TransportSmsFactor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsFactorApi();
let id = "id_example"; // String | TransportSmsFactor identifier
let transportSmsFactorPut = new AlerterSystemApi.TransportSmsFactorPut(); // TransportSmsFactorPut | The updated TransportSmsFactor resource
apiInstance.apiTransportSmsFactorIdPut(id, transportSmsFactorPut, (error, data, response) => {
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
 **id** | **String**| TransportSmsFactor identifier | 
 **transportSmsFactorPut** | [**TransportSmsFactorPut**](TransportSmsFactorPut.md)| The updated TransportSmsFactor resource | 

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsFactorPost

> TransportSmsFactorGet apiTransportSmsFactorPost(transportSmsFactorPost)

Creates a TransportSmsFactor resource.

Creates a TransportSmsFactor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsFactorApi();
let transportSmsFactorPost = new AlerterSystemApi.TransportSmsFactorPost(); // TransportSmsFactorPost | The new TransportSmsFactor resource
apiInstance.apiTransportSmsFactorPost(transportSmsFactorPost, (error, data, response) => {
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
 **transportSmsFactorPost** | [**TransportSmsFactorPost**](TransportSmsFactorPost.md)| The new TransportSmsFactor resource | 

### Return type

[**TransportSmsFactorGet**](TransportSmsFactorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

