# AppStoreConnectApi.AppPricesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appPricesGetInstance**](AppPricesApi.md#appPricesGetInstance) | **GET** /v1/appPrices/{id} | 



## appPricesGetInstance

> AppPriceResponse appPricesGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppPricesApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppPrices': ["null"], // [String] | the fields to include for returned resources of type appPrices
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appPricesGetInstance(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppPrices** | [**[String]**](String.md)| the fields to include for returned resources of type appPrices | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**AppPriceResponse**](AppPriceResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

