# AlerterSystemApi.TransportLinkedInApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportLinkedInGetCollection**](TransportLinkedInApi.md#apiTransportLinkedInGetCollection) | **GET** /api/transport-linked-in | Retrieves the collection of TransportLinkedIn resources.
[**apiTransportLinkedInIdDelete**](TransportLinkedInApi.md#apiTransportLinkedInIdDelete) | **DELETE** /api/transport-linked-in/{id} | Removes the TransportLinkedIn resource.
[**apiTransportLinkedInIdGet**](TransportLinkedInApi.md#apiTransportLinkedInIdGet) | **GET** /api/transport-linked-in/{id} | Retrieves a TransportLinkedIn resource.
[**apiTransportLinkedInIdPatch**](TransportLinkedInApi.md#apiTransportLinkedInIdPatch) | **PATCH** /api/transport-linked-in/{id} | Updates the TransportLinkedIn resource.
[**apiTransportLinkedInIdPut**](TransportLinkedInApi.md#apiTransportLinkedInIdPut) | **PUT** /api/transport-linked-in/{id} | Replaces the TransportLinkedIn resource.
[**apiTransportLinkedInPost**](TransportLinkedInApi.md#apiTransportLinkedInPost) | **POST** /api/transport-linked-in | Creates a TransportLinkedIn resource.



## apiTransportLinkedInGetCollection

> [TransportLinkedInGet] apiTransportLinkedInGetCollection(opts)

Retrieves the collection of TransportLinkedIn resources.

Retrieves the collection of TransportLinkedIn resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLinkedInApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportLinkedInGetCollection(opts, (error, data, response) => {
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

[**[TransportLinkedInGet]**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLinkedInIdDelete

> apiTransportLinkedInIdDelete(id)

Removes the TransportLinkedIn resource.

Removes the TransportLinkedIn resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLinkedInApi();
let id = "id_example"; // String | TransportLinkedIn identifier
apiInstance.apiTransportLinkedInIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportLinkedIn identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportLinkedInIdGet

> TransportLinkedInGet apiTransportLinkedInIdGet(id)

Retrieves a TransportLinkedIn resource.

Retrieves a TransportLinkedIn resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLinkedInApi();
let id = "id_example"; // String | TransportLinkedIn identifier
apiInstance.apiTransportLinkedInIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportLinkedIn identifier | 

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLinkedInIdPatch

> TransportLinkedInGet apiTransportLinkedInIdPatch(id, transportLinkedInPatch)

Updates the TransportLinkedIn resource.

Updates the TransportLinkedIn resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLinkedInApi();
let id = "id_example"; // String | TransportLinkedIn identifier
let transportLinkedInPatch = new AlerterSystemApi.TransportLinkedInPatch(); // TransportLinkedInPatch | The updated TransportLinkedIn resource
apiInstance.apiTransportLinkedInIdPatch(id, transportLinkedInPatch, (error, data, response) => {
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
 **id** | **String**| TransportLinkedIn identifier | 
 **transportLinkedInPatch** | [**TransportLinkedInPatch**](TransportLinkedInPatch.md)| The updated TransportLinkedIn resource | 

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLinkedInIdPut

> TransportLinkedInGet apiTransportLinkedInIdPut(id, transportLinkedInPut)

Replaces the TransportLinkedIn resource.

Replaces the TransportLinkedIn resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLinkedInApi();
let id = "id_example"; // String | TransportLinkedIn identifier
let transportLinkedInPut = new AlerterSystemApi.TransportLinkedInPut(); // TransportLinkedInPut | The updated TransportLinkedIn resource
apiInstance.apiTransportLinkedInIdPut(id, transportLinkedInPut, (error, data, response) => {
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
 **id** | **String**| TransportLinkedIn identifier | 
 **transportLinkedInPut** | [**TransportLinkedInPut**](TransportLinkedInPut.md)| The updated TransportLinkedIn resource | 

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLinkedInPost

> TransportLinkedInGet apiTransportLinkedInPost(transportLinkedInPost)

Creates a TransportLinkedIn resource.

Creates a TransportLinkedIn resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLinkedInApi();
let transportLinkedInPost = new AlerterSystemApi.TransportLinkedInPost(); // TransportLinkedInPost | The new TransportLinkedIn resource
apiInstance.apiTransportLinkedInPost(transportLinkedInPost, (error, data, response) => {
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
 **transportLinkedInPost** | [**TransportLinkedInPost**](TransportLinkedInPost.md)| The new TransportLinkedIn resource | 

### Return type

[**TransportLinkedInGet**](TransportLinkedInGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

