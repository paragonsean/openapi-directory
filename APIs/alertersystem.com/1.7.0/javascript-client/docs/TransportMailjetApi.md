# AlerterSystemApi.TransportMailjetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMailjetGetCollection**](TransportMailjetApi.md#apiTransportMailjetGetCollection) | **GET** /api/transport-mailjet | Retrieves the collection of TransportMailjet resources.
[**apiTransportMailjetIdDelete**](TransportMailjetApi.md#apiTransportMailjetIdDelete) | **DELETE** /api/transport-mailjet/{id} | Removes the TransportMailjet resource.
[**apiTransportMailjetIdGet**](TransportMailjetApi.md#apiTransportMailjetIdGet) | **GET** /api/transport-mailjet/{id} | Retrieves a TransportMailjet resource.
[**apiTransportMailjetIdPatch**](TransportMailjetApi.md#apiTransportMailjetIdPatch) | **PATCH** /api/transport-mailjet/{id} | Updates the TransportMailjet resource.
[**apiTransportMailjetIdPut**](TransportMailjetApi.md#apiTransportMailjetIdPut) | **PUT** /api/transport-mailjet/{id} | Replaces the TransportMailjet resource.
[**apiTransportMailjetPost**](TransportMailjetApi.md#apiTransportMailjetPost) | **POST** /api/transport-mailjet | Creates a TransportMailjet resource.



## apiTransportMailjetGetCollection

> [TransportMailjetGet] apiTransportMailjetGetCollection(opts)

Retrieves the collection of TransportMailjet resources.

Retrieves the collection of TransportMailjet resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMailjetApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMailjetGetCollection(opts, (error, data, response) => {
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

[**[TransportMailjetGet]**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMailjetIdDelete

> apiTransportMailjetIdDelete(id)

Removes the TransportMailjet resource.

Removes the TransportMailjet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMailjetApi();
let id = "id_example"; // String | TransportMailjet identifier
apiInstance.apiTransportMailjetIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMailjet identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMailjetIdGet

> TransportMailjetGet apiTransportMailjetIdGet(id)

Retrieves a TransportMailjet resource.

Retrieves a TransportMailjet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMailjetApi();
let id = "id_example"; // String | TransportMailjet identifier
apiInstance.apiTransportMailjetIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMailjet identifier | 

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMailjetIdPatch

> TransportMailjetGet apiTransportMailjetIdPatch(id, transportMailjetPatch)

Updates the TransportMailjet resource.

Updates the TransportMailjet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMailjetApi();
let id = "id_example"; // String | TransportMailjet identifier
let transportMailjetPatch = new AlerterSystemApi.TransportMailjetPatch(); // TransportMailjetPatch | The updated TransportMailjet resource
apiInstance.apiTransportMailjetIdPatch(id, transportMailjetPatch, (error, data, response) => {
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
 **id** | **String**| TransportMailjet identifier | 
 **transportMailjetPatch** | [**TransportMailjetPatch**](TransportMailjetPatch.md)| The updated TransportMailjet resource | 

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMailjetIdPut

> TransportMailjetGet apiTransportMailjetIdPut(id, transportMailjetPut)

Replaces the TransportMailjet resource.

Replaces the TransportMailjet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMailjetApi();
let id = "id_example"; // String | TransportMailjet identifier
let transportMailjetPut = new AlerterSystemApi.TransportMailjetPut(); // TransportMailjetPut | The updated TransportMailjet resource
apiInstance.apiTransportMailjetIdPut(id, transportMailjetPut, (error, data, response) => {
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
 **id** | **String**| TransportMailjet identifier | 
 **transportMailjetPut** | [**TransportMailjetPut**](TransportMailjetPut.md)| The updated TransportMailjet resource | 

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMailjetPost

> TransportMailjetGet apiTransportMailjetPost(transportMailjetPost)

Creates a TransportMailjet resource.

Creates a TransportMailjet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMailjetApi();
let transportMailjetPost = new AlerterSystemApi.TransportMailjetPost(); // TransportMailjetPost | The new TransportMailjet resource
apiInstance.apiTransportMailjetPost(transportMailjetPost, (error, data, response) => {
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
 **transportMailjetPost** | [**TransportMailjetPost**](TransportMailjetPost.md)| The new TransportMailjet resource | 

### Return type

[**TransportMailjetGet**](TransportMailjetGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

