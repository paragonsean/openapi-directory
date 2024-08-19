# TokenJayApiServices.PaymentPortalApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPaymentRequest**](PaymentPortalApi.md#addPaymentRequest) | **POST** /payment/addrequest | Creates a new payment request. Will return request id to check for transaction state and ergopay url to show the user as QR code
[**getPaymentState**](PaymentPortalApi.md#getPaymentState) | **GET** /payment/state/{requestId} | Returns the state of a payment request. Please note that payment requests are purged after some time, so persist the state at your side when needed



## addPaymentRequest

> AddRequestResponse addPaymentRequest(createPaymentRequest)

Creates a new payment request. Will return request id to check for transaction state and ergopay url to show the user as QR code

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.PaymentPortalApi();
let createPaymentRequest = new TokenJayApiServices.CreatePaymentRequest(); // CreatePaymentRequest | 
apiInstance.addPaymentRequest(createPaymentRequest, (error, data, response) => {
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
 **createPaymentRequest** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | 

### Return type

[**AddRequestResponse**](AddRequestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getPaymentState

> PaymentRequestStateResponse getPaymentState(requestId)

Returns the state of a payment request. Please note that payment requests are purged after some time, so persist the state at your side when needed

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.PaymentPortalApi();
let requestId = "requestId_example"; // String | 
apiInstance.getPaymentState(requestId, (error, data, response) => {
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
 **requestId** | **String**|  | 

### Return type

[**PaymentRequestStateResponse**](PaymentRequestStateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

