# AlerterSystemApi.TransportDiscordApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportDiscordGetCollection**](TransportDiscordApi.md#apiTransportDiscordGetCollection) | **GET** /api/transport-discord | Retrieves the collection of TransportDiscord resources.
[**apiTransportDiscordIdDelete**](TransportDiscordApi.md#apiTransportDiscordIdDelete) | **DELETE** /api/transport-discord/{id} | Removes the TransportDiscord resource.
[**apiTransportDiscordIdGet**](TransportDiscordApi.md#apiTransportDiscordIdGet) | **GET** /api/transport-discord/{id} | Retrieves a TransportDiscord resource.
[**apiTransportDiscordIdPatch**](TransportDiscordApi.md#apiTransportDiscordIdPatch) | **PATCH** /api/transport-discord/{id} | Updates the TransportDiscord resource.
[**apiTransportDiscordIdPut**](TransportDiscordApi.md#apiTransportDiscordIdPut) | **PUT** /api/transport-discord/{id} | Replaces the TransportDiscord resource.
[**apiTransportDiscordPost**](TransportDiscordApi.md#apiTransportDiscordPost) | **POST** /api/transport-discord | Creates a TransportDiscord resource.



## apiTransportDiscordGetCollection

> [TransportDiscordGet] apiTransportDiscordGetCollection(opts)

Retrieves the collection of TransportDiscord resources.

Retrieves the collection of TransportDiscord resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportDiscordApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportDiscordGetCollection(opts, (error, data, response) => {
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

[**[TransportDiscordGet]**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportDiscordIdDelete

> apiTransportDiscordIdDelete(id)

Removes the TransportDiscord resource.

Removes the TransportDiscord resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportDiscordApi();
let id = "id_example"; // String | TransportDiscord identifier
apiInstance.apiTransportDiscordIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportDiscord identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportDiscordIdGet

> TransportDiscordGet apiTransportDiscordIdGet(id)

Retrieves a TransportDiscord resource.

Retrieves a TransportDiscord resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportDiscordApi();
let id = "id_example"; // String | TransportDiscord identifier
apiInstance.apiTransportDiscordIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportDiscord identifier | 

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportDiscordIdPatch

> TransportDiscordGet apiTransportDiscordIdPatch(id, transportDiscordPatch)

Updates the TransportDiscord resource.

Updates the TransportDiscord resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportDiscordApi();
let id = "id_example"; // String | TransportDiscord identifier
let transportDiscordPatch = new AlerterSystemApi.TransportDiscordPatch(); // TransportDiscordPatch | The updated TransportDiscord resource
apiInstance.apiTransportDiscordIdPatch(id, transportDiscordPatch, (error, data, response) => {
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
 **id** | **String**| TransportDiscord identifier | 
 **transportDiscordPatch** | [**TransportDiscordPatch**](TransportDiscordPatch.md)| The updated TransportDiscord resource | 

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportDiscordIdPut

> TransportDiscordGet apiTransportDiscordIdPut(id, transportDiscordPut)

Replaces the TransportDiscord resource.

Replaces the TransportDiscord resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportDiscordApi();
let id = "id_example"; // String | TransportDiscord identifier
let transportDiscordPut = new AlerterSystemApi.TransportDiscordPut(); // TransportDiscordPut | The updated TransportDiscord resource
apiInstance.apiTransportDiscordIdPut(id, transportDiscordPut, (error, data, response) => {
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
 **id** | **String**| TransportDiscord identifier | 
 **transportDiscordPut** | [**TransportDiscordPut**](TransportDiscordPut.md)| The updated TransportDiscord resource | 

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportDiscordPost

> TransportDiscordGet apiTransportDiscordPost(transportDiscordPost)

Creates a TransportDiscord resource.

Creates a TransportDiscord resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportDiscordApi();
let transportDiscordPost = new AlerterSystemApi.TransportDiscordPost(); // TransportDiscordPost | The new TransportDiscord resource
apiInstance.apiTransportDiscordPost(transportDiscordPost, (error, data, response) => {
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
 **transportDiscordPost** | [**TransportDiscordPost**](TransportDiscordPost.md)| The new TransportDiscord resource | 

### Return type

[**TransportDiscordGet**](TransportDiscordGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

