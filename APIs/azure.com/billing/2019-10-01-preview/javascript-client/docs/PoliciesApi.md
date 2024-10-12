# BillingManagementClient.PoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policiesGetByBillingProfile**](PoliciesApi.md#policiesGetByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/policies/default | 
[**policiesGetByCustomer**](PoliciesApi.md#policiesGetByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/policies/default | 
[**policiesUpdate**](PoliciesApi.md#policiesUpdate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/policies/default | 
[**policiesUpdateCustomer**](PoliciesApi.md#policiesUpdateCustomer) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/policies/default | 



## policiesGetByBillingProfile

> Policy policiesGetByBillingProfile(billingAccountName, billingProfileName, apiVersion)



The policy for a given billing account name and billing profile name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PoliciesApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.policiesGetByBillingProfile(billingAccountName, billingProfileName, apiVersion, (error, data, response) => {
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

[**Policy**](Policy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policiesGetByCustomer

> CustomerPolicy policiesGetByCustomer(billingAccountName, customerName, apiVersion)



The policy for a given billing account name and customer name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PoliciesApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.policiesGetByCustomer(billingAccountName, customerName, apiVersion, (error, data, response) => {
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
 **customerName** | **String**| Customer name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**CustomerPolicy**](CustomerPolicy.md)

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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **parameters** | [**Policy**](Policy.md)| Parameters supplied to the update policy operation. | 

### Return type

[**Policy**](Policy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policiesUpdateCustomer

> CustomerPolicy policiesUpdateCustomer(apiVersion, billingAccountName, customerName, parameters)



The operation to update a Customer policy.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PoliciesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let parameters = new BillingManagementClient.CustomerPolicy(); // CustomerPolicy | Parameters supplied to the update customer policy operation.
apiInstance.policiesUpdateCustomer(apiVersion, billingAccountName, customerName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **customerName** | **String**| Customer name. | 
 **parameters** | [**CustomerPolicy**](CustomerPolicy.md)| Parameters supplied to the update customer policy operation. | 

### Return type

[**CustomerPolicy**](CustomerPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

