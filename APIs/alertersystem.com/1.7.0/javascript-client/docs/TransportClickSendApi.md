# AlerterSystemApi.TransportClickSendApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportClickSendGetCollection**](TransportClickSendApi.md#apiTransportClickSendGetCollection) | **GET** /api/transport-click-send | Retrieves the collection of TransportClickSend resources.
[**apiTransportClickSendIdDelete**](TransportClickSendApi.md#apiTransportClickSendIdDelete) | **DELETE** /api/transport-click-send/{id} | Removes the TransportClickSend resource.
[**apiTransportClickSendIdGet**](TransportClickSendApi.md#apiTransportClickSendIdGet) | **GET** /api/transport-click-send/{id} | Retrieves a TransportClickSend resource.
[**apiTransportClickSendIdPatch**](TransportClickSendApi.md#apiTransportClickSendIdPatch) | **PATCH** /api/transport-click-send/{id} | Updates the TransportClickSend resource.
[**apiTransportClickSendIdPut**](TransportClickSendApi.md#apiTransportClickSendIdPut) | **PUT** /api/transport-click-send/{id} | Replaces the TransportClickSend resource.
[**apiTransportClickSendPost**](TransportClickSendApi.md#apiTransportClickSendPost) | **POST** /api/transport-click-send | Creates a TransportClickSend resource.



## apiTransportClickSendGetCollection

> [TransportClickSendGet] apiTransportClickSendGetCollection(opts)

Retrieves the collection of TransportClickSend resources.

Retrieves the collection of TransportClickSend resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickSendApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportClickSendGetCollection(opts, (error, data, response) => {
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

[**[TransportClickSendGet]**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickSendIdDelete

> apiTransportClickSendIdDelete(id)

Removes the TransportClickSend resource.

Removes the TransportClickSend resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickSendApi();
let id = "id_example"; // String | TransportClickSend identifier
apiInstance.apiTransportClickSendIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportClickSend identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportClickSendIdGet

> TransportClickSendGet apiTransportClickSendIdGet(id)

Retrieves a TransportClickSend resource.

Retrieves a TransportClickSend resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickSendApi();
let id = "id_example"; // String | TransportClickSend identifier
apiInstance.apiTransportClickSendIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportClickSend identifier | 

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickSendIdPatch

> TransportClickSendGet apiTransportClickSendIdPatch(id, transportClickSendPatch)

Updates the TransportClickSend resource.

Updates the TransportClickSend resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickSendApi();
let id = "id_example"; // String | TransportClickSend identifier
let transportClickSendPatch = new AlerterSystemApi.TransportClickSendPatch(); // TransportClickSendPatch | The updated TransportClickSend resource
apiInstance.apiTransportClickSendIdPatch(id, transportClickSendPatch, (error, data, response) => {
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
 **id** | **String**| TransportClickSend identifier | 
 **transportClickSendPatch** | [**TransportClickSendPatch**](TransportClickSendPatch.md)| The updated TransportClickSend resource | 

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickSendIdPut

> TransportClickSendGet apiTransportClickSendIdPut(id, transportClickSendPut)

Replaces the TransportClickSend resource.

Replaces the TransportClickSend resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickSendApi();
let id = "id_example"; // String | TransportClickSend identifier
let transportClickSendPut = new AlerterSystemApi.TransportClickSendPut(); // TransportClickSendPut | The updated TransportClickSend resource
apiInstance.apiTransportClickSendIdPut(id, transportClickSendPut, (error, data, response) => {
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
 **id** | **String**| TransportClickSend identifier | 
 **transportClickSendPut** | [**TransportClickSendPut**](TransportClickSendPut.md)| The updated TransportClickSend resource | 

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportClickSendPost

> TransportClickSendGet apiTransportClickSendPost(transportClickSendPost)

Creates a TransportClickSend resource.

Creates a TransportClickSend resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportClickSendApi();
let transportClickSendPost = new AlerterSystemApi.TransportClickSendPost(); // TransportClickSendPost | The new TransportClickSend resource
apiInstance.apiTransportClickSendPost(transportClickSendPost, (error, data, response) => {
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
 **transportClickSendPost** | [**TransportClickSendPost**](TransportClickSendPost.md)| The new TransportClickSend resource | 

### Return type

[**TransportClickSendGet**](TransportClickSendGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

