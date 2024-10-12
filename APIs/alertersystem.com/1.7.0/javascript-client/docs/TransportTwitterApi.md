# AlerterSystemApi.TransportTwitterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportTwitterGetCollection**](TransportTwitterApi.md#apiTransportTwitterGetCollection) | **GET** /api/transport-twitter | Retrieves the collection of TransportTwitter resources.
[**apiTransportTwitterIdDelete**](TransportTwitterApi.md#apiTransportTwitterIdDelete) | **DELETE** /api/transport-twitter/{id} | Removes the TransportTwitter resource.
[**apiTransportTwitterIdGet**](TransportTwitterApi.md#apiTransportTwitterIdGet) | **GET** /api/transport-twitter/{id} | Retrieves a TransportTwitter resource.
[**apiTransportTwitterIdPatch**](TransportTwitterApi.md#apiTransportTwitterIdPatch) | **PATCH** /api/transport-twitter/{id} | Updates the TransportTwitter resource.
[**apiTransportTwitterIdPut**](TransportTwitterApi.md#apiTransportTwitterIdPut) | **PUT** /api/transport-twitter/{id} | Replaces the TransportTwitter resource.
[**apiTransportTwitterPost**](TransportTwitterApi.md#apiTransportTwitterPost) | **POST** /api/transport-twitter | Creates a TransportTwitter resource.



## apiTransportTwitterGetCollection

> [TransportTwitterGet] apiTransportTwitterGetCollection(opts)

Retrieves the collection of TransportTwitter resources.

Retrieves the collection of TransportTwitter resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwitterApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportTwitterGetCollection(opts, (error, data, response) => {
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

[**[TransportTwitterGet]**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwitterIdDelete

> apiTransportTwitterIdDelete(id)

Removes the TransportTwitter resource.

Removes the TransportTwitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwitterApi();
let id = "id_example"; // String | TransportTwitter identifier
apiInstance.apiTransportTwitterIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportTwitter identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportTwitterIdGet

> TransportTwitterGet apiTransportTwitterIdGet(id)

Retrieves a TransportTwitter resource.

Retrieves a TransportTwitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwitterApi();
let id = "id_example"; // String | TransportTwitter identifier
apiInstance.apiTransportTwitterIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportTwitter identifier | 

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwitterIdPatch

> TransportTwitterGet apiTransportTwitterIdPatch(id, transportTwitterPatch)

Updates the TransportTwitter resource.

Updates the TransportTwitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwitterApi();
let id = "id_example"; // String | TransportTwitter identifier
let transportTwitterPatch = new AlerterSystemApi.TransportTwitterPatch(); // TransportTwitterPatch | The updated TransportTwitter resource
apiInstance.apiTransportTwitterIdPatch(id, transportTwitterPatch, (error, data, response) => {
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
 **id** | **String**| TransportTwitter identifier | 
 **transportTwitterPatch** | [**TransportTwitterPatch**](TransportTwitterPatch.md)| The updated TransportTwitter resource | 

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwitterIdPut

> TransportTwitterGet apiTransportTwitterIdPut(id, transportTwitterPut)

Replaces the TransportTwitter resource.

Replaces the TransportTwitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwitterApi();
let id = "id_example"; // String | TransportTwitter identifier
let transportTwitterPut = new AlerterSystemApi.TransportTwitterPut(); // TransportTwitterPut | The updated TransportTwitter resource
apiInstance.apiTransportTwitterIdPut(id, transportTwitterPut, (error, data, response) => {
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
 **id** | **String**| TransportTwitter identifier | 
 **transportTwitterPut** | [**TransportTwitterPut**](TransportTwitterPut.md)| The updated TransportTwitter resource | 

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwitterPost

> TransportTwitterGet apiTransportTwitterPost(transportTwitterPost)

Creates a TransportTwitter resource.

Creates a TransportTwitter resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwitterApi();
let transportTwitterPost = new AlerterSystemApi.TransportTwitterPost(); // TransportTwitterPost | The new TransportTwitter resource
apiInstance.apiTransportTwitterPost(transportTwitterPost, (error, data, response) => {
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
 **transportTwitterPost** | [**TransportTwitterPost**](TransportTwitterPost.md)| The new TransportTwitter resource | 

### Return type

[**TransportTwitterGet**](TransportTwitterGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

