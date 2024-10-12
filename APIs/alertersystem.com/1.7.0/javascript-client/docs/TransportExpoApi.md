# AlerterSystemApi.TransportExpoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportExpoGetCollection**](TransportExpoApi.md#apiTransportExpoGetCollection) | **GET** /api/transport-expo | Retrieves the collection of TransportExpo resources.
[**apiTransportExpoIdDelete**](TransportExpoApi.md#apiTransportExpoIdDelete) | **DELETE** /api/transport-expo/{id} | Removes the TransportExpo resource.
[**apiTransportExpoIdGet**](TransportExpoApi.md#apiTransportExpoIdGet) | **GET** /api/transport-expo/{id} | Retrieves a TransportExpo resource.
[**apiTransportExpoIdPatch**](TransportExpoApi.md#apiTransportExpoIdPatch) | **PATCH** /api/transport-expo/{id} | Updates the TransportExpo resource.
[**apiTransportExpoIdPut**](TransportExpoApi.md#apiTransportExpoIdPut) | **PUT** /api/transport-expo/{id} | Replaces the TransportExpo resource.
[**apiTransportExpoPost**](TransportExpoApi.md#apiTransportExpoPost) | **POST** /api/transport-expo | Creates a TransportExpo resource.



## apiTransportExpoGetCollection

> [TransportExpoGet] apiTransportExpoGetCollection(opts)

Retrieves the collection of TransportExpo resources.

Retrieves the collection of TransportExpo resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportExpoApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportExpoGetCollection(opts, (error, data, response) => {
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

[**[TransportExpoGet]**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportExpoIdDelete

> apiTransportExpoIdDelete(id)

Removes the TransportExpo resource.

Removes the TransportExpo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportExpoApi();
let id = "id_example"; // String | TransportExpo identifier
apiInstance.apiTransportExpoIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportExpo identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportExpoIdGet

> TransportExpoGet apiTransportExpoIdGet(id)

Retrieves a TransportExpo resource.

Retrieves a TransportExpo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportExpoApi();
let id = "id_example"; // String | TransportExpo identifier
apiInstance.apiTransportExpoIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportExpo identifier | 

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportExpoIdPatch

> TransportExpoGet apiTransportExpoIdPatch(id, transportExpoPatch)

Updates the TransportExpo resource.

Updates the TransportExpo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportExpoApi();
let id = "id_example"; // String | TransportExpo identifier
let transportExpoPatch = new AlerterSystemApi.TransportExpoPatch(); // TransportExpoPatch | The updated TransportExpo resource
apiInstance.apiTransportExpoIdPatch(id, transportExpoPatch, (error, data, response) => {
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
 **id** | **String**| TransportExpo identifier | 
 **transportExpoPatch** | [**TransportExpoPatch**](TransportExpoPatch.md)| The updated TransportExpo resource | 

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportExpoIdPut

> TransportExpoGet apiTransportExpoIdPut(id, transportExpoPut)

Replaces the TransportExpo resource.

Replaces the TransportExpo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportExpoApi();
let id = "id_example"; // String | TransportExpo identifier
let transportExpoPut = new AlerterSystemApi.TransportExpoPut(); // TransportExpoPut | The updated TransportExpo resource
apiInstance.apiTransportExpoIdPut(id, transportExpoPut, (error, data, response) => {
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
 **id** | **String**| TransportExpo identifier | 
 **transportExpoPut** | [**TransportExpoPut**](TransportExpoPut.md)| The updated TransportExpo resource | 

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportExpoPost

> TransportExpoGet apiTransportExpoPost(transportExpoPost)

Creates a TransportExpo resource.

Creates a TransportExpo resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportExpoApi();
let transportExpoPost = new AlerterSystemApi.TransportExpoPost(); // TransportExpoPost | The new TransportExpo resource
apiInstance.apiTransportExpoPost(transportExpoPost, (error, data, response) => {
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
 **transportExpoPost** | [**TransportExpoPost**](TransportExpoPost.md)| The new TransportExpo resource | 

### Return type

[**TransportExpoGet**](TransportExpoGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

