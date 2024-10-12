# Signl4Api.PrepaidApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prepaidBalanceGet**](PrepaidApi.md#prepaidBalanceGet) | **GET** /prepaid/balance | Get your subscription&#39;s current prepaid balance.
[**prepaidSettingsGet**](PrepaidApi.md#prepaidSettingsGet) | **GET** /prepaid/settings | Get your subscription&#39;s current prepaid settings.
[**prepaidSettingsPut**](PrepaidApi.md#prepaidSettingsPut) | **PUT** /prepaid/settings | Update your subscription&#39;s current prepaid settings.
[**prepaidTransactionsGet**](PrepaidApi.md#prepaidTransactionsGet) | **GET** /prepaid/transactions | Get your subscription&#39;s prepaid transactions.
[**subscriptionsSubscriptionIdPrepaidBalanceGet**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidBalanceGet) | **GET** /subscriptions/{subscriptionId}/prepaidBalance | Get a subscription&#39;s current prepaid balance.
[**subscriptionsSubscriptionIdPrepaidSettingsGet**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidSettingsGet) | **GET** /subscriptions/{subscriptionId}/prepaidSettings | Get a subscription&#39;s current prepaid settings.
[**subscriptionsSubscriptionIdPrepaidSettingsPut**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidSettingsPut) | **PUT** /subscriptions/{subscriptionId}/prepaidSettings | Update a subscription&#39;s current prepaid settings.
[**subscriptionsSubscriptionIdPrepaidTransactionsGet**](PrepaidApi.md#subscriptionsSubscriptionIdPrepaidTransactionsGet) | **GET** /subscriptions/{subscriptionId}/prepaidTransactions | Get a subscription&#39;s prepaid transactions.



## prepaidBalanceGet

> PrepaidBalanceInfo prepaidBalanceGet()

Get your subscription&#39;s current prepaid balance.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
apiInstance.prepaidBalanceGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PrepaidBalanceInfo**](PrepaidBalanceInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## prepaidSettingsGet

> PrepaidSettingsInfo prepaidSettingsGet()

Get your subscription&#39;s current prepaid settings.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
apiInstance.prepaidSettingsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## prepaidSettingsPut

> PrepaidSettingsInfo prepaidSettingsPut(opts)

Update your subscription&#39;s current prepaid settings.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
let opts = {
  'prepaidSettingsInfo': new Signl4Api.PrepaidSettingsInfo() // PrepaidSettingsInfo | Settings object containing the new values.
};
apiInstance.prepaidSettingsPut(opts, (error, data, response) => {
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
 **prepaidSettingsInfo** | [**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)| Settings object containing the new values. | [optional] 

### Return type

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## prepaidTransactionsGet

> [PrepaidTransactionInfo] prepaidTransactionsGet()

Get your subscription&#39;s prepaid transactions.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
apiInstance.prepaidTransactionsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[PrepaidTransactionInfo]**](PrepaidTransactionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdPrepaidBalanceGet

> PrepaidBalanceInfo subscriptionsSubscriptionIdPrepaidBalanceGet(subscriptionId)

Get a subscription&#39;s current prepaid balance.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
let subscriptionId = "subscriptionId_example"; // String | 
apiInstance.subscriptionsSubscriptionIdPrepaidBalanceGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**|  | 

### Return type

[**PrepaidBalanceInfo**](PrepaidBalanceInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdPrepaidSettingsGet

> PrepaidSettingsInfo subscriptionsSubscriptionIdPrepaidSettingsGet(subscriptionId)

Get a subscription&#39;s current prepaid settings.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
let subscriptionId = "subscriptionId_example"; // String | 
apiInstance.subscriptionsSubscriptionIdPrepaidSettingsGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**|  | 

### Return type

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdPrepaidSettingsPut

> PrepaidSettingsInfo subscriptionsSubscriptionIdPrepaidSettingsPut(subscriptionId, opts)

Update a subscription&#39;s current prepaid settings.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
let subscriptionId = "subscriptionId_example"; // String | ID of the subscription
let opts = {
  'prepaidSettingsInfo': new Signl4Api.PrepaidSettingsInfo() // PrepaidSettingsInfo | Settings object containing the new values.
};
apiInstance.subscriptionsSubscriptionIdPrepaidSettingsPut(subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the subscription | 
 **prepaidSettingsInfo** | [**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)| Settings object containing the new values. | [optional] 

### Return type

[**PrepaidSettingsInfo**](PrepaidSettingsInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## subscriptionsSubscriptionIdPrepaidTransactionsGet

> [PrepaidTransactionInfo] subscriptionsSubscriptionIdPrepaidTransactionsGet(subscriptionId)

Get a subscription&#39;s prepaid transactions.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.PrepaidApi();
let subscriptionId = "subscriptionId_example"; // String | ID of the subscription to get transactions for
apiInstance.subscriptionsSubscriptionIdPrepaidTransactionsGet(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| ID of the subscription to get transactions for | 

### Return type

[**[PrepaidTransactionInfo]**](PrepaidTransactionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

