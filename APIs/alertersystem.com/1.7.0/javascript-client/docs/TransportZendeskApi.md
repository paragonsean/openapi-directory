# AlerterSystemApi.TransportZendeskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportZendeskGetCollection**](TransportZendeskApi.md#apiTransportZendeskGetCollection) | **GET** /api/transport-zendesk | Retrieves the collection of TransportZendesk resources.
[**apiTransportZendeskIdDelete**](TransportZendeskApi.md#apiTransportZendeskIdDelete) | **DELETE** /api/transport-zendesk/{id} | Removes the TransportZendesk resource.
[**apiTransportZendeskIdGet**](TransportZendeskApi.md#apiTransportZendeskIdGet) | **GET** /api/transport-zendesk/{id} | Retrieves a TransportZendesk resource.
[**apiTransportZendeskIdPatch**](TransportZendeskApi.md#apiTransportZendeskIdPatch) | **PATCH** /api/transport-zendesk/{id} | Updates the TransportZendesk resource.
[**apiTransportZendeskIdPut**](TransportZendeskApi.md#apiTransportZendeskIdPut) | **PUT** /api/transport-zendesk/{id} | Replaces the TransportZendesk resource.
[**apiTransportZendeskPost**](TransportZendeskApi.md#apiTransportZendeskPost) | **POST** /api/transport-zendesk | Creates a TransportZendesk resource.



## apiTransportZendeskGetCollection

> [TransportZendeskGet] apiTransportZendeskGetCollection(opts)

Retrieves the collection of TransportZendesk resources.

Retrieves the collection of TransportZendesk resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZendeskApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportZendeskGetCollection(opts, (error, data, response) => {
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

[**[TransportZendeskGet]**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZendeskIdDelete

> apiTransportZendeskIdDelete(id)

Removes the TransportZendesk resource.

Removes the TransportZendesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZendeskApi();
let id = "id_example"; // String | TransportZendesk identifier
apiInstance.apiTransportZendeskIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportZendesk identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportZendeskIdGet

> TransportZendeskGet apiTransportZendeskIdGet(id)

Retrieves a TransportZendesk resource.

Retrieves a TransportZendesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZendeskApi();
let id = "id_example"; // String | TransportZendesk identifier
apiInstance.apiTransportZendeskIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportZendesk identifier | 

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZendeskIdPatch

> TransportZendeskGet apiTransportZendeskIdPatch(id, transportZendeskPatch)

Updates the TransportZendesk resource.

Updates the TransportZendesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZendeskApi();
let id = "id_example"; // String | TransportZendesk identifier
let transportZendeskPatch = new AlerterSystemApi.TransportZendeskPatch(); // TransportZendeskPatch | The updated TransportZendesk resource
apiInstance.apiTransportZendeskIdPatch(id, transportZendeskPatch, (error, data, response) => {
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
 **id** | **String**| TransportZendesk identifier | 
 **transportZendeskPatch** | [**TransportZendeskPatch**](TransportZendeskPatch.md)| The updated TransportZendesk resource | 

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZendeskIdPut

> TransportZendeskGet apiTransportZendeskIdPut(id, transportZendeskPut)

Replaces the TransportZendesk resource.

Replaces the TransportZendesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZendeskApi();
let id = "id_example"; // String | TransportZendesk identifier
let transportZendeskPut = new AlerterSystemApi.TransportZendeskPut(); // TransportZendeskPut | The updated TransportZendesk resource
apiInstance.apiTransportZendeskIdPut(id, transportZendeskPut, (error, data, response) => {
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
 **id** | **String**| TransportZendesk identifier | 
 **transportZendeskPut** | [**TransportZendeskPut**](TransportZendeskPut.md)| The updated TransportZendesk resource | 

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportZendeskPost

> TransportZendeskGet apiTransportZendeskPost(transportZendeskPost)

Creates a TransportZendesk resource.

Creates a TransportZendesk resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportZendeskApi();
let transportZendeskPost = new AlerterSystemApi.TransportZendeskPost(); // TransportZendeskPost | The new TransportZendesk resource
apiInstance.apiTransportZendeskPost(transportZendeskPost, (error, data, response) => {
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
 **transportZendeskPost** | [**TransportZendeskPost**](TransportZendeskPost.md)| The new TransportZendesk resource | 

### Return type

[**TransportZendeskGet**](TransportZendeskGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

