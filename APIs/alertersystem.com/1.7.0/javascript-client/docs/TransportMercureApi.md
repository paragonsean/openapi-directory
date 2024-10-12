# AlerterSystemApi.TransportMercureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMercureGetCollection**](TransportMercureApi.md#apiTransportMercureGetCollection) | **GET** /api/transport-mercure | Retrieves the collection of TransportMercure resources.
[**apiTransportMercureIdDelete**](TransportMercureApi.md#apiTransportMercureIdDelete) | **DELETE** /api/transport-mercure/{id} | Removes the TransportMercure resource.
[**apiTransportMercureIdGet**](TransportMercureApi.md#apiTransportMercureIdGet) | **GET** /api/transport-mercure/{id} | Retrieves a TransportMercure resource.
[**apiTransportMercureIdPatch**](TransportMercureApi.md#apiTransportMercureIdPatch) | **PATCH** /api/transport-mercure/{id} | Updates the TransportMercure resource.
[**apiTransportMercureIdPut**](TransportMercureApi.md#apiTransportMercureIdPut) | **PUT** /api/transport-mercure/{id} | Replaces the TransportMercure resource.
[**apiTransportMercurePost**](TransportMercureApi.md#apiTransportMercurePost) | **POST** /api/transport-mercure | Creates a TransportMercure resource.



## apiTransportMercureGetCollection

> [TransportMercureGet] apiTransportMercureGetCollection(opts)

Retrieves the collection of TransportMercure resources.

Retrieves the collection of TransportMercure resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMercureApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMercureGetCollection(opts, (error, data, response) => {
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

[**[TransportMercureGet]**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMercureIdDelete

> apiTransportMercureIdDelete(id)

Removes the TransportMercure resource.

Removes the TransportMercure resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMercureApi();
let id = "id_example"; // String | TransportMercure identifier
apiInstance.apiTransportMercureIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMercure identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMercureIdGet

> TransportMercureGet apiTransportMercureIdGet(id)

Retrieves a TransportMercure resource.

Retrieves a TransportMercure resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMercureApi();
let id = "id_example"; // String | TransportMercure identifier
apiInstance.apiTransportMercureIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMercure identifier | 

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMercureIdPatch

> TransportMercureGet apiTransportMercureIdPatch(id, transportMercurePatch)

Updates the TransportMercure resource.

Updates the TransportMercure resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMercureApi();
let id = "id_example"; // String | TransportMercure identifier
let transportMercurePatch = new AlerterSystemApi.TransportMercurePatch(); // TransportMercurePatch | The updated TransportMercure resource
apiInstance.apiTransportMercureIdPatch(id, transportMercurePatch, (error, data, response) => {
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
 **id** | **String**| TransportMercure identifier | 
 **transportMercurePatch** | [**TransportMercurePatch**](TransportMercurePatch.md)| The updated TransportMercure resource | 

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMercureIdPut

> TransportMercureGet apiTransportMercureIdPut(id, transportMercurePut)

Replaces the TransportMercure resource.

Replaces the TransportMercure resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMercureApi();
let id = "id_example"; // String | TransportMercure identifier
let transportMercurePut = new AlerterSystemApi.TransportMercurePut(); // TransportMercurePut | The updated TransportMercure resource
apiInstance.apiTransportMercureIdPut(id, transportMercurePut, (error, data, response) => {
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
 **id** | **String**| TransportMercure identifier | 
 **transportMercurePut** | [**TransportMercurePut**](TransportMercurePut.md)| The updated TransportMercure resource | 

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMercurePost

> TransportMercureGet apiTransportMercurePost(transportMercurePost)

Creates a TransportMercure resource.

Creates a TransportMercure resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMercureApi();
let transportMercurePost = new AlerterSystemApi.TransportMercurePost(); // TransportMercurePost | The new TransportMercure resource
apiInstance.apiTransportMercurePost(transportMercurePost, (error, data, response) => {
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
 **transportMercurePost** | [**TransportMercurePost**](TransportMercurePost.md)| The new TransportMercure resource | 

### Return type

[**TransportMercureGet**](TransportMercureGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

