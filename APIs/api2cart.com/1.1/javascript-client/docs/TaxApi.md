# SwaggerApi2Cart.TaxApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxClassInfo**](TaxApi.md#taxClassInfo) | **GET** /tax.class.info.json | 



## taxClassInfo

> TaxClassInfo200Response taxClassInfo(taxClassId, opts)



Get info about tax

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.TaxApi();
let taxClassId = "taxClassId_example"; // String | Retrieves taxes specified by class id
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'params': "'tax_class_id,name,avail'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.taxClassInfo(taxClassId, opts, (error, data, response) => {
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
 **taxClassId** | **String**| Retrieves taxes specified by class id | 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;tax_class_id,name,avail&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**TaxClassInfo200Response**](TaxClassInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

