# PaymentWebhooksDeprecated.FundMovementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalancePlatformIncomingTransferCreated**](FundMovementsApi.md#postBalancePlatformIncomingTransferCreated) | **POST** /balancePlatform.incomingTransfer.created | Incoming transfer created
[**postBalancePlatformIncomingTransferUpdated**](FundMovementsApi.md#postBalancePlatformIncomingTransferUpdated) | **POST** /balancePlatform.incomingTransfer.updated | Incoming transfer updated
[**postBalancePlatformOutgoingTransferCreated**](FundMovementsApi.md#postBalancePlatformOutgoingTransferCreated) | **POST** /balancePlatform.outgoingTransfer.created | Outgoing transfer created
[**postBalancePlatformOutgoingTransferUpdated**](FundMovementsApi.md#postBalancePlatformOutgoingTransferUpdated) | **POST** /balancePlatform.outgoingTransfer.updated | Outgoing transfer updated



## postBalancePlatformIncomingTransferCreated

> BalancePlatformNotificationResponse postBalancePlatformIncomingTransferCreated(opts)

Incoming transfer created

Adyen sends this webhook when there are incoming funds due to a refund or a fund transfer. Use the &#x60;paymentId&#x60; to link to the original refund request or funds transfer request. Check the content of the webhook to differentiate the events.  * For refunds, the webhook includes the payment instrument to which funds will be refunded.  * For incoming fund transfers, the webhook only includes information about the balance account.

### Example

```javascript
import PaymentWebhooksDeprecated from 'payment_webhooks__deprecated';
let defaultClient = PaymentWebhooksDeprecated.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PaymentWebhooksDeprecated.FundMovementsApi();
let opts = {
  'incomingTransferNotificationRequest': new PaymentWebhooksDeprecated.IncomingTransferNotificationRequest() // IncomingTransferNotificationRequest | 
};
apiInstance.postBalancePlatformIncomingTransferCreated(opts, (error, data, response) => {
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
 **incomingTransferNotificationRequest** | [**IncomingTransferNotificationRequest**](IncomingTransferNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformIncomingTransferUpdated

> BalancePlatformNotificationResponse postBalancePlatformIncomingTransferUpdated(opts)

Incoming transfer updated

Adyen sends this webhook when funds were added to the balance account. This could be due to a refund or a funds transfer. Use the &#x60;data.id&#x60; to track the original incoming transfer resource in the &#x60;balancePlatform.incomingTransfer.created&#x60; webhook.  The &#x60;status&#x60; field indicates the event that triggered the webhook.   * For refunds, the &#x60;status&#x60; is **Refunded**.   * For incoming fund transfers, the &#x60;status&#x60; is **IncomingTransfer**.

### Example

```javascript
import PaymentWebhooksDeprecated from 'payment_webhooks__deprecated';
let defaultClient = PaymentWebhooksDeprecated.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PaymentWebhooksDeprecated.FundMovementsApi();
let opts = {
  'incomingTransferNotificationRequest': new PaymentWebhooksDeprecated.IncomingTransferNotificationRequest() // IncomingTransferNotificationRequest | 
};
apiInstance.postBalancePlatformIncomingTransferUpdated(opts, (error, data, response) => {
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
 **incomingTransferNotificationRequest** | [**IncomingTransferNotificationRequest**](IncomingTransferNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformOutgoingTransferCreated

> BalancePlatformNotificationResponse postBalancePlatformOutgoingTransferCreated(opts)

Outgoing transfer created

Adyen sends this webhook when funds were deducted from a balance account due to a capture or a funds transfer. Use the &#x60;paymentId&#x60; to link to the original payment authorisation or funds transfer request.  The &#x60;status&#x60; field indicates the event that triggered the webhook.   * For captures, the &#x60;status&#x60; will be **Captured**.   * For outgoing fund transfers, the &#x60;status&#x60; will be **OutgoingTransfer**.

### Example

```javascript
import PaymentWebhooksDeprecated from 'payment_webhooks__deprecated';
let defaultClient = PaymentWebhooksDeprecated.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PaymentWebhooksDeprecated.FundMovementsApi();
let opts = {
  'outgoingTransferNotificationRequest': new PaymentWebhooksDeprecated.OutgoingTransferNotificationRequest() // OutgoingTransferNotificationRequest | 
};
apiInstance.postBalancePlatformOutgoingTransferCreated(opts, (error, data, response) => {
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
 **outgoingTransferNotificationRequest** | [**OutgoingTransferNotificationRequest**](OutgoingTransferNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformOutgoingTransferUpdated

> BalancePlatformNotificationResponse postBalancePlatformOutgoingTransferUpdated(opts)

Outgoing transfer updated

Adyen sends this webhook when there is updated information after funds have been deducted from a balance account. For example, if the fund transfer failed.  Use the &#x60;data.id&#x60; to track the original outgoing transfer resource from the &#x60;balancePlatform.outgoingTransfer.created&#x60; webhook.

### Example

```javascript
import PaymentWebhooksDeprecated from 'payment_webhooks__deprecated';
let defaultClient = PaymentWebhooksDeprecated.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PaymentWebhooksDeprecated.FundMovementsApi();
let opts = {
  'outgoingTransferNotificationRequest': new PaymentWebhooksDeprecated.OutgoingTransferNotificationRequest() // OutgoingTransferNotificationRequest | 
};
apiInstance.postBalancePlatformOutgoingTransferUpdated(opts, (error, data, response) => {
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
 **outgoingTransferNotificationRequest** | [**OutgoingTransferNotificationRequest**](OutgoingTransferNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

