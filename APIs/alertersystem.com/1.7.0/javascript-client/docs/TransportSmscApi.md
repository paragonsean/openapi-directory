# AlerterSystemApi.TransportSmscApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSmscGetCollection**](TransportSmscApi.md#apiTransportSmscGetCollection) | **GET** /api/transport-smsc | Retrieves the collection of TransportSmsc resources.
[**apiTransportSmscIdDelete**](TransportSmscApi.md#apiTransportSmscIdDelete) | **DELETE** /api/transport-smsc/{id} | Removes the TransportSmsc resource.
[**apiTransportSmscIdGet**](TransportSmscApi.md#apiTransportSmscIdGet) | **GET** /api/transport-smsc/{id} | Retrieves a TransportSmsc resource.
[**apiTransportSmscIdPatch**](TransportSmscApi.md#apiTransportSmscIdPatch) | **PATCH** /api/transport-smsc/{id} | Updates the TransportSmsc resource.
[**apiTransportSmscIdPut**](TransportSmscApi.md#apiTransportSmscIdPut) | **PUT** /api/transport-smsc/{id} | Replaces the TransportSmsc resource.
[**apiTransportSmscPost**](TransportSmscApi.md#apiTransportSmscPost) | **POST** /api/transport-smsc | Creates a TransportSmsc resource.



## apiTransportSmscGetCollection

> [TransportSmscGet] apiTransportSmscGetCollection(opts)

Retrieves the collection of TransportSmsc resources.

Retrieves the collection of TransportSmsc resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmscApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSmscGetCollection(opts, (error, data, response) => {
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

[**[TransportSmscGet]**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmscIdDelete

> apiTransportSmscIdDelete(id)

Removes the TransportSmsc resource.

Removes the TransportSmsc resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmscApi();
let id = "id_example"; // String | TransportSmsc identifier
apiInstance.apiTransportSmscIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsc identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSmscIdGet

> TransportSmscGet apiTransportSmscIdGet(id)

Retrieves a TransportSmsc resource.

Retrieves a TransportSmsc resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmscApi();
let id = "id_example"; // String | TransportSmsc identifier
apiInstance.apiTransportSmscIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsc identifier | 

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmscIdPatch

> TransportSmscGet apiTransportSmscIdPatch(id, transportSmscPatch)

Updates the TransportSmsc resource.

Updates the TransportSmsc resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmscApi();
let id = "id_example"; // String | TransportSmsc identifier
let transportSmscPatch = new AlerterSystemApi.TransportSmscPatch(); // TransportSmscPatch | The updated TransportSmsc resource
apiInstance.apiTransportSmscIdPatch(id, transportSmscPatch, (error, data, response) => {
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
 **id** | **String**| TransportSmsc identifier | 
 **transportSmscPatch** | [**TransportSmscPatch**](TransportSmscPatch.md)| The updated TransportSmsc resource | 

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmscIdPut

> TransportSmscGet apiTransportSmscIdPut(id, transportSmscPut)

Replaces the TransportSmsc resource.

Replaces the TransportSmsc resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmscApi();
let id = "id_example"; // String | TransportSmsc identifier
let transportSmscPut = new AlerterSystemApi.TransportSmscPut(); // TransportSmscPut | The updated TransportSmsc resource
apiInstance.apiTransportSmscIdPut(id, transportSmscPut, (error, data, response) => {
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
 **id** | **String**| TransportSmsc identifier | 
 **transportSmscPut** | [**TransportSmscPut**](TransportSmscPut.md)| The updated TransportSmsc resource | 

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmscPost

> TransportSmscGet apiTransportSmscPost(transportSmscPost)

Creates a TransportSmsc resource.

Creates a TransportSmsc resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmscApi();
let transportSmscPost = new AlerterSystemApi.TransportSmscPost(); // TransportSmscPost | The new TransportSmsc resource
apiInstance.apiTransportSmscPost(transportSmscPost, (error, data, response) => {
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
 **transportSmscPost** | [**TransportSmscPost**](TransportSmscPost.md)| The new TransportSmsc resource | 

### Return type

[**TransportSmscGet**](TransportSmscGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

