# AlerterSystemApi.TransportFirebaseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportFirebaseGetCollection**](TransportFirebaseApi.md#apiTransportFirebaseGetCollection) | **GET** /api/transport-firebase | Retrieves the collection of TransportFirebase resources.
[**apiTransportFirebaseIdDelete**](TransportFirebaseApi.md#apiTransportFirebaseIdDelete) | **DELETE** /api/transport-firebase/{id} | Removes the TransportFirebase resource.
[**apiTransportFirebaseIdGet**](TransportFirebaseApi.md#apiTransportFirebaseIdGet) | **GET** /api/transport-firebase/{id} | Retrieves a TransportFirebase resource.
[**apiTransportFirebaseIdPatch**](TransportFirebaseApi.md#apiTransportFirebaseIdPatch) | **PATCH** /api/transport-firebase/{id} | Updates the TransportFirebase resource.
[**apiTransportFirebaseIdPut**](TransportFirebaseApi.md#apiTransportFirebaseIdPut) | **PUT** /api/transport-firebase/{id} | Replaces the TransportFirebase resource.
[**apiTransportFirebasePost**](TransportFirebaseApi.md#apiTransportFirebasePost) | **POST** /api/transport-firebase | Creates a TransportFirebase resource.



## apiTransportFirebaseGetCollection

> [TransportFirebaseGet] apiTransportFirebaseGetCollection(opts)

Retrieves the collection of TransportFirebase resources.

Retrieves the collection of TransportFirebase resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFirebaseApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportFirebaseGetCollection(opts, (error, data, response) => {
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

[**[TransportFirebaseGet]**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFirebaseIdDelete

> apiTransportFirebaseIdDelete(id)

Removes the TransportFirebase resource.

Removes the TransportFirebase resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFirebaseApi();
let id = "id_example"; // String | TransportFirebase identifier
apiInstance.apiTransportFirebaseIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportFirebase identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportFirebaseIdGet

> TransportFirebaseGet apiTransportFirebaseIdGet(id)

Retrieves a TransportFirebase resource.

Retrieves a TransportFirebase resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFirebaseApi();
let id = "id_example"; // String | TransportFirebase identifier
apiInstance.apiTransportFirebaseIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportFirebase identifier | 

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFirebaseIdPatch

> TransportFirebaseGet apiTransportFirebaseIdPatch(id, transportFirebasePatch)

Updates the TransportFirebase resource.

Updates the TransportFirebase resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFirebaseApi();
let id = "id_example"; // String | TransportFirebase identifier
let transportFirebasePatch = new AlerterSystemApi.TransportFirebasePatch(); // TransportFirebasePatch | The updated TransportFirebase resource
apiInstance.apiTransportFirebaseIdPatch(id, transportFirebasePatch, (error, data, response) => {
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
 **id** | **String**| TransportFirebase identifier | 
 **transportFirebasePatch** | [**TransportFirebasePatch**](TransportFirebasePatch.md)| The updated TransportFirebase resource | 

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFirebaseIdPut

> TransportFirebaseGet apiTransportFirebaseIdPut(id, transportFirebasePut)

Replaces the TransportFirebase resource.

Replaces the TransportFirebase resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFirebaseApi();
let id = "id_example"; // String | TransportFirebase identifier
let transportFirebasePut = new AlerterSystemApi.TransportFirebasePut(); // TransportFirebasePut | The updated TransportFirebase resource
apiInstance.apiTransportFirebaseIdPut(id, transportFirebasePut, (error, data, response) => {
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
 **id** | **String**| TransportFirebase identifier | 
 **transportFirebasePut** | [**TransportFirebasePut**](TransportFirebasePut.md)| The updated TransportFirebase resource | 

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFirebasePost

> TransportFirebaseGet apiTransportFirebasePost(transportFirebasePost)

Creates a TransportFirebase resource.

Creates a TransportFirebase resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFirebaseApi();
let transportFirebasePost = new AlerterSystemApi.TransportFirebasePost(); // TransportFirebasePost | The new TransportFirebase resource
apiInstance.apiTransportFirebasePost(transportFirebasePost, (error, data, response) => {
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
 **transportFirebasePost** | [**TransportFirebasePost**](TransportFirebasePost.md)| The new TransportFirebase resource | 

### Return type

[**TransportFirebaseGet**](TransportFirebaseGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

