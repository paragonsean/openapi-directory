# BillingManagementClient.CustomersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customersGet**](CustomersApi.md#customersGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName} | 
[**customersListByBillingAccount**](CustomersApi.md#customersListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers | 
[**customersListByBillingProfile**](CustomersApi.md#customersListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers | 



## customersGet

> Customer customersGet(apiVersion, billingAccountName, customerName, opts)



Gets a customer by its id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.CustomersApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let opts = {
  'expand': "expand_example" // String | May be used to expand enabledAzurePlans, resellers.
};
apiInstance.customersGet(apiVersion, billingAccountName, customerName, opts, (error, data, response) => {
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
 **expand** | **String**| May be used to expand enabledAzurePlans, resellers. | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersListByBillingAccount

> CustomerListResult customersListByBillingAccount(apiVersion, billingAccountName, opts)



Lists customers which the current user can work with on-behalf of a partner.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.CustomersApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let opts = {
  'filter': "filter_example", // String | May be used to filter the list of customers.
  'skiptoken': "skiptoken_example" // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
};
apiInstance.customersListByBillingAccount(apiVersion, billingAccountName, opts, (error, data, response) => {
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
 **filter** | **String**| May be used to filter the list of customers. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 

### Return type

[**CustomerListResult**](CustomerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersListByBillingProfile

> CustomerListResult customersListByBillingProfile(apiVersion, billingAccountName, billingProfileName, opts)



Lists customers by billing profile which the current user can work with on-behalf of a partner.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.CustomersApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let opts = {
  'filter': "filter_example", // String | May be used to filter the list of customers.
  'skiptoken': "skiptoken_example" // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
};
apiInstance.customersListByBillingProfile(apiVersion, billingAccountName, billingProfileName, opts, (error, data, response) => {
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
 **filter** | **String**| May be used to filter the list of customers. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 

### Return type

[**CustomerListResult**](CustomerListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

