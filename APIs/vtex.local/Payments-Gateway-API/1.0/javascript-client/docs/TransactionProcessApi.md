# PaymentsGatewayApi.TransactionProcessApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call1createanewtransaction**](TransactionProcessApi.md#call1createanewtransaction) | **POST** /api/pvt/transactions | 1. Starts a new transaction
[**call2sendPaymentsPublic**](TransactionProcessApi.md#call2sendPaymentsPublic) | **POST** /api/pub/transactions/{transactionId}/payments | 2.1 Send Payments Information Public
[**call2sendPaymentsWithSavedCreditCard**](TransactionProcessApi.md#call2sendPaymentsWithSavedCreditCard) | **POST** /api/pvt/transactions/{transactionId}/payments | 2.2 Send Payments With Saved Credit Card
[**call3sendAdditionalData**](TransactionProcessApi.md#call3sendAdditionalData) | **POST** /api/pvt/transactions/{transactionId}/additional-data | 3. Send Additional Data
[**call4doauthorization**](TransactionProcessApi.md#call4doauthorization) | **POST** /api/pvt/transactions/{transactionId}/authorization-request | Do authorization
[**paymentDetails**](TransactionProcessApi.md#paymentDetails) | **GET** /api/pvt/transactions/{transactionId}/payments/{paymentId} | Payment Details
[**transactionDetails**](TransactionProcessApi.md#transactionDetails) | **GET** /api/pvt/transactions/{transactionId} | Transaction Details
[**transactionSettlementDetails**](TransactionProcessApi.md#transactionSettlementDetails) | **GET** /api/pvt/transactions/{transactionId}/settlements | Transaction Settlement  Details



## call1createanewtransaction

> StartTransactionResponse call1createanewtransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, model1CreateanewtransactionRequest)

1. Starts a new transaction

This request is the first step to create a new transaction.

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let model1CreateanewtransactionRequest = {"channel":"{{accountName}}","referenceId":"1234567","salesChannel":"1","urn":"","value":100}; // Model1CreateanewtransactionRequest | 
apiInstance.call1createanewtransaction(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, model1CreateanewtransactionRequest, (error, data, response) => {
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
 **model1CreateanewtransactionRequest** | [**Model1CreateanewtransactionRequest**](Model1CreateanewtransactionRequest.md)|  | 

### Return type

[**StartTransactionResponse**](StartTransactionResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## call2sendPaymentsPublic

> call2sendPaymentsPublic(orderId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsPublicRequest)

2.1 Send Payments Information Public

The second step to create a new transaction. Here, you have the option to send the data in three diferent ways: doing a private request, a public request or a private request that uses a saved Credit Card. 

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let orderId = "{{orderId}}"; // String | 
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
let model2SendPaymentsPublicRequest = [{"currencyCode":"BRL","fields":{"accountId":"","address":null,"callbackUrl":"","cardNumber":"5378244888889174","document":"8041734561","dueDate":"10/19","holderName":"UserTest","validationCode":"231"},"installments":1,"installmentsInterestRate":0,"installmentsValue":100,"paymentSystem":4,"referenceValue":100,"transaction":{"id":"{{transactionId}}","merchantName":"{{accountName}}"},"value":100}]; // [Model2SendPaymentsPublicRequest] | 
apiInstance.call2sendPaymentsPublic(orderId, xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsPublicRequest, (error, data, response) => {
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
 **orderId** | **String**|  | 
 **xPROVIDERAPIAppKey** | **String**| The AppKey configured by the merchant (optional configuration) | 
 **xPROVIDERAPIAppToken** | **String**| The AppToken configured by the merchant (optional configuration) | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **transactionId** | **String**|  | 
 **model2SendPaymentsPublicRequest** | [**[Model2SendPaymentsPublicRequest]**](Model2SendPaymentsPublicRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## call2sendPaymentsWithSavedCreditCard

> call2sendPaymentsWithSavedCreditCard(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsWithSavedCreditCardRequest)

2.2 Send Payments With Saved Credit Card

The second step to create a new transaction. Here, you have the option to send the data in three diferent ways: doing a private request, a public request or a private request that uses a saved Credit Card.

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
let model2SendPaymentsWithSavedCreditCardRequest = [{"currencyCode":"BRL","fields":{"accountId":"44D964F2053642E888E3B23549937F87","address":null,"callbackUrl":"","firstDigits":"411111","validationCode":"231"},"installments":1,"installmentsInterestRate":0,"installmentsValue":100,"paymentSystem":2,"referenceValue":100,"transaction":{"id":"{{transactionId}}","merchantName":"{{accountName}}"},"value":100}]; // [Model2SendPaymentsWithSavedCreditCardRequest] | 
apiInstance.call2sendPaymentsWithSavedCreditCard(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model2SendPaymentsWithSavedCreditCardRequest, (error, data, response) => {
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
 **model2SendPaymentsWithSavedCreditCardRequest** | [**[Model2SendPaymentsWithSavedCreditCardRequest]**](Model2SendPaymentsWithSavedCreditCardRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## call3sendAdditionalData

> call3sendAdditionalData(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, requestBody)

3. Send Additional Data

The third step to create a new transaction. It will send the additional related data to the transaction, like billig and shipping adress.

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | Transaction identification.
let requestBody = null; // [Array] | 
apiInstance.call3sendAdditionalData(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, requestBody, (error, data, response) => {
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
 **transactionId** | **String**| Transaction identification. | 
 **requestBody** | [**[Array]**](Array.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## call4doauthorization

> call4doauthorization(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model4DoauthorizationRequest)

Do authorization

The fouth and last step to create a new transaction. It will authorized the new transction creation acorrdint to the data previously informed in the latests requests.

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
let model4DoauthorizationRequest = {"prepareForRecurrency":false,"softDescriptor":"{{accountName}}","transactionId":"{{transactionId}}"}; // Model4DoauthorizationRequest | 
apiInstance.call4doauthorization(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, accept, contentType, transactionId, model4DoauthorizationRequest, (error, data, response) => {
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
 **model4DoauthorizationRequest** | [**Model4DoauthorizationRequest**](Model4DoauthorizationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## paymentDetails

> PaymentDetailsResponse paymentDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId, paymentId)

Payment Details

Returns associated information details for the specified payment id.

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
let paymentId = "paymentId_example"; // String | 
apiInstance.paymentDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId, paymentId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **transactionId** | **String**|  | 
 **paymentId** | **String**|  | 

### Return type

[**PaymentDetailsResponse**](PaymentDetailsResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## transactionDetails

> TransactionDetailsResponse transactionDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId)

Transaction Details

Returns associated data for the specified transaction id, like value and status, for exemple.

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
apiInstance.transactionDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **transactionId** | **String**|  | 

### Return type

[**TransactionDetailsResponse**](TransactionDetailsResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## transactionSettlementDetails

> TransactionSettlementDetails transactionSettlementDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId)

Transaction Settlement  Details

Returns associated settlements data for the specified transaction id.

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

let apiInstance = new PaymentsGatewayApi.TransactionProcessApi();
let xPROVIDERAPIAppKey = "{{X-PROVIDER-API-AppKey}}"; // String | The AppKey configured by the merchant (optional configuration)
let xPROVIDERAPIAppToken = "{{X-PROVIDER-API-AppToken}}"; // String | The AppToken configured by the merchant (optional configuration)
let contentType = "application/json"; // String | The Media type of the body of the request.  Default value for payment provider protocol is application/json
let accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let transactionId = "transactionId_example"; // String | 
apiInstance.transactionSettlementDetails(xPROVIDERAPIAppKey, xPROVIDERAPIAppToken, contentType, accept, transactionId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request.  Default value for payment provider protocol is application/json | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | 
 **transactionId** | **String**|  | 

### Return type

[**TransactionSettlementDetails**](TransactionSettlementDetails.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

