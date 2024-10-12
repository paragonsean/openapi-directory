# AlerterSystemApi.TransportSmsapiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSmsapiGetCollection**](TransportSmsapiApi.md#apiTransportSmsapiGetCollection) | **GET** /api/transport-smsapi | Retrieves the collection of TransportSmsapi resources.
[**apiTransportSmsapiIdDelete**](TransportSmsapiApi.md#apiTransportSmsapiIdDelete) | **DELETE** /api/transport-smsapi/{id} | Removes the TransportSmsapi resource.
[**apiTransportSmsapiIdGet**](TransportSmsapiApi.md#apiTransportSmsapiIdGet) | **GET** /api/transport-smsapi/{id} | Retrieves a TransportSmsapi resource.
[**apiTransportSmsapiIdPatch**](TransportSmsapiApi.md#apiTransportSmsapiIdPatch) | **PATCH** /api/transport-smsapi/{id} | Updates the TransportSmsapi resource.
[**apiTransportSmsapiIdPut**](TransportSmsapiApi.md#apiTransportSmsapiIdPut) | **PUT** /api/transport-smsapi/{id} | Replaces the TransportSmsapi resource.
[**apiTransportSmsapiPost**](TransportSmsapiApi.md#apiTransportSmsapiPost) | **POST** /api/transport-smsapi | Creates a TransportSmsapi resource.



## apiTransportSmsapiGetCollection

> [TransportSmsapiGet] apiTransportSmsapiGetCollection(opts)

Retrieves the collection of TransportSmsapi resources.

Retrieves the collection of TransportSmsapi resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsapiApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSmsapiGetCollection(opts, (error, data, response) => {
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

[**[TransportSmsapiGet]**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsapiIdDelete

> apiTransportSmsapiIdDelete(id)

Removes the TransportSmsapi resource.

Removes the TransportSmsapi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsapiApi();
let id = "id_example"; // String | TransportSmsapi identifier
apiInstance.apiTransportSmsapiIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsapi identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSmsapiIdGet

> TransportSmsapiGet apiTransportSmsapiIdGet(id)

Retrieves a TransportSmsapi resource.

Retrieves a TransportSmsapi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsapiApi();
let id = "id_example"; // String | TransportSmsapi identifier
apiInstance.apiTransportSmsapiIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsapi identifier | 

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsapiIdPatch

> TransportSmsapiGet apiTransportSmsapiIdPatch(id, transportSmsapiPatch)

Updates the TransportSmsapi resource.

Updates the TransportSmsapi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsapiApi();
let id = "id_example"; // String | TransportSmsapi identifier
let transportSmsapiPatch = new AlerterSystemApi.TransportSmsapiPatch(); // TransportSmsapiPatch | The updated TransportSmsapi resource
apiInstance.apiTransportSmsapiIdPatch(id, transportSmsapiPatch, (error, data, response) => {
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
 **id** | **String**| TransportSmsapi identifier | 
 **transportSmsapiPatch** | [**TransportSmsapiPatch**](TransportSmsapiPatch.md)| The updated TransportSmsapi resource | 

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsapiIdPut

> TransportSmsapiGet apiTransportSmsapiIdPut(id, transportSmsapiPut)

Replaces the TransportSmsapi resource.

Replaces the TransportSmsapi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsapiApi();
let id = "id_example"; // String | TransportSmsapi identifier
let transportSmsapiPut = new AlerterSystemApi.TransportSmsapiPut(); // TransportSmsapiPut | The updated TransportSmsapi resource
apiInstance.apiTransportSmsapiIdPut(id, transportSmsapiPut, (error, data, response) => {
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
 **id** | **String**| TransportSmsapi identifier | 
 **transportSmsapiPut** | [**TransportSmsapiPut**](TransportSmsapiPut.md)| The updated TransportSmsapi resource | 

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsapiPost

> TransportSmsapiGet apiTransportSmsapiPost(transportSmsapiPost)

Creates a TransportSmsapi resource.

Creates a TransportSmsapi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsapiApi();
let transportSmsapiPost = new AlerterSystemApi.TransportSmsapiPost(); // TransportSmsapiPost | The new TransportSmsapi resource
apiInstance.apiTransportSmsapiPost(transportSmsapiPost, (error, data, response) => {
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
 **transportSmsapiPost** | [**TransportSmsapiPost**](TransportSmsapiPost.md)| The new TransportSmsapi resource | 

### Return type

[**TransportSmsapiGet**](TransportSmsapiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

