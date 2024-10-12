# ConfigurationWebhooks.PaymentInstrumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalancePlatformPaymentInstrumentCreated**](PaymentInstrumentApi.md#postBalancePlatformPaymentInstrumentCreated) | **POST** /balancePlatform.paymentInstrument.created | Payment instrument created
[**postBalancePlatformPaymentInstrumentUpdated**](PaymentInstrumentApi.md#postBalancePlatformPaymentInstrumentUpdated) | **POST** /balancePlatform.paymentInstrument.updated | Payment instrument updated



## postBalancePlatformPaymentInstrumentCreated

> BalancePlatformNotificationResponse postBalancePlatformPaymentInstrumentCreated(opts)

Payment instrument created

Adyen sends this webhook when you successfully [create a payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments).  &gt;The webhook does not include the card number when creating virtual cards. You can only get the card number in the response of the POST [/paymentInstruments](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments#responses-200-card-number) request.

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.PaymentInstrumentApi();
let opts = {
  'paymentNotificationRequest': new ConfigurationWebhooks.PaymentNotificationRequest() // PaymentNotificationRequest | 
};
apiInstance.postBalancePlatformPaymentInstrumentCreated(opts, (error, data, response) => {
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


## postBalancePlatformPaymentInstrumentUpdated

> BalancePlatformNotificationResponse postBalancePlatformPaymentInstrumentUpdated(opts)

Payment instrument updated

Adyen sends this webhook when you successfully [update a payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/paymentInstruments/_id_). 

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.PaymentInstrumentApi();
let opts = {
  'paymentNotificationRequest': new ConfigurationWebhooks.PaymentNotificationRequest() // PaymentNotificationRequest | 
};
apiInstance.postBalancePlatformPaymentInstrumentUpdated(opts, (error, data, response) => {
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

