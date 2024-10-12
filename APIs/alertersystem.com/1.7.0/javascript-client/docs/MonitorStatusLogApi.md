# AlerterSystemApi.MonitorStatusLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMonitorStatusLogGetCollection**](MonitorStatusLogApi.md#apiMonitorStatusLogGetCollection) | **GET** /api/monitor-status-log | Retrieves the collection of MonitorStatusLog resources.
[**apiMonitorStatusLogIdGet**](MonitorStatusLogApi.md#apiMonitorStatusLogIdGet) | **GET** /api/monitor-status-log/{id} | Retrieves a MonitorStatusLog resource.



## apiMonitorStatusLogGetCollection

> [MonitorStatusLogGet] apiMonitorStatusLogGetCollection(opts)

Retrieves the collection of MonitorStatusLog resources.

Retrieves the collection of MonitorStatusLog resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorStatusLogApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'monitor': "monitor_example", // String | 
  'monitor2': ["null"], // [String] | 
  'monitorStatusCode': "monitorStatusCode_example", // String | 
  'monitorStatusCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiMonitorStatusLogGetCollection(opts, (error, data, response) => {
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
 **monitor** | **String**|  | [optional] 
 **monitor2** | [**[String]**](String.md)|  | [optional] 
 **monitorStatusCode** | **String**|  | [optional] 
 **monitorStatusCode2** | [**[String]**](String.md)|  | [optional] 
 **partition** | **String**|  | [optional] 
 **partition2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[MonitorStatusLogGet]**](MonitorStatusLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiMonitorStatusLogIdGet

> MonitorStatusLogGet apiMonitorStatusLogIdGet(id)

Retrieves a MonitorStatusLog resource.

Retrieves a MonitorStatusLog resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.MonitorStatusLogApi();
let id = "id_example"; // String | MonitorStatusLog identifier
apiInstance.apiMonitorStatusLogIdGet(id, (error, data, response) => {
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
 **id** | **String**| MonitorStatusLog identifier | 

### Return type

[**MonitorStatusLogGet**](MonitorStatusLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

