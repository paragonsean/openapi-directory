# AlerterSystemApi.MonitorStatusCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMonitorStatusCodeGetCollection**](MonitorStatusCodeApi.md#apiMonitorStatusCodeGetCollection) | **GET** /api/monitor-status-code | Retrieves the collection of MonitorStatusCode resources.
[**apiMonitorStatusCodeIdGet**](MonitorStatusCodeApi.md#apiMonitorStatusCodeIdGet) | **GET** /api/monitor-status-code/{id} | Retrieves a MonitorStatusCode resource.



## apiMonitorStatusCodeGetCollection

> [MonitorStatusCodeGet] apiMonitorStatusCodeGetCollection(opts)

Retrieves the collection of MonitorStatusCode resources.

Retrieves the collection of MonitorStatusCode resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorStatusCodeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiMonitorStatusCodeGetCollection(opts, (error, data, response) => {
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
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[MonitorStatusCodeGet]**](MonitorStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiMonitorStatusCodeIdGet

> MonitorStatusCodeGet apiMonitorStatusCodeIdGet(id)

Retrieves a MonitorStatusCode resource.

Retrieves a MonitorStatusCode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorStatusCodeApi();
let id = "id_example"; // String | MonitorStatusCode identifier
apiInstance.apiMonitorStatusCodeIdGet(id, (error, data, response) => {
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
 **id** | **String**| MonitorStatusCode identifier | 

### Return type

[**MonitorStatusCodeGet**](MonitorStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

