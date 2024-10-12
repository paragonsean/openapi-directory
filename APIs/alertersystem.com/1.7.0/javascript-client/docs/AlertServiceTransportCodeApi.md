# AlerterSystemApi.AlertServiceTransportCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiAlertServiceTransportCodeGetCollection**](AlertServiceTransportCodeApi.md#apiAlertServiceTransportCodeGetCollection) | **GET** /api/alert-service-transport-code | Retrieves the collection of AlertServiceTransportCode resources.
[**apiAlertServiceTransportCodeIdGet**](AlertServiceTransportCodeApi.md#apiAlertServiceTransportCodeIdGet) | **GET** /api/alert-service-transport-code/{id} | Retrieves a AlertServiceTransportCode resource.



## apiAlertServiceTransportCodeGetCollection

> [AlertServiceTransportCodeGet] apiAlertServiceTransportCodeGetCollection(opts)

Retrieves the collection of AlertServiceTransportCode resources.

Retrieves the collection of AlertServiceTransportCode resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceTransportCodeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiAlertServiceTransportCodeGetCollection(opts, (error, data, response) => {
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

[**[AlertServiceTransportCodeGet]**](AlertServiceTransportCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiAlertServiceTransportCodeIdGet

> AlertServiceTransportCodeGet apiAlertServiceTransportCodeIdGet(id)

Retrieves a AlertServiceTransportCode resource.

Retrieves a AlertServiceTransportCode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceTransportCodeApi();
let id = "id_example"; // String | AlertServiceTransportCode identifier
apiInstance.apiAlertServiceTransportCodeIdGet(id, (error, data, response) => {
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
 **id** | **String**| AlertServiceTransportCode identifier | 

### Return type

[**AlertServiceTransportCodeGet**](AlertServiceTransportCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

