# AlerterSystemApi.TransportSimpleTextinApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSimpleTextinGetCollection**](TransportSimpleTextinApi.md#apiTransportSimpleTextinGetCollection) | **GET** /api/transport-simple-textin | Retrieves the collection of TransportSimpleTextin resources.
[**apiTransportSimpleTextinIdDelete**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdDelete) | **DELETE** /api/transport-simple-textin/{id} | Removes the TransportSimpleTextin resource.
[**apiTransportSimpleTextinIdGet**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdGet) | **GET** /api/transport-simple-textin/{id} | Retrieves a TransportSimpleTextin resource.
[**apiTransportSimpleTextinIdPatch**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdPatch) | **PATCH** /api/transport-simple-textin/{id} | Updates the TransportSimpleTextin resource.
[**apiTransportSimpleTextinIdPut**](TransportSimpleTextinApi.md#apiTransportSimpleTextinIdPut) | **PUT** /api/transport-simple-textin/{id} | Replaces the TransportSimpleTextin resource.
[**apiTransportSimpleTextinPost**](TransportSimpleTextinApi.md#apiTransportSimpleTextinPost) | **POST** /api/transport-simple-textin | Creates a TransportSimpleTextin resource.



## apiTransportSimpleTextinGetCollection

> [TransportSimpleTextinGet] apiTransportSimpleTextinGetCollection(opts)

Retrieves the collection of TransportSimpleTextin resources.

Retrieves the collection of TransportSimpleTextin resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSimpleTextinApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSimpleTextinGetCollection(opts, (error, data, response) => {
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

[**[TransportSimpleTextinGet]**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSimpleTextinIdDelete

> apiTransportSimpleTextinIdDelete(id)

Removes the TransportSimpleTextin resource.

Removes the TransportSimpleTextin resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSimpleTextinApi();
let id = "id_example"; // String | TransportSimpleTextin identifier
apiInstance.apiTransportSimpleTextinIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSimpleTextin identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSimpleTextinIdGet

> TransportSimpleTextinGet apiTransportSimpleTextinIdGet(id)

Retrieves a TransportSimpleTextin resource.

Retrieves a TransportSimpleTextin resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSimpleTextinApi();
let id = "id_example"; // String | TransportSimpleTextin identifier
apiInstance.apiTransportSimpleTextinIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSimpleTextin identifier | 

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSimpleTextinIdPatch

> TransportSimpleTextinGet apiTransportSimpleTextinIdPatch(id, transportSimpleTextinPatch)

Updates the TransportSimpleTextin resource.

Updates the TransportSimpleTextin resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSimpleTextinApi();
let id = "id_example"; // String | TransportSimpleTextin identifier
let transportSimpleTextinPatch = new AlerterSystemApi.TransportSimpleTextinPatch(); // TransportSimpleTextinPatch | The updated TransportSimpleTextin resource
apiInstance.apiTransportSimpleTextinIdPatch(id, transportSimpleTextinPatch, (error, data, response) => {
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
 **id** | **String**| TransportSimpleTextin identifier | 
 **transportSimpleTextinPatch** | [**TransportSimpleTextinPatch**](TransportSimpleTextinPatch.md)| The updated TransportSimpleTextin resource | 

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSimpleTextinIdPut

> TransportSimpleTextinGet apiTransportSimpleTextinIdPut(id, transportSimpleTextinPut)

Replaces the TransportSimpleTextin resource.

Replaces the TransportSimpleTextin resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSimpleTextinApi();
let id = "id_example"; // String | TransportSimpleTextin identifier
let transportSimpleTextinPut = new AlerterSystemApi.TransportSimpleTextinPut(); // TransportSimpleTextinPut | The updated TransportSimpleTextin resource
apiInstance.apiTransportSimpleTextinIdPut(id, transportSimpleTextinPut, (error, data, response) => {
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
 **id** | **String**| TransportSimpleTextin identifier | 
 **transportSimpleTextinPut** | [**TransportSimpleTextinPut**](TransportSimpleTextinPut.md)| The updated TransportSimpleTextin resource | 

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSimpleTextinPost

> TransportSimpleTextinGet apiTransportSimpleTextinPost(transportSimpleTextinPost)

Creates a TransportSimpleTextin resource.

Creates a TransportSimpleTextin resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSimpleTextinApi();
let transportSimpleTextinPost = new AlerterSystemApi.TransportSimpleTextinPost(); // TransportSimpleTextinPost | The new TransportSimpleTextin resource
apiInstance.apiTransportSimpleTextinPost(transportSimpleTextinPost, (error, data, response) => {
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
 **transportSimpleTextinPost** | [**TransportSimpleTextinPost**](TransportSimpleTextinPost.md)| The new TransportSimpleTextin resource | 

### Return type

[**TransportSimpleTextinGet**](TransportSimpleTextinGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

