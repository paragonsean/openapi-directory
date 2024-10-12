# AlerterSystemApi.TransportChatworkApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportChatworkGetCollection**](TransportChatworkApi.md#apiTransportChatworkGetCollection) | **GET** /api/transport-chatwork | Retrieves the collection of TransportChatwork resources.
[**apiTransportChatworkIdDelete**](TransportChatworkApi.md#apiTransportChatworkIdDelete) | **DELETE** /api/transport-chatwork/{id} | Removes the TransportChatwork resource.
[**apiTransportChatworkIdGet**](TransportChatworkApi.md#apiTransportChatworkIdGet) | **GET** /api/transport-chatwork/{id} | Retrieves a TransportChatwork resource.
[**apiTransportChatworkIdPatch**](TransportChatworkApi.md#apiTransportChatworkIdPatch) | **PATCH** /api/transport-chatwork/{id} | Updates the TransportChatwork resource.
[**apiTransportChatworkIdPut**](TransportChatworkApi.md#apiTransportChatworkIdPut) | **PUT** /api/transport-chatwork/{id} | Replaces the TransportChatwork resource.
[**apiTransportChatworkPost**](TransportChatworkApi.md#apiTransportChatworkPost) | **POST** /api/transport-chatwork | Creates a TransportChatwork resource.



## apiTransportChatworkGetCollection

> [TransportChatworkGet] apiTransportChatworkGetCollection(opts)

Retrieves the collection of TransportChatwork resources.

Retrieves the collection of TransportChatwork resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportChatworkApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportChatworkGetCollection(opts, (error, data, response) => {
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

[**[TransportChatworkGet]**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportChatworkIdDelete

> apiTransportChatworkIdDelete(id)

Removes the TransportChatwork resource.

Removes the TransportChatwork resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportChatworkApi();
let id = "id_example"; // String | TransportChatwork identifier
apiInstance.apiTransportChatworkIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportChatwork identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportChatworkIdGet

> TransportChatworkGet apiTransportChatworkIdGet(id)

Retrieves a TransportChatwork resource.

Retrieves a TransportChatwork resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportChatworkApi();
let id = "id_example"; // String | TransportChatwork identifier
apiInstance.apiTransportChatworkIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportChatwork identifier | 

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportChatworkIdPatch

> TransportChatworkGet apiTransportChatworkIdPatch(id, transportChatworkPatch)

Updates the TransportChatwork resource.

Updates the TransportChatwork resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportChatworkApi();
let id = "id_example"; // String | TransportChatwork identifier
let transportChatworkPatch = new AlerterSystemApi.TransportChatworkPatch(); // TransportChatworkPatch | The updated TransportChatwork resource
apiInstance.apiTransportChatworkIdPatch(id, transportChatworkPatch, (error, data, response) => {
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
 **id** | **String**| TransportChatwork identifier | 
 **transportChatworkPatch** | [**TransportChatworkPatch**](TransportChatworkPatch.md)| The updated TransportChatwork resource | 

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportChatworkIdPut

> TransportChatworkGet apiTransportChatworkIdPut(id, transportChatworkPut)

Replaces the TransportChatwork resource.

Replaces the TransportChatwork resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportChatworkApi();
let id = "id_example"; // String | TransportChatwork identifier
let transportChatworkPut = new AlerterSystemApi.TransportChatworkPut(); // TransportChatworkPut | The updated TransportChatwork resource
apiInstance.apiTransportChatworkIdPut(id, transportChatworkPut, (error, data, response) => {
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
 **id** | **String**| TransportChatwork identifier | 
 **transportChatworkPut** | [**TransportChatworkPut**](TransportChatworkPut.md)| The updated TransportChatwork resource | 

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportChatworkPost

> TransportChatworkGet apiTransportChatworkPost(transportChatworkPost)

Creates a TransportChatwork resource.

Creates a TransportChatwork resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportChatworkApi();
let transportChatworkPost = new AlerterSystemApi.TransportChatworkPost(); // TransportChatworkPost | The new TransportChatwork resource
apiInstance.apiTransportChatworkPost(transportChatworkPost, (error, data, response) => {
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
 **transportChatworkPost** | [**TransportChatworkPost**](TransportChatworkPost.md)| The new TransportChatwork resource | 

### Return type

[**TransportChatworkGet**](TransportChatworkGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

