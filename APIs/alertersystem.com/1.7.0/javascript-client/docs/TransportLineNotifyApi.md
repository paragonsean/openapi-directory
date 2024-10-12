# AlerterSystemApi.TransportLineNotifyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportLineNotifyGetCollection**](TransportLineNotifyApi.md#apiTransportLineNotifyGetCollection) | **GET** /api/transport-line-notify | Retrieves the collection of TransportLineNotify resources.
[**apiTransportLineNotifyIdDelete**](TransportLineNotifyApi.md#apiTransportLineNotifyIdDelete) | **DELETE** /api/transport-line-notify/{id} | Removes the TransportLineNotify resource.
[**apiTransportLineNotifyIdGet**](TransportLineNotifyApi.md#apiTransportLineNotifyIdGet) | **GET** /api/transport-line-notify/{id} | Retrieves a TransportLineNotify resource.
[**apiTransportLineNotifyIdPatch**](TransportLineNotifyApi.md#apiTransportLineNotifyIdPatch) | **PATCH** /api/transport-line-notify/{id} | Updates the TransportLineNotify resource.
[**apiTransportLineNotifyIdPut**](TransportLineNotifyApi.md#apiTransportLineNotifyIdPut) | **PUT** /api/transport-line-notify/{id} | Replaces the TransportLineNotify resource.
[**apiTransportLineNotifyPost**](TransportLineNotifyApi.md#apiTransportLineNotifyPost) | **POST** /api/transport-line-notify | Creates a TransportLineNotify resource.



## apiTransportLineNotifyGetCollection

> [TransportLineNotifyGet] apiTransportLineNotifyGetCollection(opts)

Retrieves the collection of TransportLineNotify resources.

Retrieves the collection of TransportLineNotify resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLineNotifyApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportLineNotifyGetCollection(opts, (error, data, response) => {
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

[**[TransportLineNotifyGet]**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLineNotifyIdDelete

> apiTransportLineNotifyIdDelete(id)

Removes the TransportLineNotify resource.

Removes the TransportLineNotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLineNotifyApi();
let id = "id_example"; // String | TransportLineNotify identifier
apiInstance.apiTransportLineNotifyIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportLineNotify identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportLineNotifyIdGet

> TransportLineNotifyGet apiTransportLineNotifyIdGet(id)

Retrieves a TransportLineNotify resource.

Retrieves a TransportLineNotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLineNotifyApi();
let id = "id_example"; // String | TransportLineNotify identifier
apiInstance.apiTransportLineNotifyIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportLineNotify identifier | 

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLineNotifyIdPatch

> TransportLineNotifyGet apiTransportLineNotifyIdPatch(id, transportLineNotifyPatch)

Updates the TransportLineNotify resource.

Updates the TransportLineNotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLineNotifyApi();
let id = "id_example"; // String | TransportLineNotify identifier
let transportLineNotifyPatch = new AlerterSystemApi.TransportLineNotifyPatch(); // TransportLineNotifyPatch | The updated TransportLineNotify resource
apiInstance.apiTransportLineNotifyIdPatch(id, transportLineNotifyPatch, (error, data, response) => {
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
 **id** | **String**| TransportLineNotify identifier | 
 **transportLineNotifyPatch** | [**TransportLineNotifyPatch**](TransportLineNotifyPatch.md)| The updated TransportLineNotify resource | 

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLineNotifyIdPut

> TransportLineNotifyGet apiTransportLineNotifyIdPut(id, transportLineNotifyPut)

Replaces the TransportLineNotify resource.

Replaces the TransportLineNotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLineNotifyApi();
let id = "id_example"; // String | TransportLineNotify identifier
let transportLineNotifyPut = new AlerterSystemApi.TransportLineNotifyPut(); // TransportLineNotifyPut | The updated TransportLineNotify resource
apiInstance.apiTransportLineNotifyIdPut(id, transportLineNotifyPut, (error, data, response) => {
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
 **id** | **String**| TransportLineNotify identifier | 
 **transportLineNotifyPut** | [**TransportLineNotifyPut**](TransportLineNotifyPut.md)| The updated TransportLineNotify resource | 

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLineNotifyPost

> TransportLineNotifyGet apiTransportLineNotifyPost(transportLineNotifyPost)

Creates a TransportLineNotify resource.

Creates a TransportLineNotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLineNotifyApi();
let transportLineNotifyPost = new AlerterSystemApi.TransportLineNotifyPost(); // TransportLineNotifyPost | The new TransportLineNotify resource
apiInstance.apiTransportLineNotifyPost(transportLineNotifyPost, (error, data, response) => {
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
 **transportLineNotifyPost** | [**TransportLineNotifyPost**](TransportLineNotifyPost.md)| The new TransportLineNotify resource | 

### Return type

[**TransportLineNotifyGet**](TransportLineNotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

