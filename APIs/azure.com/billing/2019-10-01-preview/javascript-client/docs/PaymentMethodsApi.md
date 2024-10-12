# BillingManagementClient.PaymentMethodsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentMethodsListByBillingAccount**](PaymentMethodsApi.md#paymentMethodsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/paymentMethods | 
[**paymentMethodsListByBillingProfile**](PaymentMethodsApi.md#paymentMethodsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/paymentMethods | 



## paymentMethodsListByBillingAccount

> PaymentMethodsListResult paymentMethodsListByBillingAccount(billingAccountName, apiVersion)



Lists the Payment Methods by billing account Id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PaymentMethodsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.paymentMethodsListByBillingAccount(billingAccountName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| billing Account Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**PaymentMethodsListResult**](PaymentMethodsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentMethodsListByBillingProfile

> PaymentMethodsListResult paymentMethodsListByBillingProfile(billingAccountName, billingProfileName, apiVersion)



Lists the Payment Methods by billing profile Id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PaymentMethodsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.paymentMethodsListByBillingProfile(billingAccountName, billingProfileName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**PaymentMethodsListResult**](PaymentMethodsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

