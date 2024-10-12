# AlerterSystemApi.TransportPushbulletApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportPushbulletGetCollection**](TransportPushbulletApi.md#apiTransportPushbulletGetCollection) | **GET** /api/transport-pushbullet | Retrieves the collection of TransportPushbullet resources.
[**apiTransportPushbulletIdDelete**](TransportPushbulletApi.md#apiTransportPushbulletIdDelete) | **DELETE** /api/transport-pushbullet/{id} | Removes the TransportPushbullet resource.
[**apiTransportPushbulletIdGet**](TransportPushbulletApi.md#apiTransportPushbulletIdGet) | **GET** /api/transport-pushbullet/{id} | Retrieves a TransportPushbullet resource.
[**apiTransportPushbulletIdPatch**](TransportPushbulletApi.md#apiTransportPushbulletIdPatch) | **PATCH** /api/transport-pushbullet/{id} | Updates the TransportPushbullet resource.
[**apiTransportPushbulletIdPut**](TransportPushbulletApi.md#apiTransportPushbulletIdPut) | **PUT** /api/transport-pushbullet/{id} | Replaces the TransportPushbullet resource.
[**apiTransportPushbulletPost**](TransportPushbulletApi.md#apiTransportPushbulletPost) | **POST** /api/transport-pushbullet | Creates a TransportPushbullet resource.



## apiTransportPushbulletGetCollection

> [TransportPushbulletGet] apiTransportPushbulletGetCollection(opts)

Retrieves the collection of TransportPushbullet resources.

Retrieves the collection of TransportPushbullet resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushbulletApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportPushbulletGetCollection(opts, (error, data, response) => {
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

[**[TransportPushbulletGet]**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushbulletIdDelete

> apiTransportPushbulletIdDelete(id)

Removes the TransportPushbullet resource.

Removes the TransportPushbullet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushbulletApi();
let id = "id_example"; // String | TransportPushbullet identifier
apiInstance.apiTransportPushbulletIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportPushbullet identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportPushbulletIdGet

> TransportPushbulletGet apiTransportPushbulletIdGet(id)

Retrieves a TransportPushbullet resource.

Retrieves a TransportPushbullet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushbulletApi();
let id = "id_example"; // String | TransportPushbullet identifier
apiInstance.apiTransportPushbulletIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportPushbullet identifier | 

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushbulletIdPatch

> TransportPushbulletGet apiTransportPushbulletIdPatch(id, transportPushbulletPatch)

Updates the TransportPushbullet resource.

Updates the TransportPushbullet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushbulletApi();
let id = "id_example"; // String | TransportPushbullet identifier
let transportPushbulletPatch = new AlerterSystemApi.TransportPushbulletPatch(); // TransportPushbulletPatch | The updated TransportPushbullet resource
apiInstance.apiTransportPushbulletIdPatch(id, transportPushbulletPatch, (error, data, response) => {
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
 **id** | **String**| TransportPushbullet identifier | 
 **transportPushbulletPatch** | [**TransportPushbulletPatch**](TransportPushbulletPatch.md)| The updated TransportPushbullet resource | 

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushbulletIdPut

> TransportPushbulletGet apiTransportPushbulletIdPut(id, transportPushbulletPut)

Replaces the TransportPushbullet resource.

Replaces the TransportPushbullet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushbulletApi();
let id = "id_example"; // String | TransportPushbullet identifier
let transportPushbulletPut = new AlerterSystemApi.TransportPushbulletPut(); // TransportPushbulletPut | The updated TransportPushbullet resource
apiInstance.apiTransportPushbulletIdPut(id, transportPushbulletPut, (error, data, response) => {
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
 **id** | **String**| TransportPushbullet identifier | 
 **transportPushbulletPut** | [**TransportPushbulletPut**](TransportPushbulletPut.md)| The updated TransportPushbullet resource | 

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPushbulletPost

> TransportPushbulletGet apiTransportPushbulletPost(transportPushbulletPost)

Creates a TransportPushbullet resource.

Creates a TransportPushbullet resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPushbulletApi();
let transportPushbulletPost = new AlerterSystemApi.TransportPushbulletPost(); // TransportPushbulletPost | The new TransportPushbullet resource
apiInstance.apiTransportPushbulletPost(transportPushbulletPost, (error, data, response) => {
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
 **transportPushbulletPost** | [**TransportPushbulletPost**](TransportPushbulletPost.md)| The new TransportPushbullet resource | 

### Return type

[**TransportPushbulletGet**](TransportPushbulletGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

