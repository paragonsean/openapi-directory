# BillingManagementClient.PoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policiesGetByBillingProfileName**](PoliciesApi.md#policiesGetByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/policies/default | 
[**policiesUpdate**](PoliciesApi.md#policiesUpdate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/policies/default | 



## policiesGetByBillingProfileName

> Policy policiesGetByBillingProfileName(billingAccountName, billingProfileName, apiVersion)



The policy for a given billing account name and billing profile name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PoliciesApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.policiesGetByBillingProfileName(billingAccountName, billingProfileName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 

### Return type

[**Policy**](Policy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policiesUpdate

> Policy policiesUpdate(apiVersion, billingAccountName, billingProfileName, parameters)



The operation to update a policy.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PoliciesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let parameters = new BillingManagementClient.Policy(); // Policy | Parameters supplied to the update policy operation.
apiInstance.policiesUpdate(apiVersion, billingAccountName, billingProfileName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 
 **billingAccountName** | **String**| Billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **parameters** | [**Policy**](Policy.md)| Parameters supplied to the update policy operation. | 

### Return type

[**Policy**](Policy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

