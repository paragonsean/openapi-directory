# SevenIoApi.PricingApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pricing**](PricingApi.md#pricing) | **GET** /pricing | 



## pricing

> pricing(opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.PricingApi();
let opts = {
  'country': "country_example", // String | The countries ISO code to get pricings for. Allowed values are de, fr, at. Omit to show pricings for all channels.
  'format': "format_example" // String | Determines the response format. Allowed values are json and csv. The default value is json.
};
apiInstance.pricing(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| The countries ISO code to get pricings for. Allowed values are de, fr, at. Omit to show pricings for all channels. | [optional] 
 **format** | **String**| Determines the response format. Allowed values are json and csv. The default value is json. | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

