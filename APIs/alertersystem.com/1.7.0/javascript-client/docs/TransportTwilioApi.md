# AlerterSystemApi.TransportTwilioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportTwilioGetCollection**](TransportTwilioApi.md#apiTransportTwilioGetCollection) | **GET** /api/transport-twilio | Retrieves the collection of TransportTwilio resources.
[**apiTransportTwilioIdDelete**](TransportTwilioApi.md#apiTransportTwilioIdDelete) | **DELETE** /api/transport-twilio/{id} | Removes the TransportTwilio resource.
[**apiTransportTwilioIdGet**](TransportTwilioApi.md#apiTransportTwilioIdGet) | **GET** /api/transport-twilio/{id} | Retrieves a TransportTwilio resource.
[**apiTransportTwilioIdPatch**](TransportTwilioApi.md#apiTransportTwilioIdPatch) | **PATCH** /api/transport-twilio/{id} | Updates the TransportTwilio resource.
[**apiTransportTwilioIdPut**](TransportTwilioApi.md#apiTransportTwilioIdPut) | **PUT** /api/transport-twilio/{id} | Replaces the TransportTwilio resource.
[**apiTransportTwilioPost**](TransportTwilioApi.md#apiTransportTwilioPost) | **POST** /api/transport-twilio | Creates a TransportTwilio resource.



## apiTransportTwilioGetCollection

> [TransportTwilioGet] apiTransportTwilioGetCollection(opts)

Retrieves the collection of TransportTwilio resources.

Retrieves the collection of TransportTwilio resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwilioApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportTwilioGetCollection(opts, (error, data, response) => {
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

[**[TransportTwilioGet]**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwilioIdDelete

> apiTransportTwilioIdDelete(id)

Removes the TransportTwilio resource.

Removes the TransportTwilio resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwilioApi();
let id = "id_example"; // String | TransportTwilio identifier
apiInstance.apiTransportTwilioIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportTwilio identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportTwilioIdGet

> TransportTwilioGet apiTransportTwilioIdGet(id)

Retrieves a TransportTwilio resource.

Retrieves a TransportTwilio resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwilioApi();
let id = "id_example"; // String | TransportTwilio identifier
apiInstance.apiTransportTwilioIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportTwilio identifier | 

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwilioIdPatch

> TransportTwilioGet apiTransportTwilioIdPatch(id, transportTwilioPatch)

Updates the TransportTwilio resource.

Updates the TransportTwilio resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwilioApi();
let id = "id_example"; // String | TransportTwilio identifier
let transportTwilioPatch = new AlerterSystemApi.TransportTwilioPatch(); // TransportTwilioPatch | The updated TransportTwilio resource
apiInstance.apiTransportTwilioIdPatch(id, transportTwilioPatch, (error, data, response) => {
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
 **id** | **String**| TransportTwilio identifier | 
 **transportTwilioPatch** | [**TransportTwilioPatch**](TransportTwilioPatch.md)| The updated TransportTwilio resource | 

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwilioIdPut

> TransportTwilioGet apiTransportTwilioIdPut(id, transportTwilioPut)

Replaces the TransportTwilio resource.

Replaces the TransportTwilio resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwilioApi();
let id = "id_example"; // String | TransportTwilio identifier
let transportTwilioPut = new AlerterSystemApi.TransportTwilioPut(); // TransportTwilioPut | The updated TransportTwilio resource
apiInstance.apiTransportTwilioIdPut(id, transportTwilioPut, (error, data, response) => {
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
 **id** | **String**| TransportTwilio identifier | 
 **transportTwilioPut** | [**TransportTwilioPut**](TransportTwilioPut.md)| The updated TransportTwilio resource | 

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTwilioPost

> TransportTwilioGet apiTransportTwilioPost(transportTwilioPost)

Creates a TransportTwilio resource.

Creates a TransportTwilio resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTwilioApi();
let transportTwilioPost = new AlerterSystemApi.TransportTwilioPost(); // TransportTwilioPost | The new TransportTwilio resource
apiInstance.apiTransportTwilioPost(transportTwilioPost, (error, data, response) => {
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
 **transportTwilioPost** | [**TransportTwilioPost**](TransportTwilioPost.md)| The new TransportTwilio resource | 

### Return type

[**TransportTwilioGet**](TransportTwilioGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

