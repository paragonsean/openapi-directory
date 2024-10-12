# AlerterSystemApi.TransportIqsmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportIqsmsGetCollection**](TransportIqsmsApi.md#apiTransportIqsmsGetCollection) | **GET** /api/transport-iqsms | Retrieves the collection of TransportIqsms resources.
[**apiTransportIqsmsIdDelete**](TransportIqsmsApi.md#apiTransportIqsmsIdDelete) | **DELETE** /api/transport-iqsms/{id} | Removes the TransportIqsms resource.
[**apiTransportIqsmsIdGet**](TransportIqsmsApi.md#apiTransportIqsmsIdGet) | **GET** /api/transport-iqsms/{id} | Retrieves a TransportIqsms resource.
[**apiTransportIqsmsIdPatch**](TransportIqsmsApi.md#apiTransportIqsmsIdPatch) | **PATCH** /api/transport-iqsms/{id} | Updates the TransportIqsms resource.
[**apiTransportIqsmsIdPut**](TransportIqsmsApi.md#apiTransportIqsmsIdPut) | **PUT** /api/transport-iqsms/{id} | Replaces the TransportIqsms resource.
[**apiTransportIqsmsPost**](TransportIqsmsApi.md#apiTransportIqsmsPost) | **POST** /api/transport-iqsms | Creates a TransportIqsms resource.



## apiTransportIqsmsGetCollection

> [TransportIqsmsGet] apiTransportIqsmsGetCollection(opts)

Retrieves the collection of TransportIqsms resources.

Retrieves the collection of TransportIqsms resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportIqsmsApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportIqsmsGetCollection(opts, (error, data, response) => {
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

[**[TransportIqsmsGet]**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportIqsmsIdDelete

> apiTransportIqsmsIdDelete(id)

Removes the TransportIqsms resource.

Removes the TransportIqsms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportIqsmsApi();
let id = "id_example"; // String | TransportIqsms identifier
apiInstance.apiTransportIqsmsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportIqsms identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportIqsmsIdGet

> TransportIqsmsGet apiTransportIqsmsIdGet(id)

Retrieves a TransportIqsms resource.

Retrieves a TransportIqsms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportIqsmsApi();
let id = "id_example"; // String | TransportIqsms identifier
apiInstance.apiTransportIqsmsIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportIqsms identifier | 

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportIqsmsIdPatch

> TransportIqsmsGet apiTransportIqsmsIdPatch(id, transportIqsmsPatch)

Updates the TransportIqsms resource.

Updates the TransportIqsms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportIqsmsApi();
let id = "id_example"; // String | TransportIqsms identifier
let transportIqsmsPatch = new AlerterSystemApi.TransportIqsmsPatch(); // TransportIqsmsPatch | The updated TransportIqsms resource
apiInstance.apiTransportIqsmsIdPatch(id, transportIqsmsPatch, (error, data, response) => {
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
 **id** | **String**| TransportIqsms identifier | 
 **transportIqsmsPatch** | [**TransportIqsmsPatch**](TransportIqsmsPatch.md)| The updated TransportIqsms resource | 

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportIqsmsIdPut

> TransportIqsmsGet apiTransportIqsmsIdPut(id, transportIqsmsPut)

Replaces the TransportIqsms resource.

Replaces the TransportIqsms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportIqsmsApi();
let id = "id_example"; // String | TransportIqsms identifier
let transportIqsmsPut = new AlerterSystemApi.TransportIqsmsPut(); // TransportIqsmsPut | The updated TransportIqsms resource
apiInstance.apiTransportIqsmsIdPut(id, transportIqsmsPut, (error, data, response) => {
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
 **id** | **String**| TransportIqsms identifier | 
 **transportIqsmsPut** | [**TransportIqsmsPut**](TransportIqsmsPut.md)| The updated TransportIqsms resource | 

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportIqsmsPost

> TransportIqsmsGet apiTransportIqsmsPost(transportIqsmsPost)

Creates a TransportIqsms resource.

Creates a TransportIqsms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportIqsmsApi();
let transportIqsmsPost = new AlerterSystemApi.TransportIqsmsPost(); // TransportIqsmsPost | The new TransportIqsms resource
apiInstance.apiTransportIqsmsPost(transportIqsmsPost, (error, data, response) => {
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
 **transportIqsmsPost** | [**TransportIqsmsPost**](TransportIqsmsPost.md)| The new TransportIqsms resource | 

### Return type

[**TransportIqsmsGet**](TransportIqsmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

