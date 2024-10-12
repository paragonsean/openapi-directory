# AlerterSystemApi.TransportFreshdeskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportFreshdeskGetCollection**](TransportFreshdeskApi.md#apiTransportFreshdeskGetCollection) | **GET** /api/transport-freshdesk | Retrieves the collection of TransportFreshdesk resources.
[**apiTransportFreshdeskIdDelete**](TransportFreshdeskApi.md#apiTransportFreshdeskIdDelete) | **DELETE** /api/transport-freshdesk/{id} | Removes the TransportFreshdesk resource.
[**apiTransportFreshdeskIdGet**](TransportFreshdeskApi.md#apiTransportFreshdeskIdGet) | **GET** /api/transport-freshdesk/{id} | Retrieves a TransportFreshdesk resource.
[**apiTransportFreshdeskIdPatch**](TransportFreshdeskApi.md#apiTransportFreshdeskIdPatch) | **PATCH** /api/transport-freshdesk/{id} | Updates the TransportFreshdesk resource.
[**apiTransportFreshdeskIdPut**](TransportFreshdeskApi.md#apiTransportFreshdeskIdPut) | **PUT** /api/transport-freshdesk/{id} | Replaces the TransportFreshdesk resource.
[**apiTransportFreshdeskPost**](TransportFreshdeskApi.md#apiTransportFreshdeskPost) | **POST** /api/transport-freshdesk | Creates a TransportFreshdesk resource.



## apiTransportFreshdeskGetCollection

> [TransportFreshdeskGet] apiTransportFreshdeskGetCollection(opts)

Retrieves the collection of TransportFreshdesk resources.

Retrieves the collection of TransportFreshdesk resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreshdeskApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportFreshdeskGetCollection(opts, (error, data, response) => {
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

[**[TransportFreshdeskGet]**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreshdeskIdDelete

> apiTransportFreshdeskIdDelete(id)

Removes the TransportFreshdesk resource.

Removes the TransportFreshdesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreshdeskApi();
let id = "id_example"; // String | TransportFreshdesk identifier
apiInstance.apiTransportFreshdeskIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportFreshdesk identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportFreshdeskIdGet

> TransportFreshdeskGet apiTransportFreshdeskIdGet(id)

Retrieves a TransportFreshdesk resource.

Retrieves a TransportFreshdesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreshdeskApi();
let id = "id_example"; // String | TransportFreshdesk identifier
apiInstance.apiTransportFreshdeskIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportFreshdesk identifier | 

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreshdeskIdPatch

> TransportFreshdeskGet apiTransportFreshdeskIdPatch(id, transportFreshdeskPatch)

Updates the TransportFreshdesk resource.

Updates the TransportFreshdesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreshdeskApi();
let id = "id_example"; // String | TransportFreshdesk identifier
let transportFreshdeskPatch = new AlerterSystemApi.TransportFreshdeskPatch(); // TransportFreshdeskPatch | The updated TransportFreshdesk resource
apiInstance.apiTransportFreshdeskIdPatch(id, transportFreshdeskPatch, (error, data, response) => {
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
 **id** | **String**| TransportFreshdesk identifier | 
 **transportFreshdeskPatch** | [**TransportFreshdeskPatch**](TransportFreshdeskPatch.md)| The updated TransportFreshdesk resource | 

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreshdeskIdPut

> TransportFreshdeskGet apiTransportFreshdeskIdPut(id, transportFreshdeskPut)

Replaces the TransportFreshdesk resource.

Replaces the TransportFreshdesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreshdeskApi();
let id = "id_example"; // String | TransportFreshdesk identifier
let transportFreshdeskPut = new AlerterSystemApi.TransportFreshdeskPut(); // TransportFreshdeskPut | The updated TransportFreshdesk resource
apiInstance.apiTransportFreshdeskIdPut(id, transportFreshdeskPut, (error, data, response) => {
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
 **id** | **String**| TransportFreshdesk identifier | 
 **transportFreshdeskPut** | [**TransportFreshdeskPut**](TransportFreshdeskPut.md)| The updated TransportFreshdesk resource | 

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreshdeskPost

> TransportFreshdeskGet apiTransportFreshdeskPost(transportFreshdeskPost)

Creates a TransportFreshdesk resource.

Creates a TransportFreshdesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreshdeskApi();
let transportFreshdeskPost = new AlerterSystemApi.TransportFreshdeskPost(); // TransportFreshdeskPost | The new TransportFreshdesk resource
apiInstance.apiTransportFreshdeskPost(transportFreshdeskPost, (error, data, response) => {
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
 **transportFreshdeskPost** | [**TransportFreshdeskPost**](TransportFreshdeskPost.md)| The new TransportFreshdesk resource | 

### Return type

[**TransportFreshdeskGet**](TransportFreshdeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

