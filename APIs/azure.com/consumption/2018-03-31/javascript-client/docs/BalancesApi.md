# ConsumptionManagementClient.BalancesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBalancesByBillingAccount**](BalancesApi.md#getBalancesByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/balances | 
[**getBalancesByBillingAccountByBillingPeriod**](BalancesApi.md#getBalancesByBillingAccountByBillingPeriod) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Billing/billingPeriods/{billingPeriodName}/providers/Microsoft.Consumption/balances | 



## getBalancesByBillingAccount

> Balance getBalancesByBillingAccount(apiVersion, billingAccountId)



Gets the balances for a scope by billingAccountId. Balances are available via this API only for May 1, 2014 or later.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BalancesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
apiInstance.getBalancesByBillingAccount(apiVersion, billingAccountId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 
 **billingAccountId** | **String**| BillingAccount ID | 

### Return type

[**Balance**](Balance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBalancesByBillingAccountByBillingPeriod

> Balance getBalancesByBillingAccountByBillingPeriod(apiVersion, billingAccountId, billingPeriodName)



Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BalancesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let billingPeriodName = "billingPeriodName_example"; // String | Billing Period Name.
apiInstance.getBalancesByBillingAccountByBillingPeriod(apiVersion, billingAccountId, billingPeriodName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **billingPeriodName** | **String**| Billing Period Name. | 

### Return type

[**Balance**](Balance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

