# PaymentsGatewayApi.InstallmentsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**installmentsoptions**](InstallmentsApi.md#installmentsoptions) | **GET** /api/pvt/installments | Installments options



## installmentsoptions

> ValidRequest installmentsoptions(requestValue, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, opts)

Installments options

Returns the best installment options according to the informed params.

### Example

```javascript
import PaymentsGatewayApi from 'payments_gateway_api';
let defaultClient = PaymentsGatewayApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new PaymentsGatewayApi.InstallmentsApi();
let requestValue = 10; // Number | 
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let opts = {
  'requestSalesChannel': 1, // Number | 
  'requestPaymentDetails0Id': 2, // Number | 
  'requestPaymentDetails0Value': 10, // Number | 
  'requestPaymentDetails0Bin': 411111 // Number | 
};
apiInstance.installmentsoptions(requestValue, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, opts, (error, data, response) => {
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
 **requestValue** | **Number**|  | 
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **requestSalesChannel** | **Number**|  | [optional] 
 **requestPaymentDetails0Id** | **Number**|  | [optional] 
 **requestPaymentDetails0Value** | **Number**|  | [optional] 
 **requestPaymentDetails0Bin** | **Number**|  | [optional] 

### Return type

[**ValidRequest**](ValidRequest.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8, application/json

