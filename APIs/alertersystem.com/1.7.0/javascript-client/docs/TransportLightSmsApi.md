# AlerterSystemApi.TransportLightSmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportLightSmsGetCollection**](TransportLightSmsApi.md#apiTransportLightSmsGetCollection) | **GET** /api/transport-light-sms | Retrieves the collection of TransportLightSms resources.
[**apiTransportLightSmsIdDelete**](TransportLightSmsApi.md#apiTransportLightSmsIdDelete) | **DELETE** /api/transport-light-sms/{id} | Removes the TransportLightSms resource.
[**apiTransportLightSmsIdGet**](TransportLightSmsApi.md#apiTransportLightSmsIdGet) | **GET** /api/transport-light-sms/{id} | Retrieves a TransportLightSms resource.
[**apiTransportLightSmsIdPatch**](TransportLightSmsApi.md#apiTransportLightSmsIdPatch) | **PATCH** /api/transport-light-sms/{id} | Updates the TransportLightSms resource.
[**apiTransportLightSmsIdPut**](TransportLightSmsApi.md#apiTransportLightSmsIdPut) | **PUT** /api/transport-light-sms/{id} | Replaces the TransportLightSms resource.
[**apiTransportLightSmsPost**](TransportLightSmsApi.md#apiTransportLightSmsPost) | **POST** /api/transport-light-sms | Creates a TransportLightSms resource.



## apiTransportLightSmsGetCollection

> [TransportLightSmsGet] apiTransportLightSmsGetCollection(opts)

Retrieves the collection of TransportLightSms resources.

Retrieves the collection of TransportLightSms resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLightSmsApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportLightSmsGetCollection(opts, (error, data, response) => {
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

[**[TransportLightSmsGet]**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLightSmsIdDelete

> apiTransportLightSmsIdDelete(id)

Removes the TransportLightSms resource.

Removes the TransportLightSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLightSmsApi();
let id = "id_example"; // String | TransportLightSms identifier
apiInstance.apiTransportLightSmsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportLightSms identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportLightSmsIdGet

> TransportLightSmsGet apiTransportLightSmsIdGet(id)

Retrieves a TransportLightSms resource.

Retrieves a TransportLightSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLightSmsApi();
let id = "id_example"; // String | TransportLightSms identifier
apiInstance.apiTransportLightSmsIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportLightSms identifier | 

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLightSmsIdPatch

> TransportLightSmsGet apiTransportLightSmsIdPatch(id, transportLightSmsPatch)

Updates the TransportLightSms resource.

Updates the TransportLightSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLightSmsApi();
let id = "id_example"; // String | TransportLightSms identifier
let transportLightSmsPatch = new AlerterSystemApi.TransportLightSmsPatch(); // TransportLightSmsPatch | The updated TransportLightSms resource
apiInstance.apiTransportLightSmsIdPatch(id, transportLightSmsPatch, (error, data, response) => {
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
 **id** | **String**| TransportLightSms identifier | 
 **transportLightSmsPatch** | [**TransportLightSmsPatch**](TransportLightSmsPatch.md)| The updated TransportLightSms resource | 

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLightSmsIdPut

> TransportLightSmsGet apiTransportLightSmsIdPut(id, transportLightSmsPut)

Replaces the TransportLightSms resource.

Replaces the TransportLightSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLightSmsApi();
let id = "id_example"; // String | TransportLightSms identifier
let transportLightSmsPut = new AlerterSystemApi.TransportLightSmsPut(); // TransportLightSmsPut | The updated TransportLightSms resource
apiInstance.apiTransportLightSmsIdPut(id, transportLightSmsPut, (error, data, response) => {
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
 **id** | **String**| TransportLightSms identifier | 
 **transportLightSmsPut** | [**TransportLightSmsPut**](TransportLightSmsPut.md)| The updated TransportLightSms resource | 

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportLightSmsPost

> TransportLightSmsGet apiTransportLightSmsPost(transportLightSmsPost)

Creates a TransportLightSms resource.

Creates a TransportLightSms resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportLightSmsApi();
let transportLightSmsPost = new AlerterSystemApi.TransportLightSmsPost(); // TransportLightSmsPost | The new TransportLightSms resource
apiInstance.apiTransportLightSmsPost(transportLightSmsPost, (error, data, response) => {
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
 **transportLightSmsPost** | [**TransportLightSmsPost**](TransportLightSmsPost.md)| The new TransportLightSms resource | 

### Return type

[**TransportLightSmsGet**](TransportLightSmsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

