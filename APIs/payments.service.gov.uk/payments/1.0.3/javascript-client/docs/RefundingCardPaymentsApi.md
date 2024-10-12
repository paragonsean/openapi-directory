# GovUkPayApi.RefundingCardPaymentsApi

All URIs are relative to *https://publicapi.payments.service.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAPaymentRefund**](RefundingCardPaymentsApi.md#getAPaymentRefund) | **GET** /v1/payments/{paymentId}/refunds/{refundId} | Find payment refund by ID
[**getAllRefundsForAPayment**](RefundingCardPaymentsApi.md#getAllRefundsForAPayment) | **GET** /v1/payments/{paymentId}/refunds | Get all refunds for a payment
[**searchRefunds**](RefundingCardPaymentsApi.md#searchRefunds) | **GET** /v1/refunds | Search refunds
[**submitARefundForAPayment**](RefundingCardPaymentsApi.md#submitARefundForAPayment) | **POST** /v1/payments/{paymentId}/refunds | Submit a refund for a payment



## getAPaymentRefund

> Refund getAPaymentRefund(paymentId, refundId)

Find payment refund by ID

Return payment refund information by Refund ID The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.RefundingCardPaymentsApi();
let paymentId = "paymentId_example"; // String | 
let refundId = "refundId_example"; // String | 
apiInstance.getAPaymentRefund(paymentId, refundId, (error, data, response) => {
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
 **paymentId** | **String**|  | 
 **refundId** | **String**|  | 

### Return type

[**Refund**](Refund.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllRefundsForAPayment

> RefundForSearchResult getAllRefundsForAPayment(paymentId)

Get all refunds for a payment

Return refunds for a payment. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.RefundingCardPaymentsApi();
let paymentId = "paymentId_example"; // String | 
apiInstance.getAllRefundsForAPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**|  | 

### Return type

[**RefundForSearchResult**](RefundForSearchResult.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchRefunds

> RefundSearchResults searchRefunds(opts)

Search refunds

Search refunds by &#39;from&#39; and &#39;to&#39; date. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.RefundingCardPaymentsApi();
let opts = {
  'fromDate': "fromDate_example", // String | From date of refunds to be searched (this date is inclusive). Example=2015-08-13T12:35:00Z
  'toDate': "toDate_example", // String | To date of refunds to be searched (this date is exclusive). Example=2015-08-14T12:35:00Z
  'fromSettledDate': "fromSettledDate_example", // String | From settled date of refund to be searched (this date is inclusive). Example=2015-08-13
  'toSettledDate': "toSettledDate_example", // String | To settled date of refund to be searched (this date is inclusive). Example=2015-08-13
  'page': "page_example", // String | Page number requested for the search, should be a positive integer (optional, defaults to 1)
  'displaySize': "displaySize_example" // String | Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500)
};
apiInstance.searchRefunds(opts, (error, data, response) => {
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
 **fromDate** | **String**| From date of refunds to be searched (this date is inclusive). Example&#x3D;2015-08-13T12:35:00Z | [optional] 
 **toDate** | **String**| To date of refunds to be searched (this date is exclusive). Example&#x3D;2015-08-14T12:35:00Z | [optional] 
 **fromSettledDate** | **String**| From settled date of refund to be searched (this date is inclusive). Example&#x3D;2015-08-13 | [optional] 
 **toSettledDate** | **String**| To settled date of refund to be searched (this date is inclusive). Example&#x3D;2015-08-13 | [optional] 
 **page** | **String**| Page number requested for the search, should be a positive integer (optional, defaults to 1) | [optional] 
 **displaySize** | **String**| Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500) | [optional] 

### Return type

[**RefundSearchResults**](RefundSearchResults.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitARefundForAPayment

> Refund submitARefundForAPayment(paymentId, body)

Submit a refund for a payment

Return issued refund information. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.RefundingCardPaymentsApi();
let paymentId = "paymentId_example"; // String | paymentId
let body = new GovUkPayApi.PaymentRefundRequest(); // PaymentRefundRequest | requestPayload
apiInstance.submitARefundForAPayment(paymentId, body, (error, data, response) => {
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
 **paymentId** | **String**| paymentId | 
 **body** | [**PaymentRefundRequest**](PaymentRefundRequest.md)| requestPayload | 

### Return type

[**Refund**](Refund.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

