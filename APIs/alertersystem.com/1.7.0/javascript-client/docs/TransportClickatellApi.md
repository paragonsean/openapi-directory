# AlerterSystemApi.TransportClickatellApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportClickatellGetCollection**](TransportClickatellApi.md#apiTransportClickatellGetCollection) | **GET** /api/transport-clickatell | Retrieves the collection of TransportClickatell resources.
[**apiTransportClickatellIdDelete**](TransportClickatellApi.md#apiTransportClickatellIdDelete) | **DELETE** /api/transport-clickatell/{id} | Removes the TransportClickatell resource.
[**apiTransportClickatellIdGet**](TransportClickatellApi.md#apiTransportClickatellIdGet) | **GET** /api/transport-clickatell/{id} | Retrieves a TransportClickatell resource.
[**apiTransportClickatellIdPatch**](TransportClickatellApi.md#apiTransportClickatellIdPatch) | **PATCH** /api/transport-clickatell/{id} | Updates the TransportClickatell resource.
[**apiTransportClickatellIdPut**](TransportClickatellApi.md#apiTransportClickatellIdPut) | **PUT** /api/transport-clickatell/{id} | Replaces the TransportClickatell resource.
[**apiTransportClickatellPost**](TransportClickatellApi.md#apiTransportClickatellPost) | **POST** /api/transport-clickatell | Creates a TransportClickatell resource.



## apiTransportClickatellGetCollection

> [TransportClickatellGet] apiTransportClickatellGetCollection(opts)

Retrieves the collection of TransportClickatell resources.

Retrieves the collection of TransportClickatell resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickatellApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportClickatellGetCollection(opts, (error, data, response) => {
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

[**[TransportClickatellGet]**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickatellIdDelete

> apiTransportClickatellIdDelete(id)

Removes the TransportClickatell resource.

Removes the TransportClickatell resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickatellApi();
let id = "id_example"; // String | TransportClickatell identifier
apiInstance.apiTransportClickatellIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportClickatell identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportClickatellIdGet

> TransportClickatellGet apiTransportClickatellIdGet(id)

Retrieves a TransportClickatell resource.

Retrieves a TransportClickatell resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickatellApi();
let id = "id_example"; // String | TransportClickatell identifier
apiInstance.apiTransportClickatellIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportClickatell identifier | 

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickatellIdPatch

> TransportClickatellGet apiTransportClickatellIdPatch(id, transportClickatellPatch)

Updates the TransportClickatell resource.

Updates the TransportClickatell resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickatellApi();
let id = "id_example"; // String | TransportClickatell identifier
let transportClickatellPatch = new AlerterSystemApi.TransportClickatellPatch(); // TransportClickatellPatch | The updated TransportClickatell resource
apiInstance.apiTransportClickatellIdPatch(id, transportClickatellPatch, (error, data, response) => {
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
 **id** | **String**| TransportClickatell identifier | 
 **transportClickatellPatch** | [**TransportClickatellPatch**](TransportClickatellPatch.md)| The updated TransportClickatell resource | 

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickatellIdPut

> TransportClickatellGet apiTransportClickatellIdPut(id, transportClickatellPut)

Replaces the TransportClickatell resource.

Replaces the TransportClickatell resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickatellApi();
let id = "id_example"; // String | TransportClickatell identifier
let transportClickatellPut = new AlerterSystemApi.TransportClickatellPut(); // TransportClickatellPut | The updated TransportClickatell resource
apiInstance.apiTransportClickatellIdPut(id, transportClickatellPut, (error, data, response) => {
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
 **id** | **String**| TransportClickatell identifier | 
 **transportClickatellPut** | [**TransportClickatellPut**](TransportClickatellPut.md)| The updated TransportClickatell resource | 

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickatellPost

> TransportClickatellGet apiTransportClickatellPost(transportClickatellPost)

Creates a TransportClickatell resource.

Creates a TransportClickatell resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickatellApi();
let transportClickatellPost = new AlerterSystemApi.TransportClickatellPost(); // TransportClickatellPost | The new TransportClickatell resource
apiInstance.apiTransportClickatellPost(transportClickatellPost, (error, data, response) => {
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
 **transportClickatellPost** | [**TransportClickatellPost**](TransportClickatellPost.md)| The new TransportClickatell resource | 

### Return type

[**TransportClickatellGet**](TransportClickatellGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

