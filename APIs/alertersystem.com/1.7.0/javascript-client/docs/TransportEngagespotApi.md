# AlerterSystemApi.TransportEngagespotApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportEngagespotGetCollection**](TransportEngagespotApi.md#apiTransportEngagespotGetCollection) | **GET** /api/transport-engagespot | Retrieves the collection of TransportEngagespot resources.
[**apiTransportEngagespotIdDelete**](TransportEngagespotApi.md#apiTransportEngagespotIdDelete) | **DELETE** /api/transport-engagespot/{id} | Removes the TransportEngagespot resource.
[**apiTransportEngagespotIdGet**](TransportEngagespotApi.md#apiTransportEngagespotIdGet) | **GET** /api/transport-engagespot/{id} | Retrieves a TransportEngagespot resource.
[**apiTransportEngagespotIdPatch**](TransportEngagespotApi.md#apiTransportEngagespotIdPatch) | **PATCH** /api/transport-engagespot/{id} | Updates the TransportEngagespot resource.
[**apiTransportEngagespotIdPut**](TransportEngagespotApi.md#apiTransportEngagespotIdPut) | **PUT** /api/transport-engagespot/{id} | Replaces the TransportEngagespot resource.
[**apiTransportEngagespotPost**](TransportEngagespotApi.md#apiTransportEngagespotPost) | **POST** /api/transport-engagespot | Creates a TransportEngagespot resource.



## apiTransportEngagespotGetCollection

> [TransportEngagespotGet] apiTransportEngagespotGetCollection(opts)

Retrieves the collection of TransportEngagespot resources.

Retrieves the collection of TransportEngagespot resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEngagespotApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportEngagespotGetCollection(opts, (error, data, response) => {
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

[**[TransportEngagespotGet]**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEngagespotIdDelete

> apiTransportEngagespotIdDelete(id)

Removes the TransportEngagespot resource.

Removes the TransportEngagespot resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEngagespotApi();
let id = "id_example"; // String | TransportEngagespot identifier
apiInstance.apiTransportEngagespotIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportEngagespot identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportEngagespotIdGet

> TransportEngagespotGet apiTransportEngagespotIdGet(id)

Retrieves a TransportEngagespot resource.

Retrieves a TransportEngagespot resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEngagespotApi();
let id = "id_example"; // String | TransportEngagespot identifier
apiInstance.apiTransportEngagespotIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportEngagespot identifier | 

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEngagespotIdPatch

> TransportEngagespotGet apiTransportEngagespotIdPatch(id, transportEngagespotPatch)

Updates the TransportEngagespot resource.

Updates the TransportEngagespot resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEngagespotApi();
let id = "id_example"; // String | TransportEngagespot identifier
let transportEngagespotPatch = new AlerterSystemApi.TransportEngagespotPatch(); // TransportEngagespotPatch | The updated TransportEngagespot resource
apiInstance.apiTransportEngagespotIdPatch(id, transportEngagespotPatch, (error, data, response) => {
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
 **id** | **String**| TransportEngagespot identifier | 
 **transportEngagespotPatch** | [**TransportEngagespotPatch**](TransportEngagespotPatch.md)| The updated TransportEngagespot resource | 

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEngagespotIdPut

> TransportEngagespotGet apiTransportEngagespotIdPut(id, transportEngagespotPut)

Replaces the TransportEngagespot resource.

Replaces the TransportEngagespot resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEngagespotApi();
let id = "id_example"; // String | TransportEngagespot identifier
let transportEngagespotPut = new AlerterSystemApi.TransportEngagespotPut(); // TransportEngagespotPut | The updated TransportEngagespot resource
apiInstance.apiTransportEngagespotIdPut(id, transportEngagespotPut, (error, data, response) => {
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
 **id** | **String**| TransportEngagespot identifier | 
 **transportEngagespotPut** | [**TransportEngagespotPut**](TransportEngagespotPut.md)| The updated TransportEngagespot resource | 

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEngagespotPost

> TransportEngagespotGet apiTransportEngagespotPost(transportEngagespotPost)

Creates a TransportEngagespot resource.

Creates a TransportEngagespot resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEngagespotApi();
let transportEngagespotPost = new AlerterSystemApi.TransportEngagespotPost(); // TransportEngagespotPost | The new TransportEngagespot resource
apiInstance.apiTransportEngagespotPost(transportEngagespotPost, (error, data, response) => {
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
 **transportEngagespotPost** | [**TransportEngagespotPost**](TransportEngagespotPost.md)| The new TransportEngagespot resource | 

### Return type

[**TransportEngagespotGet**](TransportEngagespotGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

