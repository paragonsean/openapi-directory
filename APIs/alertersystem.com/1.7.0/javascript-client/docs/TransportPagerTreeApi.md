# AlerterSystemApi.TransportPagerTreeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportPagerTreeGetCollection**](TransportPagerTreeApi.md#apiTransportPagerTreeGetCollection) | **GET** /api/transport-pager-tree | Retrieves the collection of TransportPagerTree resources.
[**apiTransportPagerTreeIdDelete**](TransportPagerTreeApi.md#apiTransportPagerTreeIdDelete) | **DELETE** /api/transport-pager-tree/{id} | Removes the TransportPagerTree resource.
[**apiTransportPagerTreeIdGet**](TransportPagerTreeApi.md#apiTransportPagerTreeIdGet) | **GET** /api/transport-pager-tree/{id} | Retrieves a TransportPagerTree resource.
[**apiTransportPagerTreeIdPatch**](TransportPagerTreeApi.md#apiTransportPagerTreeIdPatch) | **PATCH** /api/transport-pager-tree/{id} | Updates the TransportPagerTree resource.
[**apiTransportPagerTreeIdPut**](TransportPagerTreeApi.md#apiTransportPagerTreeIdPut) | **PUT** /api/transport-pager-tree/{id} | Replaces the TransportPagerTree resource.
[**apiTransportPagerTreePost**](TransportPagerTreeApi.md#apiTransportPagerTreePost) | **POST** /api/transport-pager-tree | Creates a TransportPagerTree resource.



## apiTransportPagerTreeGetCollection

> [TransportPagerTreeGet] apiTransportPagerTreeGetCollection(opts)

Retrieves the collection of TransportPagerTree resources.

Retrieves the collection of TransportPagerTree resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerTreeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportPagerTreeGetCollection(opts, (error, data, response) => {
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

[**[TransportPagerTreeGet]**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerTreeIdDelete

> apiTransportPagerTreeIdDelete(id)

Removes the TransportPagerTree resource.

Removes the TransportPagerTree resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerTreeApi();
let id = "id_example"; // String | TransportPagerTree identifier
apiInstance.apiTransportPagerTreeIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportPagerTree identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportPagerTreeIdGet

> TransportPagerTreeGet apiTransportPagerTreeIdGet(id)

Retrieves a TransportPagerTree resource.

Retrieves a TransportPagerTree resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerTreeApi();
let id = "id_example"; // String | TransportPagerTree identifier
apiInstance.apiTransportPagerTreeIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportPagerTree identifier | 

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerTreeIdPatch

> TransportPagerTreeGet apiTransportPagerTreeIdPatch(id, transportPagerTreePatch)

Updates the TransportPagerTree resource.

Updates the TransportPagerTree resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerTreeApi();
let id = "id_example"; // String | TransportPagerTree identifier
let transportPagerTreePatch = new AlerterSystemApi.TransportPagerTreePatch(); // TransportPagerTreePatch | The updated TransportPagerTree resource
apiInstance.apiTransportPagerTreeIdPatch(id, transportPagerTreePatch, (error, data, response) => {
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
 **id** | **String**| TransportPagerTree identifier | 
 **transportPagerTreePatch** | [**TransportPagerTreePatch**](TransportPagerTreePatch.md)| The updated TransportPagerTree resource | 

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerTreeIdPut

> TransportPagerTreeGet apiTransportPagerTreeIdPut(id, transportPagerTreePut)

Replaces the TransportPagerTree resource.

Replaces the TransportPagerTree resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerTreeApi();
let id = "id_example"; // String | TransportPagerTree identifier
let transportPagerTreePut = new AlerterSystemApi.TransportPagerTreePut(); // TransportPagerTreePut | The updated TransportPagerTree resource
apiInstance.apiTransportPagerTreeIdPut(id, transportPagerTreePut, (error, data, response) => {
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
 **id** | **String**| TransportPagerTree identifier | 
 **transportPagerTreePut** | [**TransportPagerTreePut**](TransportPagerTreePut.md)| The updated TransportPagerTree resource | 

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerTreePost

> TransportPagerTreeGet apiTransportPagerTreePost(transportPagerTreePost)

Creates a TransportPagerTree resource.

Creates a TransportPagerTree resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerTreeApi();
let transportPagerTreePost = new AlerterSystemApi.TransportPagerTreePost(); // TransportPagerTreePost | The new TransportPagerTree resource
apiInstance.apiTransportPagerTreePost(transportPagerTreePost, (error, data, response) => {
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
 **transportPagerTreePost** | [**TransportPagerTreePost**](TransportPagerTreePost.md)| The new TransportPagerTree resource | 

### Return type

[**TransportPagerTreeGet**](TransportPagerTreeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

