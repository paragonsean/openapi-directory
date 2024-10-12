# AlerterSystemApi.TransportPagerDutyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportPagerDutyGetCollection**](TransportPagerDutyApi.md#apiTransportPagerDutyGetCollection) | **GET** /api/transport-pager-duty | Retrieves the collection of TransportPagerDuty resources.
[**apiTransportPagerDutyIdDelete**](TransportPagerDutyApi.md#apiTransportPagerDutyIdDelete) | **DELETE** /api/transport-pager-duty/{id} | Removes the TransportPagerDuty resource.
[**apiTransportPagerDutyIdGet**](TransportPagerDutyApi.md#apiTransportPagerDutyIdGet) | **GET** /api/transport-pager-duty/{id} | Retrieves a TransportPagerDuty resource.
[**apiTransportPagerDutyIdPatch**](TransportPagerDutyApi.md#apiTransportPagerDutyIdPatch) | **PATCH** /api/transport-pager-duty/{id} | Updates the TransportPagerDuty resource.
[**apiTransportPagerDutyIdPut**](TransportPagerDutyApi.md#apiTransportPagerDutyIdPut) | **PUT** /api/transport-pager-duty/{id} | Replaces the TransportPagerDuty resource.
[**apiTransportPagerDutyPost**](TransportPagerDutyApi.md#apiTransportPagerDutyPost) | **POST** /api/transport-pager-duty | Creates a TransportPagerDuty resource.



## apiTransportPagerDutyGetCollection

> [TransportPagerDutyGet] apiTransportPagerDutyGetCollection(opts)

Retrieves the collection of TransportPagerDuty resources.

Retrieves the collection of TransportPagerDuty resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerDutyApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportPagerDutyGetCollection(opts, (error, data, response) => {
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

[**[TransportPagerDutyGet]**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerDutyIdDelete

> apiTransportPagerDutyIdDelete(id)

Removes the TransportPagerDuty resource.

Removes the TransportPagerDuty resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerDutyApi();
let id = "id_example"; // String | TransportPagerDuty identifier
apiInstance.apiTransportPagerDutyIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportPagerDuty identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportPagerDutyIdGet

> TransportPagerDutyGet apiTransportPagerDutyIdGet(id)

Retrieves a TransportPagerDuty resource.

Retrieves a TransportPagerDuty resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerDutyApi();
let id = "id_example"; // String | TransportPagerDuty identifier
apiInstance.apiTransportPagerDutyIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportPagerDuty identifier | 

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerDutyIdPatch

> TransportPagerDutyGet apiTransportPagerDutyIdPatch(id, transportPagerDutyPatch)

Updates the TransportPagerDuty resource.

Updates the TransportPagerDuty resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerDutyApi();
let id = "id_example"; // String | TransportPagerDuty identifier
let transportPagerDutyPatch = new AlerterSystemApi.TransportPagerDutyPatch(); // TransportPagerDutyPatch | The updated TransportPagerDuty resource
apiInstance.apiTransportPagerDutyIdPatch(id, transportPagerDutyPatch, (error, data, response) => {
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
 **id** | **String**| TransportPagerDuty identifier | 
 **transportPagerDutyPatch** | [**TransportPagerDutyPatch**](TransportPagerDutyPatch.md)| The updated TransportPagerDuty resource | 

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerDutyIdPut

> TransportPagerDutyGet apiTransportPagerDutyIdPut(id, transportPagerDutyPut)

Replaces the TransportPagerDuty resource.

Replaces the TransportPagerDuty resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerDutyApi();
let id = "id_example"; // String | TransportPagerDuty identifier
let transportPagerDutyPut = new AlerterSystemApi.TransportPagerDutyPut(); // TransportPagerDutyPut | The updated TransportPagerDuty resource
apiInstance.apiTransportPagerDutyIdPut(id, transportPagerDutyPut, (error, data, response) => {
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
 **id** | **String**| TransportPagerDuty identifier | 
 **transportPagerDutyPut** | [**TransportPagerDutyPut**](TransportPagerDutyPut.md)| The updated TransportPagerDuty resource | 

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportPagerDutyPost

> TransportPagerDutyGet apiTransportPagerDutyPost(transportPagerDutyPost)

Creates a TransportPagerDuty resource.

Creates a TransportPagerDuty resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportPagerDutyApi();
let transportPagerDutyPost = new AlerterSystemApi.TransportPagerDutyPost(); // TransportPagerDutyPost | The new TransportPagerDuty resource
apiInstance.apiTransportPagerDutyPost(transportPagerDutyPost, (error, data, response) => {
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
 **transportPagerDutyPost** | [**TransportPagerDutyPost**](TransportPagerDutyPost.md)| The new TransportPagerDuty resource | 

### Return type

[**TransportPagerDutyGet**](TransportPagerDutyGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

