# AlerterSystemApi.TransportAllMySmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportAllMySmsGetCollection**](TransportAllMySmsApi.md#apiTransportAllMySmsGetCollection) | **GET** /api/transport-all-my-sms | Retrieves the collection of TransportAllMySms resources.
[**apiTransportAllMySmsIdDelete**](TransportAllMySmsApi.md#apiTransportAllMySmsIdDelete) | **DELETE** /api/transport-all-my-sms/{id} | Removes the TransportAllMySms resource.
[**apiTransportAllMySmsIdGet**](TransportAllMySmsApi.md#apiTransportAllMySmsIdGet) | **GET** /api/transport-all-my-sms/{id} | Retrieves a TransportAllMySms resource.
[**apiTransportAllMySmsIdPatch**](TransportAllMySmsApi.md#apiTransportAllMySmsIdPatch) | **PATCH** /api/transport-all-my-sms/{id} | Updates the TransportAllMySms resource.
[**apiTransportAllMySmsIdPut**](TransportAllMySmsApi.md#apiTransportAllMySmsIdPut) | **PUT** /api/transport-all-my-sms/{id} | Replaces the TransportAllMySms resource.
[**apiTransportAllMySmsPost**](TransportAllMySmsApi.md#apiTransportAllMySmsPost) | **POST** /api/transport-all-my-sms | Creates a TransportAllMySms resource.



## apiTransportAllMySmsGetCollection

> [TransportAllMySmsGet] apiTransportAllMySmsGetCollection(opts)

Retrieves the collection of TransportAllMySms resources.

Retrieves the collection of TransportAllMySms resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAllMySmsApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportAllMySmsGetCollection(opts, (error, data, response) => {
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

[**[TransportAllMySmsGet]**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAllMySmsIdDelete

> apiTransportAllMySmsIdDelete(id)

Removes the TransportAllMySms resource.

Removes the TransportAllMySms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAllMySmsApi();
let id = "id_example"; // String | TransportAllMySms identifier
apiInstance.apiTransportAllMySmsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportAllMySms identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportAllMySmsIdGet

> TransportAllMySmsGet apiTransportAllMySmsIdGet(id)

Retrieves a TransportAllMySms resource.

Retrieves a TransportAllMySms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAllMySmsApi();
let id = "id_example"; // String | TransportAllMySms identifier
apiInstance.apiTransportAllMySmsIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportAllMySms identifier | 

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAllMySmsIdPatch

> TransportAllMySmsGet apiTransportAllMySmsIdPatch(id, transportAllMySmsPatch)

Updates the TransportAllMySms resource.

Updates the TransportAllMySms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAllMySmsApi();
let id = "id_example"; // String | TransportAllMySms identifier
let transportAllMySmsPatch = new AlerterSystemApi.TransportAllMySmsPatch(); // TransportAllMySmsPatch | The updated TransportAllMySms resource
apiInstance.apiTransportAllMySmsIdPatch(id, transportAllMySmsPatch, (error, data, response) => {
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
 **id** | **String**| TransportAllMySms identifier | 
 **transportAllMySmsPatch** | [**TransportAllMySmsPatch**](TransportAllMySmsPatch.md)| The updated TransportAllMySms resource | 

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAllMySmsIdPut

> TransportAllMySmsGet apiTransportAllMySmsIdPut(id, transportAllMySmsPut)

Replaces the TransportAllMySms resource.

Replaces the TransportAllMySms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAllMySmsApi();
let id = "id_example"; // String | TransportAllMySms identifier
let transportAllMySmsPut = new AlerterSystemApi.TransportAllMySmsPut(); // TransportAllMySmsPut | The updated TransportAllMySms resource
apiInstance.apiTransportAllMySmsIdPut(id, transportAllMySmsPut, (error, data, response) => {
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
 **id** | **String**| TransportAllMySms identifier | 
 **transportAllMySmsPut** | [**TransportAllMySmsPut**](TransportAllMySmsPut.md)| The updated TransportAllMySms resource | 

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAllMySmsPost

> TransportAllMySmsGet apiTransportAllMySmsPost(transportAllMySmsPost)

Creates a TransportAllMySms resource.

Creates a TransportAllMySms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAllMySmsApi();
let transportAllMySmsPost = new AlerterSystemApi.TransportAllMySmsPost(); // TransportAllMySmsPost | The new TransportAllMySms resource
apiInstance.apiTransportAllMySmsPost(transportAllMySmsPost, (error, data, response) => {
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
 **transportAllMySmsPost** | [**TransportAllMySmsPost**](TransportAllMySmsPost.md)| The new TransportAllMySms resource | 

### Return type

[**TransportAllMySmsGet**](TransportAllMySmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

