# AlerterSystemApi.MonitorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMonitorGetCollection**](MonitorApi.md#apiMonitorGetCollection) | **GET** /api/monitor | Retrieves the collection of Monitor resources.
[**apiMonitorIdDelete**](MonitorApi.md#apiMonitorIdDelete) | **DELETE** /api/monitor/{id} | Removes the Monitor resource.
[**apiMonitorIdGet**](MonitorApi.md#apiMonitorIdGet) | **GET** /api/monitor/{id} | Retrieves a Monitor resource.
[**apiMonitorIdPatch**](MonitorApi.md#apiMonitorIdPatch) | **PATCH** /api/monitor/{id} | Updates the Monitor resource.
[**apiMonitorIdPut**](MonitorApi.md#apiMonitorIdPut) | **PUT** /api/monitor/{id} | Replaces the Monitor resource.
[**apiMonitorPost**](MonitorApi.md#apiMonitorPost) | **POST** /api/monitor | Creates a Monitor resource.



## apiMonitorGetCollection

> [MonitorGet] apiMonitorGetCollection(opts)

Retrieves the collection of Monitor resources.

Retrieves the collection of Monitor resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiMonitorGetCollection(opts, (error, data, response) => {
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

[**[MonitorGet]**](MonitorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiMonitorIdDelete

> apiMonitorIdDelete(id)

Removes the Monitor resource.

Removes the Monitor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorApi();
let id = "id_example"; // String | Monitor identifier
apiInstance.apiMonitorIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Monitor identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiMonitorIdGet

> MonitorGet apiMonitorIdGet(id)

Retrieves a Monitor resource.

Retrieves a Monitor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorApi();
let id = "id_example"; // String | Monitor identifier
apiInstance.apiMonitorIdGet(id, (error, data, response) => {
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
 **id** | **String**| Monitor identifier | 

### Return type

[**MonitorGet**](MonitorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiMonitorIdPatch

> MonitorGet apiMonitorIdPatch(id, monitorPatch)

Updates the Monitor resource.

Updates the Monitor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorApi();
let id = "id_example"; // String | Monitor identifier
let monitorPatch = new AlerterSystemApi.MonitorPatch(); // MonitorPatch | The updated Monitor resource
apiInstance.apiMonitorIdPatch(id, monitorPatch, (error, data, response) => {
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
 **id** | **String**| Monitor identifier | 
 **monitorPatch** | [**MonitorPatch**](MonitorPatch.md)| The updated Monitor resource | 

### Return type

[**MonitorGet**](MonitorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiMonitorIdPut

> MonitorGet apiMonitorIdPut(id, monitorPut)

Replaces the Monitor resource.

Replaces the Monitor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorApi();
let id = "id_example"; // String | Monitor identifier
let monitorPut = new AlerterSystemApi.MonitorPut(); // MonitorPut | The updated Monitor resource
apiInstance.apiMonitorIdPut(id, monitorPut, (error, data, response) => {
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
 **id** | **String**| Monitor identifier | 
 **monitorPut** | [**MonitorPut**](MonitorPut.md)| The updated Monitor resource | 

### Return type

[**MonitorGet**](MonitorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiMonitorPost

> MonitorGet apiMonitorPost(monitorPost)

Creates a Monitor resource.

Creates a Monitor resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorApi();
let monitorPost = new AlerterSystemApi.MonitorPost(); // MonitorPost | The new Monitor resource
apiInstance.apiMonitorPost(monitorPost, (error, data, response) => {
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
 **monitorPost** | [**MonitorPost**](MonitorPost.md)| The new Monitor resource | 

### Return type

[**MonitorGet**](MonitorGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

