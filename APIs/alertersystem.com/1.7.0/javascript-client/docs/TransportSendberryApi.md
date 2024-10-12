# AlerterSystemApi.TransportSendberryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSendberryGetCollection**](TransportSendberryApi.md#apiTransportSendberryGetCollection) | **GET** /api/transport-sendberry | Retrieves the collection of TransportSendberry resources.
[**apiTransportSendberryIdDelete**](TransportSendberryApi.md#apiTransportSendberryIdDelete) | **DELETE** /api/transport-sendberry/{id} | Removes the TransportSendberry resource.
[**apiTransportSendberryIdGet**](TransportSendberryApi.md#apiTransportSendberryIdGet) | **GET** /api/transport-sendberry/{id} | Retrieves a TransportSendberry resource.
[**apiTransportSendberryIdPatch**](TransportSendberryApi.md#apiTransportSendberryIdPatch) | **PATCH** /api/transport-sendberry/{id} | Updates the TransportSendberry resource.
[**apiTransportSendberryIdPut**](TransportSendberryApi.md#apiTransportSendberryIdPut) | **PUT** /api/transport-sendberry/{id} | Replaces the TransportSendberry resource.
[**apiTransportSendberryPost**](TransportSendberryApi.md#apiTransportSendberryPost) | **POST** /api/transport-sendberry | Creates a TransportSendberry resource.



## apiTransportSendberryGetCollection

> [TransportSendberryGet] apiTransportSendberryGetCollection(opts)

Retrieves the collection of TransportSendberry resources.

Retrieves the collection of TransportSendberry resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendberryApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSendberryGetCollection(opts, (error, data, response) => {
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

[**[TransportSendberryGet]**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendberryIdDelete

> apiTransportSendberryIdDelete(id)

Removes the TransportSendberry resource.

Removes the TransportSendberry resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendberryApi();
let id = "id_example"; // String | TransportSendberry identifier
apiInstance.apiTransportSendberryIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSendberry identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSendberryIdGet

> TransportSendberryGet apiTransportSendberryIdGet(id)

Retrieves a TransportSendberry resource.

Retrieves a TransportSendberry resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendberryApi();
let id = "id_example"; // String | TransportSendberry identifier
apiInstance.apiTransportSendberryIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSendberry identifier | 

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendberryIdPatch

> TransportSendberryGet apiTransportSendberryIdPatch(id, transportSendberryPatch)

Updates the TransportSendberry resource.

Updates the TransportSendberry resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendberryApi();
let id = "id_example"; // String | TransportSendberry identifier
let transportSendberryPatch = new AlerterSystemApi.TransportSendberryPatch(); // TransportSendberryPatch | The updated TransportSendberry resource
apiInstance.apiTransportSendberryIdPatch(id, transportSendberryPatch, (error, data, response) => {
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
 **id** | **String**| TransportSendberry identifier | 
 **transportSendberryPatch** | [**TransportSendberryPatch**](TransportSendberryPatch.md)| The updated TransportSendberry resource | 

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendberryIdPut

> TransportSendberryGet apiTransportSendberryIdPut(id, transportSendberryPut)

Replaces the TransportSendberry resource.

Replaces the TransportSendberry resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendberryApi();
let id = "id_example"; // String | TransportSendberry identifier
let transportSendberryPut = new AlerterSystemApi.TransportSendberryPut(); // TransportSendberryPut | The updated TransportSendberry resource
apiInstance.apiTransportSendberryIdPut(id, transportSendberryPut, (error, data, response) => {
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
 **id** | **String**| TransportSendberry identifier | 
 **transportSendberryPut** | [**TransportSendberryPut**](TransportSendberryPut.md)| The updated TransportSendberry resource | 

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSendberryPost

> TransportSendberryGet apiTransportSendberryPost(transportSendberryPost)

Creates a TransportSendberry resource.

Creates a TransportSendberry resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSendberryApi();
let transportSendberryPost = new AlerterSystemApi.TransportSendberryPost(); // TransportSendberryPost | The new TransportSendberry resource
apiInstance.apiTransportSendberryPost(transportSendberryPost, (error, data, response) => {
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
 **transportSendberryPost** | [**TransportSendberryPost**](TransportSendberryPost.md)| The new TransportSendberry resource | 

### Return type

[**TransportSendberryGet**](TransportSendberryGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

