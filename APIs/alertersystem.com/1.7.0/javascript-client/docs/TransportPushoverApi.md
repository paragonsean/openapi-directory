# AlerterSystemApi.TransportPushoverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportPushoverGetCollection**](TransportPushoverApi.md#apiTransportPushoverGetCollection) | **GET** /api/transport-pushover | Retrieves the collection of TransportPushover resources.
[**apiTransportPushoverIdDelete**](TransportPushoverApi.md#apiTransportPushoverIdDelete) | **DELETE** /api/transport-pushover/{id} | Removes the TransportPushover resource.
[**apiTransportPushoverIdGet**](TransportPushoverApi.md#apiTransportPushoverIdGet) | **GET** /api/transport-pushover/{id} | Retrieves a TransportPushover resource.
[**apiTransportPushoverIdPatch**](TransportPushoverApi.md#apiTransportPushoverIdPatch) | **PATCH** /api/transport-pushover/{id} | Updates the TransportPushover resource.
[**apiTransportPushoverIdPut**](TransportPushoverApi.md#apiTransportPushoverIdPut) | **PUT** /api/transport-pushover/{id} | Replaces the TransportPushover resource.
[**apiTransportPushoverPost**](TransportPushoverApi.md#apiTransportPushoverPost) | **POST** /api/transport-pushover | Creates a TransportPushover resource.



## apiTransportPushoverGetCollection

> [TransportPushoverGet] apiTransportPushoverGetCollection(opts)

Retrieves the collection of TransportPushover resources.

Retrieves the collection of TransportPushover resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushoverApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportPushoverGetCollection(opts, (error, data, response) => {
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

[**[TransportPushoverGet]**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushoverIdDelete

> apiTransportPushoverIdDelete(id)

Removes the TransportPushover resource.

Removes the TransportPushover resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushoverApi();
let id = "id_example"; // String | TransportPushover identifier
apiInstance.apiTransportPushoverIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportPushover identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportPushoverIdGet

> TransportPushoverGet apiTransportPushoverIdGet(id)

Retrieves a TransportPushover resource.

Retrieves a TransportPushover resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushoverApi();
let id = "id_example"; // String | TransportPushover identifier
apiInstance.apiTransportPushoverIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportPushover identifier | 

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushoverIdPatch

> TransportPushoverGet apiTransportPushoverIdPatch(id, transportPushoverPatch)

Updates the TransportPushover resource.

Updates the TransportPushover resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushoverApi();
let id = "id_example"; // String | TransportPushover identifier
let transportPushoverPatch = new AlerterSystemApi.TransportPushoverPatch(); // TransportPushoverPatch | The updated TransportPushover resource
apiInstance.apiTransportPushoverIdPatch(id, transportPushoverPatch, (error, data, response) => {
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
 **id** | **String**| TransportPushover identifier | 
 **transportPushoverPatch** | [**TransportPushoverPatch**](TransportPushoverPatch.md)| The updated TransportPushover resource | 

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushoverIdPut

> TransportPushoverGet apiTransportPushoverIdPut(id, transportPushoverPut)

Replaces the TransportPushover resource.

Replaces the TransportPushover resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushoverApi();
let id = "id_example"; // String | TransportPushover identifier
let transportPushoverPut = new AlerterSystemApi.TransportPushoverPut(); // TransportPushoverPut | The updated TransportPushover resource
apiInstance.apiTransportPushoverIdPut(id, transportPushoverPut, (error, data, response) => {
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
 **id** | **String**| TransportPushover identifier | 
 **transportPushoverPut** | [**TransportPushoverPut**](TransportPushoverPut.md)| The updated TransportPushover resource | 

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushoverPost

> TransportPushoverGet apiTransportPushoverPost(transportPushoverPost)

Creates a TransportPushover resource.

Creates a TransportPushover resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushoverApi();
let transportPushoverPost = new AlerterSystemApi.TransportPushoverPost(); // TransportPushoverPost | The new TransportPushover resource
apiInstance.apiTransportPushoverPost(transportPushoverPost, (error, data, response) => {
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
 **transportPushoverPost** | [**TransportPushoverPost**](TransportPushoverPost.md)| The new TransportPushover resource | 

### Return type

[**TransportPushoverGet**](TransportPushoverGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

