# AlerterSystemApi.TransportGotifyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportGotifyGetCollection**](TransportGotifyApi.md#apiTransportGotifyGetCollection) | **GET** /api/transport-gotify | Retrieves the collection of TransportGotify resources.
[**apiTransportGotifyIdDelete**](TransportGotifyApi.md#apiTransportGotifyIdDelete) | **DELETE** /api/transport-gotify/{id} | Removes the TransportGotify resource.
[**apiTransportGotifyIdGet**](TransportGotifyApi.md#apiTransportGotifyIdGet) | **GET** /api/transport-gotify/{id} | Retrieves a TransportGotify resource.
[**apiTransportGotifyIdPatch**](TransportGotifyApi.md#apiTransportGotifyIdPatch) | **PATCH** /api/transport-gotify/{id} | Updates the TransportGotify resource.
[**apiTransportGotifyIdPut**](TransportGotifyApi.md#apiTransportGotifyIdPut) | **PUT** /api/transport-gotify/{id} | Replaces the TransportGotify resource.
[**apiTransportGotifyPost**](TransportGotifyApi.md#apiTransportGotifyPost) | **POST** /api/transport-gotify | Creates a TransportGotify resource.



## apiTransportGotifyGetCollection

> [TransportGotifyGet] apiTransportGotifyGetCollection(opts)

Retrieves the collection of TransportGotify resources.

Retrieves the collection of TransportGotify resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGotifyApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportGotifyGetCollection(opts, (error, data, response) => {
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

[**[TransportGotifyGet]**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGotifyIdDelete

> apiTransportGotifyIdDelete(id)

Removes the TransportGotify resource.

Removes the TransportGotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGotifyApi();
let id = "id_example"; // String | TransportGotify identifier
apiInstance.apiTransportGotifyIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportGotify identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportGotifyIdGet

> TransportGotifyGet apiTransportGotifyIdGet(id)

Retrieves a TransportGotify resource.

Retrieves a TransportGotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGotifyApi();
let id = "id_example"; // String | TransportGotify identifier
apiInstance.apiTransportGotifyIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportGotify identifier | 

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGotifyIdPatch

> TransportGotifyGet apiTransportGotifyIdPatch(id, transportGotifyPatch)

Updates the TransportGotify resource.

Updates the TransportGotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGotifyApi();
let id = "id_example"; // String | TransportGotify identifier
let transportGotifyPatch = new AlerterSystemApi.TransportGotifyPatch(); // TransportGotifyPatch | The updated TransportGotify resource
apiInstance.apiTransportGotifyIdPatch(id, transportGotifyPatch, (error, data, response) => {
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
 **id** | **String**| TransportGotify identifier | 
 **transportGotifyPatch** | [**TransportGotifyPatch**](TransportGotifyPatch.md)| The updated TransportGotify resource | 

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGotifyIdPut

> TransportGotifyGet apiTransportGotifyIdPut(id, transportGotifyPut)

Replaces the TransportGotify resource.

Replaces the TransportGotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGotifyApi();
let id = "id_example"; // String | TransportGotify identifier
let transportGotifyPut = new AlerterSystemApi.TransportGotifyPut(); // TransportGotifyPut | The updated TransportGotify resource
apiInstance.apiTransportGotifyIdPut(id, transportGotifyPut, (error, data, response) => {
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
 **id** | **String**| TransportGotify identifier | 
 **transportGotifyPut** | [**TransportGotifyPut**](TransportGotifyPut.md)| The updated TransportGotify resource | 

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGotifyPost

> TransportGotifyGet apiTransportGotifyPost(transportGotifyPost)

Creates a TransportGotify resource.

Creates a TransportGotify resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGotifyApi();
let transportGotifyPost = new AlerterSystemApi.TransportGotifyPost(); // TransportGotifyPost | The new TransportGotify resource
apiInstance.apiTransportGotifyPost(transportGotifyPost, (error, data, response) => {
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
 **transportGotifyPost** | [**TransportGotifyPost**](TransportGotifyPost.md)| The new TransportGotify resource | 

### Return type

[**TransportGotifyGet**](TransportGotifyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

