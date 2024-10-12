# AlerterSystemApi.TransportAmazonSnsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportAmazonSnsGetCollection**](TransportAmazonSnsApi.md#apiTransportAmazonSnsGetCollection) | **GET** /api/transport-amazon-sns | Retrieves the collection of TransportAmazonSns resources.
[**apiTransportAmazonSnsIdDelete**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdDelete) | **DELETE** /api/transport-amazon-sns/{id} | Removes the TransportAmazonSns resource.
[**apiTransportAmazonSnsIdGet**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdGet) | **GET** /api/transport-amazon-sns/{id} | Retrieves a TransportAmazonSns resource.
[**apiTransportAmazonSnsIdPatch**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdPatch) | **PATCH** /api/transport-amazon-sns/{id} | Updates the TransportAmazonSns resource.
[**apiTransportAmazonSnsIdPut**](TransportAmazonSnsApi.md#apiTransportAmazonSnsIdPut) | **PUT** /api/transport-amazon-sns/{id} | Replaces the TransportAmazonSns resource.
[**apiTransportAmazonSnsPost**](TransportAmazonSnsApi.md#apiTransportAmazonSnsPost) | **POST** /api/transport-amazon-sns | Creates a TransportAmazonSns resource.



## apiTransportAmazonSnsGetCollection

> [TransportAmazonSnsGet] apiTransportAmazonSnsGetCollection(opts)

Retrieves the collection of TransportAmazonSns resources.

Retrieves the collection of TransportAmazonSns resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAmazonSnsApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportAmazonSnsGetCollection(opts, (error, data, response) => {
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

[**[TransportAmazonSnsGet]**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAmazonSnsIdDelete

> apiTransportAmazonSnsIdDelete(id)

Removes the TransportAmazonSns resource.

Removes the TransportAmazonSns resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAmazonSnsApi();
let id = "id_example"; // String | TransportAmazonSns identifier
apiInstance.apiTransportAmazonSnsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportAmazonSns identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportAmazonSnsIdGet

> TransportAmazonSnsGet apiTransportAmazonSnsIdGet(id)

Retrieves a TransportAmazonSns resource.

Retrieves a TransportAmazonSns resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAmazonSnsApi();
let id = "id_example"; // String | TransportAmazonSns identifier
apiInstance.apiTransportAmazonSnsIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportAmazonSns identifier | 

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAmazonSnsIdPatch

> TransportAmazonSnsGet apiTransportAmazonSnsIdPatch(id, transportAmazonSnsPatch)

Updates the TransportAmazonSns resource.

Updates the TransportAmazonSns resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAmazonSnsApi();
let id = "id_example"; // String | TransportAmazonSns identifier
let transportAmazonSnsPatch = new AlerterSystemApi.TransportAmazonSnsPatch(); // TransportAmazonSnsPatch | The updated TransportAmazonSns resource
apiInstance.apiTransportAmazonSnsIdPatch(id, transportAmazonSnsPatch, (error, data, response) => {
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
 **id** | **String**| TransportAmazonSns identifier | 
 **transportAmazonSnsPatch** | [**TransportAmazonSnsPatch**](TransportAmazonSnsPatch.md)| The updated TransportAmazonSns resource | 

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAmazonSnsIdPut

> TransportAmazonSnsGet apiTransportAmazonSnsIdPut(id, transportAmazonSnsPut)

Replaces the TransportAmazonSns resource.

Replaces the TransportAmazonSns resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAmazonSnsApi();
let id = "id_example"; // String | TransportAmazonSns identifier
let transportAmazonSnsPut = new AlerterSystemApi.TransportAmazonSnsPut(); // TransportAmazonSnsPut | The updated TransportAmazonSns resource
apiInstance.apiTransportAmazonSnsIdPut(id, transportAmazonSnsPut, (error, data, response) => {
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
 **id** | **String**| TransportAmazonSns identifier | 
 **transportAmazonSnsPut** | [**TransportAmazonSnsPut**](TransportAmazonSnsPut.md)| The updated TransportAmazonSns resource | 

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAmazonSnsPost

> TransportAmazonSnsGet apiTransportAmazonSnsPost(transportAmazonSnsPost)

Creates a TransportAmazonSns resource.

Creates a TransportAmazonSns resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAmazonSnsApi();
let transportAmazonSnsPost = new AlerterSystemApi.TransportAmazonSnsPost(); // TransportAmazonSnsPost | The new TransportAmazonSns resource
apiInstance.apiTransportAmazonSnsPost(transportAmazonSnsPost, (error, data, response) => {
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
 **transportAmazonSnsPost** | [**TransportAmazonSnsPost**](TransportAmazonSnsPost.md)| The new TransportAmazonSns resource | 

### Return type

[**TransportAmazonSnsGet**](TransportAmazonSnsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

