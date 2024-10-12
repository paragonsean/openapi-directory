# AlerterSystemApi.AlertLogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiAlertLogGetCollection**](AlertLogApi.md#apiAlertLogGetCollection) | **GET** /api/alert-log | Retrieves the collection of AlertLog resources.
[**apiAlertLogIdGet**](AlertLogApi.md#apiAlertLogIdGet) | **GET** /api/alert-log/{id} | Retrieves a AlertLog resource.



## apiAlertLogGetCollection

> [AlertLogGet] apiAlertLogGetCollection(opts)

Retrieves the collection of AlertLog resources.

Retrieves the collection of AlertLog resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertLogApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'monitor': "monitor_example", // String | 
  'monitor2': ["null"], // [String] | 
  'alertService': "alertService_example", // String | 
  'alertService2': ["null"], // [String] | 
  'alertLogStatusCode': "alertLogStatusCode_example", // String | 
  'alertLogStatusCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiAlertLogGetCollection(opts, (error, data, response) => {
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
 **alertService** | **String**|  | [optional] 
 **alertService2** | [**[String]**](String.md)|  | [optional] 
 **alertLogStatusCode** | **String**|  | [optional] 
 **alertLogStatusCode2** | [**[String]**](String.md)|  | [optional] 
 **partition** | **String**|  | [optional] 
 **partition2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[AlertLogGet]**](AlertLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiAlertLogIdGet

> AlertLogGet apiAlertLogIdGet(id)

Retrieves a AlertLog resource.

Retrieves a AlertLog resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertLogApi();
let id = "id_example"; // String | AlertLog identifier
apiInstance.apiAlertLogIdGet(id, (error, data, response) => {
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
 **id** | **String**| AlertLog identifier | 

### Return type

[**AlertLogGet**](AlertLogGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

