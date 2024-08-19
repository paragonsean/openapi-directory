# ConfigurationWebhooks.CardOrderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalancePlatformCardorderCreated**](CardOrderApi.md#postBalancePlatformCardorderCreated) | **POST** /balancePlatform.cardorder.created | Card order created
[**postBalancePlatformCardorderUpdated**](CardOrderApi.md#postBalancePlatformCardorderUpdated) | **POST** /balancePlatform.cardorder.updated | Card order updated



## postBalancePlatformCardorderCreated

> BalancePlatformNotificationResponse postBalancePlatformCardorderCreated(opts)

Card order created

Adyen sends this webhook to indicate a successful creation of a card order after you create a [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments) of &#x60;type&#x60; **card** and &#x60;formFactor&#x60; **physical**.

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.CardOrderApi();
let opts = {
  'cardOrderNotificationRequest': new ConfigurationWebhooks.CardOrderNotificationRequest() // CardOrderNotificationRequest | 
};
apiInstance.postBalancePlatformCardorderCreated(opts, (error, data, response) => {
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
 **cardOrderNotificationRequest** | [**CardOrderNotificationRequest**](CardOrderNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformCardorderUpdated

> BalancePlatformNotificationResponse postBalancePlatformCardorderUpdated(opts)

Card order updated

Adyen sends this webhook when there is an update in card order status.

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.CardOrderApi();
let opts = {
  'cardOrderNotificationRequest': new ConfigurationWebhooks.CardOrderNotificationRequest() // CardOrderNotificationRequest | 
};
apiInstance.postBalancePlatformCardorderUpdated(opts, (error, data, response) => {
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
 **cardOrderNotificationRequest** | [**CardOrderNotificationRequest**](CardOrderNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

