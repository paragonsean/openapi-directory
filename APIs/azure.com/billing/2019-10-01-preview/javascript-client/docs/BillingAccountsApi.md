# BillingManagementClient.BillingAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingAccountsGet**](BillingAccountsApi.md#billingAccountsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName} | 
[**billingAccountsList**](BillingAccountsApi.md#billingAccountsList) | **GET** /providers/Microsoft.Billing/billingAccounts | 
[**billingAccountsListInvoiceSectionsByCreateSubscriptionPermission**](BillingAccountsApi.md#billingAccountsListInvoiceSectionsByCreateSubscriptionPermission) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/listInvoiceSectionsWithCreateSubscriptionPermission | 
[**billingAccountsUpdate**](BillingAccountsApi.md#billingAccountsUpdate) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountName} | 



## billingAccountsGet

> BillingAccount billingAccountsGet(apiVersion, billingAccountName, opts)



Get the billing account by id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the address, invoiceSections and billingProfiles.
};
apiInstance.billingAccountsGet(apiVersion, billingAccountName, opts, (error, data, response) => {
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
 **expand** | **String**| May be used to expand the address, invoiceSections and billingProfiles. | [optional] 

### Return type

[**BillingAccount**](BillingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingAccountsList

> BillingAccountListResult billingAccountsList(apiVersion, opts)



Lists all billing accounts for a user which he has access to.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let opts = {
  'expand': "expand_example" // String | May be used to expand the address, invoiceSections and billingProfiles.
};
apiInstance.billingAccountsList(apiVersion, opts, (error, data, response) => {
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
 **expand** | **String**| May be used to expand the address, invoiceSections and billingProfiles. | [optional] 

### Return type

[**BillingAccountListResult**](BillingAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingAccountsListInvoiceSectionsByCreateSubscriptionPermission

> InvoiceSectionListWithCreateSubPermissionResult billingAccountsListInvoiceSectionsByCreateSubscriptionPermission(apiVersion, billingAccountName)



Lists all invoice sections with create subscription permission for a user.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
apiInstance.billingAccountsListInvoiceSectionsByCreateSubscriptionPermission(apiVersion, billingAccountName, (error, data, response) => {
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

### Return type

[**InvoiceSectionListWithCreateSubPermissionResult**](InvoiceSectionListWithCreateSubPermissionResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingAccountsUpdate

> BillingAccount billingAccountsUpdate(apiVersion, billingAccountName, parameters)



The operation to update a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let parameters = new BillingManagementClient.BillingAccountUpdateRequest(); // BillingAccountUpdateRequest | Request parameters supplied to the update billing account operation.
apiInstance.billingAccountsUpdate(apiVersion, billingAccountName, parameters, (error, data, response) => {
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
 **parameters** | [**BillingAccountUpdateRequest**](BillingAccountUpdateRequest.md)| Request parameters supplied to the update billing account operation. | 

### Return type

[**BillingAccount**](BillingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

