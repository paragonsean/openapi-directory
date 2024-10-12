# AlerterSystemApi.TransportOrangeSmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportOrangeSmsGetCollection**](TransportOrangeSmsApi.md#apiTransportOrangeSmsGetCollection) | **GET** /api/transport-orange-sms | Retrieves the collection of TransportOrangeSms resources.
[**apiTransportOrangeSmsIdDelete**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdDelete) | **DELETE** /api/transport-orange-sms/{id} | Removes the TransportOrangeSms resource.
[**apiTransportOrangeSmsIdGet**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdGet) | **GET** /api/transport-orange-sms/{id} | Retrieves a TransportOrangeSms resource.
[**apiTransportOrangeSmsIdPatch**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdPatch) | **PATCH** /api/transport-orange-sms/{id} | Updates the TransportOrangeSms resource.
[**apiTransportOrangeSmsIdPut**](TransportOrangeSmsApi.md#apiTransportOrangeSmsIdPut) | **PUT** /api/transport-orange-sms/{id} | Replaces the TransportOrangeSms resource.
[**apiTransportOrangeSmsPost**](TransportOrangeSmsApi.md#apiTransportOrangeSmsPost) | **POST** /api/transport-orange-sms | Creates a TransportOrangeSms resource.



## apiTransportOrangeSmsGetCollection

> [TransportOrangeSmsGet] apiTransportOrangeSmsGetCollection(opts)

Retrieves the collection of TransportOrangeSms resources.

Retrieves the collection of TransportOrangeSms resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOrangeSmsApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportOrangeSmsGetCollection(opts, (error, data, response) => {
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

[**[TransportOrangeSmsGet]**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOrangeSmsIdDelete

> apiTransportOrangeSmsIdDelete(id)

Removes the TransportOrangeSms resource.

Removes the TransportOrangeSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOrangeSmsApi();
let id = "id_example"; // String | TransportOrangeSms identifier
apiInstance.apiTransportOrangeSmsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportOrangeSms identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportOrangeSmsIdGet

> TransportOrangeSmsGet apiTransportOrangeSmsIdGet(id)

Retrieves a TransportOrangeSms resource.

Retrieves a TransportOrangeSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOrangeSmsApi();
let id = "id_example"; // String | TransportOrangeSms identifier
apiInstance.apiTransportOrangeSmsIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportOrangeSms identifier | 

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOrangeSmsIdPatch

> TransportOrangeSmsGet apiTransportOrangeSmsIdPatch(id, transportOrangeSmsPatch)

Updates the TransportOrangeSms resource.

Updates the TransportOrangeSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOrangeSmsApi();
let id = "id_example"; // String | TransportOrangeSms identifier
let transportOrangeSmsPatch = new AlerterSystemApi.TransportOrangeSmsPatch(); // TransportOrangeSmsPatch | The updated TransportOrangeSms resource
apiInstance.apiTransportOrangeSmsIdPatch(id, transportOrangeSmsPatch, (error, data, response) => {
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
 **id** | **String**| TransportOrangeSms identifier | 
 **transportOrangeSmsPatch** | [**TransportOrangeSmsPatch**](TransportOrangeSmsPatch.md)| The updated TransportOrangeSms resource | 

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOrangeSmsIdPut

> TransportOrangeSmsGet apiTransportOrangeSmsIdPut(id, transportOrangeSmsPut)

Replaces the TransportOrangeSms resource.

Replaces the TransportOrangeSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOrangeSmsApi();
let id = "id_example"; // String | TransportOrangeSms identifier
let transportOrangeSmsPut = new AlerterSystemApi.TransportOrangeSmsPut(); // TransportOrangeSmsPut | The updated TransportOrangeSms resource
apiInstance.apiTransportOrangeSmsIdPut(id, transportOrangeSmsPut, (error, data, response) => {
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
 **id** | **String**| TransportOrangeSms identifier | 
 **transportOrangeSmsPut** | [**TransportOrangeSmsPut**](TransportOrangeSmsPut.md)| The updated TransportOrangeSms resource | 

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportOrangeSmsPost

> TransportOrangeSmsGet apiTransportOrangeSmsPost(transportOrangeSmsPost)

Creates a TransportOrangeSms resource.

Creates a TransportOrangeSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportOrangeSmsApi();
let transportOrangeSmsPost = new AlerterSystemApi.TransportOrangeSmsPost(); // TransportOrangeSmsPost | The new TransportOrangeSms resource
apiInstance.apiTransportOrangeSmsPost(transportOrangeSmsPost, (error, data, response) => {
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
 **transportOrangeSmsPost** | [**TransportOrangeSmsPost**](TransportOrangeSmsPost.md)| The new TransportOrangeSms resource | 

### Return type

[**TransportOrangeSmsGet**](TransportOrangeSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

