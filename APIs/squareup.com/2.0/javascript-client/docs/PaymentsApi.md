# SquareConnectApi.PaymentsApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelPayment**](PaymentsApi.md#cancelPayment) | **POST** /v2/payments/{payment_id}/cancel | CancelPayment
[**cancelPaymentByIdempotencyKey**](PaymentsApi.md#cancelPaymentByIdempotencyKey) | **POST** /v2/payments/cancel | CancelPaymentByIdempotencyKey
[**completePayment**](PaymentsApi.md#completePayment) | **POST** /v2/payments/{payment_id}/complete | CompletePayment
[**createPayment**](PaymentsApi.md#createPayment) | **POST** /v2/payments | CreatePayment
[**getPayment**](PaymentsApi.md#getPayment) | **GET** /v2/payments/{payment_id} | GetPayment
[**updatePayment**](PaymentsApi.md#updatePayment) | **PUT** /v2/payments/{payment_id} | UpdatePayment
[**v2PaymentsGet**](PaymentsApi.md#v2PaymentsGet) | **GET** /v2/payments | ListPayments



## cancelPayment

> CancelPaymentResponse cancelPayment(paymentId)

CancelPayment

Cancels (voids) a payment. You can use this endpoint to cancel a payment with  the APPROVED &#x60;status&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.PaymentsApi();
let paymentId = "paymentId_example"; // String | The ID of the payment to cancel.
apiInstance.cancelPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**| The ID of the payment to cancel. | 

### Return type

[**CancelPaymentResponse**](CancelPaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelPaymentByIdempotencyKey

> CancelPaymentByIdempotencyKeyResponse cancelPaymentByIdempotencyKey(cancelPaymentByIdempotencyKeyRequest)

CancelPaymentByIdempotencyKey

Cancels (voids) a payment identified by the idempotency key that is specified in the request.  Use this method when the status of a &#x60;CreatePayment&#x60; request is unknown (for example, after you send a &#x60;CreatePayment&#x60; request, a network error occurs and you do not get a response). In this case, you can direct Square to cancel the payment using this endpoint. In the request, you provide the same idempotency key that you provided in your &#x60;CreatePayment&#x60; request that you want to cancel. After canceling the payment, you can submit your &#x60;CreatePayment&#x60; request again.  Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint returns successfully.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.PaymentsApi();
let cancelPaymentByIdempotencyKeyRequest = new SquareConnectApi.CancelPaymentByIdempotencyKeyRequest(); // CancelPaymentByIdempotencyKeyRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.cancelPaymentByIdempotencyKey(cancelPaymentByIdempotencyKeyRequest, (error, data, response) => {
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
 **cancelPaymentByIdempotencyKeyRequest** | [**CancelPaymentByIdempotencyKeyRequest**](CancelPaymentByIdempotencyKeyRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CancelPaymentByIdempotencyKeyResponse**](CancelPaymentByIdempotencyKeyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## completePayment

> CompletePaymentResponse completePayment(paymentId)

CompletePayment

Completes (captures) a payment. By default, payments are set to complete immediately after they are created.  You can use this endpoint to complete a payment with the APPROVED &#x60;status&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.PaymentsApi();
let paymentId = "paymentId_example"; // String | The unique ID identifying the payment to be completed.
apiInstance.completePayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**| The unique ID identifying the payment to be completed. | 

### Return type

[**CompletePaymentResponse**](CompletePaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createPayment

> CreatePaymentResponse createPayment(createPaymentRequest)

CreatePayment

Creates a payment using the provided source. You can use this endpoint  to charge a card (credit/debit card or     Square gift card) or record a payment that the seller received outside of Square  (cash payment from a buyer or a payment that an external entity  processed on behalf of the seller).  The endpoint creates a  &#x60;Payment&#x60; object and returns it in the response.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.PaymentsApi();
let createPaymentRequest = new SquareConnectApi.CreatePaymentRequest(); // CreatePaymentRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createPayment(createPaymentRequest, (error, data, response) => {
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
 **createPaymentRequest** | [**CreatePaymentRequest**](CreatePaymentRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreatePaymentResponse**](CreatePaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPayment

> GetPaymentResponse getPayment(paymentId)

GetPayment

Retrieves details for a specific payment.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.PaymentsApi();
let paymentId = "paymentId_example"; // String | A unique ID for the desired payment.
apiInstance.getPayment(paymentId, (error, data, response) => {
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
 **paymentId** | **String**| A unique ID for the desired payment. | 

### Return type

[**GetPaymentResponse**](GetPaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePayment

> UpdatePaymentResponse updatePayment(paymentId, updatePaymentRequest)

UpdatePayment

Updates a payment with the APPROVED status. You can update the &#x60;amount_money&#x60; and &#x60;tip_money&#x60; using this endpoint.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.PaymentsApi();
let paymentId = "paymentId_example"; // String | The ID of the payment to update.
let updatePaymentRequest = new SquareConnectApi.UpdatePaymentRequest(); // UpdatePaymentRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updatePayment(paymentId, updatePaymentRequest, (error, data, response) => {
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
 **paymentId** | **String**| The ID of the payment to update. | 
 **updatePaymentRequest** | [**UpdatePaymentRequest**](UpdatePaymentRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdatePaymentResponse**](UpdatePaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v2PaymentsGet

> ListPaymentsResponse v2PaymentsGet(opts)

ListPayments

Retrieves a list of payments taken by the account making the request.  Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.  The maximum results per page is 100.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.PaymentsApi();
let opts = {
  'beginTime': "beginTime_example", // String | The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year.
  'endTime': "endTime_example", // String | The timestamp for the end of the reporting period, in RFC 3339 format.  Default: The current time.
  'sortOrder': "sortOrder_example", // String | The order in which results are listed: - `ASC` - Oldest to newest. - `DESC` - Newest to oldest (default).
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
  'locationId': "locationId_example", // String | Limit results to the location supplied. By default, results are returned for the default (main) location associated with the seller.
  'total': 789, // Number | The exact amount in the `total_money` for a payment.
  'last4': "last4_example", // String | The last four digits of a payment card.
  'cardBrand': "cardBrand_example", // String | The brand of the payment card (for example, VISA).
  'limit': 56 // Number | The maximum number of results to be returned in a single page. It is possible to receive fewer results than the specified limit on a given page.  The default value of 100 is also the maximum allowed value. If the provided value is  greater than 100, it is ignored and the default value is used instead.  Default: `100`
};
apiInstance.v2PaymentsGet(opts, (error, data, response) => {
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
 **beginTime** | **String**| The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year. | [optional] 
 **endTime** | **String**| The timestamp for the end of the reporting period, in RFC 3339 format.  Default: The current time. | [optional] 
 **sortOrder** | **String**| The order in which results are listed: - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default). | [optional] 
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] 
 **locationId** | **String**| Limit results to the location supplied. By default, results are returned for the default (main) location associated with the seller. | [optional] 
 **total** | **Number**| The exact amount in the &#x60;total_money&#x60; for a payment. | [optional] 
 **last4** | **String**| The last four digits of a payment card. | [optional] 
 **cardBrand** | **String**| The brand of the payment card (for example, VISA). | [optional] 
 **limit** | **Number**| The maximum number of results to be returned in a single page. It is possible to receive fewer results than the specified limit on a given page.  The default value of 100 is also the maximum allowed value. If the provided value is  greater than 100, it is ignored and the default value is used instead.  Default: &#x60;100&#x60; | [optional] 

### Return type

[**ListPaymentsResponse**](ListPaymentsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

