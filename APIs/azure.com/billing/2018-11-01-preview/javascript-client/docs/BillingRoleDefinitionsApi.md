# BillingManagementClient.BillingRoleDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingRoleDefinitionsGetByBillingAccountName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleDefinitions/{billingRoleDefinitionName} | 
[**billingRoleDefinitionsGetByBillingProfileName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleDefinitions/{billingRoleDefinitionName} | 
[**billingRoleDefinitionsGetByInvoiceSectionName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleDefinitions/{billingRoleDefinitionName} | 
[**billingRoleDefinitionsListByBillingAccountName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleDefinitions | 
[**billingRoleDefinitionsListByBillingProfileName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleDefinitions | 
[**billingRoleDefinitionsListByInvoiceSectionName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleDefinitions | 



## billingRoleDefinitionsGetByBillingAccountName

> BillingRoleDefinition billingRoleDefinitionsGetByBillingAccountName(apiVersion, billingAccountName, billingRoleDefinitionName)



Gets the role definition for a role

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
apiInstance.billingRoleDefinitionsGetByBillingAccountName(apiVersion, billingAccountName, billingRoleDefinitionName, (error, data, response) => {
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
 **billingRoleDefinitionName** | **String**| role definition id. | 

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsGetByBillingProfileName

> BillingRoleDefinition billingRoleDefinitionsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName)



Gets the role definition for a role

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
apiInstance.billingRoleDefinitionsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName, (error, data, response) => {
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
 **billingRoleDefinitionName** | **String**| role definition id. | 

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsGetByInvoiceSectionName

> BillingRoleDefinition billingRoleDefinitionsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleDefinitionName)



Gets the role definition for a role

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
apiInstance.billingRoleDefinitionsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleDefinitionName, (error, data, response) => {
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
 **billingRoleDefinitionName** | **String**| role definition id. | 

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsListByBillingAccountName

> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingAccountName(apiVersion, billingAccountName)



Lists the role definition for a billing account

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
apiInstance.billingRoleDefinitionsListByBillingAccountName(apiVersion, billingAccountName, (error, data, response) => {
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

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsListByBillingProfileName

> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName)



Lists the role definition for a Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
apiInstance.billingRoleDefinitionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName, (error, data, response) => {
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

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsListByInvoiceSectionName

> BillingRoleDefinitionListResult billingRoleDefinitionsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName)



Lists the role definition for an invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
apiInstance.billingRoleDefinitionsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, (error, data, response) => {
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

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

