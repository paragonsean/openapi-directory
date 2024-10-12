# AlerterSystemApi.TransportPushyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportPushyGetCollection**](TransportPushyApi.md#apiTransportPushyGetCollection) | **GET** /api/transport-pushy | Retrieves the collection of TransportPushy resources.
[**apiTransportPushyIdDelete**](TransportPushyApi.md#apiTransportPushyIdDelete) | **DELETE** /api/transport-pushy/{id} | Removes the TransportPushy resource.
[**apiTransportPushyIdGet**](TransportPushyApi.md#apiTransportPushyIdGet) | **GET** /api/transport-pushy/{id} | Retrieves a TransportPushy resource.
[**apiTransportPushyIdPatch**](TransportPushyApi.md#apiTransportPushyIdPatch) | **PATCH** /api/transport-pushy/{id} | Updates the TransportPushy resource.
[**apiTransportPushyIdPut**](TransportPushyApi.md#apiTransportPushyIdPut) | **PUT** /api/transport-pushy/{id} | Replaces the TransportPushy resource.
[**apiTransportPushyPost**](TransportPushyApi.md#apiTransportPushyPost) | **POST** /api/transport-pushy | Creates a TransportPushy resource.



## apiTransportPushyGetCollection

> [TransportPushyGet] apiTransportPushyGetCollection(opts)

Retrieves the collection of TransportPushy resources.

Retrieves the collection of TransportPushy resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushyApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportPushyGetCollection(opts, (error, data, response) => {
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

[**[TransportPushyGet]**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushyIdDelete

> apiTransportPushyIdDelete(id)

Removes the TransportPushy resource.

Removes the TransportPushy resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushyApi();
let id = "id_example"; // String | TransportPushy identifier
apiInstance.apiTransportPushyIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportPushy identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportPushyIdGet

> TransportPushyGet apiTransportPushyIdGet(id)

Retrieves a TransportPushy resource.

Retrieves a TransportPushy resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushyApi();
let id = "id_example"; // String | TransportPushy identifier
apiInstance.apiTransportPushyIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportPushy identifier | 

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushyIdPatch

> TransportPushyGet apiTransportPushyIdPatch(id, transportPushyPatch)

Updates the TransportPushy resource.

Updates the TransportPushy resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushyApi();
let id = "id_example"; // String | TransportPushy identifier
let transportPushyPatch = new AlerterSystemApi.TransportPushyPatch(); // TransportPushyPatch | The updated TransportPushy resource
apiInstance.apiTransportPushyIdPatch(id, transportPushyPatch, (error, data, response) => {
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
 **id** | **String**| TransportPushy identifier | 
 **transportPushyPatch** | [**TransportPushyPatch**](TransportPushyPatch.md)| The updated TransportPushy resource | 

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushyIdPut

> TransportPushyGet apiTransportPushyIdPut(id, transportPushyPut)

Replaces the TransportPushy resource.

Replaces the TransportPushy resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushyApi();
let id = "id_example"; // String | TransportPushy identifier
let transportPushyPut = new AlerterSystemApi.TransportPushyPut(); // TransportPushyPut | The updated TransportPushy resource
apiInstance.apiTransportPushyIdPut(id, transportPushyPut, (error, data, response) => {
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
 **id** | **String**| TransportPushy identifier | 
 **transportPushyPut** | [**TransportPushyPut**](TransportPushyPut.md)| The updated TransportPushy resource | 

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushyPost

> TransportPushyGet apiTransportPushyPost(transportPushyPost)

Creates a TransportPushy resource.

Creates a TransportPushy resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushyApi();
let transportPushyPost = new AlerterSystemApi.TransportPushyPost(); // TransportPushyPost | The new TransportPushy resource
apiInstance.apiTransportPushyPost(transportPushyPost, (error, data, response) => {
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
 **transportPushyPost** | [**TransportPushyPost**](TransportPushyPost.md)| The new TransportPushy resource | 

### Return type

[**TransportPushyGet**](TransportPushyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

