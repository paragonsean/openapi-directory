# PaymentWebhooksDeprecated.PaymentAuthorisationRefundOrFundsTransferInitiatedApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalancePlatformPaymentCreated**](PaymentAuthorisationRefundOrFundsTransferInitiatedApi.md#postBalancePlatformPaymentCreated) | **POST** /balancePlatform.payment.created | Payment authorisation, refund, or funds transfer initiated
[**postBalancePlatformPaymentUpdated**](PaymentAuthorisationRefundOrFundsTransferInitiatedApi.md#postBalancePlatformPaymentUpdated) | **POST** /balancePlatform.payment.updated | Payment authorisation expired or cancelled



## postBalancePlatformPaymentCreated

> BalancePlatformNotificationResponse postBalancePlatformPaymentCreated(opts)

Payment authorisation, refund, or funds transfer initiated

Adyen sends this webhook when a payment authorisation, a refund, or a funds transfer has been initiated. This webhook only informs your server of requests. For the actual fund movements, you&#39;ll get the information from the subsequent outgoing or incoming transfer webhooks.   To differentiate the requests, check the content of the webhook.  * For payments, the webhook contains the authorisation result, information about the processing merchant, and shows a negative amount.   * For refunds, the webhook contains to which payment instrument the funds will be refunded, and shows a positive amount.  * For outgoing or incoming fund transfers, the webhook shows a positive or negative amount depending on the direction of the transfer, and only includes information about the balance account.

### Example

```javascript
import PaymentWebhooksDeprecated from 'payment_webhooks__deprecated';
let defaultClient = PaymentWebhooksDeprecated.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PaymentWebhooksDeprecated.PaymentAuthorisationRefundOrFundsTransferInitiatedApi();
let opts = {
  'paymentNotificationRequest': new PaymentWebhooksDeprecated.PaymentNotificationRequest() // PaymentNotificationRequest | 
};
apiInstance.postBalancePlatformPaymentCreated(opts, (error, data, response) => {
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
 **paymentNotificationRequest** | [**PaymentNotificationRequest**](PaymentNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformPaymentUpdated

> BalancePlatformNotificationResponse postBalancePlatformPaymentUpdated(opts)

Payment authorisation expired or cancelled

Adyen sends this webhook when a payment authorisation has expired or has been cancelled. Use the &#x60;data.id&#x60; to track the original payment authorisation from the &#x60;balancePlatform.payment.created&#x60; webhook.

### Example

```javascript
import PaymentWebhooksDeprecated from 'payment_webhooks__deprecated';
let defaultClient = PaymentWebhooksDeprecated.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PaymentWebhooksDeprecated.PaymentAuthorisationRefundOrFundsTransferInitiatedApi();
let opts = {
  'paymentNotificationRequest': new PaymentWebhooksDeprecated.PaymentNotificationRequest() // PaymentNotificationRequest | 
};
apiInstance.postBalancePlatformPaymentUpdated(opts, (error, data, response) => {
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
 **paymentNotificationRequest** | [**PaymentNotificationRequest**](PaymentNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

