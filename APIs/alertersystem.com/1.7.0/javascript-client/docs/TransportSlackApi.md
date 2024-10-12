# AlerterSystemApi.TransportSlackApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSlackGetCollection**](TransportSlackApi.md#apiTransportSlackGetCollection) | **GET** /api/transport-slack | Retrieves the collection of TransportSlack resources.
[**apiTransportSlackIdDelete**](TransportSlackApi.md#apiTransportSlackIdDelete) | **DELETE** /api/transport-slack/{id} | Removes the TransportSlack resource.
[**apiTransportSlackIdGet**](TransportSlackApi.md#apiTransportSlackIdGet) | **GET** /api/transport-slack/{id} | Retrieves a TransportSlack resource.
[**apiTransportSlackIdPatch**](TransportSlackApi.md#apiTransportSlackIdPatch) | **PATCH** /api/transport-slack/{id} | Updates the TransportSlack resource.
[**apiTransportSlackIdPut**](TransportSlackApi.md#apiTransportSlackIdPut) | **PUT** /api/transport-slack/{id} | Replaces the TransportSlack resource.
[**apiTransportSlackPost**](TransportSlackApi.md#apiTransportSlackPost) | **POST** /api/transport-slack | Creates a TransportSlack resource.



## apiTransportSlackGetCollection

> [TransportSlackGet] apiTransportSlackGetCollection(opts)

Retrieves the collection of TransportSlack resources.

Retrieves the collection of TransportSlack resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSlackApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSlackGetCollection(opts, (error, data, response) => {
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

[**[TransportSlackGet]**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSlackIdDelete

> apiTransportSlackIdDelete(id)

Removes the TransportSlack resource.

Removes the TransportSlack resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSlackApi();
let id = "id_example"; // String | TransportSlack identifier
apiInstance.apiTransportSlackIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSlack identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSlackIdGet

> TransportSlackGet apiTransportSlackIdGet(id)

Retrieves a TransportSlack resource.

Retrieves a TransportSlack resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSlackApi();
let id = "id_example"; // String | TransportSlack identifier
apiInstance.apiTransportSlackIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSlack identifier | 

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSlackIdPatch

> TransportSlackGet apiTransportSlackIdPatch(id, transportSlackPatch)

Updates the TransportSlack resource.

Updates the TransportSlack resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSlackApi();
let id = "id_example"; // String | TransportSlack identifier
let transportSlackPatch = new AlerterSystemApi.TransportSlackPatch(); // TransportSlackPatch | The updated TransportSlack resource
apiInstance.apiTransportSlackIdPatch(id, transportSlackPatch, (error, data, response) => {
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
 **id** | **String**| TransportSlack identifier | 
 **transportSlackPatch** | [**TransportSlackPatch**](TransportSlackPatch.md)| The updated TransportSlack resource | 

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSlackIdPut

> TransportSlackGet apiTransportSlackIdPut(id, transportSlackPut)

Replaces the TransportSlack resource.

Replaces the TransportSlack resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSlackApi();
let id = "id_example"; // String | TransportSlack identifier
let transportSlackPut = new AlerterSystemApi.TransportSlackPut(); // TransportSlackPut | The updated TransportSlack resource
apiInstance.apiTransportSlackIdPut(id, transportSlackPut, (error, data, response) => {
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
 **id** | **String**| TransportSlack identifier | 
 **transportSlackPut** | [**TransportSlackPut**](TransportSlackPut.md)| The updated TransportSlack resource | 

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSlackPost

> TransportSlackGet apiTransportSlackPost(transportSlackPost)

Creates a TransportSlack resource.

Creates a TransportSlack resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSlackApi();
let transportSlackPost = new AlerterSystemApi.TransportSlackPost(); // TransportSlackPost | The new TransportSlack resource
apiInstance.apiTransportSlackPost(transportSlackPost, (error, data, response) => {
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
 **transportSlackPost** | [**TransportSlackPost**](TransportSlackPost.md)| The new TransportSlack resource | 

### Return type

[**TransportSlackGet**](TransportSlackGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

