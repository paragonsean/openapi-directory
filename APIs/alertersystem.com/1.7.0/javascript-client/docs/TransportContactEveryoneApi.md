# AlerterSystemApi.TransportContactEveryoneApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportContactEveryoneGetCollection**](TransportContactEveryoneApi.md#apiTransportContactEveryoneGetCollection) | **GET** /api/transport-contact-everyone | Retrieves the collection of TransportContactEveryone resources.
[**apiTransportContactEveryoneIdDelete**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdDelete) | **DELETE** /api/transport-contact-everyone/{id} | Removes the TransportContactEveryone resource.
[**apiTransportContactEveryoneIdGet**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdGet) | **GET** /api/transport-contact-everyone/{id} | Retrieves a TransportContactEveryone resource.
[**apiTransportContactEveryoneIdPatch**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdPatch) | **PATCH** /api/transport-contact-everyone/{id} | Updates the TransportContactEveryone resource.
[**apiTransportContactEveryoneIdPut**](TransportContactEveryoneApi.md#apiTransportContactEveryoneIdPut) | **PUT** /api/transport-contact-everyone/{id} | Replaces the TransportContactEveryone resource.
[**apiTransportContactEveryonePost**](TransportContactEveryoneApi.md#apiTransportContactEveryonePost) | **POST** /api/transport-contact-everyone | Creates a TransportContactEveryone resource.



## apiTransportContactEveryoneGetCollection

> [TransportContactEveryoneGet] apiTransportContactEveryoneGetCollection(opts)

Retrieves the collection of TransportContactEveryone resources.

Retrieves the collection of TransportContactEveryone resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportContactEveryoneApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportContactEveryoneGetCollection(opts, (error, data, response) => {
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

[**[TransportContactEveryoneGet]**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportContactEveryoneIdDelete

> apiTransportContactEveryoneIdDelete(id)

Removes the TransportContactEveryone resource.

Removes the TransportContactEveryone resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportContactEveryoneApi();
let id = "id_example"; // String | TransportContactEveryone identifier
apiInstance.apiTransportContactEveryoneIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportContactEveryone identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportContactEveryoneIdGet

> TransportContactEveryoneGet apiTransportContactEveryoneIdGet(id)

Retrieves a TransportContactEveryone resource.

Retrieves a TransportContactEveryone resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportContactEveryoneApi();
let id = "id_example"; // String | TransportContactEveryone identifier
apiInstance.apiTransportContactEveryoneIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportContactEveryone identifier | 

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportContactEveryoneIdPatch

> TransportContactEveryoneGet apiTransportContactEveryoneIdPatch(id, transportContactEveryonePatch)

Updates the TransportContactEveryone resource.

Updates the TransportContactEveryone resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportContactEveryoneApi();
let id = "id_example"; // String | TransportContactEveryone identifier
let transportContactEveryonePatch = new AlerterSystemApi.TransportContactEveryonePatch(); // TransportContactEveryonePatch | The updated TransportContactEveryone resource
apiInstance.apiTransportContactEveryoneIdPatch(id, transportContactEveryonePatch, (error, data, response) => {
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
 **id** | **String**| TransportContactEveryone identifier | 
 **transportContactEveryonePatch** | [**TransportContactEveryonePatch**](TransportContactEveryonePatch.md)| The updated TransportContactEveryone resource | 

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportContactEveryoneIdPut

> TransportContactEveryoneGet apiTransportContactEveryoneIdPut(id, transportContactEveryonePut)

Replaces the TransportContactEveryone resource.

Replaces the TransportContactEveryone resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportContactEveryoneApi();
let id = "id_example"; // String | TransportContactEveryone identifier
let transportContactEveryonePut = new AlerterSystemApi.TransportContactEveryonePut(); // TransportContactEveryonePut | The updated TransportContactEveryone resource
apiInstance.apiTransportContactEveryoneIdPut(id, transportContactEveryonePut, (error, data, response) => {
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
 **id** | **String**| TransportContactEveryone identifier | 
 **transportContactEveryonePut** | [**TransportContactEveryonePut**](TransportContactEveryonePut.md)| The updated TransportContactEveryone resource | 

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportContactEveryonePost

> TransportContactEveryoneGet apiTransportContactEveryonePost(transportContactEveryonePost)

Creates a TransportContactEveryone resource.

Creates a TransportContactEveryone resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportContactEveryoneApi();
let transportContactEveryonePost = new AlerterSystemApi.TransportContactEveryonePost(); // TransportContactEveryonePost | The new TransportContactEveryone resource
apiInstance.apiTransportContactEveryonePost(transportContactEveryonePost, (error, data, response) => {
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
 **transportContactEveryonePost** | [**TransportContactEveryonePost**](TransportContactEveryonePost.md)| The new TransportContactEveryone resource | 

### Return type

[**TransportContactEveryoneGet**](TransportContactEveryoneGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

