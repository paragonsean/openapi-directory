# AlerterSystemApi.TransportMobytApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMobytGetCollection**](TransportMobytApi.md#apiTransportMobytGetCollection) | **GET** /api/transport-mobyt | Retrieves the collection of TransportMobyt resources.
[**apiTransportMobytIdDelete**](TransportMobytApi.md#apiTransportMobytIdDelete) | **DELETE** /api/transport-mobyt/{id} | Removes the TransportMobyt resource.
[**apiTransportMobytIdGet**](TransportMobytApi.md#apiTransportMobytIdGet) | **GET** /api/transport-mobyt/{id} | Retrieves a TransportMobyt resource.
[**apiTransportMobytIdPatch**](TransportMobytApi.md#apiTransportMobytIdPatch) | **PATCH** /api/transport-mobyt/{id} | Updates the TransportMobyt resource.
[**apiTransportMobytIdPut**](TransportMobytApi.md#apiTransportMobytIdPut) | **PUT** /api/transport-mobyt/{id} | Replaces the TransportMobyt resource.
[**apiTransportMobytPost**](TransportMobytApi.md#apiTransportMobytPost) | **POST** /api/transport-mobyt | Creates a TransportMobyt resource.



## apiTransportMobytGetCollection

> [TransportMobytGet] apiTransportMobytGetCollection(opts)

Retrieves the collection of TransportMobyt resources.

Retrieves the collection of TransportMobyt resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMobytApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMobytGetCollection(opts, (error, data, response) => {
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

[**[TransportMobytGet]**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMobytIdDelete

> apiTransportMobytIdDelete(id)

Removes the TransportMobyt resource.

Removes the TransportMobyt resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMobytApi();
let id = "id_example"; // String | TransportMobyt identifier
apiInstance.apiTransportMobytIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMobyt identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMobytIdGet

> TransportMobytGet apiTransportMobytIdGet(id)

Retrieves a TransportMobyt resource.

Retrieves a TransportMobyt resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMobytApi();
let id = "id_example"; // String | TransportMobyt identifier
apiInstance.apiTransportMobytIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMobyt identifier | 

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMobytIdPatch

> TransportMobytGet apiTransportMobytIdPatch(id, transportMobytPatch)

Updates the TransportMobyt resource.

Updates the TransportMobyt resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMobytApi();
let id = "id_example"; // String | TransportMobyt identifier
let transportMobytPatch = new AlerterSystemApi.TransportMobytPatch(); // TransportMobytPatch | The updated TransportMobyt resource
apiInstance.apiTransportMobytIdPatch(id, transportMobytPatch, (error, data, response) => {
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
 **id** | **String**| TransportMobyt identifier | 
 **transportMobytPatch** | [**TransportMobytPatch**](TransportMobytPatch.md)| The updated TransportMobyt resource | 

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMobytIdPut

> TransportMobytGet apiTransportMobytIdPut(id, transportMobytPut)

Replaces the TransportMobyt resource.

Replaces the TransportMobyt resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMobytApi();
let id = "id_example"; // String | TransportMobyt identifier
let transportMobytPut = new AlerterSystemApi.TransportMobytPut(); // TransportMobytPut | The updated TransportMobyt resource
apiInstance.apiTransportMobytIdPut(id, transportMobytPut, (error, data, response) => {
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
 **id** | **String**| TransportMobyt identifier | 
 **transportMobytPut** | [**TransportMobytPut**](TransportMobytPut.md)| The updated TransportMobyt resource | 

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMobytPost

> TransportMobytGet apiTransportMobytPost(transportMobytPost)

Creates a TransportMobyt resource.

Creates a TransportMobyt resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMobytApi();
let transportMobytPost = new AlerterSystemApi.TransportMobytPost(); // TransportMobytPost | The new TransportMobyt resource
apiInstance.apiTransportMobytPost(transportMobytPost, (error, data, response) => {
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
 **transportMobytPost** | [**TransportMobytPost**](TransportMobytPost.md)| The new TransportMobyt resource | 

### Return type

[**TransportMobytGet**](TransportMobytGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

