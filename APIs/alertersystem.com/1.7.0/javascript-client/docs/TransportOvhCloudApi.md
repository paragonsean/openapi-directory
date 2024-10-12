# AlerterSystemApi.TransportOvhCloudApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportOvhCloudGetCollection**](TransportOvhCloudApi.md#apiTransportOvhCloudGetCollection) | **GET** /api/transport-ovh-cloud | Retrieves the collection of TransportOvhCloud resources.
[**apiTransportOvhCloudIdDelete**](TransportOvhCloudApi.md#apiTransportOvhCloudIdDelete) | **DELETE** /api/transport-ovh-cloud/{id} | Removes the TransportOvhCloud resource.
[**apiTransportOvhCloudIdGet**](TransportOvhCloudApi.md#apiTransportOvhCloudIdGet) | **GET** /api/transport-ovh-cloud/{id} | Retrieves a TransportOvhCloud resource.
[**apiTransportOvhCloudIdPatch**](TransportOvhCloudApi.md#apiTransportOvhCloudIdPatch) | **PATCH** /api/transport-ovh-cloud/{id} | Updates the TransportOvhCloud resource.
[**apiTransportOvhCloudIdPut**](TransportOvhCloudApi.md#apiTransportOvhCloudIdPut) | **PUT** /api/transport-ovh-cloud/{id} | Replaces the TransportOvhCloud resource.
[**apiTransportOvhCloudPost**](TransportOvhCloudApi.md#apiTransportOvhCloudPost) | **POST** /api/transport-ovh-cloud | Creates a TransportOvhCloud resource.



## apiTransportOvhCloudGetCollection

> [TransportOvhCloudGet] apiTransportOvhCloudGetCollection(opts)

Retrieves the collection of TransportOvhCloud resources.

Retrieves the collection of TransportOvhCloud resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOvhCloudApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportOvhCloudGetCollection(opts, (error, data, response) => {
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

[**[TransportOvhCloudGet]**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOvhCloudIdDelete

> apiTransportOvhCloudIdDelete(id)

Removes the TransportOvhCloud resource.

Removes the TransportOvhCloud resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOvhCloudApi();
let id = "id_example"; // String | TransportOvhCloud identifier
apiInstance.apiTransportOvhCloudIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportOvhCloud identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportOvhCloudIdGet

> TransportOvhCloudGet apiTransportOvhCloudIdGet(id)

Retrieves a TransportOvhCloud resource.

Retrieves a TransportOvhCloud resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOvhCloudApi();
let id = "id_example"; // String | TransportOvhCloud identifier
apiInstance.apiTransportOvhCloudIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportOvhCloud identifier | 

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOvhCloudIdPatch

> TransportOvhCloudGet apiTransportOvhCloudIdPatch(id, transportOvhCloudPatch)

Updates the TransportOvhCloud resource.

Updates the TransportOvhCloud resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOvhCloudApi();
let id = "id_example"; // String | TransportOvhCloud identifier
let transportOvhCloudPatch = new AlerterSystemApi.TransportOvhCloudPatch(); // TransportOvhCloudPatch | The updated TransportOvhCloud resource
apiInstance.apiTransportOvhCloudIdPatch(id, transportOvhCloudPatch, (error, data, response) => {
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
 **id** | **String**| TransportOvhCloud identifier | 
 **transportOvhCloudPatch** | [**TransportOvhCloudPatch**](TransportOvhCloudPatch.md)| The updated TransportOvhCloud resource | 

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOvhCloudIdPut

> TransportOvhCloudGet apiTransportOvhCloudIdPut(id, transportOvhCloudPut)

Replaces the TransportOvhCloud resource.

Replaces the TransportOvhCloud resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOvhCloudApi();
let id = "id_example"; // String | TransportOvhCloud identifier
let transportOvhCloudPut = new AlerterSystemApi.TransportOvhCloudPut(); // TransportOvhCloudPut | The updated TransportOvhCloud resource
apiInstance.apiTransportOvhCloudIdPut(id, transportOvhCloudPut, (error, data, response) => {
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
 **id** | **String**| TransportOvhCloud identifier | 
 **transportOvhCloudPut** | [**TransportOvhCloudPut**](TransportOvhCloudPut.md)| The updated TransportOvhCloud resource | 

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOvhCloudPost

> TransportOvhCloudGet apiTransportOvhCloudPost(transportOvhCloudPost)

Creates a TransportOvhCloud resource.

Creates a TransportOvhCloud resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOvhCloudApi();
let transportOvhCloudPost = new AlerterSystemApi.TransportOvhCloudPost(); // TransportOvhCloudPost | The new TransportOvhCloud resource
apiInstance.apiTransportOvhCloudPost(transportOvhCloudPost, (error, data, response) => {
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
 **transportOvhCloudPost** | [**TransportOvhCloudPost**](TransportOvhCloudPost.md)| The new TransportOvhCloud resource | 

### Return type

[**TransportOvhCloudGet**](TransportOvhCloudGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

