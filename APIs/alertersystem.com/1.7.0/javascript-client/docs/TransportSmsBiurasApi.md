# AlerterSystemApi.TransportSmsBiurasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSmsBiurasGetCollection**](TransportSmsBiurasApi.md#apiTransportSmsBiurasGetCollection) | **GET** /api/transport-sms-biuras | Retrieves the collection of TransportSmsBiuras resources.
[**apiTransportSmsBiurasIdDelete**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdDelete) | **DELETE** /api/transport-sms-biuras/{id} | Removes the TransportSmsBiuras resource.
[**apiTransportSmsBiurasIdGet**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdGet) | **GET** /api/transport-sms-biuras/{id} | Retrieves a TransportSmsBiuras resource.
[**apiTransportSmsBiurasIdPatch**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdPatch) | **PATCH** /api/transport-sms-biuras/{id} | Updates the TransportSmsBiuras resource.
[**apiTransportSmsBiurasIdPut**](TransportSmsBiurasApi.md#apiTransportSmsBiurasIdPut) | **PUT** /api/transport-sms-biuras/{id} | Replaces the TransportSmsBiuras resource.
[**apiTransportSmsBiurasPost**](TransportSmsBiurasApi.md#apiTransportSmsBiurasPost) | **POST** /api/transport-sms-biuras | Creates a TransportSmsBiuras resource.



## apiTransportSmsBiurasGetCollection

> [TransportSmsBiurasGet] apiTransportSmsBiurasGetCollection(opts)

Retrieves the collection of TransportSmsBiuras resources.

Retrieves the collection of TransportSmsBiuras resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsBiurasApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSmsBiurasGetCollection(opts, (error, data, response) => {
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

[**[TransportSmsBiurasGet]**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsBiurasIdDelete

> apiTransportSmsBiurasIdDelete(id)

Removes the TransportSmsBiuras resource.

Removes the TransportSmsBiuras resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsBiurasApi();
let id = "id_example"; // String | TransportSmsBiuras identifier
apiInstance.apiTransportSmsBiurasIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsBiuras identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSmsBiurasIdGet

> TransportSmsBiurasGet apiTransportSmsBiurasIdGet(id)

Retrieves a TransportSmsBiuras resource.

Retrieves a TransportSmsBiuras resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsBiurasApi();
let id = "id_example"; // String | TransportSmsBiuras identifier
apiInstance.apiTransportSmsBiurasIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSmsBiuras identifier | 

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsBiurasIdPatch

> TransportSmsBiurasGet apiTransportSmsBiurasIdPatch(id, transportSmsBiurasPatch)

Updates the TransportSmsBiuras resource.

Updates the TransportSmsBiuras resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsBiurasApi();
let id = "id_example"; // String | TransportSmsBiuras identifier
let transportSmsBiurasPatch = new AlerterSystemApi.TransportSmsBiurasPatch(); // TransportSmsBiurasPatch | The updated TransportSmsBiuras resource
apiInstance.apiTransportSmsBiurasIdPatch(id, transportSmsBiurasPatch, (error, data, response) => {
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
 **id** | **String**| TransportSmsBiuras identifier | 
 **transportSmsBiurasPatch** | [**TransportSmsBiurasPatch**](TransportSmsBiurasPatch.md)| The updated TransportSmsBiuras resource | 

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsBiurasIdPut

> TransportSmsBiurasGet apiTransportSmsBiurasIdPut(id, transportSmsBiurasPut)

Replaces the TransportSmsBiuras resource.

Replaces the TransportSmsBiuras resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsBiurasApi();
let id = "id_example"; // String | TransportSmsBiuras identifier
let transportSmsBiurasPut = new AlerterSystemApi.TransportSmsBiurasPut(); // TransportSmsBiurasPut | The updated TransportSmsBiuras resource
apiInstance.apiTransportSmsBiurasIdPut(id, transportSmsBiurasPut, (error, data, response) => {
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
 **id** | **String**| TransportSmsBiuras identifier | 
 **transportSmsBiurasPut** | [**TransportSmsBiurasPut**](TransportSmsBiurasPut.md)| The updated TransportSmsBiuras resource | 

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSmsBiurasPost

> TransportSmsBiurasGet apiTransportSmsBiurasPost(transportSmsBiurasPost)

Creates a TransportSmsBiuras resource.

Creates a TransportSmsBiuras resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSmsBiurasApi();
let transportSmsBiurasPost = new AlerterSystemApi.TransportSmsBiurasPost(); // TransportSmsBiurasPost | The new TransportSmsBiuras resource
apiInstance.apiTransportSmsBiurasPost(transportSmsBiurasPost, (error, data, response) => {
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
 **transportSmsBiurasPost** | [**TransportSmsBiurasPost**](TransportSmsBiurasPost.md)| The new TransportSmsBiuras resource | 

### Return type

[**TransportSmsBiurasGet**](TransportSmsBiurasGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

