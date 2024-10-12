# AlerterSystemApi.TransportTurboSmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportTurboSmsGetCollection**](TransportTurboSmsApi.md#apiTransportTurboSmsGetCollection) | **GET** /api/transport-turbo-sms | Retrieves the collection of TransportTurboSms resources.
[**apiTransportTurboSmsIdDelete**](TransportTurboSmsApi.md#apiTransportTurboSmsIdDelete) | **DELETE** /api/transport-turbo-sms/{id} | Removes the TransportTurboSms resource.
[**apiTransportTurboSmsIdGet**](TransportTurboSmsApi.md#apiTransportTurboSmsIdGet) | **GET** /api/transport-turbo-sms/{id} | Retrieves a TransportTurboSms resource.
[**apiTransportTurboSmsIdPatch**](TransportTurboSmsApi.md#apiTransportTurboSmsIdPatch) | **PATCH** /api/transport-turbo-sms/{id} | Updates the TransportTurboSms resource.
[**apiTransportTurboSmsIdPut**](TransportTurboSmsApi.md#apiTransportTurboSmsIdPut) | **PUT** /api/transport-turbo-sms/{id} | Replaces the TransportTurboSms resource.
[**apiTransportTurboSmsPost**](TransportTurboSmsApi.md#apiTransportTurboSmsPost) | **POST** /api/transport-turbo-sms | Creates a TransportTurboSms resource.



## apiTransportTurboSmsGetCollection

> [TransportTurboSmsGet] apiTransportTurboSmsGetCollection(opts)

Retrieves the collection of TransportTurboSms resources.

Retrieves the collection of TransportTurboSms resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTurboSmsApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportTurboSmsGetCollection(opts, (error, data, response) => {
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

[**[TransportTurboSmsGet]**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTurboSmsIdDelete

> apiTransportTurboSmsIdDelete(id)

Removes the TransportTurboSms resource.

Removes the TransportTurboSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTurboSmsApi();
let id = "id_example"; // String | TransportTurboSms identifier
apiInstance.apiTransportTurboSmsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportTurboSms identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportTurboSmsIdGet

> TransportTurboSmsGet apiTransportTurboSmsIdGet(id)

Retrieves a TransportTurboSms resource.

Retrieves a TransportTurboSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTurboSmsApi();
let id = "id_example"; // String | TransportTurboSms identifier
apiInstance.apiTransportTurboSmsIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportTurboSms identifier | 

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTurboSmsIdPatch

> TransportTurboSmsGet apiTransportTurboSmsIdPatch(id, transportTurboSmsPatch)

Updates the TransportTurboSms resource.

Updates the TransportTurboSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTurboSmsApi();
let id = "id_example"; // String | TransportTurboSms identifier
let transportTurboSmsPatch = new AlerterSystemApi.TransportTurboSmsPatch(); // TransportTurboSmsPatch | The updated TransportTurboSms resource
apiInstance.apiTransportTurboSmsIdPatch(id, transportTurboSmsPatch, (error, data, response) => {
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
 **id** | **String**| TransportTurboSms identifier | 
 **transportTurboSmsPatch** | [**TransportTurboSmsPatch**](TransportTurboSmsPatch.md)| The updated TransportTurboSms resource | 

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTurboSmsIdPut

> TransportTurboSmsGet apiTransportTurboSmsIdPut(id, transportTurboSmsPut)

Replaces the TransportTurboSms resource.

Replaces the TransportTurboSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTurboSmsApi();
let id = "id_example"; // String | TransportTurboSms identifier
let transportTurboSmsPut = new AlerterSystemApi.TransportTurboSmsPut(); // TransportTurboSmsPut | The updated TransportTurboSms resource
apiInstance.apiTransportTurboSmsIdPut(id, transportTurboSmsPut, (error, data, response) => {
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
 **id** | **String**| TransportTurboSms identifier | 
 **transportTurboSmsPut** | [**TransportTurboSmsPut**](TransportTurboSmsPut.md)| The updated TransportTurboSms resource | 

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTurboSmsPost

> TransportTurboSmsGet apiTransportTurboSmsPost(transportTurboSmsPost)

Creates a TransportTurboSms resource.

Creates a TransportTurboSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTurboSmsApi();
let transportTurboSmsPost = new AlerterSystemApi.TransportTurboSmsPost(); // TransportTurboSmsPost | The new TransportTurboSms resource
apiInstance.apiTransportTurboSmsPost(transportTurboSmsPost, (error, data, response) => {
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
 **transportTurboSmsPost** | [**TransportTurboSmsPost**](TransportTurboSmsPost.md)| The new TransportTurboSms resource | 

### Return type

[**TransportTurboSmsGet**](TransportTurboSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

