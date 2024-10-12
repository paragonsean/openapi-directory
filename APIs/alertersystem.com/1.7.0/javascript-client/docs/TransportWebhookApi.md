# AlerterSystemApi.TransportWebhookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportWebhookGetCollection**](TransportWebhookApi.md#apiTransportWebhookGetCollection) | **GET** /api/transport-webhook | Retrieves the collection of TransportWebhook resources.
[**apiTransportWebhookIdDelete**](TransportWebhookApi.md#apiTransportWebhookIdDelete) | **DELETE** /api/transport-webhook/{id} | Removes the TransportWebhook resource.
[**apiTransportWebhookIdGet**](TransportWebhookApi.md#apiTransportWebhookIdGet) | **GET** /api/transport-webhook/{id} | Retrieves a TransportWebhook resource.
[**apiTransportWebhookIdPatch**](TransportWebhookApi.md#apiTransportWebhookIdPatch) | **PATCH** /api/transport-webhook/{id} | Updates the TransportWebhook resource.
[**apiTransportWebhookIdPut**](TransportWebhookApi.md#apiTransportWebhookIdPut) | **PUT** /api/transport-webhook/{id} | Replaces the TransportWebhook resource.
[**apiTransportWebhookPost**](TransportWebhookApi.md#apiTransportWebhookPost) | **POST** /api/transport-webhook | Creates a TransportWebhook resource.



## apiTransportWebhookGetCollection

> [TransportWebhookGet] apiTransportWebhookGetCollection(opts)

Retrieves the collection of TransportWebhook resources.

Retrieves the collection of TransportWebhook resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportWebhookApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportWebhookGetCollection(opts, (error, data, response) => {
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

[**[TransportWebhookGet]**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportWebhookIdDelete

> apiTransportWebhookIdDelete(id)

Removes the TransportWebhook resource.

Removes the TransportWebhook resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportWebhookApi();
let id = "id_example"; // String | TransportWebhook identifier
apiInstance.apiTransportWebhookIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportWebhook identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportWebhookIdGet

> TransportWebhookGet apiTransportWebhookIdGet(id)

Retrieves a TransportWebhook resource.

Retrieves a TransportWebhook resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportWebhookApi();
let id = "id_example"; // String | TransportWebhook identifier
apiInstance.apiTransportWebhookIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportWebhook identifier | 

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportWebhookIdPatch

> TransportWebhookGet apiTransportWebhookIdPatch(id, transportWebhookPatch)

Updates the TransportWebhook resource.

Updates the TransportWebhook resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportWebhookApi();
let id = "id_example"; // String | TransportWebhook identifier
let transportWebhookPatch = new AlerterSystemApi.TransportWebhookPatch(); // TransportWebhookPatch | The updated TransportWebhook resource
apiInstance.apiTransportWebhookIdPatch(id, transportWebhookPatch, (error, data, response) => {
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
 **id** | **String**| TransportWebhook identifier | 
 **transportWebhookPatch** | [**TransportWebhookPatch**](TransportWebhookPatch.md)| The updated TransportWebhook resource | 

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportWebhookIdPut

> TransportWebhookGet apiTransportWebhookIdPut(id, transportWebhookPut)

Replaces the TransportWebhook resource.

Replaces the TransportWebhook resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportWebhookApi();
let id = "id_example"; // String | TransportWebhook identifier
let transportWebhookPut = new AlerterSystemApi.TransportWebhookPut(); // TransportWebhookPut | The updated TransportWebhook resource
apiInstance.apiTransportWebhookIdPut(id, transportWebhookPut, (error, data, response) => {
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
 **id** | **String**| TransportWebhook identifier | 
 **transportWebhookPut** | [**TransportWebhookPut**](TransportWebhookPut.md)| The updated TransportWebhook resource | 

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportWebhookPost

> TransportWebhookGet apiTransportWebhookPost(transportWebhookPost)

Creates a TransportWebhook resource.

Creates a TransportWebhook resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportWebhookApi();
let transportWebhookPost = new AlerterSystemApi.TransportWebhookPost(); // TransportWebhookPost | The new TransportWebhook resource
apiInstance.apiTransportWebhookPost(transportWebhookPost, (error, data, response) => {
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
 **transportWebhookPost** | [**TransportWebhookPost**](TransportWebhookPost.md)| The new TransportWebhook resource | 

### Return type

[**TransportWebhookGet**](TransportWebhookGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

