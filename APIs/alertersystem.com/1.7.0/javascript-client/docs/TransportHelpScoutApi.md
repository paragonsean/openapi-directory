# AlerterSystemApi.TransportHelpScoutApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportHelpScoutGetCollection**](TransportHelpScoutApi.md#apiTransportHelpScoutGetCollection) | **GET** /api/transport-help-scout | Retrieves the collection of TransportHelpScout resources.
[**apiTransportHelpScoutIdDelete**](TransportHelpScoutApi.md#apiTransportHelpScoutIdDelete) | **DELETE** /api/transport-help-scout/{id} | Removes the TransportHelpScout resource.
[**apiTransportHelpScoutIdGet**](TransportHelpScoutApi.md#apiTransportHelpScoutIdGet) | **GET** /api/transport-help-scout/{id} | Retrieves a TransportHelpScout resource.
[**apiTransportHelpScoutIdPatch**](TransportHelpScoutApi.md#apiTransportHelpScoutIdPatch) | **PATCH** /api/transport-help-scout/{id} | Updates the TransportHelpScout resource.
[**apiTransportHelpScoutIdPut**](TransportHelpScoutApi.md#apiTransportHelpScoutIdPut) | **PUT** /api/transport-help-scout/{id} | Replaces the TransportHelpScout resource.
[**apiTransportHelpScoutPost**](TransportHelpScoutApi.md#apiTransportHelpScoutPost) | **POST** /api/transport-help-scout | Creates a TransportHelpScout resource.



## apiTransportHelpScoutGetCollection

> [TransportHelpScoutGet] apiTransportHelpScoutGetCollection(opts)

Retrieves the collection of TransportHelpScout resources.

Retrieves the collection of TransportHelpScout resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportHelpScoutApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportHelpScoutGetCollection(opts, (error, data, response) => {
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

[**[TransportHelpScoutGet]**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportHelpScoutIdDelete

> apiTransportHelpScoutIdDelete(id)

Removes the TransportHelpScout resource.

Removes the TransportHelpScout resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportHelpScoutApi();
let id = "id_example"; // String | TransportHelpScout identifier
apiInstance.apiTransportHelpScoutIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportHelpScout identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportHelpScoutIdGet

> TransportHelpScoutGet apiTransportHelpScoutIdGet(id)

Retrieves a TransportHelpScout resource.

Retrieves a TransportHelpScout resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportHelpScoutApi();
let id = "id_example"; // String | TransportHelpScout identifier
apiInstance.apiTransportHelpScoutIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportHelpScout identifier | 

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportHelpScoutIdPatch

> TransportHelpScoutGet apiTransportHelpScoutIdPatch(id, transportHelpScoutPatch)

Updates the TransportHelpScout resource.

Updates the TransportHelpScout resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportHelpScoutApi();
let id = "id_example"; // String | TransportHelpScout identifier
let transportHelpScoutPatch = new AlerterSystemApi.TransportHelpScoutPatch(); // TransportHelpScoutPatch | The updated TransportHelpScout resource
apiInstance.apiTransportHelpScoutIdPatch(id, transportHelpScoutPatch, (error, data, response) => {
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
 **id** | **String**| TransportHelpScout identifier | 
 **transportHelpScoutPatch** | [**TransportHelpScoutPatch**](TransportHelpScoutPatch.md)| The updated TransportHelpScout resource | 

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportHelpScoutIdPut

> TransportHelpScoutGet apiTransportHelpScoutIdPut(id, transportHelpScoutPut)

Replaces the TransportHelpScout resource.

Replaces the TransportHelpScout resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportHelpScoutApi();
let id = "id_example"; // String | TransportHelpScout identifier
let transportHelpScoutPut = new AlerterSystemApi.TransportHelpScoutPut(); // TransportHelpScoutPut | The updated TransportHelpScout resource
apiInstance.apiTransportHelpScoutIdPut(id, transportHelpScoutPut, (error, data, response) => {
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
 **id** | **String**| TransportHelpScout identifier | 
 **transportHelpScoutPut** | [**TransportHelpScoutPut**](TransportHelpScoutPut.md)| The updated TransportHelpScout resource | 

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportHelpScoutPost

> TransportHelpScoutGet apiTransportHelpScoutPost(transportHelpScoutPost)

Creates a TransportHelpScout resource.

Creates a TransportHelpScout resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportHelpScoutApi();
let transportHelpScoutPost = new AlerterSystemApi.TransportHelpScoutPost(); // TransportHelpScoutPost | The new TransportHelpScout resource
apiInstance.apiTransportHelpScoutPost(transportHelpScoutPost, (error, data, response) => {
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
 **transportHelpScoutPost** | [**TransportHelpScoutPost**](TransportHelpScoutPost.md)| The new TransportHelpScout resource | 

### Return type

[**TransportHelpScoutGet**](TransportHelpScoutGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

