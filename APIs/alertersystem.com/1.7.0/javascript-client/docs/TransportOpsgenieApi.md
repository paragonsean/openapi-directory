# AlerterSystemApi.TransportOpsgenieApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportOpsgenieGetCollection**](TransportOpsgenieApi.md#apiTransportOpsgenieGetCollection) | **GET** /api/transport-opsgenie | Retrieves the collection of TransportOpsgenie resources.
[**apiTransportOpsgenieIdDelete**](TransportOpsgenieApi.md#apiTransportOpsgenieIdDelete) | **DELETE** /api/transport-opsgenie/{id} | Removes the TransportOpsgenie resource.
[**apiTransportOpsgenieIdGet**](TransportOpsgenieApi.md#apiTransportOpsgenieIdGet) | **GET** /api/transport-opsgenie/{id} | Retrieves a TransportOpsgenie resource.
[**apiTransportOpsgenieIdPatch**](TransportOpsgenieApi.md#apiTransportOpsgenieIdPatch) | **PATCH** /api/transport-opsgenie/{id} | Updates the TransportOpsgenie resource.
[**apiTransportOpsgenieIdPut**](TransportOpsgenieApi.md#apiTransportOpsgenieIdPut) | **PUT** /api/transport-opsgenie/{id} | Replaces the TransportOpsgenie resource.
[**apiTransportOpsgeniePost**](TransportOpsgenieApi.md#apiTransportOpsgeniePost) | **POST** /api/transport-opsgenie | Creates a TransportOpsgenie resource.



## apiTransportOpsgenieGetCollection

> [TransportOpsgenieGet] apiTransportOpsgenieGetCollection(opts)

Retrieves the collection of TransportOpsgenie resources.

Retrieves the collection of TransportOpsgenie resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOpsgenieApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportOpsgenieGetCollection(opts, (error, data, response) => {
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

[**[TransportOpsgenieGet]**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOpsgenieIdDelete

> apiTransportOpsgenieIdDelete(id)

Removes the TransportOpsgenie resource.

Removes the TransportOpsgenie resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOpsgenieApi();
let id = "id_example"; // String | TransportOpsgenie identifier
apiInstance.apiTransportOpsgenieIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportOpsgenie identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportOpsgenieIdGet

> TransportOpsgenieGet apiTransportOpsgenieIdGet(id)

Retrieves a TransportOpsgenie resource.

Retrieves a TransportOpsgenie resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOpsgenieApi();
let id = "id_example"; // String | TransportOpsgenie identifier
apiInstance.apiTransportOpsgenieIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportOpsgenie identifier | 

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOpsgenieIdPatch

> TransportOpsgenieGet apiTransportOpsgenieIdPatch(id, transportOpsgeniePatch)

Updates the TransportOpsgenie resource.

Updates the TransportOpsgenie resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOpsgenieApi();
let id = "id_example"; // String | TransportOpsgenie identifier
let transportOpsgeniePatch = new AlerterSystemApi.TransportOpsgeniePatch(); // TransportOpsgeniePatch | The updated TransportOpsgenie resource
apiInstance.apiTransportOpsgenieIdPatch(id, transportOpsgeniePatch, (error, data, response) => {
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
 **id** | **String**| TransportOpsgenie identifier | 
 **transportOpsgeniePatch** | [**TransportOpsgeniePatch**](TransportOpsgeniePatch.md)| The updated TransportOpsgenie resource | 

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOpsgenieIdPut

> TransportOpsgenieGet apiTransportOpsgenieIdPut(id, transportOpsgeniePut)

Replaces the TransportOpsgenie resource.

Replaces the TransportOpsgenie resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOpsgenieApi();
let id = "id_example"; // String | TransportOpsgenie identifier
let transportOpsgeniePut = new AlerterSystemApi.TransportOpsgeniePut(); // TransportOpsgeniePut | The updated TransportOpsgenie resource
apiInstance.apiTransportOpsgenieIdPut(id, transportOpsgeniePut, (error, data, response) => {
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
 **id** | **String**| TransportOpsgenie identifier | 
 **transportOpsgeniePut** | [**TransportOpsgeniePut**](TransportOpsgeniePut.md)| The updated TransportOpsgenie resource | 

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOpsgeniePost

> TransportOpsgenieGet apiTransportOpsgeniePost(transportOpsgeniePost)

Creates a TransportOpsgenie resource.

Creates a TransportOpsgenie resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOpsgenieApi();
let transportOpsgeniePost = new AlerterSystemApi.TransportOpsgeniePost(); // TransportOpsgeniePost | The new TransportOpsgenie resource
apiInstance.apiTransportOpsgeniePost(transportOpsgeniePost, (error, data, response) => {
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
 **transportOpsgeniePost** | [**TransportOpsgeniePost**](TransportOpsgeniePost.md)| The new TransportOpsgenie resource | 

### Return type

[**TransportOpsgenieGet**](TransportOpsgenieGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

