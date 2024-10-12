# FoodAndSuppliesDepartmentHaryana.APIsApi

All URIs are relative to *https://apisetu.gov.in/fsdhr/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ratcr**](APIsApi.md#ratcr) | **POST** /ratcr/certificate | Ration Card



## ratcr

> ratcr(opts)

Ration Card

API to verify Ration Card.

### Example

```javascript
import FoodAndSuppliesDepartmentHaryana from 'food_and_supplies_department_haryana';
let defaultClient = FoodAndSuppliesDepartmentHaryana.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new FoodAndSuppliesDepartmentHaryana.APIsApi();
let opts = {
  'ratcrRequest': new FoodAndSuppliesDepartmentHaryana.RatcrRequest() // RatcrRequest | Request format
};
apiInstance.ratcr(opts, (error, data, response) => {
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
 **ratcrRequest** | [**RatcrRequest**](RatcrRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

