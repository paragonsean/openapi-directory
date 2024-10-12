# AlerterSystemApi.TransportOctopushApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportOctopushGetCollection**](TransportOctopushApi.md#apiTransportOctopushGetCollection) | **GET** /api/transport-octopush | Retrieves the collection of TransportOctopush resources.
[**apiTransportOctopushIdDelete**](TransportOctopushApi.md#apiTransportOctopushIdDelete) | **DELETE** /api/transport-octopush/{id} | Removes the TransportOctopush resource.
[**apiTransportOctopushIdGet**](TransportOctopushApi.md#apiTransportOctopushIdGet) | **GET** /api/transport-octopush/{id} | Retrieves a TransportOctopush resource.
[**apiTransportOctopushIdPatch**](TransportOctopushApi.md#apiTransportOctopushIdPatch) | **PATCH** /api/transport-octopush/{id} | Updates the TransportOctopush resource.
[**apiTransportOctopushIdPut**](TransportOctopushApi.md#apiTransportOctopushIdPut) | **PUT** /api/transport-octopush/{id} | Replaces the TransportOctopush resource.
[**apiTransportOctopushPost**](TransportOctopushApi.md#apiTransportOctopushPost) | **POST** /api/transport-octopush | Creates a TransportOctopush resource.



## apiTransportOctopushGetCollection

> [TransportOctopushGet] apiTransportOctopushGetCollection(opts)

Retrieves the collection of TransportOctopush resources.

Retrieves the collection of TransportOctopush resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOctopushApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportOctopushGetCollection(opts, (error, data, response) => {
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

[**[TransportOctopushGet]**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOctopushIdDelete

> apiTransportOctopushIdDelete(id)

Removes the TransportOctopush resource.

Removes the TransportOctopush resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOctopushApi();
let id = "id_example"; // String | TransportOctopush identifier
apiInstance.apiTransportOctopushIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportOctopush identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportOctopushIdGet

> TransportOctopushGet apiTransportOctopushIdGet(id)

Retrieves a TransportOctopush resource.

Retrieves a TransportOctopush resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOctopushApi();
let id = "id_example"; // String | TransportOctopush identifier
apiInstance.apiTransportOctopushIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportOctopush identifier | 

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOctopushIdPatch

> TransportOctopushGet apiTransportOctopushIdPatch(id, transportOctopushPatch)

Updates the TransportOctopush resource.

Updates the TransportOctopush resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOctopushApi();
let id = "id_example"; // String | TransportOctopush identifier
let transportOctopushPatch = new AlerterSystemApi.TransportOctopushPatch(); // TransportOctopushPatch | The updated TransportOctopush resource
apiInstance.apiTransportOctopushIdPatch(id, transportOctopushPatch, (error, data, response) => {
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
 **id** | **String**| TransportOctopush identifier | 
 **transportOctopushPatch** | [**TransportOctopushPatch**](TransportOctopushPatch.md)| The updated TransportOctopush resource | 

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOctopushIdPut

> TransportOctopushGet apiTransportOctopushIdPut(id, transportOctopushPut)

Replaces the TransportOctopush resource.

Replaces the TransportOctopush resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOctopushApi();
let id = "id_example"; // String | TransportOctopush identifier
let transportOctopushPut = new AlerterSystemApi.TransportOctopushPut(); // TransportOctopushPut | The updated TransportOctopush resource
apiInstance.apiTransportOctopushIdPut(id, transportOctopushPut, (error, data, response) => {
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
 **id** | **String**| TransportOctopush identifier | 
 **transportOctopushPut** | [**TransportOctopushPut**](TransportOctopushPut.md)| The updated TransportOctopush resource | 

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOctopushPost

> TransportOctopushGet apiTransportOctopushPost(transportOctopushPost)

Creates a TransportOctopush resource.

Creates a TransportOctopush resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOctopushApi();
let transportOctopushPost = new AlerterSystemApi.TransportOctopushPost(); // TransportOctopushPost | The new TransportOctopush resource
apiInstance.apiTransportOctopushPost(transportOctopushPost, (error, data, response) => {
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
 **transportOctopushPost** | [**TransportOctopushPost**](TransportOctopushPost.md)| The new TransportOctopush resource | 

### Return type

[**TransportOctopushGet**](TransportOctopushGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

