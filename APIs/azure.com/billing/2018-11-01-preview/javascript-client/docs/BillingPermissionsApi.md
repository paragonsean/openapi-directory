# BillingManagementClient.BillingPermissionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingPermissionsListByBillingAccount**](BillingPermissionsApi.md#billingPermissionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingPermissions | 
[**billingPermissionsListByBillingProfile**](BillingPermissionsApi.md#billingPermissionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingPermissions | 
[**billingPermissionsListByCustomers**](BillingPermissionsApi.md#billingPermissionsListByCustomers) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/providers/Microsoft.Billing/billingPermissions | 
[**billingPermissionsListByInvoiceSections**](BillingPermissionsApi.md#billingPermissionsListByInvoiceSections) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingPermissions | 



## billingPermissionsListByBillingAccount

> BillingPermissionsListResult billingPermissionsListByBillingAccount(apiVersion, billingAccountName)



Lists all billing permissions for the caller under a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingPermissionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
apiInstance.billingPermissionsListByBillingAccount(apiVersion, billingAccountName, (error, data, response) => {
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

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingPermissionsListByBillingProfile

> BillingPermissionsListResult billingPermissionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName)



Lists all billingPermissions for the caller has for a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingPermissionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
apiInstance.billingPermissionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName, (error, data, response) => {
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

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingPermissionsListByCustomers

> BillingPermissionsListResult billingPermissionsListByCustomers(apiVersion, billingAccountName, customerName)



Lists all billing permissions for the caller under customer.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingPermissionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let customerName = "customerName_example"; // String | Customer Id.
apiInstance.billingPermissionsListByCustomers(apiVersion, billingAccountName, customerName, (error, data, response) => {
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
 **customerName** | **String**| Customer Id. | 

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingPermissionsListByInvoiceSections

> BillingPermissionsListResult billingPermissionsListByInvoiceSections(apiVersion, billingAccountName, invoiceSectionName)



Lists all billing permissions for the caller under invoice section.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingPermissionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
apiInstance.billingPermissionsListByInvoiceSections(apiVersion, billingAccountName, invoiceSectionName, (error, data, response) => {
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
 **invoiceSectionName** | **String**| InvoiceSection Id. | 

### Return type

[**BillingPermissionsListResult**](BillingPermissionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

