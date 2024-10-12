# AlerterSystemApi.TransportMastodonApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMastodonGetCollection**](TransportMastodonApi.md#apiTransportMastodonGetCollection) | **GET** /api/transport-mastodon | Retrieves the collection of TransportMastodon resources.
[**apiTransportMastodonIdDelete**](TransportMastodonApi.md#apiTransportMastodonIdDelete) | **DELETE** /api/transport-mastodon/{id} | Removes the TransportMastodon resource.
[**apiTransportMastodonIdGet**](TransportMastodonApi.md#apiTransportMastodonIdGet) | **GET** /api/transport-mastodon/{id} | Retrieves a TransportMastodon resource.
[**apiTransportMastodonIdPatch**](TransportMastodonApi.md#apiTransportMastodonIdPatch) | **PATCH** /api/transport-mastodon/{id} | Updates the TransportMastodon resource.
[**apiTransportMastodonIdPut**](TransportMastodonApi.md#apiTransportMastodonIdPut) | **PUT** /api/transport-mastodon/{id} | Replaces the TransportMastodon resource.
[**apiTransportMastodonPost**](TransportMastodonApi.md#apiTransportMastodonPost) | **POST** /api/transport-mastodon | Creates a TransportMastodon resource.



## apiTransportMastodonGetCollection

> [TransportMastodonGet] apiTransportMastodonGetCollection(opts)

Retrieves the collection of TransportMastodon resources.

Retrieves the collection of TransportMastodon resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMastodonApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMastodonGetCollection(opts, (error, data, response) => {
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

[**[TransportMastodonGet]**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMastodonIdDelete

> apiTransportMastodonIdDelete(id)

Removes the TransportMastodon resource.

Removes the TransportMastodon resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMastodonApi();
let id = "id_example"; // String | TransportMastodon identifier
apiInstance.apiTransportMastodonIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMastodon identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMastodonIdGet

> TransportMastodonGet apiTransportMastodonIdGet(id)

Retrieves a TransportMastodon resource.

Retrieves a TransportMastodon resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMastodonApi();
let id = "id_example"; // String | TransportMastodon identifier
apiInstance.apiTransportMastodonIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMastodon identifier | 

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMastodonIdPatch

> TransportMastodonGet apiTransportMastodonIdPatch(id, transportMastodonPatch)

Updates the TransportMastodon resource.

Updates the TransportMastodon resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMastodonApi();
let id = "id_example"; // String | TransportMastodon identifier
let transportMastodonPatch = new AlerterSystemApi.TransportMastodonPatch(); // TransportMastodonPatch | The updated TransportMastodon resource
apiInstance.apiTransportMastodonIdPatch(id, transportMastodonPatch, (error, data, response) => {
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
 **id** | **String**| TransportMastodon identifier | 
 **transportMastodonPatch** | [**TransportMastodonPatch**](TransportMastodonPatch.md)| The updated TransportMastodon resource | 

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMastodonIdPut

> TransportMastodonGet apiTransportMastodonIdPut(id, transportMastodonPut)

Replaces the TransportMastodon resource.

Replaces the TransportMastodon resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMastodonApi();
let id = "id_example"; // String | TransportMastodon identifier
let transportMastodonPut = new AlerterSystemApi.TransportMastodonPut(); // TransportMastodonPut | The updated TransportMastodon resource
apiInstance.apiTransportMastodonIdPut(id, transportMastodonPut, (error, data, response) => {
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
 **id** | **String**| TransportMastodon identifier | 
 **transportMastodonPut** | [**TransportMastodonPut**](TransportMastodonPut.md)| The updated TransportMastodon resource | 

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMastodonPost

> TransportMastodonGet apiTransportMastodonPost(transportMastodonPost)

Creates a TransportMastodon resource.

Creates a TransportMastodon resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMastodonApi();
let transportMastodonPost = new AlerterSystemApi.TransportMastodonPost(); // TransportMastodonPost | The new TransportMastodon resource
apiInstance.apiTransportMastodonPost(transportMastodonPost, (error, data, response) => {
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
 **transportMastodonPost** | [**TransportMastodonPost**](TransportMastodonPost.md)| The new TransportMastodon resource | 

### Return type

[**TransportMastodonGet**](TransportMastodonGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

