# AlerterSystemApi.TransportEmailApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportEmailGetCollection**](TransportEmailApi.md#apiTransportEmailGetCollection) | **GET** /api/transport-email | Retrieves the collection of TransportEmail resources.
[**apiTransportEmailIdDelete**](TransportEmailApi.md#apiTransportEmailIdDelete) | **DELETE** /api/transport-email/{id} | Removes the TransportEmail resource.
[**apiTransportEmailIdGet**](TransportEmailApi.md#apiTransportEmailIdGet) | **GET** /api/transport-email/{id} | Retrieves a TransportEmail resource.
[**apiTransportEmailIdPatch**](TransportEmailApi.md#apiTransportEmailIdPatch) | **PATCH** /api/transport-email/{id} | Updates the TransportEmail resource.
[**apiTransportEmailIdPut**](TransportEmailApi.md#apiTransportEmailIdPut) | **PUT** /api/transport-email/{id} | Replaces the TransportEmail resource.
[**apiTransportEmailPost**](TransportEmailApi.md#apiTransportEmailPost) | **POST** /api/transport-email | Creates a TransportEmail resource.



## apiTransportEmailGetCollection

> [TransportEmailGet] apiTransportEmailGetCollection(opts)

Retrieves the collection of TransportEmail resources.

Retrieves the collection of TransportEmail resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEmailApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportEmailGetCollection(opts, (error, data, response) => {
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

[**[TransportEmailGet]**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEmailIdDelete

> apiTransportEmailIdDelete(id)

Removes the TransportEmail resource.

Removes the TransportEmail resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEmailApi();
let id = "id_example"; // String | TransportEmail identifier
apiInstance.apiTransportEmailIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportEmail identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportEmailIdGet

> TransportEmailGet apiTransportEmailIdGet(id)

Retrieves a TransportEmail resource.

Retrieves a TransportEmail resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEmailApi();
let id = "id_example"; // String | TransportEmail identifier
apiInstance.apiTransportEmailIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportEmail identifier | 

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEmailIdPatch

> TransportEmailGet apiTransportEmailIdPatch(id, transportEmailPatch)

Updates the TransportEmail resource.

Updates the TransportEmail resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEmailApi();
let id = "id_example"; // String | TransportEmail identifier
let transportEmailPatch = new AlerterSystemApi.TransportEmailPatch(); // TransportEmailPatch | The updated TransportEmail resource
apiInstance.apiTransportEmailIdPatch(id, transportEmailPatch, (error, data, response) => {
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
 **id** | **String**| TransportEmail identifier | 
 **transportEmailPatch** | [**TransportEmailPatch**](TransportEmailPatch.md)| The updated TransportEmail resource | 

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEmailIdPut

> TransportEmailGet apiTransportEmailIdPut(id, transportEmailPut)

Replaces the TransportEmail resource.

Replaces the TransportEmail resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEmailApi();
let id = "id_example"; // String | TransportEmail identifier
let transportEmailPut = new AlerterSystemApi.TransportEmailPut(); // TransportEmailPut | The updated TransportEmail resource
apiInstance.apiTransportEmailIdPut(id, transportEmailPut, (error, data, response) => {
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
 **id** | **String**| TransportEmail identifier | 
 **transportEmailPut** | [**TransportEmailPut**](TransportEmailPut.md)| The updated TransportEmail resource | 

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportEmailPost

> TransportEmailGet apiTransportEmailPost(transportEmailPost)

Creates a TransportEmail resource.

Creates a TransportEmail resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportEmailApi();
let transportEmailPost = new AlerterSystemApi.TransportEmailPost(); // TransportEmailPost | The new TransportEmail resource
apiInstance.apiTransportEmailPost(transportEmailPost, (error, data, response) => {
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
 **transportEmailPost** | [**TransportEmailPost**](TransportEmailPost.md)| The new TransportEmail resource | 

### Return type

[**TransportEmailGet**](TransportEmailGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

