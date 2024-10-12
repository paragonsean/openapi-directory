# AlerterSystemApi.AlertLogStatusCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiAlertLogStatusCodeGetCollection**](AlertLogStatusCodeApi.md#apiAlertLogStatusCodeGetCollection) | **GET** /api/alert-log-status-code | Retrieves the collection of AlertLogStatusCode resources.
[**apiAlertLogStatusCodeIdGet**](AlertLogStatusCodeApi.md#apiAlertLogStatusCodeIdGet) | **GET** /api/alert-log-status-code/{id} | Retrieves a AlertLogStatusCode resource.



## apiAlertLogStatusCodeGetCollection

> [AlertLogStatusCodeGet] apiAlertLogStatusCodeGetCollection(opts)

Retrieves the collection of AlertLogStatusCode resources.

Retrieves the collection of AlertLogStatusCode resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertLogStatusCodeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiAlertLogStatusCodeGetCollection(opts, (error, data, response) => {
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

[**[AlertLogStatusCodeGet]**](AlertLogStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiAlertLogStatusCodeIdGet

> AlertLogStatusCodeGet apiAlertLogStatusCodeIdGet(id)

Retrieves a AlertLogStatusCode resource.

Retrieves a AlertLogStatusCode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertLogStatusCodeApi();
let id = "id_example"; // String | AlertLogStatusCode identifier
apiInstance.apiAlertLogStatusCodeIdGet(id, (error, data, response) => {
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
 **id** | **String**| AlertLogStatusCode identifier | 

### Return type

[**AlertLogStatusCodeGet**](AlertLogStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

