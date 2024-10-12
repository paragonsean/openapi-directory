# AlerterSystemApi.TransportKazInfoTehApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportKazInfoTehGetCollection**](TransportKazInfoTehApi.md#apiTransportKazInfoTehGetCollection) | **GET** /api/transport-kaz-info-teh | Retrieves the collection of TransportKazInfoTeh resources.
[**apiTransportKazInfoTehIdDelete**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdDelete) | **DELETE** /api/transport-kaz-info-teh/{id} | Removes the TransportKazInfoTeh resource.
[**apiTransportKazInfoTehIdGet**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdGet) | **GET** /api/transport-kaz-info-teh/{id} | Retrieves a TransportKazInfoTeh resource.
[**apiTransportKazInfoTehIdPatch**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdPatch) | **PATCH** /api/transport-kaz-info-teh/{id} | Updates the TransportKazInfoTeh resource.
[**apiTransportKazInfoTehIdPut**](TransportKazInfoTehApi.md#apiTransportKazInfoTehIdPut) | **PUT** /api/transport-kaz-info-teh/{id} | Replaces the TransportKazInfoTeh resource.
[**apiTransportKazInfoTehPost**](TransportKazInfoTehApi.md#apiTransportKazInfoTehPost) | **POST** /api/transport-kaz-info-teh | Creates a TransportKazInfoTeh resource.



## apiTransportKazInfoTehGetCollection

> [TransportKazInfoTehGet] apiTransportKazInfoTehGetCollection(opts)

Retrieves the collection of TransportKazInfoTeh resources.

Retrieves the collection of TransportKazInfoTeh resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportKazInfoTehApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportKazInfoTehGetCollection(opts, (error, data, response) => {
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

[**[TransportKazInfoTehGet]**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportKazInfoTehIdDelete

> apiTransportKazInfoTehIdDelete(id)

Removes the TransportKazInfoTeh resource.

Removes the TransportKazInfoTeh resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportKazInfoTehApi();
let id = "id_example"; // String | TransportKazInfoTeh identifier
apiInstance.apiTransportKazInfoTehIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportKazInfoTeh identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportKazInfoTehIdGet

> TransportKazInfoTehGet apiTransportKazInfoTehIdGet(id)

Retrieves a TransportKazInfoTeh resource.

Retrieves a TransportKazInfoTeh resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportKazInfoTehApi();
let id = "id_example"; // String | TransportKazInfoTeh identifier
apiInstance.apiTransportKazInfoTehIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportKazInfoTeh identifier | 

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportKazInfoTehIdPatch

> TransportKazInfoTehGet apiTransportKazInfoTehIdPatch(id, transportKazInfoTehPatch)

Updates the TransportKazInfoTeh resource.

Updates the TransportKazInfoTeh resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportKazInfoTehApi();
let id = "id_example"; // String | TransportKazInfoTeh identifier
let transportKazInfoTehPatch = new AlerterSystemApi.TransportKazInfoTehPatch(); // TransportKazInfoTehPatch | The updated TransportKazInfoTeh resource
apiInstance.apiTransportKazInfoTehIdPatch(id, transportKazInfoTehPatch, (error, data, response) => {
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
 **id** | **String**| TransportKazInfoTeh identifier | 
 **transportKazInfoTehPatch** | [**TransportKazInfoTehPatch**](TransportKazInfoTehPatch.md)| The updated TransportKazInfoTeh resource | 

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportKazInfoTehIdPut

> TransportKazInfoTehGet apiTransportKazInfoTehIdPut(id, transportKazInfoTehPut)

Replaces the TransportKazInfoTeh resource.

Replaces the TransportKazInfoTeh resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportKazInfoTehApi();
let id = "id_example"; // String | TransportKazInfoTeh identifier
let transportKazInfoTehPut = new AlerterSystemApi.TransportKazInfoTehPut(); // TransportKazInfoTehPut | The updated TransportKazInfoTeh resource
apiInstance.apiTransportKazInfoTehIdPut(id, transportKazInfoTehPut, (error, data, response) => {
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
 **id** | **String**| TransportKazInfoTeh identifier | 
 **transportKazInfoTehPut** | [**TransportKazInfoTehPut**](TransportKazInfoTehPut.md)| The updated TransportKazInfoTeh resource | 

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportKazInfoTehPost

> TransportKazInfoTehGet apiTransportKazInfoTehPost(transportKazInfoTehPost)

Creates a TransportKazInfoTeh resource.

Creates a TransportKazInfoTeh resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportKazInfoTehApi();
let transportKazInfoTehPost = new AlerterSystemApi.TransportKazInfoTehPost(); // TransportKazInfoTehPost | The new TransportKazInfoTeh resource
apiInstance.apiTransportKazInfoTehPost(transportKazInfoTehPost, (error, data, response) => {
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
 **transportKazInfoTehPost** | [**TransportKazInfoTehPost**](TransportKazInfoTehPost.md)| The new TransportKazInfoTeh resource | 

### Return type

[**TransportKazInfoTehGet**](TransportKazInfoTehGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

