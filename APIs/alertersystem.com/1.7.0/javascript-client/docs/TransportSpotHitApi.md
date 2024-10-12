# AlerterSystemApi.TransportSpotHitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSpotHitGetCollection**](TransportSpotHitApi.md#apiTransportSpotHitGetCollection) | **GET** /api/transport-spot-hit | Retrieves the collection of TransportSpotHit resources.
[**apiTransportSpotHitIdDelete**](TransportSpotHitApi.md#apiTransportSpotHitIdDelete) | **DELETE** /api/transport-spot-hit/{id} | Removes the TransportSpotHit resource.
[**apiTransportSpotHitIdGet**](TransportSpotHitApi.md#apiTransportSpotHitIdGet) | **GET** /api/transport-spot-hit/{id} | Retrieves a TransportSpotHit resource.
[**apiTransportSpotHitIdPatch**](TransportSpotHitApi.md#apiTransportSpotHitIdPatch) | **PATCH** /api/transport-spot-hit/{id} | Updates the TransportSpotHit resource.
[**apiTransportSpotHitIdPut**](TransportSpotHitApi.md#apiTransportSpotHitIdPut) | **PUT** /api/transport-spot-hit/{id} | Replaces the TransportSpotHit resource.
[**apiTransportSpotHitPost**](TransportSpotHitApi.md#apiTransportSpotHitPost) | **POST** /api/transport-spot-hit | Creates a TransportSpotHit resource.



## apiTransportSpotHitGetCollection

> [TransportSpotHitGet] apiTransportSpotHitGetCollection(opts)

Retrieves the collection of TransportSpotHit resources.

Retrieves the collection of TransportSpotHit resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSpotHitApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSpotHitGetCollection(opts, (error, data, response) => {
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

[**[TransportSpotHitGet]**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSpotHitIdDelete

> apiTransportSpotHitIdDelete(id)

Removes the TransportSpotHit resource.

Removes the TransportSpotHit resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSpotHitApi();
let id = "id_example"; // String | TransportSpotHit identifier
apiInstance.apiTransportSpotHitIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSpotHit identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSpotHitIdGet

> TransportSpotHitGet apiTransportSpotHitIdGet(id)

Retrieves a TransportSpotHit resource.

Retrieves a TransportSpotHit resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSpotHitApi();
let id = "id_example"; // String | TransportSpotHit identifier
apiInstance.apiTransportSpotHitIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSpotHit identifier | 

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSpotHitIdPatch

> TransportSpotHitGet apiTransportSpotHitIdPatch(id, transportSpotHitPatch)

Updates the TransportSpotHit resource.

Updates the TransportSpotHit resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSpotHitApi();
let id = "id_example"; // String | TransportSpotHit identifier
let transportSpotHitPatch = new AlerterSystemApi.TransportSpotHitPatch(); // TransportSpotHitPatch | The updated TransportSpotHit resource
apiInstance.apiTransportSpotHitIdPatch(id, transportSpotHitPatch, (error, data, response) => {
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
 **id** | **String**| TransportSpotHit identifier | 
 **transportSpotHitPatch** | [**TransportSpotHitPatch**](TransportSpotHitPatch.md)| The updated TransportSpotHit resource | 

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSpotHitIdPut

> TransportSpotHitGet apiTransportSpotHitIdPut(id, transportSpotHitPut)

Replaces the TransportSpotHit resource.

Replaces the TransportSpotHit resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSpotHitApi();
let id = "id_example"; // String | TransportSpotHit identifier
let transportSpotHitPut = new AlerterSystemApi.TransportSpotHitPut(); // TransportSpotHitPut | The updated TransportSpotHit resource
apiInstance.apiTransportSpotHitIdPut(id, transportSpotHitPut, (error, data, response) => {
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
 **id** | **String**| TransportSpotHit identifier | 
 **transportSpotHitPut** | [**TransportSpotHitPut**](TransportSpotHitPut.md)| The updated TransportSpotHit resource | 

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSpotHitPost

> TransportSpotHitGet apiTransportSpotHitPost(transportSpotHitPost)

Creates a TransportSpotHit resource.

Creates a TransportSpotHit resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSpotHitApi();
let transportSpotHitPost = new AlerterSystemApi.TransportSpotHitPost(); // TransportSpotHitPost | The new TransportSpotHit resource
apiInstance.apiTransportSpotHitPost(transportSpotHitPost, (error, data, response) => {
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
 **transportSpotHitPost** | [**TransportSpotHitPost**](TransportSpotHitPost.md)| The new TransportSpotHit resource | 

### Return type

[**TransportSpotHitGet**](TransportSpotHitGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

