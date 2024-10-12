# AlerterSystemApi.MonitorTypeCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMonitorTypeCodeGetCollection**](MonitorTypeCodeApi.md#apiMonitorTypeCodeGetCollection) | **GET** /api/monitor-type-code | Retrieves the collection of MonitorTypeCode resources.
[**apiMonitorTypeCodeIdGet**](MonitorTypeCodeApi.md#apiMonitorTypeCodeIdGet) | **GET** /api/monitor-type-code/{id} | Retrieves a MonitorTypeCode resource.



## apiMonitorTypeCodeGetCollection

> [MonitorTypeCodeGet] apiMonitorTypeCodeGetCollection(opts)

Retrieves the collection of MonitorTypeCode resources.

Retrieves the collection of MonitorTypeCode resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorTypeCodeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiMonitorTypeCodeGetCollection(opts, (error, data, response) => {
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

[**[MonitorTypeCodeGet]**](MonitorTypeCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiMonitorTypeCodeIdGet

> MonitorTypeCodeGet apiMonitorTypeCodeIdGet(id)

Retrieves a MonitorTypeCode resource.

Retrieves a MonitorTypeCode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorTypeCodeApi();
let id = "id_example"; // String | MonitorTypeCode identifier
apiInstance.apiMonitorTypeCodeIdGet(id, (error, data, response) => {
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
 **id** | **String**| MonitorTypeCode identifier | 

### Return type

[**MonitorTypeCodeGet**](MonitorTypeCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

