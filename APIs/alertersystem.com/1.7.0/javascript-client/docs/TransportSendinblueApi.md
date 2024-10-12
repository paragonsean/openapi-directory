# AlerterSystemApi.TransportSendinblueApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSendinblueGetCollection**](TransportSendinblueApi.md#apiTransportSendinblueGetCollection) | **GET** /api/transport-sendinblue | Retrieves the collection of TransportSendinblue resources.
[**apiTransportSendinblueIdDelete**](TransportSendinblueApi.md#apiTransportSendinblueIdDelete) | **DELETE** /api/transport-sendinblue/{id} | Removes the TransportSendinblue resource.
[**apiTransportSendinblueIdGet**](TransportSendinblueApi.md#apiTransportSendinblueIdGet) | **GET** /api/transport-sendinblue/{id} | Retrieves a TransportSendinblue resource.
[**apiTransportSendinblueIdPatch**](TransportSendinblueApi.md#apiTransportSendinblueIdPatch) | **PATCH** /api/transport-sendinblue/{id} | Updates the TransportSendinblue resource.
[**apiTransportSendinblueIdPut**](TransportSendinblueApi.md#apiTransportSendinblueIdPut) | **PUT** /api/transport-sendinblue/{id} | Replaces the TransportSendinblue resource.
[**apiTransportSendinbluePost**](TransportSendinblueApi.md#apiTransportSendinbluePost) | **POST** /api/transport-sendinblue | Creates a TransportSendinblue resource.



## apiTransportSendinblueGetCollection

> [TransportSendinblueGet] apiTransportSendinblueGetCollection(opts)

Retrieves the collection of TransportSendinblue resources.

Retrieves the collection of TransportSendinblue resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendinblueApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSendinblueGetCollection(opts, (error, data, response) => {
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

[**[TransportSendinblueGet]**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendinblueIdDelete

> apiTransportSendinblueIdDelete(id)

Removes the TransportSendinblue resource.

Removes the TransportSendinblue resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendinblueApi();
let id = "id_example"; // String | TransportSendinblue identifier
apiInstance.apiTransportSendinblueIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSendinblue identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSendinblueIdGet

> TransportSendinblueGet apiTransportSendinblueIdGet(id)

Retrieves a TransportSendinblue resource.

Retrieves a TransportSendinblue resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendinblueApi();
let id = "id_example"; // String | TransportSendinblue identifier
apiInstance.apiTransportSendinblueIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSendinblue identifier | 

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendinblueIdPatch

> TransportSendinblueGet apiTransportSendinblueIdPatch(id, transportSendinbluePatch)

Updates the TransportSendinblue resource.

Updates the TransportSendinblue resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendinblueApi();
let id = "id_example"; // String | TransportSendinblue identifier
let transportSendinbluePatch = new AlerterSystemApi.TransportSendinbluePatch(); // TransportSendinbluePatch | The updated TransportSendinblue resource
apiInstance.apiTransportSendinblueIdPatch(id, transportSendinbluePatch, (error, data, response) => {
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
 **id** | **String**| TransportSendinblue identifier | 
 **transportSendinbluePatch** | [**TransportSendinbluePatch**](TransportSendinbluePatch.md)| The updated TransportSendinblue resource | 

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendinblueIdPut

> TransportSendinblueGet apiTransportSendinblueIdPut(id, transportSendinbluePut)

Replaces the TransportSendinblue resource.

Replaces the TransportSendinblue resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendinblueApi();
let id = "id_example"; // String | TransportSendinblue identifier
let transportSendinbluePut = new AlerterSystemApi.TransportSendinbluePut(); // TransportSendinbluePut | The updated TransportSendinblue resource
apiInstance.apiTransportSendinblueIdPut(id, transportSendinbluePut, (error, data, response) => {
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
 **id** | **String**| TransportSendinblue identifier | 
 **transportSendinbluePut** | [**TransportSendinbluePut**](TransportSendinbluePut.md)| The updated TransportSendinblue resource | 

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendinbluePost

> TransportSendinblueGet apiTransportSendinbluePost(transportSendinbluePost)

Creates a TransportSendinblue resource.

Creates a TransportSendinblue resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendinblueApi();
let transportSendinbluePost = new AlerterSystemApi.TransportSendinbluePost(); // TransportSendinbluePost | The new TransportSendinblue resource
apiInstance.apiTransportSendinbluePost(transportSendinbluePost, (error, data, response) => {
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
 **transportSendinbluePost** | [**TransportSendinbluePost**](TransportSendinbluePost.md)| The new TransportSendinblue resource | 

### Return type

[**TransportSendinblueGet**](TransportSendinblueGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

