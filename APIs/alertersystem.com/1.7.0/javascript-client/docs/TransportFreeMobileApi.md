# AlerterSystemApi.TransportFreeMobileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportFreeMobileGetCollection**](TransportFreeMobileApi.md#apiTransportFreeMobileGetCollection) | **GET** /api/transport-free-mobile | Retrieves the collection of TransportFreeMobile resources.
[**apiTransportFreeMobileIdDelete**](TransportFreeMobileApi.md#apiTransportFreeMobileIdDelete) | **DELETE** /api/transport-free-mobile/{id} | Removes the TransportFreeMobile resource.
[**apiTransportFreeMobileIdGet**](TransportFreeMobileApi.md#apiTransportFreeMobileIdGet) | **GET** /api/transport-free-mobile/{id} | Retrieves a TransportFreeMobile resource.
[**apiTransportFreeMobileIdPatch**](TransportFreeMobileApi.md#apiTransportFreeMobileIdPatch) | **PATCH** /api/transport-free-mobile/{id} | Updates the TransportFreeMobile resource.
[**apiTransportFreeMobileIdPut**](TransportFreeMobileApi.md#apiTransportFreeMobileIdPut) | **PUT** /api/transport-free-mobile/{id} | Replaces the TransportFreeMobile resource.
[**apiTransportFreeMobilePost**](TransportFreeMobileApi.md#apiTransportFreeMobilePost) | **POST** /api/transport-free-mobile | Creates a TransportFreeMobile resource.



## apiTransportFreeMobileGetCollection

> [TransportFreeMobileGet] apiTransportFreeMobileGetCollection(opts)

Retrieves the collection of TransportFreeMobile resources.

Retrieves the collection of TransportFreeMobile resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreeMobileApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportFreeMobileGetCollection(opts, (error, data, response) => {
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

[**[TransportFreeMobileGet]**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreeMobileIdDelete

> apiTransportFreeMobileIdDelete(id)

Removes the TransportFreeMobile resource.

Removes the TransportFreeMobile resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreeMobileApi();
let id = "id_example"; // String | TransportFreeMobile identifier
apiInstance.apiTransportFreeMobileIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportFreeMobile identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportFreeMobileIdGet

> TransportFreeMobileGet apiTransportFreeMobileIdGet(id)

Retrieves a TransportFreeMobile resource.

Retrieves a TransportFreeMobile resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreeMobileApi();
let id = "id_example"; // String | TransportFreeMobile identifier
apiInstance.apiTransportFreeMobileIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportFreeMobile identifier | 

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreeMobileIdPatch

> TransportFreeMobileGet apiTransportFreeMobileIdPatch(id, transportFreeMobilePatch)

Updates the TransportFreeMobile resource.

Updates the TransportFreeMobile resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreeMobileApi();
let id = "id_example"; // String | TransportFreeMobile identifier
let transportFreeMobilePatch = new AlerterSystemApi.TransportFreeMobilePatch(); // TransportFreeMobilePatch | The updated TransportFreeMobile resource
apiInstance.apiTransportFreeMobileIdPatch(id, transportFreeMobilePatch, (error, data, response) => {
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
 **id** | **String**| TransportFreeMobile identifier | 
 **transportFreeMobilePatch** | [**TransportFreeMobilePatch**](TransportFreeMobilePatch.md)| The updated TransportFreeMobile resource | 

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreeMobileIdPut

> TransportFreeMobileGet apiTransportFreeMobileIdPut(id, transportFreeMobilePut)

Replaces the TransportFreeMobile resource.

Replaces the TransportFreeMobile resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreeMobileApi();
let id = "id_example"; // String | TransportFreeMobile identifier
let transportFreeMobilePut = new AlerterSystemApi.TransportFreeMobilePut(); // TransportFreeMobilePut | The updated TransportFreeMobile resource
apiInstance.apiTransportFreeMobileIdPut(id, transportFreeMobilePut, (error, data, response) => {
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
 **id** | **String**| TransportFreeMobile identifier | 
 **transportFreeMobilePut** | [**TransportFreeMobilePut**](TransportFreeMobilePut.md)| The updated TransportFreeMobile resource | 

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFreeMobilePost

> TransportFreeMobileGet apiTransportFreeMobilePost(transportFreeMobilePost)

Creates a TransportFreeMobile resource.

Creates a TransportFreeMobile resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFreeMobileApi();
let transportFreeMobilePost = new AlerterSystemApi.TransportFreeMobilePost(); // TransportFreeMobilePost | The new TransportFreeMobile resource
apiInstance.apiTransportFreeMobilePost(transportFreeMobilePost, (error, data, response) => {
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
 **transportFreeMobilePost** | [**TransportFreeMobilePost**](TransportFreeMobilePost.md)| The new TransportFreeMobile resource | 

### Return type

[**TransportFreeMobileGet**](TransportFreeMobileGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

