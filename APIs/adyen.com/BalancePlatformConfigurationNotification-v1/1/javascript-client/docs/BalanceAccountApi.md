# ConfigurationWebhooks.BalanceAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalancePlatformBalanceAccountCreated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountCreated) | **POST** /balancePlatform.balanceAccount.created | Balance account created
[**postBalancePlatformBalanceAccountSweepCreated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountSweepCreated) | **POST** /balancePlatform.balanceAccountSweep.created | Sweep created
[**postBalancePlatformBalanceAccountSweepDeleted**](BalanceAccountApi.md#postBalancePlatformBalanceAccountSweepDeleted) | **POST** /balancePlatform.balanceAccountSweep.deleted | Sweep deleted
[**postBalancePlatformBalanceAccountSweepUpdated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountSweepUpdated) | **POST** /balancePlatform.balanceAccountSweep.updated | Sweep updated
[**postBalancePlatformBalanceAccountUpdated**](BalanceAccountApi.md#postBalancePlatformBalanceAccountUpdated) | **POST** /balancePlatform.balanceAccount.updated | Balance account updated



## postBalancePlatformBalanceAccountCreated

> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountCreated(opts)

Balance account created

Adyen sends this webhook when you successfully [create a balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts).

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.BalanceAccountApi();
let opts = {
  'balanceAccountNotificationRequest': new ConfigurationWebhooks.BalanceAccountNotificationRequest() // BalanceAccountNotificationRequest | 
};
apiInstance.postBalancePlatformBalanceAccountCreated(opts, (error, data, response) => {
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
 **balanceAccountNotificationRequest** | [**BalanceAccountNotificationRequest**](BalanceAccountNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformBalanceAccountSweepCreated

> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountSweepCreated(opts)

Sweep created

Adyen sends this webhook when you successfully [create a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/_balanceAccountId_/sweeps).

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.BalanceAccountApi();
let opts = {
  'sweepConfigurationNotificationRequest': new ConfigurationWebhooks.SweepConfigurationNotificationRequest() // SweepConfigurationNotificationRequest | 
};
apiInstance.postBalancePlatformBalanceAccountSweepCreated(opts, (error, data, response) => {
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
 **sweepConfigurationNotificationRequest** | [**SweepConfigurationNotificationRequest**](SweepConfigurationNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformBalanceAccountSweepDeleted

> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountSweepDeleted(opts)

Sweep deleted

Adyen sends this webhook when you successfully [delete a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/_balanceAccountId_/sweeps/_sweepId_).

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.BalanceAccountApi();
let opts = {
  'sweepConfigurationNotificationRequest': new ConfigurationWebhooks.SweepConfigurationNotificationRequest() // SweepConfigurationNotificationRequest | 
};
apiInstance.postBalancePlatformBalanceAccountSweepDeleted(opts, (error, data, response) => {
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
 **sweepConfigurationNotificationRequest** | [**SweepConfigurationNotificationRequest**](SweepConfigurationNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformBalanceAccountSweepUpdated

> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountSweepUpdated(opts)

Sweep updated

Adyen sends this webhook when you successfully [update a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/_balanceAccountId_/sweeps/_sweepId_).

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.BalanceAccountApi();
let opts = {
  'sweepConfigurationNotificationRequest': new ConfigurationWebhooks.SweepConfigurationNotificationRequest() // SweepConfigurationNotificationRequest | 
};
apiInstance.postBalancePlatformBalanceAccountSweepUpdated(opts, (error, data, response) => {
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
 **sweepConfigurationNotificationRequest** | [**SweepConfigurationNotificationRequest**](SweepConfigurationNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postBalancePlatformBalanceAccountUpdated

> BalancePlatformNotificationResponse postBalancePlatformBalanceAccountUpdated(opts)

Balance account updated

Adyen sends this webhook when you successfully [update a balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/_id_).

### Example

```javascript
import ConfigurationWebhooks from 'configuration_webhooks';
let defaultClient = ConfigurationWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ConfigurationWebhooks.BalanceAccountApi();
let opts = {
  'balanceAccountNotificationRequest': new ConfigurationWebhooks.BalanceAccountNotificationRequest() // BalanceAccountNotificationRequest | 
};
apiInstance.postBalancePlatformBalanceAccountUpdated(opts, (error, data, response) => {
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
 **balanceAccountNotificationRequest** | [**BalanceAccountNotificationRequest**](BalanceAccountNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

