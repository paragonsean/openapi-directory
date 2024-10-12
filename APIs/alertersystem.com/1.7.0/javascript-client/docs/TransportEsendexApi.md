# AlerterSystemApi.TransportEsendexApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportEsendexGetCollection**](TransportEsendexApi.md#apiTransportEsendexGetCollection) | **GET** /api/transport-esendex | Retrieves the collection of TransportEsendex resources.
[**apiTransportEsendexIdDelete**](TransportEsendexApi.md#apiTransportEsendexIdDelete) | **DELETE** /api/transport-esendex/{id} | Removes the TransportEsendex resource.
[**apiTransportEsendexIdGet**](TransportEsendexApi.md#apiTransportEsendexIdGet) | **GET** /api/transport-esendex/{id} | Retrieves a TransportEsendex resource.
[**apiTransportEsendexIdPatch**](TransportEsendexApi.md#apiTransportEsendexIdPatch) | **PATCH** /api/transport-esendex/{id} | Updates the TransportEsendex resource.
[**apiTransportEsendexIdPut**](TransportEsendexApi.md#apiTransportEsendexIdPut) | **PUT** /api/transport-esendex/{id} | Replaces the TransportEsendex resource.
[**apiTransportEsendexPost**](TransportEsendexApi.md#apiTransportEsendexPost) | **POST** /api/transport-esendex | Creates a TransportEsendex resource.



## apiTransportEsendexGetCollection

> [TransportEsendexGet] apiTransportEsendexGetCollection(opts)

Retrieves the collection of TransportEsendex resources.

Retrieves the collection of TransportEsendex resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEsendexApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportEsendexGetCollection(opts, (error, data, response) => {
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

[**[TransportEsendexGet]**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEsendexIdDelete

> apiTransportEsendexIdDelete(id)

Removes the TransportEsendex resource.

Removes the TransportEsendex resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEsendexApi();
let id = "id_example"; // String | TransportEsendex identifier
apiInstance.apiTransportEsendexIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportEsendex identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportEsendexIdGet

> TransportEsendexGet apiTransportEsendexIdGet(id)

Retrieves a TransportEsendex resource.

Retrieves a TransportEsendex resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEsendexApi();
let id = "id_example"; // String | TransportEsendex identifier
apiInstance.apiTransportEsendexIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportEsendex identifier | 

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEsendexIdPatch

> TransportEsendexGet apiTransportEsendexIdPatch(id, transportEsendexPatch)

Updates the TransportEsendex resource.

Updates the TransportEsendex resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEsendexApi();
let id = "id_example"; // String | TransportEsendex identifier
let transportEsendexPatch = new AlerterSystemApi.TransportEsendexPatch(); // TransportEsendexPatch | The updated TransportEsendex resource
apiInstance.apiTransportEsendexIdPatch(id, transportEsendexPatch, (error, data, response) => {
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
 **id** | **String**| TransportEsendex identifier | 
 **transportEsendexPatch** | [**TransportEsendexPatch**](TransportEsendexPatch.md)| The updated TransportEsendex resource | 

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEsendexIdPut

> TransportEsendexGet apiTransportEsendexIdPut(id, transportEsendexPut)

Replaces the TransportEsendex resource.

Replaces the TransportEsendex resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEsendexApi();
let id = "id_example"; // String | TransportEsendex identifier
let transportEsendexPut = new AlerterSystemApi.TransportEsendexPut(); // TransportEsendexPut | The updated TransportEsendex resource
apiInstance.apiTransportEsendexIdPut(id, transportEsendexPut, (error, data, response) => {
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
 **id** | **String**| TransportEsendex identifier | 
 **transportEsendexPut** | [**TransportEsendexPut**](TransportEsendexPut.md)| The updated TransportEsendex resource | 

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEsendexPost

> TransportEsendexGet apiTransportEsendexPost(transportEsendexPost)

Creates a TransportEsendex resource.

Creates a TransportEsendex resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEsendexApi();
let transportEsendexPost = new AlerterSystemApi.TransportEsendexPost(); // TransportEsendexPost | The new TransportEsendex resource
apiInstance.apiTransportEsendexPost(transportEsendexPost, (error, data, response) => {
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
 **transportEsendexPost** | [**TransportEsendexPost**](TransportEsendexPost.md)| The new TransportEsendex resource | 

### Return type

[**TransportEsendexGet**](TransportEsendexGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

