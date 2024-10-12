# GovUkPayApi.CardPaymentsApi

All URIs are relative to *https://publicapi.payments.service.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelAPayment**](CardPaymentsApi.md#cancelAPayment) | **POST** /v1/payments/{paymentId}/cancel | Cancel payment
[**captureAPayment**](CardPaymentsApi.md#captureAPayment) | **POST** /v1/payments/{paymentId}/capture | Capture payment
[**createAPayment**](CardPaymentsApi.md#createAPayment) | **POST** /v1/payments | Create new payment
[**getAPayment**](CardPaymentsApi.md#getAPayment) | **GET** /v1/payments/{paymentId} | Find payment by ID
[**getEventsForAPayment**](CardPaymentsApi.md#getEventsForAPayment) | **GET** /v1/payments/{paymentId}/events | Return payment events by ID
[**searchPayments**](CardPaymentsApi.md#searchPayments) | **GET** /v1/payments | Search payments



## cancelAPayment

> cancelAPayment(paymentId)

Cancel payment

Cancel a payment based on the provided payment ID and the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;. A payment can only be cancelled if it&#39;s in a state that isn&#39;t finished.

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.CardPaymentsApi();
let paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
apiInstance.cancelAPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**| Payment identifier | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## captureAPayment

> captureAPayment(paymentId)

Capture payment

Capture a payment based on the provided payment ID and the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;. A payment can only be captured if it&#39;s in &#39;submitted&#39; state

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.CardPaymentsApi();
let paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
apiInstance.captureAPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**| Payment identifier | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createAPayment

> CreatePaymentResult createAPayment(body)

Create new payment

Create a new payment for the account associated to the Authorisation token. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.CardPaymentsApi();
let body = new GovUkPayApi.CreateCardPaymentRequest(); // CreateCardPaymentRequest | requestPayload
apiInstance.createAPayment(body, (error, data, response) => {
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
 **body** | [**CreateCardPaymentRequest**](CreateCardPaymentRequest.md)| requestPayload | 

### Return type

[**CreatePaymentResult**](CreatePaymentResult.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAPayment

> GetPaymentResult getAPayment(paymentId)

Find payment by ID

Return information about the payment The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.CardPaymentsApi();
let paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
apiInstance.getAPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**| Payment identifier | 

### Return type

[**GetPaymentResult**](GetPaymentResult.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsForAPayment

> PaymentEvents getEventsForAPayment(paymentId)

Return payment events by ID

Return payment events information about a certain payment The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.CardPaymentsApi();
let paymentId = "hu20sqlact5260q2nanm0q8u93"; // String | Payment identifier
apiInstance.getEventsForAPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**| Payment identifier | 

### Return type

[**PaymentEvents**](PaymentEvents.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchPayments

> PaymentSearchResults searchPayments(opts)

Search payments

Search payments by reference, state, &#39;from&#39; and &#39;to&#39; date. The Authorisation token needs to be specified in the &#39;authorization&#39; header as &#39;authorization: Bearer YOUR_API_KEY_HERE&#39;

### Example

```javascript
import GovUkPayApi from 'gov_uk_pay_api';
let defaultClient = GovUkPayApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new GovUkPayApi.CardPaymentsApi();
let opts = {
  'reference': "reference_example", // String | Your payment reference to search (exact match, case insensitive)
  'email': "email_example", // String | The user email used in the payment to be searched
  'state': "state_example", // String | State of payments to be searched. Example=success
  'cardBrand': "cardBrand_example", // String | Card brand used for payment. Example=master-card
  'fromDate': "fromDate_example", // String | From date of payments to be searched (this date is inclusive). Example=2015-08-13T12:35:00Z
  'toDate': "toDate_example", // String | To date of payments to be searched (this date is exclusive). Example=2015-08-14T12:35:00Z
  'page': "page_example", // String | Page number requested for the search, should be a positive integer (optional, defaults to 1)
  'displaySize': "displaySize_example", // String | Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500)
  'cardholderName': "cardholderName_example", // String | Name on card used to make payment
  'firstDigitsCardNumber': "firstDigitsCardNumber_example", // String | First six digits of the card used to make payment
  'lastDigitsCardNumber': "lastDigitsCardNumber_example", // String | Last four digits of the card used to make payment
  'fromSettledDate': "fromSettledDate_example", // String | From settled date of payment to be searched (this date is inclusive). Example=2015-08-13
  'toSettledDate': "toSettledDate_example" // String | To settled date of payment to be searched (this date is inclusive). Example=2015-08-14
};
apiInstance.searchPayments(opts, (error, data, response) => {
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
 **reference** | **String**| Your payment reference to search (exact match, case insensitive) | [optional] 
 **email** | **String**| The user email used in the payment to be searched | [optional] 
 **state** | **String**| State of payments to be searched. Example&#x3D;success | [optional] 
 **cardBrand** | **String**| Card brand used for payment. Example&#x3D;master-card | [optional] 
 **fromDate** | **String**| From date of payments to be searched (this date is inclusive). Example&#x3D;2015-08-13T12:35:00Z | [optional] 
 **toDate** | **String**| To date of payments to be searched (this date is exclusive). Example&#x3D;2015-08-14T12:35:00Z | [optional] 
 **page** | **String**| Page number requested for the search, should be a positive integer (optional, defaults to 1) | [optional] 
 **displaySize** | **String**| Number of results to be shown per page, should be a positive integer (optional, defaults to 500, max 500) | [optional] 
 **cardholderName** | **String**| Name on card used to make payment | [optional] 
 **firstDigitsCardNumber** | **String**| First six digits of the card used to make payment | [optional] 
 **lastDigitsCardNumber** | **String**| Last four digits of the card used to make payment | [optional] 
 **fromSettledDate** | **String**| From settled date of payment to be searched (this date is inclusive). Example&#x3D;2015-08-13 | [optional] 
 **toSettledDate** | **String**| To settled date of payment to be searched (this date is inclusive). Example&#x3D;2015-08-14 | [optional] 

### Return type

[**PaymentSearchResults**](PaymentSearchResults.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

