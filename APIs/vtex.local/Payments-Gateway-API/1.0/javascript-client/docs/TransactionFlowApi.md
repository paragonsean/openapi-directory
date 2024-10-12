# PaymentsGatewayApi.TransactionFlowApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelthetransaction**](TransactionFlowApi.md#cancelthetransaction) | **POST** /api/pvt/transactions/{transactionId}/cancellation-request | Cancel the transaction
[**refundthetransaction**](TransactionFlowApi.md#refundthetransaction) | **POST** /api/pvt/transactions/{transactionId}/refunding-request | Refund the transaction
[**settlethetransaction**](TransactionFlowApi.md#settlethetransaction) | **POST** /api/pvt/transactions/{transactionId}/settlement-request | Settle the transaction



## cancelthetransaction

> cancelthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, cancelthetransactionRequest)

Cancel the transaction

Cancel&#39;s transaction that was previously approved, but not settled.

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

let apiInstance = new PaymentsGatewayApi.TransactionFlowApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
let cancelthetransactionRequest = {"minicart":{"freight":200,"items":[{"discount":50,"id":"122323","name":"Tenis Preto I","quantity":1,"shippingDiscount":0,"value":1000},{"discount":50,"id":"122324","name":"Tenis Nike Azul","quantity":1,"shippingDiscount":0,"value":1100}],"tax":0},"value":2300}; // CancelthetransactionRequest | 
apiInstance.cancelthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, cancelthetransactionRequest, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **transactionId** | **String**|  | 
 **cancelthetransactionRequest** | [**CancelthetransactionRequest**](CancelthetransactionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## refundthetransaction

> refundthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, refundthetransactionRequest)

Refund the transaction

Refunds transaction&#39;s value that was previously settled.

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

let apiInstance = new PaymentsGatewayApi.TransactionFlowApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
let refundthetransactionRequest = {"minicart":{"freight":200,"items":[{"discount":50,"id":"122323","name":"Tenis Preto I","quantity":1,"shippingDiscount":0,"value":1000},{"discount":50,"id":"122324","name":"Tenis Nike Azul","quantity":1,"shippingDiscount":0,"value":1100}],"tax":0},"value":2300}; // RefundthetransactionRequest | 
apiInstance.refundthetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, refundthetransactionRequest, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **transactionId** | **String**|  | 
 **refundthetransactionRequest** | [**RefundthetransactionRequest**](RefundthetransactionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## settlethetransaction

> SettleResponse settlethetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, settlethetransactionRequest)

Settle the transaction

Settles transaction&#39;s value.

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

let apiInstance = new PaymentsGatewayApi.TransactionFlowApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
let settlethetransactionRequest = {"value":100}; // SettlethetransactionRequest | 
apiInstance.settlethetransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, settlethetransactionRequest, (error, data, response) => {
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
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **transactionId** | **String**|  | 
 **settlethetransactionRequest** | [**SettlethetransactionRequest**](SettlethetransactionRequest.md)|  | 

### Return type

[**SettleResponse**](SettleResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

