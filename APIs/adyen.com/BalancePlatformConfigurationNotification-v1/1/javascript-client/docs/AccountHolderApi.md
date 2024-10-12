# ConfigurationWebhooks.AccountHolderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalancePlatformAccountHolderCreated**](AccountHolderApi.md#postBalancePlatformAccountHolderCreated) | **POST** /balancePlatform.accountHolder.created | Account holder created
[**postBalancePlatformAccountHolderUpdated**](AccountHolderApi.md#postBalancePlatformAccountHolderUpdated) | **POST** /balancePlatform.accountHolder.updated | Account holder updated



## postBalancePlatformAccountHolderCreated

> BalancePlatformNotificationResponse postBalancePlatformAccountHolderCreated(opts)

Account holder created

Adyen sends this webhook when you successfully [create an account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders).

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.AccountHolderApi();
let opts = {
  'accountHolderNotificationRequest': new ConfigurationWebhooks.AccountHolderNotificationRequest() // AccountHolderNotificationRequest | 
};
apiInstance.postBalancePlatformAccountHolderCreated(opts, (error, data, response) => {
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
 **accountHolderNotificationRequest** | [**AccountHolderNotificationRequest**](AccountHolderNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformAccountHolderUpdated

> BalancePlatformNotificationResponse postBalancePlatformAccountHolderUpdated(opts)

Account holder updated

Adyen sends this webhook when you successfully [update an account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/accountHolders/_id_).

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.AccountHolderApi();
let opts = {
  'accountHolderNotificationRequest': new ConfigurationWebhooks.AccountHolderNotificationRequest() // AccountHolderNotificationRequest | 
};
apiInstance.postBalancePlatformAccountHolderUpdated(opts, (error, data, response) => {
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
 **accountHolderNotificationRequest** | [**AccountHolderNotificationRequest**](AccountHolderNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

