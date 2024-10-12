# AlerterSystemApi.TimezoneCodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTimezoneCodeGetCollection**](TimezoneCodeApi.md#apiTimezoneCodeGetCollection) | **GET** /api/timezone-code | Retrieves the collection of TimezoneCode resources.
[**apiTimezoneCodeIdGet**](TimezoneCodeApi.md#apiTimezoneCodeIdGet) | **GET** /api/timezone-code/{id} | Retrieves a TimezoneCode resource.



## apiTimezoneCodeGetCollection

> [TimezoneCodeGet] apiTimezoneCodeGetCollection(opts)

Retrieves the collection of TimezoneCode resources.

Retrieves the collection of TimezoneCode resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TimezoneCodeApi();
let opts = {
  'page': 1, // Number | The collection page number
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTimezoneCodeGetCollection(opts, (error, data, response) => {
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

[**[TimezoneCodeGet]**](TimezoneCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTimezoneCodeIdGet

> TimezoneCodeGet apiTimezoneCodeIdGet(id)

Retrieves a TimezoneCode resource.

Retrieves a TimezoneCode resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TimezoneCodeApi();
let id = "id_example"; // String | TimezoneCode identifier
apiInstance.apiTimezoneCodeIdGet(id, (error, data, response) => {
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
 **id** | **String**| TimezoneCode identifier | 

### Return type

[**TimezoneCodeGet**](TimezoneCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html

