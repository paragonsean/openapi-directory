# ExoApi.UnitConverterApi

All URIs are relative to *https://api.exoapi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**unitConverterGet**](UnitConverterApi.md#unitConverterGet) | **GET** /unit-converter | 



## unitConverterGet

> UnitConverterGet200Response unitConverterGet(from, to, value)



Quickly convert between all different kinds of measurement units

### Example

```javascript
import ExoApi from 'exo_api';
let defaultClient = ExoApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExoApi.UnitConverterApi();
let from = "from_example"; // String | 
let to = "to_example"; // String | 
let value = 3.4; // Number | 
apiInstance.unitConverterGet(from, to, value, (error, data, response) => {
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
 **from** | **String**|  | 
 **to** | **String**|  | 
 **value** | **Number**|  | 

### Return type

[**UnitConverterGet200Response**](UnitConverterGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

